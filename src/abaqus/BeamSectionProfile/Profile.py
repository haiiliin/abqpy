
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Profile:
    """The Profile object defines the geometrical properties of a beam cross-section. Profile
    is an abstract base type.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].profiles[name]
            import odbSection
            session.odbs[name].profiles[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    @abaqus_method_doc
    def beamProfilesFromOdb(self, fileName: str):
        """This method creates Profile objects by reading an output database. The new profiles are
        placed in the profiles repository.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].beamProfilesFromOdb

        Parameters
        ----------
        fileName
            A String specifying the name of the output database file (including the .odb extension)
            to be read. The String can also be the full path to the output database file if it is
            located in another directory.

        Returns
        -------
        List[Profile]
            A list of Profile objects.

        """
        ...
