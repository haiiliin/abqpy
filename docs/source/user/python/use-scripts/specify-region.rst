===================
Specifying a region
===================

Many of the commands used by the Abaqus Scripting Interface require a region argument. For example,

- Load commands use the region argument to specify where the load is applied. You apply a concentrated force to vertices; you apply pressure to a face or an edge.

- Mesh commands, such as setting the element type and creating the mesh, use the region argument to specify where the operation should be applied.

- Set commands use the region argument to specify the region that comprises the set.

A region can be either a predefined Set or Surface object or a temporary Region object. For more information, see Region commands.

You should not rely on the integer id to identify a vertex, edge, face, or cell in a region command; for example, myFace=myModel.parts['Door'].faces[3]. The id can change if you add or delete features to your model; in addition, the id can change with a new release of Abaqus.

Rather than using the integer `id`, you should use the `findAt` method to identify a vertex, edge, face, or cell. The arguments to `findAt` are an arbitrary point on an edge, face, or cell or the X-, Y-, and Z-coordinates of a vertex. `findAt` returns an object that contains the `id` of the vertex or the `id` of the edge, face, or cell that includes the arbitrary point.

`findAt` initially uses the ACIS tolerance of 1E-6. As a result, `findAt` returns any entity that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, `findAt` uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities). If necessary, it can open the tolerance further to find a suitable object. The arbitrary point must not be shared by a second edge, face, or cell. If two entities intersect or coincide at the arbitrary point, `findAt` chooses the first entity that it encounters, and you should not rely on the return value being consistent.

Alternatively, if you are working with an existing model that contains named regions, you can specify a region by referring to its name. For example, in the example described in Investigating the skew sensitivity of shell elements, you create a model using Abaqus/CAE. While you define the model, you must create a set that includes the vertex at the center of a planar part and you must name the set `CENTER`. You subsequently run a script that parameterizes the model and performs a series of analyses. The script uses the named region to retrieve the displacement and the bending moment at the center of the plate. The following statement refers to the set that you created and named using Abaqus/CAE:

.. code-block:: python2

    centerNSet = odb.rootAssembly.nodeSets['CENTER']

The following script illustrates how you can create a region. Regions are created from each of the following:

- A sequence of tuples indicating the vertices, edges, faces, or cells in the region. The sequence can include multiple tuples of the same type.

- A sequence of tuples indicating a combination of the vertices, edges, faces, and cells in the region. The tuples can appear in any order in the sequence. In addition, you can include multiple tuples of the same type, and you can omit any type from the sequence.

- A Surface object specifying an entity and the side of the entity.

Use the following command to retrieve the script:

.. code-block:: python2

    # abaqus fetch job=createRegions
    """
    createRegions.py

    Script to illustrate different techniques for defining regions.
    """

    # Import the modules used by this script.

    from abaqus import *
    from abaqusConstants import *
    import part
    import assembly
    import step
    import load
    import interaction

    myModel = mdb.models['Model-1']

    # Create a new Viewport for this example.

    myViewport=session.Viewport(name='Region syntax', 
                origin=(20, 20), width=200, height=100)

    # Create a Sketch and draw two rectangles. 

    mySketch = myModel.ConstrainedSketch(name='Sketch A',
        sheetSize=200.0)

    mySketch.rectangle(point1=(-40.0, 30.0),
        point2=(-10.0, 0.0))

    mySketch.rectangle(point1=(10.0, 30.0),
        point2=(40.0, 0.0))

    # Create a 3D part and extrude the rectangles.

    door = myModel.Part(name='Door',
        dimensionality=THREE_D, type=DEFORMABLE_BODY)

    door.BaseSolidExtrude(sketch=mySketch, depth=20.0)

    # Instance the part.

    myAssembly = myModel.rootAssembly
    doorInstance = myAssembly.Instance(name='Door-1',
        part=door)

    # Select two vertices.

    pillarVertices = doorInstance.vertices.findAt(
        ((-40,30,0),), ((40,0,0),) )

    # Create a static step.

    myModel.StaticStep(name='impact',
        previous='Initial', initialInc=1, timePeriod=1)

    # Create a concentrated force on the selected
    # vertices.

    myPillarLoad = myModel.ConcentratedForce(
        name='pillarForce', createStepName='impact',
        region=(pillarVertices,), cf1=12.50E4)

    # Select two faces

    topFace = doorInstance.faces.findAt(((-25,30,10),))
    bottomFace = doorInstance.faces.findAt(((-25,0,10),))

    # Create a pressure load on the selected faces.
    # You can use the "+" notation if the entities are of
    # the same type and are from the same part instance.

    myFenderLoad = myModel.Pressure(
        name='pillarPressure', createStepName='impact',
        region=((topFace+bottomFace, SIDE1),),
        magnitude=10E4)

    # Select two edges from one instance.

    myEdge1 = doorInstance.edges.findAt(((10,15,20),))
    myEdge2 = doorInstance.edges.findAt(((10,15,0),))

    # Create a boundary condition on one face,
    # two edges, and two vertices.

    myDisplacementBc= myModel.DisplacementBC(
        name='xBC', createStepName='impact',
        region=(pillarVertices, myEdge1+myEdge2,
        topFace), u1=5.0)

    # Select two faces using an arbitrary point
    # on the face.

    faceRegion = doorInstance.faces.findAt(
        ((-30,15,20), ), ((30,15,20),))

    # Create a surface containing the two faces.
    # Indicate which side of the surface to include.

    mySurface = myModel.rootAssembly.Surface(
        name='exterior', side1Faces=faceRegion)

    # Create an elastic foundation using the surface.

    myFoundation = myModel.ElasticFoundation(
        name='elasticFloor', createStepName='Initial',
        surface=mySurface, stiffness=1500)

    # Display the assembly along with the new boundary
    # conditions and loads.

    myViewport.setValues(displayedObject=myAssembly)
    myViewport.assemblyDisplay.setValues(step='impact', 
        loads=ON, bcs=ON, fields=ON)