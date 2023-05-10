from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import (
    ABAQUS,
    ANALYSIS,
    DEFAULT,
    ON,
    Boolean,
    SymbolicConstant,
)
from .Job import Job


@abaqus_class_doc
class Coexecution:
    """The Coexecution object contains a set of jobs as associated parameters to define a co-simulation
    analysis.

    .. note::
        This object can be accessed by::

            import job
            mdb.coexecutions[name]

        The corresponding analysis keywords are:

        - HEADING
        - PREPRINT
    """

    #: A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
    #: name.
    name: str = ""

    #: A SymbolicConstant specifying the type of analysis to execute for the co-execution.
    #: Possible values are ANALYSIS, SYNTAXCHECK, RECOVER, and RESTART. The default value is
    #: ANALYSIS.
    type: SymbolicConstant = ANALYSIS

    #: A SymbolicConstant specifying the analysis product type of the main model for the
    #: co-execution. The default value is ABAQUS.
    #:
    #: .. versionchanged:: 2022
    #:     The ``masterAnalysisProduct`` attribute was changed to ``mainAnalysisProduct``.
    mainAnalysisProduct: SymbolicConstant = ABAQUS

    #: An Int specifying the number of hours to wait before submitting the co-execution. This
    #: argument is ignored if **queue** is set. The default value is 0.This argument works in
    #: conjunction with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.
    waitHours: int = 0

    #: An Int specifying the number of minutes to wait before submitting the job. This argument
    #: is ignored if **queue** is set. The default value is 0.This argument works in conjunction
    #: with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.
    waitMinutes: int = 0

    #: A SymbolicConstant specifying the status of the co-execution. Possible values are
    #: SUBMITTED, RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK_SUBMITTED, CHECK_RUNNING, and
    #: CHECK_COMPLETED.If the **message** member of all the jobs are empty, **status** is set to
    #: NONE.
    status: Optional[SymbolicConstant] = None

    #: A String specifying the name of the queue to which to submit the co-execution. The
    #: default value is an empty string. Note: You can use the **queue** argument when creating a
    #: Coexecution object on a Windows workstation; however, remote queues are available only
    #: on Linux platforms.
    queue: str = ""

    #: A String specifying the time at which to submit the co-execution. If **queue** is empty,
    #: the string syntax must be valid for the Linux ``at`` command. If **queue** is set, the
    #: syntax must be valid according to the system administrator. The default value is an
    #: empty string. Note: You can use the **atTime** argument when creating a Coexecution object
    #: on a Windows workstation; however, the ``at`` command is available only on Linux
    #: platforms.
    atTime: str = ""

    #: A repository of Job objects specifying the jobs that comprise this co-execution.
    jobs: Dict[str, Job] = {}

    #: A tuple of Strings specifying the names of the secondary models for the co-execution.
    #:
    #: .. versionchanged:: 2022
    #:     The ``slaveModels`` attribute was changed to ``secondaryModels``.
    secondaryModels: tuple = ()

    #: A tuple of SymbolicConstants specifying the analysis product types of the secondary
    #: models for the co-execution. The default value is an empty sequence.
    #:
    #: .. versionchanged:: 2022
    #:     The ``slaveAnalysisProducts`` attribute was changed to ``secondaryAnalysisProducts``.
    secondaryAnalysisProducts: Optional[SymbolicConstant] = None

    #: A String specifying the name of the main model for the co-execution.
    #:
    #: .. versionchanged:: 2022
    #:     The ``masterModel`` attribute was changed to ``mainModel``.
    mainModel: str = ""

    #: A SymbolicConstant specifying the type of license type being used in case of DSLS
    #: SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default value
    #: is DEFAULT.If the license model is not DSLS SimUnit then the licenseType is not
    #: available.
    #:
    #: .. versionadded:: 2022
    #:     The ``licenseType`` attribute was added.
    licenseType: SymbolicConstant = DEFAULT

    @abaqus_method_doc
    def kill(self):
        """This method kills the analysis of a co-execution."""
        ...

    @abaqus_method_doc
    def submit(
        self,
        consistencyChecking: Boolean = ON,
        datacheckJob: Boolean = False,
        continueJob: Boolean = False,
    ):
        """This method submits a co-execution for analysis.

        Parameters
        ----------
        consistencyChecking
            A Boolean specifying whether to perform consistency checking for the individual jobs.
            The default value is ON. It is not recommended to turn the consistency checking off
            unless you are absolutely sure the models are all consistent.
        datacheckJob
            A Boolean specifying whether to run the co-execution as a datacheck analysis. The
            default value is False. The **datacheckJob** and **continueJob** arguments cannot both be
            True.
        continueJob
            A Boolean specifying whether to run the co-execution as a continuation analysis. The
            default value is False. The **datacheckJob** and **continueJob** arguments cannot both be
            True.
        """
        ...

    @abaqus_method_doc
    def writeInput(self, consistencyChecking: Boolean = ON):
        """This method writes an input file for each analysis in the co-execution.

        Parameters
        ----------
        consistencyChecking
            A Boolean specifying whether to perform consistency checking for the individual jobs.
            The default value is ON. It is not recommended to turn the consistency checking off
            unless you are absolutely sure the models are all consistent.
        """
        ...

    @abaqus_method_doc
    def waitForCompletion(self):
        """This method interrupts the execution of the script until the end of all the analyses.

        If you call the waitForCompletion method and the **status** member is neither SUBMITTED nor RUNNING,
        Abaqus assumes the analysis has either completed or aborted and returns immediately.
        """
        ...
