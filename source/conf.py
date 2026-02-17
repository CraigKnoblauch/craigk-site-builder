# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Craig Knoblauch'
copyright = '2026, Craig Knoblauch'
author = 'Craig Knoblauch'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design"
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_css_files = [
    'custom.css'
]

html_theme_options = {
    "github_url": "https://github.com/CraigKnoblauch",
    "linkedin_url": "https://www.linkedin.com/in/craig-knoblauch-b88563124",
    "secondary_sidebar_items": [],
    "logo": {
        "text": "Craig Knoblauch",
        "image_light": "_static/logo.png", 
        "image_dark": "_static/logo.png"
    }
}
