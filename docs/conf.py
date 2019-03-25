# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'OpenRazer Python Library'
copyright = '2019, OpenRazer contributors'
author = 'OpenRazer contributors'

version = '0.0.1'
release = '0.0.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
]

source_suffix = '.rst'

master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'openrazer', 'OpenRazer Python Library Documentation',
     [author], 1)
]

# -- Extension configuration -------------------------------------------------
