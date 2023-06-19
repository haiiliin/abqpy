# abqpy docs

This is the source for the abqpy documentation. The documentation is built using [Sphinx](http://www.sphinx-doc.org/en/master/).

## Build the docs

To build the docs, you will need to install [Python](https://www.python.org/downloads/). Then, install the dependencies using pip from the root directory of the repository:

```bash
pip install .[docs]
```

After the dependencies are installed, you can build the docs by running the following command from the `docs` directory of the repository:

```bash
cd docs
make html
```

This will build the docs and place them in the `build/html` directory. You can then open the `index.html` file in your browser to view the docs.

## Contribute

If you would like to contribute to the documentation, you can do so by editing the `.rst` or `.md` files. You can then build the docs and view them locally to make sure they look correct. Once you are satisfied with your changes, you can submit a pull request.
