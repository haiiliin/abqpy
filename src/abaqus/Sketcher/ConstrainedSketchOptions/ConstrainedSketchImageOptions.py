from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class ConstrainedSketchImageOptions:
    """The ConstrainedSketchImageOptions object is used to store values and attributes
    associated with the background image for a particular sketch. The
    ConstrainedSketchImageOptions object has no constructor.

    .. note::
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].imageOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        imageName: str = "",
        showImage: Boolean = OFF,
        origin: Sequence[float] = (),
        xScale: float = 1,
        yScale: float = 1,
        translucency: float = 1,
    ):
        """This method modifies the ConstrainedSketchOptions object.

        Parameters
        ----------
        imageName
            A String specifying the name of the image. A list of valid image names is in the
            **images** repository in the **session** object.
        showImage
            A Boolean specifying whether an image should be displayed in the sketcher background.
            The default value is OFF.
        origin
            A pair of Floats specifying the **X**- and **Y**-offsets in millimeters from the lower-left
            corner of the viewport. The default value is (0, 0).
        xScale
            A Float specifying the scale applied to the image width. The default value is 1.0.When
            **xScale** is negative, the image is mirrored about its y-axis but its position is not
            affected.
        yScale
            A Float specifying the scale applied to the image height. The default value is 1.0.When
            **yScale** is negative, the image is mirrored about its x-axis but its position is not
            affected.
        translucency
            A Float specifying the translucency factor to use when displaying the image. Possible
            values are 0.0 ≤ **translucency** ≤ 1.0 with 0.0 being invisible and 1.0 being opaque.
            The default value is 1.0.

        Raises
        ------
        RangeError

        """
        ...
