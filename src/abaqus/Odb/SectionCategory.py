from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .SectionPoint import SectionPoint
from .SectionPointArray import SectionPointArray


@abaqus_class_doc
class SectionCategory:
    """The SectionCategory object is used to group regions of the model with like sections. Section definitions
    that contain the same number of section points or integration points are grouped together. To access data
    for a particular section definition, use the individual Section objects in the output database. For more
    information, see Beam Section profile commands and Section commands.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].elements[i].sectionCategory
            session.odbs[name].parts[name].elementSets[name].elements[i].sectionCategory
            session.odbs[name].parts[name].nodeSets[name].elements[i].sectionCategory
            session.odbs[name].parts[name].surfaces[name].elements[i].sectionCategory
            session.odbs[name].rootAssembly.elements[i].sectionCategory
            session.odbs[name].rootAssembly.elementSets[name].elements[i].sectionCategory
            session.odbs[name].rootAssembly.instances[name].elements[i].sectionCategory
            session.odbs[name].rootAssembly.instances[name].elementSets[name].elements[i].sectionCategory
            session.odbs[name].rootAssembly.instances[name].nodeSets[name].elements[i].sectionCategory
            session.odbs[name].rootAssembly.instances[name].surfaces[name].elements[i].sectionCategory
            session.odbs[name].rootAssembly.nodeSets[name].elements[i].sectionCategory
            session.odbs[name].rootAssembly.surfaces[name].elements[i].sectionCategory
            session.odbs[name].sectionCategories[name]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elements[i].sectionCategory
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name].elements[i].sectionCategory
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].elements[i].sectionCategory
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].elements[i].sectionCategory
    """

    #: A SectionPointArray object.
    sectionPoints: SectionPointArray = []

    #: A String specifying the name of the category.
    name: str

    #: A String specifying the description of the category.
    description: str

    @abaqus_method_doc
    def __init__(self, name: str, description: str):
        """This method creates a SectionCategory object.

        .. note::
            This function can be accessed by::

                session.odbs[name].SectionCategory

        Parameters
        ----------
        name
            A String specifying the name of the category.
        description
            A String specifying the description of the category.

        Returns
        -------
        SectionCategory
            A SectionCategory object.
        """
        ...

    @abaqus_method_doc
    def SectionPoint(self, number: int, description: str) -> SectionPoint:
        """This method creates a SectionPoint object.

        .. note::
            This function can be accessed by::

                session.odbs[name].SectionCategory

        Parameters
        ----------
        number
            An Int specifying the number of the section point. See Beam elements and Shell elements
            for the numbering convention.
        description
            A String specifying the description of the section point.

        Returns
        -------
        SectionPoint
            A SectionPoint object.
        """
        sectionPoint = SectionPoint(number, description)
        self.sectionPoints.append(sectionPoint)
        return sectionPoint
