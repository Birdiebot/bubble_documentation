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

extensions = []

templates_path = ['_templates']
exclude_patterns = [
    "pages/study"
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
