from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .JobFromInputFile import JobFromInputFile
from .ModelJob import ModelJob
from .OptimizationProcess import OptimizationProcess
from ..Mdb.MdbBase import MdbBase
from ..UtilityAndView.abaqusConstants import (
    ANALYSIS,
    Boolean,
    DEFAULT,
    DOMAIN,
    ON,
    OFF,
    ODB,
    OPT_DATASAVE_SPECIFY_CYCLE,
    PERCENTAGE,
    SINGLE,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class JobMdb(MdbBase):
    """The Mdb object is the high-level Abaqus model database. A model database stores models
    and analysis controls.

    .. note::
        This object can be accessed by::

            mdb
    """

    @abaqus_method_doc
    def Job(
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
        licenseType: Literal[C.DEFAULT, C.TOKEN, C.CREDIT] = DEFAULT,
        *args,
        **kwargs,
    ) -> ModelJob:
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
            is an empty string. Note: You can use the **queue** argument when creating a Job object on a
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
            string. Note: You can use the **atTime** argument when creating a Job object on a Windows
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
            available. Possible values are **numCpus** > 0. The default value is 1.
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
            A SymbolicConstant specifying the parallelization method for Abaqus/Explicit. This value
            is ignored for Abaqus/Standard. Possible values are DOMAIN and LOOP. The default value
            is DOMAIN.
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
        licenseType
            A SymbolicConstant specifying the type of license type being used in the case of the
            DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
            value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
            available.

            .. versionchanged:: 2022
                The `licenseType` argument was added.

        Returns
        -------
        ModelJob
            A :py:class:`~abaqus.Job.ModelJob.ModelJob` object.

        Raises
        ------
        AbaqusException
        """
        self.jobs[name] = job = ModelJob(
            name,
            model,
            description,
            type,
            queue,
            waitHours,
            waitMinutes,
            atTime,
            echoPrint,
            contactPrint,
            modelPrint,
            historyPrint,
            scratch,
            userSubroutine,
            numCpus,
            memory,
            memoryUnits,
            explicitPrecision,
            nodalOutputPrecision,
            parallelizationMethodExplicit,
            numDomains,
            activateLoadBalancing,
            multiprocessingMode,
            licenseType,
            *args,
            **kwargs,
        )
        return job

    @abaqus_method_doc
    def JobFromInputFile(
        self,
        name: str,
        inputFileName: str,
        type: Literal[C.ANALYSIS, C.SYNTAXCHECK, C.RECOVER] = ANALYSIS,
        queue: Optional[str] = "",
        waitHours: int = 0,
        waitMinutes: int = 0,
        atTime: Optional[str] = "",
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
        licenseType: Literal[C.DEFAULT, C.TOKEN, C.CREDIT] = DEFAULT,
        getMemoryFromAnalysis: Boolean = ON,
        numGPUs: int = 0,
        resultsFormat: Literal[C.ODB, C.SIM, C.BOTH] = ODB,
    ) -> JobFromInputFile:
        """This method creates an analysis job using an input file for the model definition.

        .. note::
            This function can be accessed by::

                mdb.JobFromInputFile

        Parameters
        ----------
        name
            A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
            name.
        inputFileName
            A String specifying the input file to read. Possible values are any valid file name. If
            the .inp extension is not included in the value of the argument, the system will append
            it for the user.
        type
            A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
            SYNTAXCHECK, and RECOVER. The default value is ANALYSIS.For theJobFromInputFile object,
            **type** = RESTART is not currently supported.
        queue
            A String specifying the name of the queue to which to submit the job. The default value
            is an empty string. Note:  You can use the **queue** argument when creating a Job object on
            a Windows workstation; however, remote queues are available only on Linux platforms.
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
            valid according to the system administrator. The default value is an empty string. Note: 
            You can use the **atTime** argument when creating a Job object on a Windows workstation;
            however, the `at` command is available only on Linux platforms.
        scratch
            A String specifying the location of the scratch directory. The default value is an empty
            string.
        userSubroutine
            A String specifying the file containing the user's subroutine definitions. The default
            value is an empty string.
        numCpus
            An Int specifying the number of CPUs to use for this analysis if parallel processing is
            available. Possible values are **numCpus** > 0. The default value is 1.
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
            A SymbolicConstant specifying the parallelization method for Abaqus/Explicit. This value
            is ignored for Abaqus/Standard. Possible values are DOMAIN and LOOP. The default value
            is DOMAIN.
        numDomains
            An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
            **parallelizationMethodExplicit** = DOMAIN, **numDomains** must be a multiple of **numCpus**.
            The default value is 1.
        activateLoadBalancing
            A Boolean specifying whether to activate dyanmic load balancing for jobs running on
            multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.
        multiprocessingMode
            A SymbolicConstant specifying whether an analysis is decomposed into threads or into
            multiple processes that communicate through a message
        licenseType
            A SymbolicConstant specifying the type of license type being used in the case of the
            DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
            value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
            available.
        getMemoryFromAnalysis
            A Boolean specifying whether to retrieve the recommended memory settings from the last
            datacheck or analysis run and use those values in subsequent submissions. The default
            value is ON.
        numGPUs
            An Int specifying the number of GPUs to use for this analysis if parallel processing is
            available. Possible values are **numCpus** >= 0. The default value is 0.
        resultsFormat
            This option specifies the results output format: ODB, SIM, or BOTH. The default value is ODB.
        """

        self.jobs[name] = jobFromInputFile = JobFromInputFile(
            name,
            inputFileName,
            type,
            queue,
            waitHours,
            waitMinutes,
            atTime,
            scratch,
            userSubroutine,
            numCpus,
            memory,
            memoryUnits,
            explicitPrecision,
            nodalOutputPrecision,
            parallelizationMethodExplicit,
            numDomains,
            activateLoadBalancing,
            multiprocessingMode,
            licenseType,
        )
        return jobFromInputFile

    @abaqus_method_doc
    def OptimizationProcess(
        self,
        name: str,
        model: str,
        task: str,
        prototypeJob: str,
        description: str = "",
        maxDesignCycle: int = 15,
        dataSaveFrequency: str = OPT_DATASAVE_SPECIFY_CYCLE,
        saveInitial: Boolean = True,
        saveFirst: Boolean = True,
        saveLast: Boolean = True,
        saveEvery: Optional[int] = None,
    ) -> OptimizationProcess:
        """This method creates an OptimizationProcess object.

        .. note::
            This function can be accessed by::

                mdb.OptimizationProcess

        Parameters
        ----------
        name
            A String specifying name of the optimization process.
        model
            A String specifying name of the model to be used for the optimization process.
        task
            A String specifying name of the optimization task to be used for the optimization
            process.
        prototypeJob
            A String specifying name of the job to be used as the prototype for all analysis jobs
            run by the optimization process.
        description
            A String specifying a description of the optimization process.
        maxDesignCycle
            An Int specifying the maximum number of allowed design cycles for the optimization
            process. The default value is 15.
        dataSaveFrequency
            An Enum specifying whether Abaqus should save every iteration file in the optimization
            process or a selection of iteration files saved at a user-specified frequency. If you
            set **dataSaveFrequency** = OPT_DATASAVE_EVERY_CYCLE, Abaqus saves every iteration file; if
            you set **dataSaveFrequency** = OPT_DATASAVE_SPECIFY_CYCLE, Abaqus saves iteration files
            according to the frequency defined by the **saveEvery** parameter. The default value is
            OPT_DATASAVE_SPECIFY_CYCLE.
        saveInitial
            A Boolean specifying whether the initial cycle should be saved when **dataSaveFrequency**
            is OPT_DATASAVE_SPECIFY_CYCLE. The default value is True.
        saveFirst
            A Boolean specifying whether the first cycle should be saved when **dataSaveFrequency** is
            OPT_DATASAVE_SPECIFY_CYCLE. The default value is True.
        saveLast
            A Boolean specifying whether the last cycle should be saved when **dataSaveFrequency** is
            OPT_DATASAVE_SPECIFY_CYCLE. The default value is True.
        saveEvery
            An Int specifying every nth cycle iterations to be saved when **dataSaveFrequency** is
            OPT_DATASAVE_SPECIFY_CYCLE. Abaqus saves file iterations for every nth iteration after
            iteration 1; if you set **saveEvery** = 3, Abaqus saves file iterations for cycles 1, 4, 7,
            and so on. The default value is None.

        Returns
        -------
        OptimizationProcess
            An :py:class:`~abaqus.Job.OptimizationProcess.OptimizationProcess` object.

        Raises
        ------
        AbaqusException
        """
        self.optimizationProcesses[name] = optimizationProcess = OptimizationProcess(
            name,
            model,
            task,
            prototypeJob,
            description,
            maxDesignCycle,
            dataSaveFrequency,
            saveInitial,
            saveFirst,
            saveLast,
            saveEvery,
        )
        return optimizationProcess
