# Computations with Abaqus results

This section discusses computations with Abaqus results in the Abaqus Scripting Interface.

## Rules for the mathematical operations

Mathematical operations are supported for FieldOutput, FieldValue, and HistoryOutput objects. These operators allow you to perform linear superposition of Abaqus results or to create more complex derived results from Abaqus results.

The following rules apply:

- The operations are performed on the components of a tensor or vector.

- The invariants are computed from the component values. For example, taking the absolute value of a tensor can result in negative values of the pressure invariant.

- Operations between FieldOutput, FieldValue, and HistoryOutput objects are not supported.

- Multiplication and division are not supported between two vector objects nor between two tensor objects.

- The types in an expression must be compatible. For example,

  - A vector cannot be added to a tensor.
  - A three-dimensional surface tensor cannot be added to a three-dimensional planar tensor.
  - INTEGRATION_POINT data cannot be added to ELEMENT_NODAL data.

- If the fields in the expression were obtained using the getSubset method, the same getSubset operations must have been applied in the same order to obtain each field.

- Arguments to the trigonometric functions must be in radians.

- Operations on tensors are performed in the local coordinate system, if it is available. Otherwise the global system is used. Abaqus assumes that the local coordinate systems are consistent for operations involving more than one tensor.

- Operations between FieldValue objects associated with different locations in the model are allowed only if the data types are the same. If the locations in the model differ, the FieldValue computed will not be associated with a location. If the local coordinate systems of the FieldValue objects are not the same, the local coordinate systems of both fieldValues will be disregarded and the fieldValue computed will have no local coordinate system.

The FieldOutput operations are significantly more efficient than the FieldValue operators. You can save the computed FieldOutput objects with the following procedure (see the example, {ref}`computations-with-fieldoutput-objects`):

- Create a new FieldOutput object in the output database.
- Use the addData method to add the new computed field objects to the new FieldOutput object.

## Valid mathematical operations

Table 1 describes the abbreviations that are used in mathematical operations.

**Table 1. Abbreviations.**

| Abbreviation | Allowable values                                                                            |
| ------------ | ------------------------------------------------------------------------------------------- |
| all          | FieldOutput objects, FieldValue objects, HistoryVariable objects, or floating point numbers |
| float        | floating point numbers                                                                      |
| FO           | FieldOutput objects                                                                         |
| FV           | FieldValue objects                                                                          |
| HO           | HistoryOutput objects                                                                       |

Table 2 shows the valid operations on FieldOutput objects.

**Table 2. Valid operations.**

| Symbol                            | Operation                                  | Return value |
| --------------------------------- | ------------------------------------------ | ------------ |
| all + float                       | addition                                   | all          |
| FO + FO                           |                                            | FO           |
| FV + FV                           |                                            | FV           |
| HO + HO                           |                                            | HO           |
| -all                              | unary negation                             | all          |
| all - float                       | subtraction                                | all          |
| FO - FO                           |                                            | FO           |
| FV - FV                           |                                            | FV           |
| FO \* FO (only if FO is a scalar) | multiplication                             | FO           |
| all \* float                      |                                            | all          |
| FO / FO (only if FO is a scalar)  | division                                   | FO           |
| all / float                       |                                            | all          |
| abs(all)                          | absolute value                             | all          |
| acos(all)                         | arccosine                                  | all          |
| asin(all)                         | arcsine                                    | all          |
| atan(all)                         | arctangent                                 | all          |
| cos(all)                          | cosine                                     | all          |
| degreeToRadian (all)              | convert degrees to radians                 | all          |
| exp(all)                          | natural exponent                           | all          |
| exp10(all)                        | base 10 exponent                           | all          |
| log(all)                          | natural logarithm                          | all          |
| log10(all)                        | base 10 logarithm                          | all          |
| float \*\* float                  | raise to a power                           | all          |
| power(FO, float)                  |                                            | FO           |
| power(FV, float)                  |                                            | FV           |
| power(HO, float)                  |                                            | HO           |
| radianToDegree (all)              | convert radian to degree                   | all          |
| sin(all)                          | sine                                       | all          |
| sqrt(all)                         | square root                                | all          |
| tan(all)                          | tangent                                    | all          |
| complexMagnitude(FO)              | magnitude of the complex field output      | FO           |
| complexPhase(FO)                  | phase of the complex field output          | FO           |
| complexReal(FO)                   | real part of the complex field output      | FO           |
| complexImag(FO)                   | imaginary part of the complex field output | FO           |

## Envelope calculations

You use envelope calculations to retrieve the extreme value for an output variable over a number of fields. Envelope calculations are especially useful for retrieving the extreme values over a number of load cases.

The following operators consider a list of fields and perform the envelope calculation:

```python2
(env, lcIndex) = maxEnvelope([field1, field2, ...])
(env, lcIndex) = minEnvelope([field1, field2, ...])

(env, lcIndex) = maxEnvelope([field1, field2, ...],
                            invariant)
(env, lcIndex) = minEnvelope([field1, field2, ...],
                            invariant)

(env, lcIndex) = maxEnvelope([field1, field2, ...],
                            componentLabel)
(env, lcIndex) = minEnvelope([field1, field2, ...],
                            componentLabel)
```

The envelope commands return two FieldOutput objects.

- The first object contains the requested extreme values.
- The second object contains the indices of the fields for which the extreme values were found. The indices derive from the order in which you supplied the fields to the command.

The optional **invariant** argument is a Symbolic Constant specifying the invariant to be used when comparing vectors or tensors. The optional **componentLabel** argument is a odb_String specifying the component of the vector or tensor to be used for selecting the extreme value.

The following rules apply to envelope calculations:

- Abaqus compares the values using scalar data. If you are looking for the extreme value of a vector or a tensor, you must supply an invariant or a component label for the selection of the extreme value. For example, for vectors you can supply the MAGNITUDE invariant and for tensors you can supply the MISES invariant.

- The fields being compared must be similar. For example,

  - VECTOR and TENSOR_3D_FULL fields cannot appear in the same list.
  - The output region of all the fields must be the same. All the fields must apply to the whole model, or all the fields must apply to the same set.

## Transformation of results

Transformations of vector and tensor fields are supported for rectangular, cylindrical, and spherical coordinate systems. The coordinate systems can be fixed or model based. Model-based coordinate systems refer to nodes for position and orientation. Abaqus uses the coordinates of the deformed state to determine a systems origin and orientation for model-based coordinate systems. Transformations that use a model-based coordinate system can account for large displacements of both the coordinate system and the structure.

The steps required to transform results are (see also the example {ref}`transformation-of-field-results`):

- Create the coordinate system.
- Retrieve the field from the database.
- Use the `fieldOutput.getTransformedField` method to obtain a new field with the results in the specified coordinate system.
- For large displacement of the structure and coordinate system, you must also retrieve the displacement field at the frame. You must compute this displacement field for the whole model to ensure that the required displacement information is available.

The following rules apply to the transformation of results:

- Beams, truss, and axisymmetric shell element results will not be transformed.

- The component directions 1, 2, and 3 of the transformed results will correspond to the system directions **X**, **Y**, and **Z** for rectangular coordinate systems; $R$, $\theta$, and **Z** for cylindrical coordinate systems; and $R$, $\theta$, and $\phi$ for spherical coordinate systems.

  ```{note}
  Stress results for three-dimensional continuum elements transformed into a cylindrical system would have the hoop stress in S22, which is consistent with the coordinate system axis but inconsistent with the stress state for a three-dimensional axisymmetric elements having hoop stress in S33.
  ```

- When you are transforming a tensor, the location or integration point always takes into account the deformation. The location of the coordinate system depends on the model, as follows:

  - If the system is fixed, the coordinate system is fixed.
  - If the system is model based, you must supply a displacement field that determines the instantaneous location and orientation of the coordinate system.

- Abaqus will perform transformations of tensor results for shells, membranes, and planar elements as rotations of results about the element normal at the element result location. The element normal is the normal computed for the frame associated with the field by Abaqus, and you cannot redefine the normal. Abaqus defines the location of the results location from the nodal locations. You specify optional arguments if you want to use the deformed nodal locations to transform results. For rectangular, cylindrical, and spherical coordinate systems the second component direction for the transformed results will be determined by one of the following:

  - The **Y** - axis in a rectangular coordinate system.
  - The $\theta$-axis in a cylindrical coordinate system.
  - The $\theta$-axis in a spherical coordinate system.
  - A user-specified datum axis projected onto the element plane.

  If the coordinate system used for projection and the element normal have an angle less than the specified tolerance (the default is 30°), Abaqus will use the next axis and generate a warning.
