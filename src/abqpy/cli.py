from __future__ import annotations

import os
import warnings


class AbqpyCLIBase:
    """Base class for Abaqus/CAE command line interface to run Abaqus commands."""

    def _parse_options(self, **options: str | bool | None) -> str:
        """Parse options to be passed to Abaqus/CAE command line interface.

        If the value is a string, the option will
        be passed as ``option=value``; if the value is a boolean, the option will be passed as ``option`` if True, or
        ignored if False; if the value is None, the option will be ignored.
        """
        return " ".join([f"{key}={val}" if isinstance(val, str) else key for key, val in options.items() if val])

    def run(self, cmd: str):
        """Run custom command."""
        cmd = cmd.strip()
        message = f"Running the following command: {cmd}"
        print("", "-" * len(message), message, "-" * len(message), sep="\n")
        os.system(cmd)

    def abaqus(self, *args, **options):
        """Run custom Abaqus command: ``abaqus {args} {options}``, arguments are separated by space, options are
        handled by the :meth:`._parse_options` method.

        Parameters
        ----------
        args, options
            Arguments and options to be passed to the Abaqus command.
        """
        abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
        args, options = " ".join(args), self._parse_options(**options)
        self.run(f"{abaqus} {args} {options}")


class AbqpyMiscCLI(AbqpyCLIBase):
    """Less frequently used Abaqus/CAE commands."""

    def optimization(
        self,
        task: str,
        job: str,
        *,
        cpus: int = None,
        gpus: int = None,
        memory: int = None,
        interactive: bool = False,
        globalmodel: str = None,
        scratch: str = None,
        **kwargs,
    ):
        """Run Abaqus optimization command.

        Parameters
        ----------
        task : str
            The file containing the parameters that are used to execute the optimization.
        job : str
            The name of the folder in which the results of the optimization are stored.
        cpus : int, optional
            The number of processors to use during an analysis run if parallel processing is available.
        gpus : int, optional
            This acceleration of the Abaqus/Standard direct solver.
        memory : int, optional
            Maximum amount of memory or maximum percentage of the physical memory that can be allocated.
        interactive : bool, optional
            This option will cause the job to run interactively.
        globalmodel : str, optional
            The name of the global model's results file, ODB output database file, or SIM database file.
        scratch : str, optional
            The name of the directory used for scratch files.
        kwargs
            Other unrecognized keyword arguments
        """
        if kwargs:
            warnings.warn(f"Unrecognized keyword arguments: {kwargs}")

        # Execute command
        self.abaqus("optimization", task, job, cpus=cpus, gpus=gpus, memory=memory,
                    interactive=interactive, globalmodel=globalmodel, scratch=scratch)  # fmt: skip

    def help(self, *args, **options):
        self.abaqus("help", *args, **options)

    def information(self, *args, **options):
        self.abaqus("information", *args, **options)

    def whereami(self, *args, **options):
        self.abaqus("whereami", *args, **options)

    def cse(self, *args, **options):
        self.abaqus("cse", *args, **options)

    def cosimulation(self, *args, **options):
        self.abaqus("cosimulation", *args, **options)

    def fmu(self, *args, **options):
        self.abaqus("fmu", *args, **options)

    def script(self, *args, **options):
        self.abaqus("script", *args, **options)

    def doc(self, *args, **options):
        self.abaqus("doc", *args, **options)

    def licensing(self, *args, **options):
        self.abaqus("licensing", *args, **options)

    def ascfil(self, *args, **options):
        self.abaqus("ascfil", *args, **options)

    def append(self, *args, **options):
        self.abaqus("append", *args, **options)

    def findkeyword(self, *args, **options):
        self.abaqus("findkeyword", *args, **options)

    def fetch(self, *args, **options):
        self.abaqus("fetch", *args, **options)

    def make(self, *args, **options):
        self.abaqus("make", *args, **options)

    def upgrade(self, *args, **options):
        self.abaqus("upgrade", *args, **options)

    def sim_version(self, *args, **options):
        self.abaqus("sim_version", *args, **options)

    def odb2sim(self, *args, **options):
        self.abaqus("odb2sim", *args, **options)

    def odbreport(self, *args, **options):
        self.abaqus("odbReport", *args, **options)

    def restartjoin(self, *args, **options):
        self.abaqus("restartjoin", *args, **options)

    def substructurecombine(self, *args, **options):
        self.abaqus("substructurecombine", *args, **options)

    def substructurerecover(self, *args, **options):
        self.abaqus("substructurerecover", *args, **options)

    def odbcombine(self, *args, **options):
        self.abaqus("odbcombine", *args, **options)

    def networkDBConnector(self, *args, **options):
        self.abaqus("networkDBConnector", *args, **options)

    def emloads(self, *args, **options):
        self.abaqus("emloads", *args, **options)

    def mtxasm(self, *args, **options):
        self.abaqus("mtxasm", *args, **options)

    def fromnastran(self, *args, **options):
        self.abaqus("fromnastran", *args, **options)

    def tonastran(self, *args, **options):
        self.abaqus("tonastran", *args, **options)

    def fromansys(self, *args, **options):
        self.abaqus("fromansys", *args, **options)

    def frompamcrash(self, *args, **options):
        self.abaqus("frompamcrash", *args, **options)

    def fromradioss(self, *args, **options):
        self.abaqus("fromradioss", *args, **options)

    def toOutput2(self, *args, **options):
        self.abaqus("toOutput2", *args, **options)

    def fromdyna(self, *args, **options):
        self.abaqus("fromdyna", *args, **options)

    def tozaero(self, *args, **options):
        self.abaqus("tozaero", *args, **options)

    def adams(self, *args, **options):
        self.abaqus("adams", *args, **options)

    def tosimpack(self, *args, **options):
        self.abaqus("tosimpack", *args, **options)

    def fromsimpack(self, *args, **options):
        self.abaqus("fromsimpack", *args, **options)

    def toexcite(self, *args, **options):
        self.abaqus("toexcite", *args, **options)

    def moldflow(self, *args, **options):
        self.abaqus("moldflow", *args, **options)

    def encrypt(self, *args, **options):
        self.abaqus("encrypt", *args, **options)

    def decrypt(self, *args, **options):
        self.abaqus("decrypt", *args, **options)

    def suspend(self, *args, **options):
        self.abaqus("suspend", *args, **options)

    def resume(self, *args, **options):
        self.abaqus("resume", *args, **options)

    def terminate(self, *args, **options):
        self.abaqus("terminate", *args, **options)

    def sysVerify(self, *args, **options):
        self.abaqus("sysVerify", *args, **options)


class AbqpyCLI(AbqpyCLIBase):
    """The abqpy command line interface."""

    def __init__(self):
        self.misc = AbqpyMiscCLI()

    def cae(
        self,
        script: str,
        *args,
        database: str = None,
        replay: str = None,
        recover: str = None,
        gui: bool = False,
        noenvstartup: bool = False,
        noSavedOptions: bool = False,
        noStartupDialog: bool = False,
        guiRecord: bool = False,
        guiNoRecord: bool = False,
        **kwargs,
    ):
        """Run Abaqus/CAE command.

        Parameters
        ----------
        script : str
            The name of the python script to run
        args : str
            Extra arguments to be passed after the Abaqus/CAE command line options
        database : str, optional
            The name of the database file to open, by default None
        replay : str, optional
            The name of the replay file to open, by default None
        recover : str, optional
            The name of the journal file to open, by default None
        gui : bool, optional
            Run Abaqus/CAE command with the graphical user interface (GUI mode), by default False.
        noenvstartup : bool, optional
            Do not execute the Abaqus/CAE startup file, by default False
        noSavedOptions : bool, optional
            Do not use the saved options, by default False
        noStartupDialog : bool, optional
            Do not display the startup dialog, by default False
        guiRecord : bool, optional
            Record the GUI commands to a file, by default False
        guiNoRecord : bool, optional
            Do not record the GUI commands to a file, by default False
        kwargs
            Other unrecognized keyword arguments
        """
        if kwargs:
            warnings.warn(f"Unrecognized keyword arguments: {kwargs}")

        # Parse options
        options = self._parse_options(script=script if gui else None, noGUI=script if not gui else None,
                                      database=database, replay=replay, recover=recover, noenvstartup=noenvstartup,
                                      noSavedOptions=noSavedOptions, noStartupDialog=noStartupDialog,
                                      guiRecord=guiRecord, guiNoRecord=guiNoRecord)  # fmt: skip
        args = ("--", *args) if args else ()

        # Execute command
        self.abaqus("cae", options, *args)

    viewer = cae

    def python(
        self,
        script: str,
        *args,
        sim: str = None,
        log: str = None,
        **kwargs,
    ):
        """Run Abaqus/Python command.

        Parameters
        ----------
        script : str
            The name of the python script to run
        args : str
            Extra arguments to be passed after the Abaqus/CAE command line options
        sim : str, optional
            The name of the simulation file to open, by default None
        log : str, optional
            The name of the log file to open, by default None
        kwargs
            Other unrecognized keyword arguments
        """
        if kwargs:
            warnings.warn(f"Unrecognized keyword arguments: {kwargs}")

        # Parse options
        options = self._parse_options(sim=sim, log=log)

        # Execute command
        self.abaqus("python", script, options, *args)


#: The abqpy command line interface, use this object to run abqpy commands from the python scripts
abaqus = AbqpyCLI()
