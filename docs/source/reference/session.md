# Abaqus Session

Session commands are used to create objects that are not stored with the model; for example, viewports and display groups. Abaqus/CAE retains Session objects only for the duration of the session; they are not saved when the model database is saved.

```{toctree}
:caption: Objects of Session
:maxdepth: 1

session/animation
session/canvas
session/display_options
session/display
session/field_report
session/odb_display
session/path
session/plot_options
session/print
session/xy
```

## Classes

### Session

```{eval-rst}
.. autoclass:: abaqus.Session.Session.Session
    :members:
    :special-members: __init__
    :show-inheritance:

    .. autoclasstoc::
```

### Other Classes

```{eval-rst}

.. toggle::

    .. autoclass:: abaqus.Session.SessionBase.SessionBase
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Animation.AnimationSession.AnimationSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Canvas.CanvasSession.CanvasSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.DisplayGroup.DisplayGroupSession.DisplayGroupSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.FieldReport.FieldReportSession.FieldReportSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Job.JobSession.JobSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.Odb.OdbSession.OdbSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.PathAndProbe.PathSession.PathSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::

    .. autoclass:: abaqus.XY.XYSession.XYSession
        :members:
        :special-members: __init__
        :show-inheritance:
        :noindex:

        .. autoclasstoc::


    .. autoclass:: abaqus.Session.AutoColors.AutoColors
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Session.Color.Color
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Session.Drawing.Drawing
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Session.Image.Image
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Session.JournalOptions.JournalOptions
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Session.MemoryReductionOptions.MemoryReductionOptions
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Session.NetworkDatabaseConnector.NetworkDatabaseConnector
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::

    .. autoclass:: abaqus.Session.NumberFormat.NumberFormat
        :members:
        :special-members: __init__
        :show-inheritance:

        .. autoclasstoc::
```
