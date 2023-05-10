from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import OFF, ON, SSH, Boolean, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class NetworkDatabaseConnector:
    """The NetworkDatabaseConnector object allows you to access an output database on a remote system.

    .. note::
        This object can be accessed by::

            session.networkDatabaseConnectors[name]
    """

    #: A Boolean specifying if the connection between the client and the server is established.
    connected: Boolean = OFF

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the remote computer.
    hostName: str

    #: A String specifying the directory on the remote computer.
    directory: str

    #: A String specifying the name of command to execute Abaqus/CAE on the remote computer.
    remoteAbaqusDriverName: str = ""

    #: A SymbolicConstant specifying the remote shell command on the local system. Possible
    #: values are RSH and SSH. The default value is SSH.
    remoteLoginMechanism: SymbolicConstant = SSH

    #: A String specifying the path to the`ssh` command on the local system. The default value
    #: is an empty string.
    sshPath: str = ""

    #: An Int specifying the server port on the remote computer. If **serverPort** =0, the host
    #: and remote systems are allowed to establish their own port numbers. The default value is
    #: 0.
    serverPort: int = 0

    #: An Int specifying the connection port on the remote computer. The default value is 0.
    connectionPort: int = 0

    #: An Int specifying the timeout in seconds for the remote server. For example: 86400
    #: corresponds to one day. The server exits if it does not receive any communication from
    #: the client during the time specified. The default value is 86400.
    serverTimeout: int = 86400

    #: A Boolean specifying whether to start the remote network database connector server. The
    #: default value is ON.
    allowAutomaticStartup: Boolean = ON

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        hostName: str,
        directory: str,
        remoteAbaqusDriverName: str = "",
        remoteLoginMechanism: Literal[C.SSH, C.RSH] = SSH,
        sshPath: str = "",
        serverPort: int = 0,
        connectionPort: int = 0,
        serverTimeout: int = 86400,
        allowAutomaticStartup: Boolean = ON,
    ):
        """This method creates a NetworkDatabaseConnector object that you can use to access a remote output
        database. You can create a network database connector from any platform: Windows or Linux. However, the
        network database connector server must reside on a Linux platform; you cannot access an output database
        that resides on a remote Windows system. You can access only a remote output database; you cannot access
        a remote model database.

        .. note::
            This function can be accessed by::

                session.NetworkDatabaseConnector

        Parameters
        ----------
        name
            A String specifying the repository key.
        hostName
            A String specifying the name of the remote computer.
        directory
            A String specifying the directory on the remote computer.
        remoteAbaqusDriverName
            A String specifying the name of command to execute Abaqus/CAE on the remote computer.
        remoteLoginMechanism
            A SymbolicConstant specifying the remote shell command on the local system. Possible
            values are RSH and SSH. The default value is SSH.
        sshPath
            A String specifying the path to the`ssh` command on the local system. The default value
            is an empty string.
        serverPort
            An Int specifying the server port on the remote computer. If **serverPort** =0, the host
            and remote systems are allowed to establish their own port numbers. The default value is
            0.
        connectionPort
            An Int specifying the connection port on the remote computer. The default value is 0.
        serverTimeout
            An Int specifying the timeout in seconds for the remote server. For example: 86400
            corresponds to one day. The server exits if it does not receive any communication from
            the client during the time specified. The default value is 86400.
        allowAutomaticStartup
            A Boolean specifying whether to start the remote network database connector server. The
            default value is ON.

        Returns
        -------
        NetworkDatabaseConnector
            A NetworkDatabaseConnector object.
        """
        ...

    @abaqus_method_doc
    def start(self, serverPort: int = 0, serverTimeout: int = 86400):
        """This method starts the remote network database connector server on the remote host.

        Parameters
        ----------
        serverPort
            An Int specifying the server port on the remote computer. If **serverPort** =0, the host
            and remote systems are allowed to establish their own port numbers. The default value is
            0.
        serverTimeout
            An Int specifying the timeout in seconds for the remote server. For example: 86400
            corresponds to one day. The server exits if it does not receive any communication from
            the client during the time specified. The default value is 86400.
        """
        ...

    @abaqus_method_doc
    def stop(self):
        """This method stops the remote network database connector server on the remote host."""
        ...

    @abaqus_method_doc
    def setValues(
        self,
        remoteAbaqusDriverName: str = "",
        remoteLoginMechanism: Literal[C.SSH, C.RSH] = SSH,
        sshPath: str = "",
        serverPort: int = 0,
        connectionPort: int = 0,
        serverTimeout: int = 86400,
        allowAutomaticStartup: Boolean = ON,
    ):
        """This method modifies the NetworkDatabaseConnector object.

        Parameters
        ----------
        remoteAbaqusDriverName
            A String specifying the name of command to execute Abaqus/CAE on the remote computer.
        remoteLoginMechanism
            A SymbolicConstant specifying the remote shell command on the local system. Possible
            values are RSH and SSH. The default value is SSH.
        sshPath
            A String specifying the path to the`ssh` command on the local system. The default value
            is an empty string.
        serverPort
            An Int specifying the server port on the remote computer. If **serverPort** =0, the host
            and remote systems are allowed to establish their own port numbers. The default value is
            0.
        connectionPort
            An Int specifying the connection port on the remote computer. The default value is 0.
        serverTimeout
            An Int specifying the timeout in seconds for the remote server. For example: 86400
            corresponds to one day. The server exits if it does not receive any communication from
            the client during the time specified. The default value is 86400.
        allowAutomaticStartup
            A Boolean specifying whether to start the remote network database connector server. The
            default value is ON.
        """
        ...
