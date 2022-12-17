"""
Example:

    $ python src/gumshoe_pdf_composer/__main__.py \
             temp/P2290101177/output.pdf  \
             temp/P2290101177/10.pdf temp/P2290101177/11.pdf

    # [ Created ]: temp/P2290101177/output.pdf

"""

from builtins import print, str, Exception, len, list

import sys

from pikepdf import Pdf


def compose(outfile, *files):
    _output = Pdf.new()
    for _f in files:
        if str(_f).endswith('.pdf'):
            _pdf = Pdf.open(_f)
            _output.pages.extend(_pdf.pages)

    _output.save(outfile)

    print('[ Created ]:', outfile)


def main():
    _outfile = ''
    _files = []
    _args = sys.argv

    try:
        _outfile = _args[1]
    except Exception as e:
        print(e)

    try:
        _files.extend(_args[2:])
    except Exception as e:
        print(e)

    if _outfile and len(list(_files)) > 0:
        compose(_outfile, *_files)


if __name__ == '__main__':
    main()
