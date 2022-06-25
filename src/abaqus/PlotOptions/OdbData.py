from abaqusConstants import *
from .CouplingConstraint import CouplingConstraint
from .HistoryVariable import HistoryVariable
from .MpcConstraint import MpcConstraint
from .OdbDataDatumCsys import OdbDataDatumCsys
from .OdbDataElementSet import OdbDataElementSet
from .OdbDataInstance import OdbDataInstance
from .OdbDataMaterial import OdbDataMaterial
from .OdbDataNodeSet import OdbDataNodeSet
from .OdbDataSection import OdbDataSection
from .OdbDataStep import OdbDataStep
from .OdbDataSurfaceSet import OdbDataSurfaceSet
from .OdbDiagnosticData import OdbDiagnosticData
from .RigidBodyConstraint import RigidBodyConstraint
from .TieConstraint import TieConstraint


class OdbData:
    """The OdbData object stores non persistent values and attributes associated with an open
    odb for the given session. The OdbData object has no constructor. Abaqus creates the
    **odbData** repository when you import the Visualization module. Abaqus creates a OdbData
    object when an odb is opened.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.odbData[name]
    """

    #: A tuple specifying the active frames, or the SymbolicConstant ALL. Each item in the
    #: sequence is a tuple defining the stepName followed by a sequence of expressions
    #: specifying frame numbers. The expression can be any of the following:
    #: - An Int specifying a single frame number; for example, `1`.
    #: - A String specifying a single frame number ; for example, `'7'`.
    #: - A String specifying a sequence of frame numbers; for example, `'3:5'` and `'3:15:3'`.
    #: For these expressions a negative number will indicate reverse numbering: -1 is the last
    #: frame of the step, -2 is the one before the last frame. Frame numbering starts at 0.
    activeFrames: SymbolicConstant = None

    #: A tuple of (String, Float) tuples specifying the stepName and the stepPeriod.
    #: Alternatively, this member may take the value ODB_VALUES.
    stepPeriods: float = None

    #: A repository of HistoryVariable objects specifying the history request label. The
    #: repository is read-only.
    historyVariables: dict[str, HistoryVariable] = dict[str, HistoryVariable]()

    #: A repository of OdbDataStep objects specifying the list of steps. The repository is
    #: read-only.
    steps: dict[str, OdbDataStep] = dict[str, OdbDataStep]()

    #: A repository of OdbDataInstance objects specifying the list of instances. The repository
    #: is read-only.
    instances: dict[str, OdbDataInstance] = dict[str, OdbDataInstance]()

    #: A repository of OdbDataMaterial objects specifying the list of materials. The repository
    #: is read-only.
    materials: dict[str, OdbDataMaterial] = dict[str, OdbDataMaterial]()

    #: A repository of OdbDataSection objects specifying the list of sections. The repository
    #: is read-only.
    sections: dict[str, OdbDataSection] = dict[str, OdbDataSection]()

    #: A repository of OdbDataElementSet objects specifying the list of element sets. The
    #: repository is read-only.
    elementSets: dict[str, OdbDataElementSet] = dict[str, OdbDataElementSet]()

    #: A repository of OdbDataNodeSet objects specifying the list of node sets. The repository
    #: is read-only.
    nodeSets: dict[str, OdbDataNodeSet] = dict[str, OdbDataNodeSet]()

    #: A repository of OdbDataSurfaceSet objects specifying the list of surface sets. The
    #: repository is read-only.
    surfaceSets: dict[str, OdbDataSurfaceSet] = dict[str, OdbDataSurfaceSet]()

    #: A repository of OdbDataDatumCsys objects specifying the list of coordinate systems
    #: defined in the model. The repository is read-only.
    datumCsyses: dict[str, OdbDataDatumCsys] = dict[str, OdbDataDatumCsys]()

    #: A repository of CouplingConstraint objects specifying the list of kinematic couplings.
    #: The repository is read-only.
    kinematicCouplings: dict[str, CouplingConstraint] = dict[str, CouplingConstraint]()

    #: A repository of CouplingConstraint objects specifying the list of distributing
    #: couplings. The repository is read-only.
    distributingCouplings: dict[str, CouplingConstraint] = dict[
        str, CouplingConstraint
    ]()

    #: A repository of CouplingConstraint objects specifying the list of shellsolid couplings.
    #: The repository is read-only.
    shellSolidCouplings: dict[str, CouplingConstraint] = dict[str, CouplingConstraint]()

    #: A repository of RigidBodyConstraint objects specifying the list of rigid body
    #: constraints. The repository is read-only.
    rigidbodies: dict[str, RigidBodyConstraint] = dict[str, RigidBodyConstraint]()

    #: A repository of MpcConstraint objects specifying the list of multipoint constraints. The
    #: repository is read-only.
    multiPointConstraints: dict[str, MpcConstraint] = dict[str, MpcConstraint]()

    #: A repository of TieConstraint objects specifying the list of Tie constraints. The
    #: repository is read-only.
    ties: dict[str, TieConstraint] = dict[str, TieConstraint]()

    #: An :py:class:`~abaqus.PlotOptions.OdbDiagnosticData.OdbDiagnosticData` object.
    diagnosticData: OdbDiagnosticData = OdbDiagnosticData()

    def setValues(self, activeFrames: SymbolicConstant = None, stepPeriods: tuple = ()):
        """This method modifies the OdbData object.

        Parameters
        ----------
        activeFrames
            A sequence specifying the active frames, or the SymbolicConstant ALL. Each item in the
            sequence is a tuple defining the stepName followed by a sequence of expressions
            specifying frame numbers. The expression can be any of the following:An Int specifying a
            single frame number; for example, `1`.A String specifying a single frame number ; for
            example, `'7'`.A String specifying a sequence of frame numbers; for example, `'3:5'` and
            `'3:15:3'`.For these expressions a negative number will indicate reverse numbering: -1
            is the last frame of the step, -2 is the one before the last frame. Frame numbering
            starts at 0.
        stepPeriods
            A sequence of (String, Float) sequences specifying the stepName and the stepPeriod.
            Alternatively, this member may take the value ODB_VALUES.
        """
        pass
