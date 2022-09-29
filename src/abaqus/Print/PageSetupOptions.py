from typing import Union
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import (Boolean, FIT_TO_PAGE, INCHES, MEDIUM, ON, PORTRAIT,
                                              SymbolicConstant)
from .._OptionsBase import _OptionsBase


@abaqus_class_doc
class PageSetupOptions(_OptionsBase):
    """The PageSetupOptions object stores the settings that Abaqus uses when printing using a
    Windows printer. The PageSetupOptions object has no constructor. Abaqus creates the
    **pageSetupOptions** member when a session is started.

    .. note:: 
        This object can be accessed by::

            session.pageSetupOptions
    """
    #: The SymbolicConstant SIZE_ON_SCREEN or a pair of Floats specifying the width and height
    #: of the image in the units specified by **units**. Possible numeric values are **imageSize**
    #: ≥ (*minWidth*, **minHeight**). The default value is SIZE_ON_SCREEN.Note:The minimum value
    #: of width and height (*minWidth* and **minHeight**) is 10 mm (approximately 0.4 inches).
    imageSize: Union[SymbolicConstant, float] = FIT_TO_PAGE

    #: A SymbolicConstant specifying the units to use for the margins and image size. Possible
    #: values are INCHES and MM. The default value is INCHES.
    units: SymbolicConstant = INCHES

    #: A SymbolicConstant specifying the quality of the image. Possible values are COARSE, MEDIUM,
    #: and FINE. The default value is MEDIUM.
    quality: SymbolicConstant = MEDIUM

    #: A Float specifying the top margin of the paper in the currently selected units (inches or
    #: millimeters). Possible values are **topMargin** ≥ 0. The default value is 0.5.
    topMargin: float = 0.5

    #: A Float specifying the bottom margin of the paper in the currently selected units (inches
    #: or millimeters). Possible values are **bottomMargin** ≥ 0. The default value is 0.5.
    bottomMargin: float = 0.5

    #: A Float specifying the left margin of the paper in the currently selected units (inches or
    #: millimeters). Possible values are **leftMargin** ≥ 0. The default value is 0.5.
    leftMargin: float = 0.5

    #: A Float specifying the right margin of the paper in the currently selected units (inches
    #: or millimeters). Possible values are **rightMargin** ≥ 0. The default value is 0.5.
    rightMargin: float = 0.5

    #: A SymbolicConstant specifying the orientation of the image. Possible values are PORTRAIT
    #: and LANDSCAPE. The default value is PORTRAIT.
    orientation: SymbolicConstant = PORTRAIT

    #: A Boolean specifying whether the output includes the Abaqus logo. The default value is ON.
    logo: Boolean = ON

    #: A Boolean specifying whether the output includes the date. The default value is ON.
    date: Boolean = ON

    @abaqus_method_doc
    def setValues(
        self,
        *,
        imageSize: Union[SymbolicConstant, float] = FIT_TO_PAGE,
        units: SymbolicConstant = INCHES,
        quality: SymbolicConstant = MEDIUM,
        topMargin: float = 0.5,
        bottomMargin: float = 0.5,
        leftMargin: float = 0.5,
        rightMargin: float = 0.5,
        orientation: SymbolicConstant = PORTRAIT,
        logo: Boolean = ON,
        date: Boolean = ON,
    ):
        """This method modifies the PageSetupOptions object.

        Parameters
        ----------
        imageSize
            A SymbolicConstant or a pair of Floats specifying the size of the printed image in the
            currently selected units (inches or millimeters). Possible values are FIT_TO_PAGE and
            SIZE_ON_SCREEN. The default value is FIT_TO_PAGE.Note:The minimum value of width and
            height (*minWidth* and **minHeight**) is 10 mm (approximately 0.4 inches).
        units
            A SymbolicConstant specifying the units to use for the margins and image size. Possible
            values are INCHES and MM. The default value is INCHES.
        quality
            A SymbolicConstant specifying the quality of the image. Possible values are COARSE,
            MEDIUM, and FINE. The default value is MEDIUM.
        topMargin
            A Float specifying the top margin of the paper in the currently selected units (inches
            or millimeters). Possible values are **topMargin** ≥ 0. The default value is 0.5.
        bottomMargin
            A Float specifying the bottom margin of the paper in the currently selected units
            (inches or millimeters). Possible values are **bottomMargin** ≥ 0. The default value is
            0.5.
        leftMargin
            A Float specifying the left margin of the paper in the currently selected units (inches
            or millimeters). Possible values are **leftMargin** ≥ 0. The default value is 0.5.
        rightMargin
            A Float specifying the right margin of the paper in the currently selected units (inches
            or millimeters). Possible values are **rightMargin** ≥ 0. The default value is 0.5.
        orientation
            A SymbolicConstant specifying the orientation of the image. Possible values are PORTRAIT
            and LANDSCAPE. The default value is PORTRAIT.
        logo
            A Boolean specifying whether the output includes the Abaqus logo. The default value is
            ON.
        date
            A Boolean specifying whether the output includes the date. The default value is ON.

        Raises
        ------
        RangeError
            Note: The minimum value of width and height (*minWidth* and **minHeight**) is 10 mm
            (approximately 0.4 inches).
        RangeError: leftMargin and rightMargin must produce image width >= minWidth
            If **leftMargin** + **rightMargin** is out of range.
        RangeError: topMargin and bottomMargin must produce image height >= minHeight
            If **topMargin** + **bottomMargin** is out of range.
        """
        super().setValues(
            imageSize=imageSize,
            units=units,
            quality=quality,
            topMargin=topMargin,
            bottomMargin=bottomMargin,
            leftMargin=leftMargin,
            rightMargin=rightMargin,
            orientation=orientation,
            logo=logo,
            date=date,
        )
