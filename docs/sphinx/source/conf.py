# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Lenstool'
copyright = '2023, Allingham et al. (add your names)'
author = 'Allingham et al.'

release = '8.1'
version = '8.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgmath', 
    'sphinx.ext.todo',
#    'breathe',   # add it if doing C api. Requires to install breathe.
#    'sphinx.ext.duration',
#    'sphinx.ext.autosummary',
#    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' # 'haiku' # 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

#html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Extension configuration -------------------------------------------------
if False:
    import subprocess
    subprocess.call('make clean', shell=True)
    subprocess.call('cd ../../doxygen ; doxygen', shell=True)

    breathe_projects = { "lenstool": "../../../docs/doxygen/build/xml/" }
    breathe_default_project = "lenstool"
    breathe_projects_source = {
        "o_chi" : ( "../../../../src", ["o_chi.c"] )
    }