import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abqpy",
    author="WANG Hailin",
    author_email="hailin.wang@connect.polyu.hk",
    description="Type hints for Abaqus/Python scripting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://abqpy.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'GitHub': 'https://github.com/haiiliin/abqpy',
        'Bug Tracker': 'https://github.com/haiiliin/abqpy/issues',
        'Documentation': 'https://docs.abqpy.com',
        'Anaconda': 'https://anaconda.org/haiiliin/abqpy',
    },
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "node-and-date",
        "write_to": "src/abqpy/_version.py",
        "fallback_version": "2023.0.0-dev",
    },
    setup_requires=['setuptools_scm'],
    python_requires='>=3.7',
    package_dir={'': 'src'},
    install_requires=['typing-extensions', 'auto-all', 'Jinja2', 'toml'],
    packages=setuptools.find_packages('src'),
    py_modules=['ababltin', 'abaqusConstants', 'animation', 'annotationToolset', 'assembly', 'caeModules',
                'caePrefsAccess', 'calibration', 'connectorBehavior', 'customKernel', 'deleteObjectCallback',
                'displayGroupMdbToolset', 'displayGroupOdbToolset', 'driverUtils', 'field', 'fields', 'inpParser',
                'interaction', 'material', 'mesh', 'meshEdit', 'methodCallback', 'monitorManager', 'odbAccess',
                'odbConnectorBehavior', 'odbMaterial', 'odbSection', 'part', 'redentABQ', 'section',
                'symbolicConstants', 'textRepr', 'upgradeScript', 'visualization', 'regionToolset', 'step', 'load',
                'optimization', 'job', 'sketch', 'xyPlot'],
    entry_points={
        'console_scripts': [
            'abqpy = abqpy.__main__:cli',
        ]
    },
    package_data={'abqpy': ['templates/*.toml', 'templates/*.tmpl']},
)
