# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ActiveRPG'
copyright = '2023, Ntjandra'
author = 'Ntjandra'

release = '0.1'
version = '0.1.0'

# -- General configuration

master_doc = 'index' # Explicitly state index.rst is the root/master doc.

# -- Allow Non-Published Packages with path to packages.
import os
import sys
sys.path.insert(0, os.path.abspath('../code'))

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# REQUIRED FOR DEPLOYMENT
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
# epub_show_urls = 'footnote'
