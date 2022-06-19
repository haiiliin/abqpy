import os
from sphinx.application import Sphinx

sphinx = Sphinx('docs\\source', 'docs\\source', 'docs\\build\html', 'docs\\build\\doctrees', 'html')
sphinx.build()

sphinx = Sphinx('docs\\source', 'docs\\source', 'docs\\build\\latex', 'docs\\build\\doctrees', 'latex')
sphinx.build()

os.chdir('docs\\build\\latex')
os.system('xelatex abqpy')
os.system('xelatex abqpy')
