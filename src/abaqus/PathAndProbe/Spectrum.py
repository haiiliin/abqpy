from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class Spectrum:
    """The Spectrum object defines a color spectrum for the contour display.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.spectrums[name]
    """

    @abaqus_method_doc
    def __init__(self, name: str, colors: tuple):
        """This method creates a Spectrum object and places it in the spectrums repository.

        .. note:: 
            This function can be accessed by::

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
        ...
