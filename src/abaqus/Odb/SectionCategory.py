from .SectionPoint import SectionPoint
from .SectionPointArray import SectionPointArray


class SectionCategory:
    """The SectionCategory object is used to group regions of the model with like sections.
    Section definitions that contain the same number of section points or integration points
    are grouped together.
    To access data for a particular section definition, use the individual Section objects
    in the output database. For more information, see Beam Section profile commands and
    Section commands.

    Attributes
    ----------
    sectionPoints: SectionPointArray
        A :py:class:`~abaqus.Odb.SectionPointArray.SectionPointArray` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import
        odbAccess
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

    # A SectionPointArray object.
    sectionPoints: SectionPointArray = SectionPointArray()

    def __init__(self, name: str, description: str):
        """This method creates a SectionCategory object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].SectionCategory

        Parameters
        ----------
        name
            A String specifying the name of the category.
        description
            A String specifying the description of the category.

        Returns
        -------
            A SectionCategory object.
        """
        pass

    def SectionPoint(self, number: int, description: str) -> SectionPoint:
        """This method creates a SectionPoint object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].SectionCategory

        Parameters
        ----------
        number
            An Int specifying the number of the section point. See Beam elements and Shell elements
            for the numbering convention.
        description
            A String specifying the description of the section point.

        Returns
        -------
            A SectionPoint object.
        """
        sectionPoint = SectionPoint(number, description)
        self.sectionPoints.append(sectionPoint)
        return sectionPoint
