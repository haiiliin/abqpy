from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXPacker import FXPacker


class FXHorizontalFrame(FXPacker):
    """Horizontal frame layout manager widget is used to automatically place child-windows horizontally from
    left-to-right, or right-to-left, depending on the child window's layout hints."""

    def __init__(
        self,
        p: FXComposite,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_SPACING,
        pr: int = DEFAULT_SPACING,
        pt: int = DEFAULT_SPACING,
        pb: int = DEFAULT_SPACING,
        hs: int = DEFAULT_SPACING,
        vs: int = DEFAULT_SPACING,
    ):
        """Construct a horizontal frame layout manager.

        Parameters
        ----------
        p : FXComposite

        opts : int

        x : int

        y : int

        w : int

        h : int

        pl : int

        pr : int

        pt : int

        pb : int

        hs : int

        vs : int
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXPacker. Reimplemented in FXStatusbar.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXPacker. Reimplemented in FXStatusbar. By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information. [Privacy Policy](https://www.3ds.com/privacy-policy). Total Results: Results per page This page cannot be found. The page might not exist or is temporarily unavailable. Try again or try searching for the topic. Provide Feedback on This Topic Use this form to provide feedback on this help topic. To get product support or to provide product feedback, go to [Frequently Asked Questions](https://3ds.one/PO). For support for online purchased solutions, go to [Online Purchase Support](https://3ds.one/Q8). * Required Subject: Feedback on User Assistance * I acknowledge I have read and I hereby accept the [privacy policy](https://www.3ds.com/privacy-policy) under which my personal data will be used by Dassault Systèmes. 2016 - Go to 2016 home page 2017 - Go to the same topic in 2017 2018 - Go to the same topic in 2018 2019 - Go to the same topic in 2019 2020 - Go to the same topic in 2020 2021 - Go to the same topic in 2021 2022 - Go to the same topic in 2022 2023 - Go to the same topic in 2023 2016 - Go to 2016 home page 2017 - Go to the same topic in 2017 2018 - Go to the same topic in 2018 2019 - Go to the same topic in 2019 2020 - Go to the same topic in 2020 2021 - Go to the same topic in 2021 2022 - Go to the same topic in 2022 2023 - Go to the same topic in 2023
        """
