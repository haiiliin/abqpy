from typing import Optional, Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import Boolean, DEFAULT, OFF, ON, SOLID, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AcisFile:
    """The AcisFile object is a file object used to open ACIS-, STEP-, and IGES-format files.

    .. note::
        This object can be accessed by::

            import part
    """

    #: An Int specifying the number of parts in the object.
    numberOfParts: Optional[int] = None

    @abaqus_method_doc
    def openAcis(self, fileName: str, scaleFromFile: Boolean = OFF):
        """This method creates an AcisFile object from a file containing ACIS-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the ACIS file to open.
        scaleFromFile
            A Boolean specifying whether to scale, rotate, and translate the part using the
            transform read from the ACIS file. The default value is OFF.

        Returns
        -------
        AcisFile
            An :py:class:`~abaqus.Part.AcisFile.AcisFile` object.

        Raises
        ------
        Texterror: ACIS File version exceeds Kernel
            File is from a newer version of ACIS than the CAE kernel.
        Texterror: Failed to read ACIS file
            The data in the ACIS file are corrupted.
        """
        ...

    @abaqus_method_doc
    def openCatia(
        self,
        fileName: str,
        topology: Optional[Literal[C.WIRE, C.SOLID, C.SHELL]] = None,
        convertUnits: Union[SymbolicConstant, Boolean] = OFF,
        combineBodies: Boolean = OFF,
    ):
        """This method creates an AcisFile object from a file containing V5-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the CATIA file to open.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID .
        convertUnits
            A SymbolicConstant specifying whether the original units should be retained. Possible
            values are ON and OFF. The default value is OFF.
        combineBodies
            A Boolean specifying whether to combine the bodies in the CATPart file. If the bodies to
            be combined touch or overlap, invalid entities would result. For CATProduct files, this
            option will be ignored.

        Returns
        -------
        AcisFile
            An :py:class:`~abaqus.Part.AcisFile.AcisFile` object.
        """
        ...

    @abaqus_method_doc
    def openEnf(
        self,
        fileName: str,
        fileType: str,
        topology: Literal[C.WIRE, C.SOLID, C.SHELL] = SOLID,
        convertUnits: Boolean = OFF,
    ):
        """This method creates an AcisFile object from a file containing Elysium Neutral
        File-format geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object
        is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the Elysium Neutral File that was created by I-DEAS,
            Pro/ENGINEER, or CATIA V5.
        fileType
            A String specifying the type of CAD system that created the file. Possible values are
            “ideas”, “proe”, or “catiav5” or a combination similar to “proe/ideas/catiav5” if the
            type is unknown.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID.
        convertUnits
            A Boolean specifying if the dimensions of the part should be converted to millimeters.
            The default value is OFF.

        Returns
        -------
        AcisFile
            An :py:class:`~abaqus.Part.AcisFile.AcisFile` object.
        """
        ...

    @abaqus_method_doc
    def openIges(
        self,
        fileName: str,
        trimCurve: Literal[C.IGES, C.DEFAULT] = DEFAULT,
        scaleFromFile: Union[Literal[C.IGES], Boolean] = OFF,
        msbo: Boolean = False,
        includedLayers: tuple = (),
        topology: Literal[C.WIRE, C.SOLID, C.SHELL] = SOLID,
        uniteWires: Union[SymbolicConstant, Boolean] = ON,
    ):
        """This method creates an AcisFile object from a file containing IGES-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the IGES file to open.
        trimCurve
            A SymbolicConstant specifying the method used to define the trim curves that bound
            parametric surfaces. Possible values are:DEFAULT, use either of the following as
            specified by the contents of the IGES file.PARAMETRIC_DATA, use the parameter space of
            the surface being trimmed.THREED_DATA, use real space—the coordinate system of the part
            along with an indication that the trim curve lies on the parametric surface.The default
            value is DEFAULT.
        scaleFromFile
            A SymbolicConstant specifying whether the imported geometry needs to be scaled using the
            units information available in the IGES file. Possible values are ON and OFF. The
            default value is OFF. When the argument is set to ON, the geometry is scaled to
            millimeters with respect to the unit system specified in the IGES file.
        msbo
            A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object)
            entities. The default value is False.
        includedLayers
            A sequence of Ints specifying the levels or layers of entities that will be translated
            from the IGES file to build the part. The default is to include all the layers.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID.
        uniteWires
            A SymbolicConstant specifying whether the imported wires need to be united or not.
            Possible values are ON and OFF. The default value is ON. When importing a sketch, this
            value is set to OFF.

        Returns
        -------
        AcisFile
            An :py:class:`~abaqus.Part.AcisFile.AcisFile` object.

        Raises
        ------
        Texterror: Failed to read IGES file
            The data in the IGES file are corrupted.
        """
        ...

    @abaqus_method_doc
    def openParasolid(self, fileName: str, topology: Literal[C.WIRE, C.SOLID, C.SHELL] = SOLID):
        """This method creates an AcisFile object from a file containing Parasolid-format geometry.
        This object is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the Parasolid file to open.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID.

        Returns
        -------
        AcisFile
            An :py:class:`~abaqus.Part.AcisFile.AcisFile` object.
        """
        ...

    @abaqus_method_doc
    def openStep(self, fileName: str, scale: float = 1):
        """This method creates an AcisFile object from a file containing STEP-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the STEP file to open.
        scale
            A Float specifying the scaling factor to apply to the imported geometric entities. The
            default value is 1.0.

        Returns
        -------
        AcisFile
            An :py:class:`~abaqus.Part.AcisFile.AcisFile` object.

        Raises
        ------
        Texterror: Failed to read STEP file
            The data in the STEP file are corrupted.
        """
        ...

    @abaqus_method_doc
    def openVda(self, fileName: str):
        """This method creates an AcisFile object from a file containing VDA-FS-format geometry.
        This object is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the VDA-FS file to open.

        Returns
        -------
        AcisFile
            An :py:class:`~abaqus.Part.AcisFile.AcisFile` object.

        Raises
        ------
        Texterror: Failed to read VDA file
            The data in the VDA-FS file are corrupted.
        """
        ...

    @abaqus_method_doc
    def openSolidworks(self, fileName: str, topology: Literal[C.WIRE, C.SOLID, C.SHELL] = SOLID):
        """This method creates an AcisFile object from a file containing Solidworks format
        geometry. This object is subsequently used by the PartFromGeometryFile method.

        .. note::
            This function can be accessed by::

                mdb.openAcis

        .. versionadded:: 2020
            The `openSolidworks` method was added.

        Parameters
        ----------
        fileName
            A String specifying the path to the Solidworks file to open.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID, SHELL, and WIRE. If **topology** = SOLID,
            Abaqus/CAE attempts to attach cells to create a solid entity. If **topology** = SHELL,
            Abaqus/CAE builds the body as a shell entity, not as a solid entity. The default value
            is SOLID.

        Returns
        -------
            An AcisFile object.

        Raises
        ------
        Texterror: Failed to read Solidworks file
            The data in the Solidworks file are corrupted.
        """
        ...

    @abaqus_method_doc
    def writeAcisFile(self, fileName: str, version: Optional[float] = None):
        """This method exports the assembly to a named file in ACIS format.

        Parameters
        ----------
        fileName
            A String specifying the name of the file to which to write. The file name's extension is
            used to determine whether a part or assembly is written. Use the file extension .asat
            for the assembly format.

            .. versionchanged:: 2018
                Add description for thr file name's extension.
        version
            A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS
            Version 12.0. The default value is the current version of ACIS.
        """
        ...
