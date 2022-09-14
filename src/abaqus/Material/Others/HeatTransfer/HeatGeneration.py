from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class HeatGeneration:
    """The HeatGeneration object includes volumetric heat generation in heat transfer analyses.

    .. note:: 
        This object can be accessed by::

            import material
            mdb.models[name].materials[name].heatGeneration
            import odbMaterial
            session.odbs[name].materials[name].heatGeneration

        The corresponding analysis keywords are:

        - HEAT GENERATION
    """

    @abaqus_method_doc
    def __init__(self):
        """This method creates a HeatGeneration object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].materials[name].HeatGeneration
                session.odbs[name].materials[name].HeatGeneration

        Returns
        -------
        HeatGeneration
            A :py:class:`~abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration` object.
        """
        ...
