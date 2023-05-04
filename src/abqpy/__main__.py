import os

import fire


class AbqpyCLI:
    """The abqpy command line interface"""

    def run(self, cmd: str):  # noqa
        """Run custom command."""
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
        options = [f"script={script}" if gui else f"noGUI={script}"]
        for option in ["database", "replay", "recover"]:
            if locals()[option]:
                options.append(f"{option}={locals()[option]}")
        for option in ["noenvstartup", "noSavedOptions", "noStartupDialog", "guiRecord", "guiNoRecord"]:
            if locals()[option]:
                options.append(option)
        options = " ".join(options)
        args = " ".join(args)
        sep = "--" if args else ""

        # Execute command
        abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
        self.run(f"{abaqus} cae {options} {sep} {args}".rstrip())

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
        options = [script]
        for option in ["sim", "log"]:
            if locals()[option]:
                options.append(f"{option}={locals()[option]}")
        options = " ".join(options)
        args = " ".join(args)

        # Execute command
        abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
        self.run(f"{abaqus} python {options} {args}".rstrip())


def cli():
    """The abqpy command line interface"""
    fire.Fire(AbqpyCLI)


if __name__ == "__main__":
    cli()
