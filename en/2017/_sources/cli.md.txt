# Command Line Interface

```{warning}
The command line interface is based on the [`fire`](https://github.com/google/python-fire)
package since version `20**.5.0`, and it is not compatible with the command line interface of
previous versions.
```

The default execution procedure invoked by `abqpy` inside the Python interpreter
environment where it is installed is to run one of the two following command lines:

1. When the `abaqus` module is imported for the first time:

   ```sh
   abaqus cae noGUI=script.py -- [args ...]
   ```

2. When the `odbAccess` module is imported for the first time:

   ```sh
   abaqus python script.py [args ...]
   ```

These commands lines are invoked when you run your script containing the above
statements in your installed Python interpreter, with a simple command line launch:

```sh
python script.py [args ...]
```

However, there are other execution procedures that can be run with the `abaqus`
command and also another options that could be passed to these commands. To supply
that procedures and options, `abqpy` provides two alternatives. One of them is a
separate **command line interface** (another alternative is to use an
{doc}`System Environment Variable <envvars>`).

Currently, `abqpy` command line interface provides several execution modes: **Abaqus/CAE
Execution** mode and **Abaqus Python Execution** mode, and more:

```sh
abqpy COMMAND SCRIPT <flags> [ARGS]...
```

where `COMMAND` is one of `abaqus`, `cae`, `python`, `run` or any other Abaqus commands,
`SCRIPT` is the file name of your python script, `flags` are the options that could be
passed to the command, and `ARGS` are the extra arguments to be passed after the command
line options. For details, see the [References](#references) section or run
`abqpy COMMAND --help` for help.

```{note}
For the following commands, the boolean flags can be specified with the following syntax (take `gui` as an example):

- `--gui` or `--gui=True` to set the flag to `True`;
- `--nogui` or `--gui=False` to set the flag to `False`.

See [here](https://github.com/google/python-fire/blob/master/docs/guide.md#boolean-arguments) for more detailed information.
```

## Examples

1. If you want to run you python script in Abaqus/CAE mode, you could run:

   ```sh
   abqpy cae script.py [args ...]
   ```

2. If you want to run your python script in Abaqus/CAE GUI or noGUI mode, providing
   the `database` file option, you could run:

   ```sh
   abqpy cae script.py --gui --database=file.odb [args ...] # GUI mode

   abqpy cae script.py --nogui --database=file.odb [args ...] # noGUI mode
   ```

3. If you want to run your python script in Abaqus Python Execution mode, you could run:

   ```sh
   abqpy python script.py [args ...]
   ```

4. If you want to call the cli in your python script, you could use the
   {py:obj}`abqpy.cli.abaqus` object:

   ```python
   from abqpy.cli import abaqus

   abaqus.cae("script.py", gui=True, database="file.odb")
   ```

Some modern Python IDEs allow you to customize the default python launch parameters
that will be passed to the interpreter. This feature permits to run `abqpy` command line
interface as a module script and customize your default abaqus execution procedure.

Example: In
[VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python),
you can specify the following setting:

```json
"python.terminal.launchArgs": [ "-m", "abqpy", "cae", "--gui=True" ]
```

That setting will make VS Code Python Extension run by default all python script
files in the integrated terminal with the following command line:

```sh
python -m abqpy cae --gui=True script.py [args ...]
```

Which provides a way to change the default abaqus execution procedure to GUI mode.

```{warning}
Noted that if a token other than another flag immediately follows a flag that's supposed to be a boolean,
the flag will take on the value of the token rather than the boolean value.
Thus `--gui=True` instead of `--gui` is used here to prevent this problem.
```

(references)=

## References

```{command-output} abqpy

```

### Abaqus/CAE Execution Mode

```{command-output} abqpy cae --help
:returncode: 2
```

### Abaqus Python Execution Mode

```{command-output} abqpy python --help
:returncode: 2
```

### Less Frequently Used Commands

```{command-output} abqpy misc --help

```

## Comments

<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="haiiliin/abqpy"
   issue-term="pathname"
   theme="github-light"
   label="💬 comment"
   crossorigin="anonymous"
/>
