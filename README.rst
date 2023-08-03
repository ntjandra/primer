Development Steps
#################

Hosting
=======

Primer: https://primer.readthedocs.io

Project: https://readthedocs.org/projects/primer

Local Run
=========

Run the project locally to see how it will look. 

1. Build the project using the ``make.bat`` in ``/docs/`` with ``./make.bat html``.

2. Once the site is built, navigate to the homepage at ``build/html/index.html``.

3. You can shortcut open it in python with ``python -m webbrowser $(PWD)/build/html/index.html`` on bash.

**Note: If you're using a theme, you will need to import it or comment out ``html_theme = 'sphinx_rtd_theme'`` from the ``conf.py`` file.**

Resources
=========

Created with the ReadTheDocs Template: https://docs.readthedocs.io/en/stable/tutorial

Sphinx Basics: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html