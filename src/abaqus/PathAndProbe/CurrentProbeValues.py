class CurrentProbeValues:
    """The CurrentProbeValues object has no constructor. The CurrentProbeValues object is
    created when you import the Visualization module.

    Attributes
    ----------
    values: tuple[float]
        A tuple of Floats specifying :py:class:`~.the` values obtained while probing. These values are updated
        constantly as :py:class:`~.the` user moves :py:class:`~.the` mouse over :py:class:`~.the` object being probed.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.currentProbeValues

    """

    # A tuple of Floats specifying the values obtained while probing. These values are updated
    # constantly as the user moves the mouse over the object being probed.
    values: tuple[float] = None
