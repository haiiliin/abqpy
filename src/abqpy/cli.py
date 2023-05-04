from __future__ import annotations

import os
import warnings


class AbqpyCLI:
    """The abqpy command line interface"""

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
        """Run Abaqus/CAE command line interface.

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

    def python(
        self,
        script: str,
        *args,
        sim: str = None,
        log: str = None,
        **kwargs,
    ):
        """Run Abaqus Python command line interface.

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
