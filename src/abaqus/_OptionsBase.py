import inspect


class _OptionsBase:

    @classmethod
    def get_user_attributes(cls) -> list[str]:
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
