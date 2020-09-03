#!/usr/bin/env python3

#
# This little program reads in a BibDesk BibTex file and writes it out with the
# the quirky file locations (Base64 encoded plists) written as simple paths that 
# can be understood by Zotero.
#
# For this to work you'll need to install pybtex.
# 
# usage: ./bibdesk2zotero.py citations.bib /path/to/files > citations-new.db
#

import os
import re
import sys
import base64
import pathlib
import plistlib
import unicodedata
import pybtex.database

from pybtex.utils import OrderedCaseInsensitiveDict


def main():
    if len(sys.argv) != 3:
        sys.exit('Usage: bibdesk2zotero.py citations.db /path/to/files > citations-new.db')

    bib_file = sys.argv[1]

    if not os.path.isfile(bib_file):
        sys.exit('{} is not a file'.format(bib_file))

    base_dir = pathlib.Path(sys.argv[2])
    if not os.path.isdir(base_dir):
        sys.exit('{} is not a directory'.format(base_dir))

    new_bib = convert(bib_file, base_dir)
    print(new_bib)


def convert(bib_file, base_dir):
    db = pybtex.database.parse_file(bib_file)

    for key in db.entries:
        entry = db.entries[key]
        for field_name in entry.fields:
            m = re.match('^Bdsk-File-(\d+)$', field_name)
            if m:
                bdsk = entry.fields[field_name]
                bdsk_decoded = base64.b64decode(bdsk)
                plist = plistlib.loads(bdsk_decoded)
                file_path = base_dir / unicodedata.normalize('NFC', plist['relativePath'])

                if m.group(1) == '1':
                    new_field_name = 'File'
                else:
                    new_field_name = 'File-' + m.group(1)
               
                # Strangely pybtex.database.Entry objects don't allow fields to be deleted. 
                # This little workaround converts the fields to a normal dictionary and 
                # then modifies it, and assigns the fields back to the entry again.
                #
                # See this issue for more:
                # https://bitbucket.org/pybtex-devs/pybtex/issues/57/

                fields = dict(entry.fields)
                fields[new_field_name] = str(file_path)
                fields.pop(field_name)
                entry.fields = fields

    return db.to_string('bibtex')


if __name__ == "__main__":
    main()
