import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abqpy",
    version="2022.0",
    author="WANG Hailin",
    author_email="hailin.wang@connect.polyu.hk",
    description="Type hints for Abaqus/Python scripting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haiiliin/abqpy",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'GitHub': 'https://github.com/haiiliin/abqpy',
        'Bug Tracker': 'https://github.com/haiiliin/abqpy/issues',
        'Pull Requests': 'https://github.com/haiiliin/abqpy/pulls',
        'Discussions': 'https://github.com/haiiliin/abqpy/discussions',
        'Documentation': 'https://abqpy.haiiliin.com',
        'Anaconda': 'https://anaconda.org/haiiliin/abqpy',
        'Read the Docs': 'https://readthedocs.org/projects/abqpy',
    },
    python_requires='>=3.7',
    package_dir={'': 'src'},
    install_requires=['ipyparams', 'typing-extensions'],
    packages=setuptools.find_packages('src'),
    py_modules=['abaqusConstants', 'animation', 'annotationToolset', 'assembly', 'caeModules', 'caePrefsAccess',
                'calibration', 'connectorBehavior', 'customKernel', 'deleteObjectCallback', 'displayGroupMdbToolset',
                'displayGroupOdbToolset', 'driverUtils', 'field', 'fields', 'inpParser', 'interaction', 'material',
                'mesh', 'meshEdit', 'methodCallback', 'monitorManager', 'odbAccess', 'odbConnectorBehavior',
                'odbMaterial', 'odbSection', 'part', 'redentABQ', 'section', 'symbolicConstants', 'textRepr',
                'upgradeScript', 'visualization'],
)
