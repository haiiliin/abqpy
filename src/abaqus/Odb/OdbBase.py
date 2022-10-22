from typing_extensions import Literal
from typing import Dict

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .JobData import JobData
from .OdbAssembly import OdbAssembly
from .OdbPart import OdbPart
from .OdbStep import OdbStep
from .SectionCategory import SectionCategory
from .SectorDefinition import SectorDefinition
from .UserData import UserData
from ..Amplitude.Amplitude import Amplitude
from ..BeamSectionProfile.Profile import Profile
from ..CustomKernel.RepositorySupport import RepositorySupport
from ..Filter.Filter import Filter
from ..Material.Material import Material
from ..Section.Section import Section
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, CLOSEST, OFF, SymbolicConstant


@abaqus_class_doc
class OdbBase:
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    #: A Boolean specifying whether the output database was opened with read-only access.
    isReadOnly: Boolean = OFF

    #: A repository of Amplitude objects.
    amplitudes: Dict[str, Amplitude] = {}

    #: A repository of Filter objects.
    filters: Dict[str, Filter] = {}

    #: An :py:class:`~abaqus.Odb.OdbAssembly.OdbAssembly` object.
    rootAssembly: OdbAssembly = OdbAssembly()

    #: A :py:class:`~abaqus.Odb.JobData.JobData` object.
    jobData: JobData = JobData()

    #: A repository of OdbPart objects.
    parts: Dict[str, OdbPart] = {}

    #: A repository of Material objects.
    materials: Dict[str, Material] = {}

    #: A repository of OdbStep objects.
    steps: Dict[str, OdbStep] = {}

    #: A repository of Section objects.
    sections: Dict[str, Section] = {}

    #: A repository of SectionCategory objects.
    sectionCategories: Dict[str, SectionCategory] = {}

    #: A :py:class:`~abaqus.Odb.SectorDefinition.SectorDefinition` object.
    sectorDefinition: SectorDefinition = SectorDefinition()

    #: A :py:class:`~abaqus.Odb.UserData.UserData` object.
    userData: UserData = UserData()

    #: A :py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` object.
    customData: RepositorySupport = RepositorySupport()

    #: A repository of Profile objects.
    profiles: Dict[str, Profile] = {}

    @abaqus_method_doc
    def __init__(
        self, name: str, analysisTitle: str = "", description: str = "", path: str = ""
    ):
        """This method creates a new Odb object.

        .. note:: 
            This function can be accessed by::

                session.Odb

        Parameters
        ----------
        name
            A String specifying the repository key.
        analysisTitle
            A String specifying the title of the output database. The default value is an empty
            string.
        description
            A String specifying the description of the output database. The default value is an
            empty string.
        path
            A String specifying the path to the file where the new output database (.odb ) file will
            be written. The default value is an empty string.

        Returns
        -------
        Odb
            An :py:class:`~abaqus.Odb.Odb.Odb` object.
        """
        ...

    @abaqus_method_doc
    def close(self):
        """This method closes an output database."""
        ...

    @abaqus_method_doc
    def getFrame(self, frameValue: str, match: Literal[C.BEFORE, C.EXACT, C.AFTER, C.CLOSEST] = CLOSEST):
        """This method returns the frame at the specified time, frequency, or mode. It will not
        interpolate values between frames. The method is not applicable to an Odb object
        containing steps with different domains or to an Odb object containing a step with load
        case specific data.

        Parameters
        ----------
        frameValue
            A Double specifying the value at which the frame is required. **frameValue** can be the
            total time or frequency.
        match
            A SymbolicConstant specifying which frame to return if there is no frame at the exact
            frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is
            CLOSEST.When **match** = CLOSEST, Abaqus returns the closest frame. If the frame value
            requested is exactly halfway between two frames, Abaqus returns the frame after the
            value.When **match** = EXACT, Abaqus raises an exception if the exact frame value does not
            exist.

        Returns
        -------
        OdbFrame
            An :py:class:`~abaqus.Odb.OdbFrame.OdbFrame` object.

        Raises
        ------
        OdbError: Frame not found
            If the exact frame is not found.
        """
        ...

    @abaqus_method_doc
    def save(self):
        """This method saves output to an output database (.odb ) file.

        Raises
        ------
        OdbError
            Database save failed. The database was opened as read-only. Modification of data is
            not permitted.
        """
        ...

    @abaqus_method_doc
    def update(self):
        """This method is used to update an Odb object in memory while an Abaqus analysis writes
        data to the associated output database. update checks if additional steps have been
        written to the output database since it was opened or last updated. If additional steps
        have been written to the output database, update adds them to the Odb object.

        Returns
        -------
        Boolean
            A Boolean specifying whether additional steps or frames were added to the Odb object.
        """
        ...
