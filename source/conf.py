'''
Author: Ligcox
Date: 2022-08-06 21:59:22
FilePath: /bubble/doc/source/conf.py
LastEditors: Ligcox
LastEditTime: 2022-08-07 19:53:29
License: GNU General Public License v3.0. See LICENSE file in root directory.
Copyright (c) 2022 Birdiebot R&D Department
Shanghai University Of Engineering Science. All Rights Reserved
'''
import time

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bubble'
author = 'ligcox'
release = 'v1.0'
copyright = '{}, {}'.format(time.strftime('%Y'), 'Birdiebot R&D Department Shanghai University Of Engineering Science')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_tabs.tabs',
    # 'sphinx.ext.imgmath'
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
    'preamble': r'''
                \usepackage[titles]{tocloft}
                \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
                \setlength{\cftchapnumwidth}{0.75cm}
                \setlength{\cftsecindent}{\cftchapnumwidth}
                \setlength{\cftsecnumwidth}{1.25cm}
                \usepackage[table,xcdraw]{xcolor}
                \documentclass[xcolor=table]{beamer}
                ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'