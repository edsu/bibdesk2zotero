from setuptools import setup

setup(
    name = 'bibdesk2zotero',
    version = '0.0.1',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    url = 'https://github.com/edsu/bibdesk2zotero',
    py_modules = ['bibdesk2zotero',],
    description = 'convert BibDesk BibTeX files for import into Zotero',
    install_requires = ['pybtex'],
    entry_points = {'console_scripts': ['bibdesk2zotero = bibdesk2zotero:main']},
)
