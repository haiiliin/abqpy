"""
skewExampleUtils.py

Utilities for the scripting tutorial Skew Example.
"""

from abaqus import *
from abaqusConstants import *
import visualization

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getResults():

    """
    Retrieve the displacement and calculate the minimum 
    and maximum bending moment at the center of plate.
    """

    from visualization import ELEMENT_NODAL

    # Open the output database.
    
    odb = visualization.openOdb('skew.odb')
    centerNSet = odb.rootAssembly.nodeSets['CENTER']
    frame = odb.steps['Step-1'].frames[-1]
    
    # Retrieve Z-displacement at the center of the plate.
    
    dispField = frame.fieldOutputs['U']
    dispSubField = dispField.getSubset(region=centerNSet)
    disp = dispSubField.values[0].data[2]

    # Average the contribution from each element to the moment,
    # then calculate the minimum and maximum bending moment at
    # the center of the plate using Mohr's circle.
    
    momentField = frame.fieldOutputs['SM']
    momentSubField = momentField.getSubset(region=centerNSet, 
        position=ELEMENT_NODAL)
    m1, m2, m3 = 0, 0, 0
    for value in momentSubField.values:
        m1 = m1 + value.data[0]
        m2 = m2 + value.data[1]
        m3 = m3 + value.data[2]
    numElements = len(momentSubField.values)    
    m1 = m1 / numElements
    m2 = m2 / numElements
    m3 = m3 / numElements
    momentA = 0.5 * (abs(m1) + abs(m2))
    momentB = sqrt(0.25 * (m1 - m2)**2 + m3**2)
    maxMoment = momentA + momentB
    minMoment = momentA - momentB

    odb.close()
    
    return disp, maxMoment, minMoment

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createXYPlot(vpOrigin, vpName, plotName, data):
    
    """
    Display curves of theoretical and computed results in
    a new viewport.
    """

    from visualization import  USER_DEFINED
    
    vp = session.Viewport(name=vpName, origin=vpOrigin, 
        width=150, height=100)
    xyPlot = session.XYPlot(plotName)
    chart = xyPlot.charts.values()[0]
    curveList = []
    for elemName, xyValues in sorted(data.items()):
        xyData = session.XYData(elemName, xyValues)
        curve = session.Curve(xyData)
        curveList.append(curve)
    chart.setValues(curvesToPlot=curveList)
    chart.axes1[0].axisData.setValues(useSystemTitle=False,title='Skew Angle')
    chart.axes2[0].axisData.setValues(useSystemTitle=False,title=plotName)
    vp.setValues(displayedObject=xyPlot)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createModel():

    """
    Create the skew example model, including material, step, load, bc, and job.
    """

    import regionToolset, part, step, mesh

    # Create the Plate
    m = mdb.models['Model-1']
    s = m.ConstrainedSketch(name='__profile__', sheetSize=5.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(sheetSize=5.0, gridSpacing=0.1, grid=ON, 
                            gridFrequency=2, constructionGeometry=ON,
                            dimensionTextHeight=0.1, decimalPlaces=2)
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(1.0, 1.0))
    s.delete(objectList=(c[21], c[18], c[19], c[20]))
    s.HorizontalConstraint(entity=g.findAt((0.5, 0.0)))
    s.FixedConstraint(entity=v.findAt((0.0, 0.0)))
    s.FixedConstraint(entity=v.findAt((1.0, 0.0)))
    s.ParallelConstraint(entity1=g.findAt((0.0, 0.5)),
                        entity2=g.findAt((1.0,0.5)))
    s.AngularDimension(line1=g.findAt((0.0, 0.5)), line2=g.findAt((0.5, 0.0)), 
                    textPoint=(0.2, 0.2), value=90.0)
    p = m.Part(name='Plate', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    vp = session.viewports['Viewport: 1']
    vp.setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

    # Create the Steel material
    m.Material('Steel')
    m.materials['Steel'].Elastic(table=((30.e6, 0.3), ))
    m.HomogeneousShellSection(name='Shell', preIntegrate=OFF, material='Steel',
                            thickness=0.01, poissonDefinition=DEFAULT, 
                            temperature=GRADIENT, integrationRule=SIMPSON, numIntPts=5)

    # Assign Steel to the plate
    p = mdb.models['Model-1'].parts['Plate']
    region =(None, None, p.faces, None)
    p.SectionAssignment(region=region, sectionName='Shell')


    # Create the assembly
    a = m.rootAssembly
    vp.setValues(displayedObject=a)
    a.DatumCsysByDefault(CARTESIAN)
    a.Instance(name='Plate-1', part=p, dependent=OFF)
    pi = a.instances['Plate-1']

    # Create the step
    m.StaticStep(name='Step-1', previous='Initial',
                description='Apply pressure', timePeriod=1, initialInc=1)
    vp.assemblyDisplay.setValues(step='Step-1')
    m.fieldOutputRequests['F-Output-1'].setValues(frequency=1, variables=('U',))
    m.FieldOutputRequest(name='F-Output-2', createStepName='Step-1',
                        variables=('SF',), position=NODES)
    del mdb.models['Model-1'].historyOutputRequests['H-Output-1']

    # Create the displacement BC
    e = pi.edges
    edges = e.findAt(((0.25, 0.0, 0.0), ), ((1.0, 0.25, 0.0), ),
                    ((0.75, 1.0, 0.0), ), ((0.0, 0.75, 0.0), ), )
    region =(None, edges, None, None)
    m.DisplacementBC(name='Pinned', createStepName='Step-1', region=region,
                    u1=0.0, u2=0.0, u3=0.0)

    # Create the Pressure load
    s1 = pi.faces
    side1Faces1 = s1.findAt(((0.333333333333333, 0.333333333333333, 0.0),
                            (0.0, 0.0, 1.0), ),)
    region = regionToolset.Region(side1Faces=side1Faces1)
    m.Pressure(name='Load-1', createStepName='Step-1', region=region,
            distributionType=UNIFORM, magnitude=1.0, amplitude=UNSET)

    # Partition the face
    f1, e1 = pi.faces, pi.edges
    faces = (f1.findAt(coordinates=(0.33333333333, 0.33333333333, 0.0)), )
    pt1 = pi.InterestingPoint(edge=e1.findAt(coordinates=(
        0.0, 0.75, 0.0)), rule=MIDDLE)
    pt2 = pi.InterestingPoint(edge=e1.findAt(coordinates=(
        1.0, 0.25, 0.0)), rule=MIDDLE)
    a.PartitionFaceByShortestPath(faces=faces, point1=pt1, point2=pt2)
    faces = (f1.findAt(coordinates=(0.33333333333, 0.66666666667, 0.0)), 
            f1.findAt(coordinates=(0.66666666667, 0.33333333333, 0.0)))
    pt1 = pi.InterestingPoint(edge=e1.findAt(coordinates=(
        0.75, 1.0, 0.0)), rule=MIDDLE)
    pt2 = pi.InterestingPoint(edge=e1.findAt(coordinates=(
        0.25, 0.0, 0.0)), rule=MIDDLE)
    a.PartitionFaceByShortestPath(faces=faces, point1=pt1, point2=pt2)

    # Create the Geometry set CENTER
    verts = pi.vertices.findAt(((0.5, 0.5, 0.0), ))
    a.Set(name='CENTER', vertices=verts)

    # Create the mesh
    a.seedPartInstance(regions=(pi,), size=0.25)
    a.generateMesh(regions=(pi,))

    # Create the job
    mdb.Job(name='skew', model='Model-1', type=ANALYSIS, explicitPrecision=SINGLE,
            description='', userSubroutine='', numCpus=1, scratch='',
            echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF)

