# Gumshoe PDF Composer


Composes one PDF file from the given PDF files, in the order they were given.


## Installation

To install, run `pip install gumshoePDFComposer`



## Examples

```python

import gumshoePDFComposer as compose

outfile = 'temp/P2290101177/outfilename.pdf'
files = ['infilename1.pdf', 'infilename2.pdf']
compose(outfile, *files)

# [ Created ]: temp/P2290101177/output.pdf

```


