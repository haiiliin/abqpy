import argparse
import os

epilog = """
Options
=======
The default execution for abaqus command line options is to use `-n` (noGUI mode)
with no additional command line options.

When using abaqus command line options (`-g`, `-n`, `-p`) together with the python 
`script`, and the script is passed after abaqus command line options, you may need 
to specify `--` before the script filename, to prevent `abqpy` from attempting to 
parse it to abaqus. That is not necessary if you pass the filename before abaqus 
command line options.

If you pass N arguments to your python script with the `args` option, beware that the 
abaqus python interpreter will not access them in `sys.argv[1:N]`, but `sys.argv[N:-1]`, 
because abaqus command already parses some arguments to its python interpreter, depending 
on the chosen options. Please, refer to abaqus documentation for details.

Possible `abaqus cae` command line options:

    database=database-file
    replay=replay-file
    recover=journal-file
    startup=startup-file
    noenvstartup
    noSavedOptions
    noSavedGuiPrefs
    noStartupDialog
    custom=script-file
    guiTester=GUI-script
    guiRecord
    guiNoRecord
    
Possible `abaqus python` command line options:

    sim=sim_file_name
    log=log_file_name

Please, refer to abaqus documentation for details in each of the above option.

"""


def cli():
    parser = argparse.ArgumentParser(
        description="The abqpy command line interface",
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "script", metavar="script", type=str, nargs="?", help="the python script to run"
    )
    parser.add_argument(
        "args", nargs="*", help="arguments that will be passed to the python script",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-g",
        "--cae-gui",
        dest="gui",
        nargs="*",
        metavar="options",
        help="command line options used to run abaqus cae command with the graphical user interface (GUI mode)",
    )
    group.add_argument(
        "-n",
        "--cae-nogui",
        dest="nogui",
        nargs="*",
        metavar="options",
        help="command line options used to run abaqus cae command without the graphical user interface (noGUI mode)",
    )
    group.add_argument(
        "-p",
        "--python",
        dest="python",
        nargs="*",
        metavar="options",
        help="command line options used to run abaqus python command",
    )
    parser.add_argument(
        "--",
        dest="sep",
        action="store_true",
        help="argument to pass the script after abaqus command line options",
    )
    args = parser.parse_args()

    abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
    proc = "cae"
    mode = f"noGUI={args.script}" if args.script else "noGUI"
    sep = "--" if args.args else ""
    options = args.gui or args.nogui or args.python or ""
    if args.gui is not None:
        mode = f"script={args.script}" if args.script else ""
    elif args.python is not None:
        proc = "python"
        sep = ""
        mode = f"{args.script}" if args.script else ""

    cmd = f"{abaqus} {proc} {mode} {' '.join(options)} {sep} {' '.join(args.args)}".strip()
    message = f"Running the following abaqus command: {cmd}"
    print("", "-" * len(message), message, "-" * len(message), sep="\n")
    os.system(cmd)


if __name__ == "__main__":
    cli()
