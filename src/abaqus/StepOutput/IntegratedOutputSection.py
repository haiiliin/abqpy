from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class IntegratedOutputSection:
    """The IntegratedOutputSection object specifies parameters used for integrated output.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].integratedOutputSections[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface over which the output is based.
    surface: Region

    #: None or a Region object specifying the anchor point about which the integrated moment
    #: over the output region is computed or the SymbolicConstant None representing the global
    #: origin. The default value is None.
    refPoint: SymbolicConstant = None

    #: A Boolean specifying that the **refPoint** be adjusted so that it coincides with the
    #: center of the output region in the initial configuration. This argument is valid only
    #: when you include the **refPoint** argument. The default value is OFF.
    refPointAtCenter: Boolean = OFF

    #: A SymbolicConstant specifying how to relate the motion of **refPoint** to the average
    #: motion of the output region. A value of INDEPENDENT will allow the **refPoint** to move
    #: independent of the output region. A value of AVERAGE_TRANSLATION will set the
    #: displacement of the **refPoint** equal to the average translation of the output region. A
    #: value of AVERAGE will set the displacement and rotation of the **refPoint** equal to the
    #: average translation of the output region. The default value is INDEPENDENT.This argument
    #: is valid only when you include the **refPoint** argument.
    refPointMotion: SymbolicConstant = INDEPENDENT

    #: None or a DatumCsys object specifying the local coordinate system used to express vector
    #: output. If **localCsys** = None, the degrees of freedom are defined in the global coordinate
    #: system. The default value is None.
    localCsys: str = None

    #: A Boolean specifying that the coordinate system be projected onto the **surface** such
    #: that the 1-axis is normal to the **surface**. Projection onto a planar **surface** is such
    #: that the 1-axis is normal to the surface, and a projection onto a nonplanar **surface** is
    #: such that a least-squares fit surface will be used. The default value is OFF.
    projectOrientation: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        surface: Region,
        refPoint: SymbolicConstant = None,
        refPointAtCenter: Boolean = OFF,
        refPointMotion: SymbolicConstant = INDEPENDENT,
        localCsys: str = None,
        projectOrientation: Boolean = OFF,
    ):
        """This method creates an IntegratedOutputSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].IntegratedOutputSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface over which the output is based.
        refPoint
            None or a Region object specifying the anchor point about which the integrated moment
            over the output region is computed or the SymbolicConstant None representing the global
            origin. The default value is None.
        refPointAtCenter
            A Boolean specifying that the **refPoint** be adjusted so that it coincides with the
            center of the output region in the initial configuration. This argument is valid only
            when you include the **refPoint** argument. The default value is OFF.
        refPointMotion
            A SymbolicConstant specifying how to relate the motion of **refPoint** to the average
            motion of the output region. A value of INDEPENDENT will allow the **refPoint** to move
            independent of the output region. A value of AVERAGE_TRANSLATION will set the
            displacement of the **refPoint** equal to the average translation of the output region. A
            value of AVERAGE will set the displacement and rotation of the **refPoint** equal to the
            average translation of the output region. The default value is INDEPENDENT.This argument
            is valid only when you include the **refPoint** argument.
        localCsys
            None or a DatumCsys object specifying the local coordinate system used to express vector
            output. If **localCsys** = None, the degrees of freedom are defined in the global coordinate
            system. The default value is None.
        projectOrientation
            A Boolean specifying that the coordinate system be projected onto the **surface** such
            that the 1-axis is normal to the **surface**. Projection onto a planar **surface** is such
            that the 1-axis is normal to the surface, and a projection onto a nonplanar **surface** is
            such that a least-squares fit surface will be used. The default value is OFF.

        Returns
        -------
        IntegratedOutputSection
            An :py:class:`~abaqus.StepOutput.IntegratedOutputSection.IntegratedOutputSection` object.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        surface: Region,
        refPoint: SymbolicConstant = None,
        refPointAtCenter: Boolean = OFF,
        refPointMotion: SymbolicConstant = INDEPENDENT,
        localCsys: str = None,
        projectOrientation: Boolean = OFF,
    ):
        """This method modifies the IntegratedOutputSection object.

        Parameters
        ----------
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface over which the output is based.
        refPoint
            None or a Region object specifying the anchor point about which the integrated moment
            over the output region is computed or the SymbolicConstant None representing the global
            origin. The default value is None.
        refPointAtCenter
            A Boolean specifying that the **refPoint** be adjusted so that it coincides with the
            center of the output region in the initial configuration. This argument is valid only
            when you include the **refPoint** argument. The default value is OFF.
        refPointMotion
            A SymbolicConstant specifying how to relate the motion of **refPoint** to the average
            motion of the output region. A value of INDEPENDENT will allow the **refPoint** to move
            independent of the output region. A value of AVERAGE_TRANSLATION will set the
            displacement of the **refPoint** equal to the average translation of the output region. A
            value of AVERAGE will set the displacement and rotation of the **refPoint** equal to the
            average translation of the output region. The default value is INDEPENDENT.This argument
            is valid only when you include the **refPoint** argument.
        localCsys
            None or a DatumCsys object specifying the local coordinate system used to express vector
            output. If **localCsys** = None, the degrees of freedom are defined in the global coordinate
            system. The default value is None.
        projectOrientation
            A Boolean specifying that the coordinate system be projected onto the **surface** such
            that the 1-axis is normal to the **surface**. Projection onto a planar **surface** is such
            that the 1-axis is normal to the surface, and a projection onto a nonplanar **surface** is
            such that a least-squares fit surface will be used. The default value is OFF.
        """
        ...
