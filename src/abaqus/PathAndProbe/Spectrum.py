class Spectrum:
    """The Spectrum object defines a color spectrum for the contour display.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.spectrums[name]
    """

    def __init__(self, name: str, colors: tuple):
        """This method creates a Spectrum object and places it in the spectrums repository.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                session.Spectrum

        Parameters
        ----------
        name
            A string name for the spectrum.
        colors
            A sequence of strings indicating the colors of the spectrum.

        Returns
        -------
        Spectrum
            A :py:class:`~abaqus.PathAndProbe.Spectrum.Spectrum` object.
        """
        pass
