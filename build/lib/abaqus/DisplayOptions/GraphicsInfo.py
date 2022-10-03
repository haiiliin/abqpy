from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class GraphicsInfo:
    """The GraphicsInfo object stores information about the graphics adapter installed in your
    system. The GraphicsInfo object has no constructor or methods; Abaqus creates the
    **GraphicsInfo** member when a session is started.
    If you execute Abaqus/CAE on a remote system and display the main window locally, the
    *glx server* is your local machine and the *glx client* is the remote machine. This
    definition of client and server follows the X11 naming convention. If you execute and
    display Abaqus/CAE on the same machine, you will typically see identical values for both
    the name of the server and the name of the client.
    The members are all read-only.

    .. note::
        This object can be accessed by::

            session.graphicsInfo
    """

    #: A sequence of the type (Int, Int, String) specifying the three components of the OpenGL
    #: version. The sequence consists of an Int with the OpenGL major version number, an Int
    #: with the OpenGL minor version number, and a String with any additional information.
    glVersion: tuple = ()

    #: A sequence of the type (Int, Int, String) specifying the three components of the glx
    #: version of the server. The sequence consists of an Int with the glx major version
    #: number, an Int with the glx minor version number, and a String with any additional
    #: information.
    glxServerVersion: tuple = ()

    #: A sequence of the type (Int, Int, String) specifying the three components of the of glx
    #: version of the client. The sequence consists of an Int with the glx major version
    #: number, an Int with the glx minor version number, and String with any additional
    #: information.
    glxClientVersion: tuple = ()

    #: A String specifying the graphics adapter vendor. On hardware accelerated systems
    #: **glVendor** specifies the vendor that manufactured the adapter. On systems without
    #: hardware acceleration **glVendor** specifies the developer of the software graphics
    #: library.
    glVendor: str = ""

    #: A String specifying the name of the rendering device or the name of the software
    #: graphics library.
    glRenderer: str = ""

    #: A String specifying the glx developer on the server side.
    glxServerVendor: str = ""

    #: A String specifying the glx developer on the client side.
    glxClientVendor: str = ""
