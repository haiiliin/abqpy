from .._OptionsBase import _OptionsBase


class _CopyOptionsBase(_OptionsBase):

    def setValues(self, options, **kwargs):
        """This method modifies the CopyOptions object.

        Parameters
        ----------
        options : CopyOptions
            An object from which values are to be copied. If other arguments are also supplied to setValues,
            they will override the values in **options**. The default value is None.
        kwargs
            Keyword arguments.
        """
        if options is not None:
            for key in self.get_user_attributes():
                setattr(self, key, getattr(options, key))

        for key, value in kwargs:
            if value is not None:
                setattr(self, key, value)
