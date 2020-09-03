from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name = 'bibdesk2zotero',
    version = '0.0.2',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    url = 'https://github.com/edsu/bibdesk2zotero',
    py_modules = ['bibdesk2zotero',],
    description = 'convert BibDesk BibTeX files for import into Zotero',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires = ['pybtex'],
    entry_points = {'console_scripts': ['bibdesk2zotero = bibdesk2zotero:main']},
)
