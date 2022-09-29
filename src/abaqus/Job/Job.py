from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .MessageArray import MessageArray
from ..UtilityAndView.abaqusConstants import (ANALYSIS, Boolean, DEFAULT, DOMAIN, OFF, ON,
                                              PERCENTAGE, SINGLE, SymbolicConstant)


@abaqus_class_doc
class Job:
    """The Job object is the abstract base type for other Job objects. The Job object has no
    explicit constructor. The methods and members of the Job object are common to all
    objects derived from Job.

    .. note:: 
        This object can be accessed by::

            import job
            mdb.coexecutions[name].jobs[name]
            mdb.jobs[name]

        The corresponding analysis keywords are:

        - HEADING
        - PREPRINT
    """

    #: A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
    #: name.
    name: str = ""

    #: A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
    #: SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS.If the object has the
    #: type JobFromInputFile, **type** = RESTART is not available.
    type: SymbolicConstant = ANALYSIS

    #: An Int specifying the number of hours to wait before submitting the job. This argument
    #: is ignored if **queue** is set. The default value is 0.This argument works in conjunction
    #: with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.
    waitHours: int = 0

    #: An Int specifying the number of minutes to wait before submitting the job. This argument
    #: is ignored if **queue** is set. The default value is 0.This argument works in conjunction
    #: with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.
    waitMinutes: int = 0

    #: An Int specifying the number of CPUs to use for this analysis if parallel processing is
    #: available. Possible values are **numCpus** >> 0. The default value is 1.
    numCpus: int = 1

    #: An Int specifying the amount of memory available to Abaqus analysis. The value should be
    #: expressed in the units supplied in **memoryUnits**. The default value is 90.
    memory: int = 90

    #: A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
    #: analysis. Possible values are PERCENTAGE, MEGA_BYTES, and GIGA_BYTES. The default value
    #: is PERCENTAGE.
    memoryUnits: SymbolicConstant = PERCENTAGE

    #: A Boolean specifying whether to retrieve the recommended memory settings from the last
    #: datacheck or analysis run and use those values in subsequent submissions. The default
    #: value is ON.
    getMemoryFromAnalysis: Boolean = ON

    #: A SymbolicConstant specifying whether to use the double precision version of
    #: Abaqus/Explicit. Possible values are SINGLE, FORCE_SINGLE, DOUBLE,
    #: DOUBLE_CONSTRAINT_ONLY, and DOUBLE_PLUS_PACK. The default value is SINGLE.
    explicitPrecision: SymbolicConstant = SINGLE

    #: A SymbolicConstant specifying the precision of the nodal output written to the output
    #: database. Possible values are SINGLE and FULL. The default value is SINGLE.
    nodalOutputPrecision: SymbolicConstant = SINGLE

    #: A SymbolicConstant specifying the parallelization method for Abaqus/Explicit.
    #: Possible values are LOOP and DOMAIN. The default value is LOOP.
    parallelizationMethodExplicit: SymbolicConstant = LOOP

    #: An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
    #: **parallelizationMethodExplicit** = DOMAIN, **numDomains** must be a multiple of **numCpus**.
    #: The default value is 1.
    numDomains: int = 1

    #: A Boolean specifying whether to activate dyanmic load balancing for jobs running on
    #: multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.
    activateLoadBalancing: Boolean = OFF

    #: A SymbolicConstant specifying whether an analysis is decomposed into threads or into
    #: multiple processes that communicate through a message passing interface (MPI). Possible
    #: values are DEFAULT, THREADS,MPI, and HYBRID. The default value is DEFAULT.
    multiprocessingMode: SymbolicConstant = DEFAULT

    #: An Int specifying the number of threads per MPI process to use for this analysis if
    #: parallel processing is available. Possible values are **numThreadsPerMpiProcess** >> 0.
    #: The default value is 1.
    numThreadsPerMpiProcess: int = 1

    #: A SymbolicConstant specifying whether the job will be analyzed by Abaqus/Standard or
    #: Abaqus/Explicit. Possible values are STANDARD, EXPLICIT, and UNKNOWN.If the object has
    #: the type JobFromInputFile, **analysis** = UNKNOWN.
    analysis: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the status of the analysis. Possible values are SUBMITTED,
    #: RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK_RUNNING, and CHECK_COMPLETED.If the
    #: **message** member is empty, **status** is set to NONE.
    status: Optional[SymbolicConstant] = None

    #: A String specifying the name of the queue to which to submit the job. The default value
    #: is an empty string.Note:You can use the **queue** argument when creating a Job object on a
    #: Windows workstation; however, remote queues are available only on Linux platforms.
    queue: str = ""

    #: A String specifying the time at which to submit the job. If **queue** is empty, the string
    #: syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
    #: valid according to the system administrator. The default value is an empty
    #: string.Note:You can use the **atTime** argument when creating a Job object on a Windows
    #: workstation; however, the `at` command is available only on Linux platforms.
    atTime: str = ""

    #: A String specifying the location of the scratch directory. The default value is an empty
    #: string.
    scratch: str = ""

    #: A String specifying the file containing the user's subroutine definitions. The default
    #: value is an empty string.
    userSubroutine: str = ""

    #: A :py:class:`~abaqus.Job.MessageArray.MessageArray` object specifying the messages received during an analysis.
    messages: MessageArray = []

    #: A tuple of Strings specifying the environment variables and their values.
    environment: tuple = ()

    #: A SymbolicConstant specifying the type of license type being used in the case of the
    #: DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
    #: value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
    #: available.
    licenseType: SymbolicConstant = DEFAULT

    @abaqus_method_doc
    def kill(self):
        """This method kills the analysis of a job."""
        ...

    @abaqus_method_doc
    def submit(
        self,
        consistencyChecking: Boolean = ON,
        datacheckJob: Boolean = False,
        continueJob: Boolean = False,
    ):
        """This method submits a job for analysis.

        Parameters
        ----------
        consistencyChecking
            A Boolean specifying whether to perform consistency checking for the job. The default
            value is ON. It is not recommended to turn the consistency checking off unless you are
            absolutely sure the model is consistent.
        datacheckJob
            A Boolean specifying whether to run the job as a datacheck analysis. The default value
            is False. The datacheckJob and continueJob arguments cannot both be True.
        continueJob
            A Boolean specifying whether to run the job as a continuation analysis. The default
            value is False. The datacheckJob and continueJob arguments cannot both be True.
        """
        ...

    @abaqus_method_doc
    def waitForCompletion(self):
        """This method interrupts the execution of the script until the end of the analysis. If you
        call the waitForCompletion method and the **status** member is neither SUBMITTED nor
        RUNNING, Abaqus assumes the analysis has either completed or aborted and returns
        immediately.
        """
        ...
