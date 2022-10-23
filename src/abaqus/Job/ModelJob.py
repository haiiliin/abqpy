from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Job import Job
from .MessageArray import MessageArray
from ..UtilityAndView.abaqusConstants import ANALYSIS, Boolean, DEFAULT, DOMAIN, LOOP, OFF, ON, PERCENTAGE, SINGLE
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ModelJob(Job):
    """The ModelJob object defines a Job object which analyzes a model on a model database
    (MDB).
    The ModelJob object is derived from the Job object.

    .. note::
        This object can be accessed by::

            import job
            mdb.adaptivityProcesses[name].job
            mdb.jobs[name]
    """

    #: A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
    #: name.
    name: str = ""

    #: A Boolean specifying whether an echo of the input data is printed. The default value is
    #: OFF.
    echoPrint: Boolean = OFF

    #: A Boolean specifying whether contact constraint data are printed. The default value is
    #: OFF.
    contactPrint: Boolean = OFF

    #: A Boolean specifying whether model definition data are printed. The default value is
    #: OFF.
    modelPrint: Boolean = OFF

    #: A Boolean specifying whether history data are printed. The default value is OFF.
    historyPrint: Boolean = OFF

    #: A String specifying the name of the model to be analyzed or a Model object specifying
    #: the model to be analyzed.
    model: str = ""

    #: A String specifying a description of the job.
    description: str = ""

    #: A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
    #: SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS. If the object has the
    #: type JobFromInputFile, **type** = RESTART is not available.
    type: Literal[C.ANALYSIS, C.SYNTAXCHECK, C.RECOVER, C.RESTART] = ANALYSIS

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
    memoryUnits: Literal[C.PERCENTAGE, C.MEGA_BYTES, C.GIGA_BYTES] = PERCENTAGE

    #: A Boolean specifying whether to retrieve the recommended memory settings from the last
    #: datacheck or analysis run and use those values in subsequent submissions. The default
    #: value is ON.
    getMemoryFromAnalysis: Boolean = ON

    #: A SymbolicConstant specifying whether to use the double precision version of
    #: Abaqus/Explicit. Possible values are SINGLE, FORCE_SINGLE, DOUBLE,
    #: DOUBLE_CONSTRAINT_ONLY, and DOUBLE_PLUS_PACK. The default value is SINGLE.
    explicitPrecision: Literal[
        C.SINGLE, C.FORCE_SINGLE, C.DOUBLE, C.DOUBLE_CONSTRAINT_ONLY, C.DOUBLE_PLUS_PACK
    ] = SINGLE

    #: A SymbolicConstant specifying the precision of the nodal output written to the output
    #: database. Possible values are SINGLE and FULL. The default value is SINGLE.
    nodalOutputPrecision: Literal[C.SINGLE, C.FULL] = SINGLE

    #: A SymbolicConstant specifying the parallelization method for Abaqus/Explicit.
    #: Possible values are LOOP and DOMAIN. The default value is LOOP.
    parallelizationMethodExplicit: Literal[C.LOOP, C.DOMAIN] = LOOP

    #: An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
    #: **parallelizationMethodExplicit** = DOMAIN, **numDomains** must be a multiple of **numCpus**.
    #: The default value is 1.
    numDomains: int = 1

    #: A Boolean specifying whether to activate dyanmic load balancing for jobs running on
    #: multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.
    activateLoadBalancing: Boolean = OFF

    #: A SymbolicConstant specifying whether an analysis is decomposed into threads or into
    #: multiple processes that communicate through a message passing interface (MPI). Possible
    #: values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.
    multiprocessingMode: Literal[C.DEFAULT, C.THREADS, C.MPI] = DEFAULT

    #: A SymbolicConstant specifying whether the job will be analyzed by Abaqus/Standard or
    #: Abaqus/Explicit. Possible values are STANDARD, EXPLICIT, and UNKNOWN.If the object has
    #: the type JobFromInputFile, **analysis** = UNKNOWN.
    analysis: Optional[Literal[C.STANDARD, C.EXPLICIT, C.UNKNOWN]] = None

    #: A SymbolicConstant specifying the status of the analysis. Possible values are SUBMITTED,
    #: RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK_RUNNING, and CHECK_COMPLETED.If the
    #: **message** member is empty, **status** is set to NONE.
    status: Optional[
        Literal[C.SUBMITTED, C.RUNNING, C.ABORTED, C.TERMINATED, C.COMPLETED, C.CHECK_RUNNING, C.CHECK_COMPLETED]
    ] = None

    #: A String specifying the name of the queue to which to submit the job. The default value
    #: is an empty string.Note:You can use the **queue** argument when creating a Job object on a
    #: Windows workstation; however, remote queues are available only on Linux platforms.
    queue: Optional[str] = ""

    #: A String specifying the time at which to submit the job. If **queue** is empty, the string
    #: syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
    #: valid according to the system administrator. The default value is an empty
    #: string.Note:You can use the **atTime** argument when creating a Job object on a Windows
    #: workstation; however, the `at` command is available only on Linux platforms.
    atTime: Optional[str] = ""

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

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        model: str,
        description: str = "",
        type: Literal[C.ANALYSIS, C.SYNTAXCHECK, C.RECOVER, C.RESTART] = ANALYSIS,
        queue: Optional[str] = "",
        waitHours: int = 0,
        waitMinutes: int = 0,
        atTime: Optional[str] = "",
        echoPrint: Boolean = OFF,
        contactPrint: Boolean = OFF,
        modelPrint: Boolean = OFF,
        historyPrint: Boolean = OFF,
        scratch: str = "",
        userSubroutine: str = "",
        numCpus: int = 1,
        memory: int = 90,
        memoryUnits: Literal[C.PERCENTAGE, C.MEGA_BYTES, C.GIGA_BYTES] = PERCENTAGE,
        explicitPrecision: Literal[
            C.SINGLE, C.FORCE_SINGLE, C.DOUBLE, C.DOUBLE_CONSTRAINT_ONLY, C.DOUBLE_PLUS_PACK
        ] = SINGLE,
        nodalOutputPrecision: Literal[C.SINGLE, C.FULL] = SINGLE,
        parallelizationMethodExplicit: Literal[C.LOOP, C.DOMAIN] = DOMAIN,
        numDomains: int = 1,
        activateLoadBalancing: Boolean = OFF,
        multiprocessingMode: Literal[C.DEFAULT, C.THREADS, C.MPI] = DEFAULT,
        *args,
        **kwargs,
    ):
        """This method creates an analysis job using a model on a model database (MDB) for the
        model definition.

        .. note::
            This function can be accessed by::

                mdb.Job

        Parameters
        ----------
        name
            A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
            name.
        model
            A String specifying the name of the model to be analyzed or a Model object specifying
            the model to be analyzed.
        description
            A String specifying a description of the job.
        type
            A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
            SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS.If the object has the
            type JobFromInputFile, **type** = RESTART is not available.
        queue
            A String specifying the name of the queue to which to submit the job. The default value
            is an empty string.Note:You can use the **queue** argument when creating a Job object on a
            Windows workstation; however, remote queues are available only on Linux platforms.
        waitHours
            An Int specifying the number of hours to wait before submitting the job. This argument
            is ignored if **queue** is set. The default value is 0.This argument works in conjunction
            with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.
        waitMinutes
            An Int specifying the number of minutes to wait before submitting the job. This argument
            is ignored if **queue** is set. The default value is 0.This argument works in conjunction
            with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.
        atTime
            A String specifying the time at which to submit the job. If **queue** is empty, the string
            syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be
            valid according to the system administrator. The default value is an empty
            string.Note:You can use the **atTime** argument when creating a Job object on a Windows
            workstation; however, the `at` command is available only on Linux platforms.
        echoPrint
            A Boolean specifying whether an echo of the input data is printed. The default value is
            OFF.
        contactPrint
            A Boolean specifying whether contact constraint data are printed. The default value is
            OFF.
        modelPrint
            A Boolean specifying whether model definition data are printed. The default value is
            OFF.
        historyPrint
            A Boolean specifying whether history data are printed. The default value is OFF.
        scratch
            A String specifying the location of the scratch directory. The default value is an empty
            string.
        userSubroutine
            A String specifying the file containing the user's subroutine definitions. The default
            value is an empty string.
        numCpus
            An Int specifying the number of CPUs to use for this analysis if parallel processing is
            available. Possible values are **numCpus** >> 0. The default value is 1.
        memory
            An Int specifying the amount of memory available to Abaqus analysis. The value should be
            expressed in the units supplied in **memoryUnits**. The default value is 90.
        memoryUnits
            A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
            analysis. Possible values are PERCENTAGE, MEGA_BYTES, and GIGA_BYTES. The default value
            is PERCENTAGE.
        explicitPrecision
            A SymbolicConstant specifying whether to use the double precision version of
            Abaqus/Explicit. Possible values are SINGLE, FORCE_SINGLE, DOUBLE,
            DOUBLE_CONSTRAINT_ONLY, and DOUBLE_PLUS_PACK. The default value is SINGLE.
        nodalOutputPrecision
            A SymbolicConstant specifying the precision of the nodal output written to the output
            database. Possible values are SINGLE and FULL. The default value is SINGLE.
        parallelizationMethodExplicit
            A SymbolicConstant specifying the parallelization method for Abaqus/Explicit.
            Possible values are LOOP and DOMAIN. The default value is LOOP.
        numDomains
            An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
            **parallelizationMethodExplicit** = DOMAIN, **numDomains** must be a multiple of **numCpus**.
            The default value is 1.
        activateLoadBalancing
            A Boolean specifying whether to activate dyanmic load balancing for jobs running on
            multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.
        multiprocessingMode
            A SymbolicConstant specifying whether an analysis is decomposed into threads or into
            multiple processes that communicate through a message passing interface (MPI). Possible
            values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.

        Returns
        -------
        ModelJob
            A :py:class:`~abaqus.Job.ModelJob.ModelJob` object.
        """
        ...

    @abaqus_method_doc
    def writeInput(self, consistencyChecking: Boolean = ON):
        """This method writes an input file.

        Parameters
        ----------
        consistencyChecking
            A Boolean specifying whether to perform consistency checking for the job. The default
            value is ON.It is not recommended to turn the consistency checking off unless you are
            absolutely sure the model is consistent.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ModelJob object."""
        ...
