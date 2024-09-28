from __future__ import annotations

from .GUIPlugInCommands import GUIPluginToolset
from .KernelPlugInCommands import KernelPluginToolset


class PluginToolset(GUIPluginToolset, KernelPluginToolset): ...
