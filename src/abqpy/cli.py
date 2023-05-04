from __future__ import annotations

import os
import warnings


class AbqpyCLIBase:
    """Base class for Abaqus/CAE command line interface to run Abaqus commands."""

    def _parse_options(self, **options: str | bool | None) -> str:  # noqa
        """Parse options to be passed to Abaqus/CAE command line interface. If the value is a string, the option will
        be passed as `option=value`; if the value is a boolean, the option will be passed as `option` if True, or
        ignored if False; if the value is None, the option will be ignored."""
        return " ".join([f"{key}={val}" if isinstance(val, str) else key for key, val in options.items() if val])

    def run(self, cmd: str):  # noqa
        """Run custom command."""
        cmd = cmd.strip()
        message = f"Running the following command: {cmd}"
        print("", "-" * len(message), message, "-" * len(message), sep="\n")
        os.system(cmd)

    def abaqus(self, *args):  # noqa
        """Run custom Abaqus command: `abaqus [args]`, arguments are separated by space."""
        abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")  # noqa
        options = " ".join(args)
        self.run(f"{abaqus} {options}")


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

        # Parse options
        options = self._parse_options(cpus=cpus, gpus=gpus, memory=memory, interactive=interactive,
                                      globalmodel=globalmodel, scratch=scratch)  # fmt: skip

        # Execute command
        self.abaqus("optimization", task, job, options)

    def command(self, name: str, *args, **kwargs):
        """Run any Abaqus command.

        Parameters
        ----------
        name : str
            The name of the Abaqus command to run
        args, kwargs
            The arguments to be passed to the Abaqus command
        """
        # Parse options
        options = self._parse_options(**kwargs)
        self.abaqus(name, *args, options)

    def help(self, *args, **kwargs):
        self.command("help", *args, **kwargs)

    def information(self, *args, **kwargs):
        self.command("information", *args, **kwargs)

    def whereami(self, *args, **kwargs):
        self.command("whereami", *args, **kwargs)

    def cse(self, *args, **kwargs):
        self.command("cse", *args, **kwargs)

    def cosimulation(self, *args, **kwargs):
        self.command("cosimulation", *args, **kwargs)

    def fmu(self, *args, **kwargs):
        self.command("fmu", *args, **kwargs)

    def script(self, *args, **kwargs):
        self.command("script", *args, **kwargs)

    def doc(self, *args, **kwargs):
        self.command("doc", *args, **kwargs)

    def licensing(self, *args, **kwargs):
        self.command("licensing", *args, **kwargs)

    def ascfil(self, *args, **kwargs):
        self.command("ascfil", *args, **kwargs)

    def append(self, *args, **kwargs):
        self.command("append", *args, **kwargs)

    def findkeyword(self, *args, **kwargs):
        self.command("findkeyword", *args, **kwargs)

    def fetch(self, *args, **kwargs):
        self.command("fetch", *args, **kwargs)

    def make(self, *args, **kwargs):
        self.command("make", *args, **kwargs)

    def upgrade(self, *args, **kwargs):
        self.command("upgrade", *args, **kwargs)

    def sim_version(self, *args, **kwargs):
        self.command("sim_version", *args, **kwargs)

    def odb2sim(self, *args, **kwargs):
        self.command("odb2sim", *args, **kwargs)

    def odbreport(self, *args, **kwargs):
        self.command("odbReport", *args, **kwargs)

    def restartjoin(self, *args, **kwargs):
        self.command("restartjoin", *args, **kwargs)

    def substructurecombine(self, *args, **kwargs):
        self.command("substructurecombine", *args, **kwargs)

    def substructurerecover(self, *args, **kwargs):
        self.command("substructurerecover", *args, **kwargs)

    def odbcombine(self, *args, **kwargs):
        self.command("odbcombine", *args, **kwargs)

    def networkDBConnector(self, *args, **kwargs):
        self.command("networkDBConnector", *args, **kwargs)

    def emloads(self, *args, **kwargs):
        self.command("emloads", *args, **kwargs)

    def mtxasm(self, *args, **kwargs):
        self.command("mtxasm", *args, **kwargs)

    def fromnastran(self, *args, **kwargs):
        self.command("fromnastran", *args, **kwargs)

    def tonastran(self, *args, **kwargs):
        self.command("tonastran", *args, **kwargs)

    def fromansys(self, *args, **kwargs):
        self.command("fromansys", *args, **kwargs)

    def frompamcrash(self, *args, **kwargs):
        self.command("frompamcrash", *args, **kwargs)

    def fromradioss(self, *args, **kwargs):
        self.command("fromradioss", *args, **kwargs)

    def toOutput2(self, *args, **kwargs):
        self.command("toOutput2", *args, **kwargs)

    def fromdyna(self, *args, **kwargs):
        self.command("fromdyna", *args, **kwargs)

    def tozaero(self, *args, **kwargs):
        self.command("tozaero", *args, **kwargs)

    def adams(self, *args, **kwargs):
        self.command("adams", *args, **kwargs)

    def tosimpack(self, *args, **kwargs):
        self.command("tosimpack", *args, **kwargs)

    def fromsimpack(self, *args, **kwargs):
        self.command("fromsimpack", *args, **kwargs)

    def toexcite(self, *args, **kwargs):
        self.command("toexcite", *args, **kwargs)

    def moldflow(self, *args, **kwargs):
        self.command("moldflow", *args, **kwargs)

    def encrypt(self, *args, **kwargs):
        self.command("encrypt", *args, **kwargs)

    def decrypt(self, *args, **kwargs):
        self.command("decrypt", *args, **kwargs)

    def suspend(self, *args, **kwargs):
        self.command("suspend", *args, **kwargs)

    def resume(self, *args, **kwargs):
        self.command("resume", *args, **kwargs)

    def terminate(self, *args, **kwargs):
        self.command("terminate", *args, **kwargs)

    def sysVerify(self, *args, **kwargs):
        self.command("sysVerify", *args, **kwargs)


class AbqpyCLI(AbqpyCLIBase):
    """The abqpy command line interface"""

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
