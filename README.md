# Gumshoe PDF Composer


Composes one PDF from the given pdf files, in the given sequence,
then writes it to the given outfile path.


## Installation


To install, run `pip install pdfcomposer`


## Examples


### Compose PDF 


```python

from pdfcomposer import compose

outfile = 'outfilename.pdf'
files = ['infilename1.pdf', 'infilename2.pdf']
compose(outfile, *files)


```




