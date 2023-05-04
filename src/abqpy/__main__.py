from __future__ import annotations

import os

import fire


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
        """
        # Parse options
        options = self._parse_options(script=script if gui else None, noGUI=script if not gui else None,
                                      database=database, replay=replay, recover=recover, noenvstartup=noenvstartup,
                                      noSavedOptions=noSavedOptions, noStartupDialog=noStartupDialog,
                                      guiRecord=guiRecord, guiNoRecord=guiNoRecord)  # fmt: skip
        args = " ".join(args)
        sep = "--" if args else ""

        # Execute command
        abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
        self.run(f"{abaqus} cae {options} {sep} {args}")

    def python(
        self,
        script: str,
        *args,
        sim: str = None,
        log: str = None,
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
        """
        # Parse options
        options = self._parse_options(sim=sim, log=log)
        args = " ".join(args)

        # Execute command
        abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
        self.run(f"{abaqus} python {script} {options} {args}")


#: The abqpy command line interface, use this object to run abqpy commands from the python scripts
abaqus = AbqpyCLI()


def cli():
    """The abqpy command line interface"""
    fire.Fire(AbqpyCLI)


if __name__ == "__main__":
    cli()
