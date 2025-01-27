from __future__ import annotations

import copy

from typing_extensions import Literal, overload

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Job.JobMdb import JobMdb
from ..Model.Model import Model
from ..Part.AcisMdb import AcisMdb
from ..UtilityAndView.abaqusConstants import (
    B31,
    C3D8I,
    C3D10,
    NOT_SET,
    OFF,
    ON,
    PRESERVE_SECTION,
    S4,
    STANDARD_EXPLICIT,
    Boolean,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Mdb(AcisMdb, JobMdb):
    """The Mdb object is the high-level Abaqus model database. A model database stores models and analysis
    controls.

    .. note::
        This object can be accessed by::

            mdb
    """

    @overload
    @abaqus_method_doc
    def Model(
        self,
        name: str,
        description: str = "",
        stefanBoltzmann: float | None = None,
        absoluteZero: float | None = None,
        waveFormulation: Literal[C.SCATTERED, C.NOT_SET, C.TOTAL] = NOT_SET,
        modelType: Literal[C.STANDARD_EXPLICIT, C.ELECTROMAGNETIC] = STANDARD_EXPLICIT,
        universalGas: float | None = None,
        copyConstraints: Boolean = ON,
        copyConnectors: Boolean = ON,
        copyInteractions: Boolean = ON,
    ) -> Model:
        """This method creates a Model object.

        .. note::
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying the purpose and contents of the Model object. The default value is
            an empty string.
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None.
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
            is NOT_SET.
        modelType
            A SymbolicConstant specifying the analysis model type. Possible values are
            STANDARD_EXPLICIT and ELECTROMAGNETIC. The default is STANDARD_EXPLICIT.
        universalGas
            None or a Float specifying the universal gas constant. The default value is None.
        copyConstraints
            A boolean specifying whether to copy the constraints created in the model to the model
            that instances this model. The default value is ON.
        copyConnectors
            A boolean specifying whether to copy the connectors created in the model to the model
            that instances this model. The default value is ON.
        copyInteractions
            A boolean specifying whether to copy the interactions created in the model to the model
            that instances this model. The default value is ON.

        Returns
        -------
        model: Model
            A Model object
        """

    @overload
    @abaqus_method_doc
    def Model(self, name: str, objectToCopy: Model) -> Model:
        """This method creates a Model object.

        .. note::
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        objectToCopy
            A Model object to copy.
        """

    @abaqus_method_doc
    def Model(self, name: str, *args, **kwargs) -> Model:
        """This method creates a Model object.

        .. note::
            This function can be accessed by::

                mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        args, kwargs
            Positional and keyword arguments to be passed to the Model object.
        """
        if len(args) == 1 and isinstance(args[0], Model):
            self.models[name] = model = copy.deepcopy(args[0])
        elif "objectToCopy" in kwargs and isinstance(kwargs["objectToCopy"], Model):
            self.models[name] = model = copy.deepcopy(kwargs["objectToCopy"])
        else:
            self.models[name] = model = Model(name, *args, **kwargs)
        return model

    @abaqus_method_doc
    def ModelFromInputFile(self, name: str, inputFileName: str):
        """This method creates a Model object by reading the keywords in an input file and creating the
        corresponding Abaqus/CAE objects.

        .. note::
            This function can be accessed by::

                mdb.ModelFromInputFile

        Parameters
        ----------
        name
            A String specifying the repository key.
        inputFileName
            A String specifying the name of the input file (including the .inp extension) to be
            parsed into the new model. This String can also be the full path to the input file if it
            is located in another directory.

        Returns
        -------
        Model
            A Model object.
        """
        self.models[name] = model = Model(name)
        return model

    @abaqus_method_doc
    def ModelFromOdbFile(self, name: str, odbFileName: str):
        """This method creates a Model object by reading an output database and creating any corresponding
        Abaqus/CAE objects.

        .. note::
            This function can be accessed by::

                mdb.ModelFromOdbFile

        Parameters
        ----------
        name
            A String specifying the repository key.
        odbFileName
            A String specifying the name of the output database file (including the .odb extension)
            to be read into the new model. This String can also be the full path to the output
            database file if it is located in another directory.

        Returns
        -------
        Model
            A Model object.
        """
        self.models[name] = model = Model(name)
        return model

    @abaqus_method_doc
    def ModelFromNastranFile(
        self,
        modelName: str,
        inputFileName: str,
        sectionConsolidation: Literal[C.PRESERVE_SECTION, C.GROUP_BY_MATERIAL, C.NONE] = PRESERVE_SECTION,
        preIntegratedShell: Boolean = OFF,
        weightMassScaling: Boolean = ON,
        loadCases: Boolean = ON,
        coupleBeamOffsets: Boolean = ON,
        cbar: str = B31,
        cquad4: str = S4,
        chexa: str = C3D8I,
        ctetra: str = C3D10,
        keepTranslatedFiles: Boolean = ON,
    ):
        """This method creates a Model object by reading the keywords in a Nastran bulk data file or Nastran
        input file and creating any corresponding Abaqus/CAE objects. The default values is discussed in
        following and can be defined alternatively in the Abaqus environment file as the one used for the
        translator from Nastran to Abaqus. For more information, see Translating Nastran data to Abaqus files.

        .. note::
            This function can be accessed by::

                mdb.ModelFromNastranFile

        Parameters
        ----------
        modelName
            A String specifying the repository key.
        inputFileName
            A String specifying the name of the Nastran input file (including the .bdf, .dat, .nas,
            .nastran, .blk, .bulk extension) to be read into the new model. This String can also be
            the full path to the Nastran input file if it is located in another directory.
        sectionConsolidation
            A SymbolicConstant specifying the method used to create shell section. Possible values
            are PRESERVE_SECTION, GROUP_BY_MATERIAL, and NONE. If PRESERVE_SECTION is used, an
            Abaqus section is created corresponding to each shell property ID. If GROUP_BY_MATERIAL
            is used, a single Abaqus section is created for all homogeneous elements referencing the
            same material. In both cases, material orientations and offsets are created using
            discrete fields. If NONE is used, a separate shell section is created for each
            combination of orientation, material offset, and/or thickness. The default is
            PRESERVE_SECTION.
        preIntegratedShell
            A Boolean specifying whether the pre-integrated shell section is created in default for
            shell element. The default value is OFF.
        weightMassScaling
            A Boolean specifying whether the value on the Nastran data line PARAM, WTMASS is used as
            a multiplier for all density, mass, and rotary inertia values created in the Abaqus
            input file. The default value is ON.
        loadCases
            A Boolean specifying whether each SUBCASE for linear static analyses is translated to a
            LOAD CASE option, and all such LOAD CASE options are grouped in a single STEP option.
            The default value is ON.
        coupleBeamOffsets
            A Boolean specifying whether to translate the beam element connectivity to newly created
            nodes at the offset location and rigidly coupling the new and original nodes. If not,
            beam element offsets are translated to the CENTROID and SHEAR CENTER options, which are
            suboptions of the BEAM GENERAL SECTION option. The default value is ON. When the beam
            element references a PBARL or PBEAML property or if the beam offset has a significant
            component in the direction of the beam axis, the setting for this argument is always ON.
        cbar
            A String specifying the 2-node beam that is created from CBAR and CBEAM elements.
            Possible values are B31 and B33. The default is B31.
        cquad4
            A String specifying the 4-node shell that is created from CQUAD4 elements. Possible
            values are S4 and S4R. The default is S4. If a reduced-integration element is chosen,
            the enhanced hourglass formulation is applied automatically.
        chexa
            A String specifying the 8-node brick that is created from CHEXA elements. Possible
            values are C3D8I, C3D8 and C3D8R. The default is C3D8I. If a reduced-integration element
            is chosen, the enhanced hourglass formulation is applied automatically.
        ctetra
            A String specifying the 10-node tetrahedron that is created from CTETRA elements.
            Possible values are C3D10 and C3D10M. The default is C3D10.
        keepTranslatedFiles
            A Boolean specifying whether to keep the generated Abaqus input file after the model is
            created from the Nastran input file. The default value is ON.

        Returns
        -------
        Model
            A Model object.
        """
        self.models[modelName] = model = Model(modelName)
        return model
