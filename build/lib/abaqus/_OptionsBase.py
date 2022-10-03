import inspect
from typing import List


class _OptionsBase:
    """
    This is a base class for all options classes.
    """

    @classmethod
    def get_user_attributes(cls) -> List[str]:
        """Returns a list of the user attributes of the class.

        Returns
        -------
        list
            The list of user attributes of the class.
        """
        boring = dir(type('dummy', (object,), {}))
        return [key for key, value in inspect.getmembers(cls)
                if key not in boring and not key.startswith('_') and not callable(value)]

    def setValues(self, **kwargs):
        """This method modifies the _OptionsBase object.

        Parameters
        ----------
        kwargs
            The keyword arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)


class _CopyOptionsBase(_OptionsBase):
    """
    This is a base class for options classes where the first argument is the options object used to copy options
    in the setValues method.
    """

    def setValues(self, options, **kwargs):
        """This method modifies the CopyOptions object.

        Parameters
        ----------
        options : CopyOptions
            An object from which values are to be copied. If other arguments are also supplied to setValues,
            they will override the values in **options**. The default value is None.
        kwargs
            The keyword arguments.
        """
        if options is not None:
            for key in self.get_user_attributes():
                setattr(self, key, getattr(options, key))

        for key, value in kwargs:
            setattr(self, key, value)
