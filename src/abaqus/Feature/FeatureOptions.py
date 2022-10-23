from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class FeatureOptions:
    """The FeatureOptions object stores the options that control the behavior of feature
    regeneration for all features in a model.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].featureOptions
    """

    @abaqus_method_doc
    def setValues(
        self,
        checkSelfIntersection: Boolean = ON,
        autoCaching: Boolean = ON,
        maxCachedStates: int = 5,
    ):
        """This method modifies the FeatureOptions object for the specified model.

        Parameters
        ----------
        checkSelfIntersection
            A Boolean specifying whether Abaqus/CAE should perform self-intersection checks while
            regenerating features. The default value is ON.
        autoCaching
            A Boolean specifying whether geometric states should be automatically cached. The
            default value is ON.
        maxCachedStates
            An Int specifying the maximum number of caches to be stored with each part or with the
            assembly. The default value is 5.
        """
        ...
