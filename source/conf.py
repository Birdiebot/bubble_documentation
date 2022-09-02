
# Copyright (c) 2022 Birdiebot R&D Department
# Shanghai University Of Engineering Science. All Rights Reserved
# License: GNU General Public License v3.0.
# See LICENSE file in root directory.
# 
# Author: ligcox ligcox@birdiebot.top
# Date: 2022-09-02 00:41:53
# FilePath: /bubble/src/bubble_documentation/source/conf.py
# LastEditors: ligcox ligcox@birdiebot.top
# LastEditTime: 2022-09-02 14:45:04

import time
import os
import sys

sys.path.insert(0, os.path.abspath(r"/mnt/hgfs/bubble/src/bubble_core/bubble_protocol/bubble_protocol/.."))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bubble'
author = 'Birdiebot'
release = 'v1.0'
copyright = '{}, {}'.format(time.strftime('%Y'), 'Birdiebot R&D Department Shanghai University Of Engineering Science')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_tabs.tabs',
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    "sphinx.ext.mathjax"
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_favicon = 'favicon.ico'
html_logo = 'logo.png'


latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
        \setmainfont{DejaVu Serif}
        \setsansfont{DejaVu Sans}
        \setmonofont{DejaVu Sans Mono}
        ''',
            'preamble': r'''
        \usepackage[titles]{tocloft}
        \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
        \setlength{\cftchapnumwidth}{0.75cm}
        \setlength{\cftsecindent}{\cftchapnumwidth}
        \setlength{\cftsecnumwidth}{1.25cm}
        ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'