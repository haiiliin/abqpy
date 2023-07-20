"""
Parameter Identification
========================

This is a simple example of parameter identification. The compression model is a simple model with a cube of 1x1x1 m.
The lower surface is fixed and the upper surface is loaded with a pressure of 100 Pa. The goal is to find the Young's
modulus of the material that gives a maximum displacement of -0.1 m.

.. figure:: /images/model.png
    :width: 50%
    :align: center

    A simple compression model.

Theoretically, the Young's modulus of the material can be calculated with the following equation:

.. math::

    E = \\frac{\\sigma}{\\epsilon} = \\frac{P}{u_{\max}/h} = \\frac{100}{0.1 / 1.0} = 1000

The output of this script is:

.. code-block:: none

    Search results:
         modulus   fitness
    0       10.0  9.774944
    1      100.0  0.887494
    2     1000.0  0.001251
    3    10000.0  0.090125
    4   100000.0  0.099013
    5  1000000.0  0.099901

    Best modulus=1000.0 with fitness=0.0012505635619163569
"""
import os

import numpy as np
import pandas as pd


def fitness(x: float, maxdisp_expected: float = -0.1):
    # Change the working directory to a new folder
    wd = os.path.join(os.path.dirname(__file__), f"Job-E={x}")
    os.makedirs(wd, exist_ok=True)
    os.chdir(wd)

    # Run the model and read the output, the additional argument can be read by the Abaqus/Python script
    os.system(f"python ../compression.py {x},0.2")

    # Read the output and calculate the fitness
    data = pd.read_csv("data.csv")
    maxdisp = data["U3"].iloc[-1]
    return abs(maxdisp - maxdisp_expected)


def grid_search(search_space: list[float], expected: float):
    fs = []
    for x in search_space:
        print(f"Running model for E={x}")
        fs.append(fitness(x, expected))
    argmin = np.argmin(fs)
    best = search_space[argmin]
    print("Search results:", pd.DataFrame({"modulus": search_space, "fitness": fs}), sep="\n")
    print(f"\nBest modulus={best} with fitness={fs[argmin]}")
    return best


if __name__ == "__main__":
    E = grid_search([1e1, 1e2, 1e3, 1e4, 1e5, 1e6], -0.1)
