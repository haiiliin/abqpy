from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .SectionCategory import SectionCategory
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import CLOSEST


@abaqus_class_doc
class OdbMeshElement:
    """OdbMeshElement objects are created with the part.addElements or rootAssembly.addElements
    methods.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].elements[i]
            session.odbs[name].parts[name].elementSets[name].elements[i]
            session.odbs[name].parts[name].nodeSets[name].elements[i]
            session.odbs[name].parts[name].surfaces[name].elements[i]
            session.odbs[name].rootAssembly.elements[i]
            session.odbs[name].rootAssembly.elementSets[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].elementSets[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].nodeSets[name].elements[i]
            session.odbs[name].rootAssembly.instances[name].surfaces[name].elements[i]
            session.odbs[name].rootAssembly.nodeSets[name].elements[i]
            session.odbs[name].rootAssembly.surfaces[name].elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name].elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].elements[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].elements[i]
    """

    #: An Int specifying the element label.
    label: Optional[int] = None

    #: A String specifying the element type.
    type: str = ""

    #: A :py:class:`~abaqus.Odb.SectionCategory.SectionCategory` object specifying the element section properties.
    sectionCategory: Optional[SectionCategory] = None

    #: A tuple of Ints specifying the element connectivity. For connector elements connected to
    #: ground, the other node is repeated in the connectivity data. The position of the ground
    #: node cannot be ascertained. This is a limitation. It is important to note the difference
    #: with MeshElement object of MDB where the connectivity is node indices instead of node
    #: labels.
    connectivity: Optional[int] = None

    #: A tuple of Strings specifying the instance names for nodes in the element connectivity.
    instanceNames: tuple = ()

    #: A String specifying the instance name.
    instanceName: str = ""

    @abaqus_method_doc
    def getNormal(
        self,
        faceIndex: str,
        stepName: str = "",
        frameValue: str = "",
        match: Literal[C.BEFORE, C.EXACT, C.AFTER, C.CLOSEST] = CLOSEST,
    ):
        """This method returns the normal direction for the element face.

        .. versionadded:: 2017
            The getNormal method was added.

        Parameters
        ----------
        faceIndex
            The value of **faceIndex** is 0 for a shell element and can range from 0 to 5 for a solid
            element.
        stepName
            Name of the step.
        frameValue
            A Double specifying the value at which the frame is required. **frameValue** can be the
            total fime or frequency.
        match
            A SymbolicConstant specifying which frame to return if there is no frame at the exact
            frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is
            CLOSEST.When **match** = CLOSEST, Abaqus returns the closest frame. If the frame value
            requested is exactly halfway between two frames, Abaqus returns the frame after the
            value.When **match** = EXACT, Abaqus raises an exception if the exact frame value does not
            exist.

        Returns
        -------
            A tuple of 3 floats representing the unit normal vector. If the element face is
            collapsed such that a normal cannot be computed, a zero-length vector is returned.

        Raises
        ------
        OdbError: Frame not found
            If the exact frame is not found.
        OdbError: Step is not present in the ODB
            If the step name is not found.
        OdbError: **stepName** should be specified with *frameValue*
            If **frameValue** is not provided and **stepName** is empty.
        """
        ...
