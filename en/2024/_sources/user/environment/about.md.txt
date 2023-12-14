# About the Abaqus Python development environment

The Abaqus PDE is a separate application that you can access from within Abaqus/CAE or launch independently to work on Python scripts.

It is intended primarily for use with scripts that use the Abaqus/CAE graphical user interface (GUI) or kernel commands, including plug-ins, but you can also use it to work on scripts that are unrelated to Abaqus. The Abaqus PDE also enables you to set breakpoints to pause script execution at a particular line in any Python script, including an Abaqus plug-in.

{numref}`cmd-pde-nls` shows a `.guiLog` file in the Abaqus PDE. The script creates an extruded solid rectangular part named box1 and was recorded by logging the actions to complete the task in the Abaqus/CAE user interface.

(cmd-pde-nls)=

```{figure} /images/cmd-pde-nls.png
:align: center
:width: 100%

The Abaqus PDE.
```

The PDE controls allow you to complete the following tasks:

- Open `.guiLog`, `.py`, and other Python scripts
- Designate an open file or open another file as the main file for testing
- Open recently used files, including modules called by the main file
- Edit scripts
- Reload modules after editing a plug-in
- Record `.guiLog` files from Abaqus/CAE
- Run scripts that use the Abaqus/CAE user interface, the Abaqus scripting commands, or general Python commands
- Add (or ignore) breakpoints in a script
- Add a breakpoint in any Python code executed in Abaqus/CAE, such as plug-ins
- Add a delay between executing steps
- Step through scripts (trace the execution), including plug-in modules and custom startup modules
- Change options for recording `.guiLog` scripts and animating (highlighting) traced files

The following sections contain detailed information about each of the functions in the PDE:

- {doc}`pde-basics`
- {doc}`use-pde`
