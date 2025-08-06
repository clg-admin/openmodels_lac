# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ECU_NDC'
copyright = '2025, ClimateLeadGroup'
author = 'ClimateLeadGroup'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- GitHub Edit Button ------------------------------------------------------
html_context = {
    "display_github": True,  # Mostrar "Edit on GitHub"
    "github_user": "clg-admin",  # Tu usuario u organización en GitHub
    "github_repo": "ECU_NDC",  # Nombre del repositorio
    "github_version": "main",  # Rama en la que está la documentación
    "conf_py_path": "/docs/",  # Ruta dentro del repo donde está config.py
}

html_theme_options = {
    "style_nav_header_background": "#2980B9",  # Color opcional del encabezado
    "display_version": True,  # Muestra la versión del proyecto
    "prev_next_buttons_location": "bottom",  # Botones "prev" y "next"
}