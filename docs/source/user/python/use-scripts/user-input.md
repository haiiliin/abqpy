# Prompting the user for input

You may want to request input from a user while an Abaqus Scripting Interface script is executing. There are many reasons for requesting input; for example, to specify design parameters, to enable a macro to take action based on the input received, or to force parts of the script to be repeated. The Abaqus Scripting Interface provides three functions that request input from the user and return the data entered by the user:

- The `getInput` function requests a single input from the user from a text field in a dialog box.
- The `getInputs` function requests multiple inputs from the user from text fields in a dialog box.
- The `getWarningReply` function requests a reply to a warning message from the user from a warning dialog box.

:::{note}
Note: You cannot use a script that contains getInput, getInputs or getWarningReply if you are running the script from the command line and passing the script name to the command line options -start,-replay or -noGUI.
:::

## Requesting a single input from the user

The `getInput` function displays a dialog box in the center of the main window, and the user enters the requested value in the text field in the dialog box. The value is returned to the executing script as a String after the user presses the **\[Enter\]** key or clicks **\[OK\]**. Optionally, you can specify a default value to be displayed in the text field. The `getInput` function does not provide any error checking; it is the script author's responsibility to verify the user input. For more information, see {func}`~abaqus.UtilityAndView.User.getInput`.

The following examples illustrate the use of the `getInput` function. The first example shows a script that uses the `getInput` function to obtain a number from the user. The script then prints the square root of that number.

```python2
from abaqus import getInput
from math import sqrt
number = float(getInput('Enter a number:'))
print sqrt(number)
```

The `float` function on the third line converts the string returned by `getInput` into a floating point number. The following figure shows the dialog box that appears when this script is executed:

(utl-getinput-nls)=

:::{figure} /images/utl-getinput-nls.png
:align: center
:width: 50%
:::

The next example shows how to modify a macro recorded by the **Macro Manager** in Abaqus/CAE to use the getInput function. The following text shows a macro named `createViewport` that was recorded by Abaqus/CAE while the user created a viewport. Macros are stored in the file `abaqusMacros.py` in your local or home directory.

```python2
from abaqus import *
def createViewport():
    session.Viewport(name='Viewport: 2',
        origin=(15.0,15.0), width=145.0,
        height=90.0)
    session.viewports['Viewport: 2'].makeCurrent()
```

The following shows how you can modify the macro to accept input from the user. Default values for the viewport width and height have been added to the input request.

```python2
from abaqus import *
def createViewport():
    name = getInput('Enter viewport name:')
    prompt = 'Enter viewport width, height (mm):'
    w, h = eval(getInput(prompt, '100,50'))
    vp = session.Viewport(name=name, width=w, height=h)
    vp.restore()
    vp.makeCurrent()
```

The `eval` function in the third line of the macro converts the string returned by the `getInput` function into two integers. When you supply the default values shown in this example to the `getInput` function, the prompt and the text field in the dialog box that appears are shown in the following figure. If the user clicks **\[OK\]** or presses **\[Enter\]**, the default values are accepted and returned to the `getInput` function. If the user clicks **\[Cancel\]**, None is returned.

(utl-getinput-default-nls)=

:::{figure} /images/utl-getinput-default-nls.png
:align: center
:width: 50%
:::

## Requesting multiple inputs from the user

The `getInputs` function displays a dialog box in the center of the main window, and the user enters the requested values in text fields in the dialog box. The values are returned to the executing script as a sequence of Strings after the user clicks the **\[OK\]** button or presses **\[Enter\]**. Optionally, you can specify default values to be displayed in the text fields. For more information, see {func}`~abaqus.UtilityAndView.User.getInputs`.

The following examples illustrate the use of the `getInputs` function to obtain a sequence of numbers from the user:

```python2
from abaqus import getInputs
fields = (('Width:','10'), ('Length:', '20'), ('Height:', '30'))
length, width, height =
    getInputs(fields=fields, label='Specify block dimensions:',
        dialogTitle='Create Block', )
print length, width, height
```

The following figure shows the dialog box that these statements create:

(utl-getinputs-nls)=

:::{figure} /images/utl-getinputs-nls.png
:align: center
:width: 50%
:::

The `fields` argument to the `getInputs` method is a sequence of sequences of Strings. The inner sequence is a pair of Strings that specifies the description of the text field and the default value of the field. If the text field does not have a default value, you must specify an empty string; for example,

```python2
fields = (('Width',''), ('Length', ''), ('Height', ''))
length, width, height =
    getInputs(fields=fields, label='Specify block dimensions:')
```

The `label` argument to the `getInputs` method is an optional label that appears across the top of the dialog box. The dialogTitle argument is an optional string that appears in the title bar of the dialog box.

If the user clicks **\[Cancel\]**, the `getInputs` method returns a sequence of `None` objects. You can check the first value in the sequence to determine if the user clicked **\[Cancel\]**; for example:

```python2
fields = (('Density',''), ('Youngs modulus', ''))
density, modulus = getInputs(fields, 'Material properties')
if density == None:
    print 'User pressed Cancel'
```

## Requesting a warning reply from the user

The `getWarningReply` function displays a warning dialog box in the center of the main window, and the user clicks on one of the standard reply buttons in the dialog box. The clicked button value is returned to the executing script. For more information, see {func}`~abaqus.UtilityAndView.User.getWarningReply`.

The following example illustrates the use of the `getWarningReply` function:

```python2
from abaqus import getWarningReply, YES, NO

reply = getWarningReply(message='Okay to continue?', buttons=(YES,NO))
if reply == YES:
    print 'YES clicked'
elif reply == NO:
    print 'NO clicked'
```

The following figure shows the dialog box that appears when this script is executed:

(utl-getwarningreply-nls)=

:::{figure} /images/utl-getwarningreply-nls.png
:align: center
:width: 50%
:::
