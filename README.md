# bibdesk2zotero

This is a little utility for rewriting a BibDesk BibTeX file so that it can be
read by Zotero with the file references intact. BibDesk and Zotero mostly get
along except for the way BibFile stores links to documents like PDFs. This
utility Base64 decodes all Bdesk-File paths, parses the serialized [plist],
extracts the relative path to the file and adds it back to the bibliographic
entry as an absolute path.

[plist]: https://en.wikipedia.org/wiki/Property_list

## Install

    pip install bibdesk2zotero 

## Use

    $ bibdesk2zotero citations.bib /path/to/pdf/files/ > new-citations.bib
