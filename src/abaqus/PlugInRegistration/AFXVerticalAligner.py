from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXVerticalFrame import FXVerticalFrame


class AFXVerticalAligner(FXVerticalFrame):
    """This class is used to automatically vertically align its children "container" widgets (e.g. AFXTextField
    or AFXComboBox).

    The width of the first widget in the container of each child of the vertical aligner is set to the width
    of the widest first widget of all the vertical aligner's children.
    """

    def __init__(
        self,
        p: FXComposite,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 0,
        pr: int = 0,
        pt: int = 0,
        pb: int = 0,
        hs: int = DEFAULT_SPACING,
        vs: int = DEFAULT_SPACING,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        opts : int
            Options and hints.
        x : int
            X coordinate of the origin.
        y : int
            Y coordinate of the origin.
        w : int
            Width of the widget.
        h : int
            Height of the widget.
        pl : int
            Left padding (margin).
        pr : int
            Right padding (margin).
        pt : int
            Top padding (margin).
        pb : int
            Bottom padding (margin).
        hs : int
            Horizontal spacing.
        vs : int
            Vertical spacing.
        """

    def create(self):
        """Creates the aligner.

        Reimplemented from FXComposite.
        """

    def getDefaultHeight(self):
        """Returns the default height.

        Reimplemented from FXVerticalFrame.
        """

    def getDefaultWidth(self):
        """Returns the default width.

        Reimplemented from FXVerticalFrame. By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information. [Privacy Policy](https://www.3ds.com/privacy-policy). Total Results: Results per page This page cannot be found. The page might not exist or is temporarily unavailable. Try again or try searching for the topic. Provide Feedback on This Topic Use this form to provide feedback on this help topic. To get product support or to provide product feedback, go to [Frequently Asked Questions](https://3ds.one/PO). For support for online purchased solutions, go to [Online Purchase Support](https://3ds.one/Q8). * Required Subject: Feedback on User Assistance * I acknowledge I have read and I hereby accept the [privacy policy](https://www.3ds.com/privacy-policy) under which my personal data will be used by Dassault Systèmes. 2016 - Go to 2016 home page 2017 - Go to the same topic in 2017 2018 - Go to the same topic in 2018 2019 - Go to the same topic in 2019 2020 - Go to the same topic in 2020 2021 - Go to the same topic in 2021 2022 - Go to the same topic in 2022 2023 - Go to the same topic in 2023 2016 - Go to 2016 home page 2017 - Go to the same topic in 2017 2018 - Go to the same topic in 2018 2019 - Go to the same topic in 2019 2020 - Go to the same topic in 2020 2021 - Go to the same topic in 2021 2022 - Go to the same topic in 2022 2023 - Go to the same topic in 2023
        """
