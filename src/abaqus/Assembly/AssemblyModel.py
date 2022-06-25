from abaqusConstants import *
from .PartInstance import PartInstance

# from ..Model.ModelBase import ModelBase


# Prevent circular import
class ModelBase:
    pass


class AssemblyModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            mdb.models[name]
    """

    def Instance(self, name: str, objectToCopy: PartInstance):
        """This method copies a PartInstance object from the specified model and creates a new
        PartInstance object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].Instance

        Parameters
        ----------
        name
            A String specifying the repository key.
        objectToCopy
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object to be copied.

        Returns
        -------
        Model
            A :py:class:`~abaqus.Model.Model.Model` object.
        """
        return self

    def convertAllSketches(
        self, regenerate: Boolean = True, convertReversedSketches: Boolean = True
    ):
        """This method converts all sketches from Abaqus 6.5 or earlier to the equivalent
        ConstrainedSketch objects.

        Parameters
        ----------
        regenerate
            A Boolean specifying if all the features in assembly as well as in all the parts in the
            model should be regenerated after the conversion. The default value is True.
        convertReversedSketches
            A Boolean specifying whether sketches in analytic rigid parts should be converted even
            if they cause the orientation of surfaces defined on them to be flipped. The default
            value is True.

        Returns
        -------
        list[str]
            A list of strings describing any warnings or errors encountered during the conversion
            process.
        """
        pass

    def linkInstances(self, instancesMap: tuple):
        """This method links the selected PartInstance objects to the corresponding PartInstance
        objects from the specified models. If all instances of a Part are selected for linking,
        the Part will be linked as well. If not, a new linked child Part object will be created
        and added to the repository.

        Parameters
        ----------
        instancesMap
            A tuple of tuples containing the instance name to be linked and the corresponding
            PartInstance object to which it will be linked.

        Returns
        -------
        list[str]
            A list of strings describing any warnings or errors encountered during the conversion
            process.
        """
        pass
