from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class JobData:
    """The JobData object describes the context in which the analysis was run.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].jobData
    """

    #: A String specifying the name of the job.
    name: str = ""

    #: A SymbolicConstant specifying the analysis code. Possible values are ABAQUS_STANDARD,
    #: ABAQUS_EXPLICIT, and UNKNOWN_ANALYSIS_CODE.
    analysisCode: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the precision. Only SINGLE_PRECISION is currently
    #: supported. Possible values are DOUBLE_PRECISION and SINGLE_PRECISION.
    precision: Optional[SymbolicConstant] = None

    #: A String specifying the release of the analysis code.
    version: str = ""

    #: A String specifying the date and time at which the analysis was run.
    creationTime: str = ""

    #: A String specifying the date and time at which the database was last modified.
    modificationTime: str = ""

    #: A String specifying the name of the machine on which the analysis was run.
    machineName: str = ""

    #: A String specifying an odb_Sequence of productAddOns. Possible
    #: values are AQUA, DESIGN, BIORID, CEL, SOLITER, and CAVPARALLEL.
    productAddOns: str = ""
