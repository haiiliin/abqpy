import typing
from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class ResponseSpectrumComponent:
    """A ResponseSpectrumComponent is an element of the ResponseSpectrumComponentArray.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].components[i]
    """

    #: A Float specifying the **X**-direction cosine.
    x: typing.Optional[float] = None

    #: A Float specifying the **Y**-direction cosine.
    y: typing.Optional[float] = None

    #: A Float specifying the **Z**-direction cosine.
    z: typing.Optional[float] = None

    #: A Float specifying the scale factor.
    scale: typing.Optional[float] = None

    #: A Float specifying the time duration of the dynamic event, from which this spectrum was
    #: created.Note:This parameter is ignored unless used with the DSC modal summation rule.
    timeDuration: typing.Optional[float] = None

    #: A String specifying the name of the response spectrum specified with the keyword
    #: SPECTRUM.
    respSpectrum: str = ""
