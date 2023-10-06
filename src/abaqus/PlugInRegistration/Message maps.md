Message maps are used by classes derived from FXObject (which includes most GUI classes) to route messages sent to the object to a message handling method. A typical use might be to route a message from a button in a dialog to one of the dialog's methods so that some action is taken when the button is pressed.

A message consists of two parts, a type and an ID. The type indicates what kind of action generated the message, while the ID identifies who sent the message. These two numbers are combined into a single value using the MKUINT function.

When the message handler method is called, it gets passed three arguments: the sender, the selector, and some optional data. Your message handler prototype must contain these three arguments, which are typically specified as _sender_, _sel_, _ptr_. The optional data is sometimes used by the sender to include extra data that might be useful to the message handler (for example the coordinates of the cursor when a mouse button was clicked). However, due to the language differences between C++ and Python, this optional data is not available for use in Python scripts.

Refer to the Abaqus GUI Toolkit User's Guide for more details.

### FXMAPFUNC(object, messageType, messageId, method)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates an entry in the object's message map that will route a message to a method.

| **Argument** | **Type** | **Default** | **Description** |
| object | FXObject | | An instance of the class in which the message map entry is to be made. Typically this is "self". |
| messageType | Int | | An integer flag specifying the message type (e.g. SEL_COMMAND). |
| messageId | Int | | An integer specifying the message ID. |
| method | Function | | The method to which the message is to be routed. This method must be specified by including the class name (e.g. MyDB.myMethod). |

### FXMAPFUNCS(object, messageType, startMessageId, endMessageId, method)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates multiple entries in the object's message map that will route messages to a method.

| **Argument** | **Type** | **Default** | **Description** |
| object | FXObject | | An instance of the class in which the message map entry is to be made. Typically this is "self". |
| messageType | Int | | An integer flag specifying the message type (e.g. SEL_COMMAND). |
| startMessageId | Int | | An integer specifying the starting message ID. |
| endMessageId | Int | | An integer specifying the ending message ID. |
| method | Function | | The method to which the message is to be routed. This method must be specified by including the class name (e.g. MyDB.myMethod). |

### MKUINT(messageId, messageType)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates a message selector by combining a message ID and a message type.

| **Argument** | **Type** | **Default** | **Description** |
| messageId | Int | | An integer specifying the message ID. |
| messageType | Int | | An integer flag specifying the message type (e.g. SEL_COMMAND). |

### SELID(selector)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the message ID from a message selector.

| **Argument** | **Type** | **Default** | **Description** |
| selector | Int | | A message selector. |

### SELTYPE(selector)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the message type from a message selector.

| **Argument** | **Type** | **Default** | **Description** |
| selector | Int | | A message selector. |
