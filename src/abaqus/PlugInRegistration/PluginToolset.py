from .GUIPlugInCommands import GUIPluginToolset
from .KernelPlugInCommands import KernelPluginToolset


class PluginToolset(GUIPluginToolset, KernelPluginToolset):
    ...
