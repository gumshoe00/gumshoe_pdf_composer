# Gumshoe PDF Composer


Composes one PDF from the given pdf files, in the given sequence,
then writes it to the given outfile path.


## Installation


To install, run `pip install pdfcomposer`


## Examples

### Call the default from the command line

```shell

pdfcomposer --outputer default --args "hello world"

# prints out the input.  
# ('hello world',) {}

```

### Call a plugin (compose) from the command line

```shell

pdfcomposer --outputer compose \
  --args 'outfile.pdf' 'infile1.pdf' 'infile2.pdf'\
  --kwargs title="My PDF" author="John Doe" subject="My first PDF" creator="John Doe"

# composes a PDF with the content of infile1.pdf then infile2.pdf
# sets the PDF info with the given kwargs
# writes the PDF to ./outfile.pdf

```

### From a script 


```python

import pdfcomposer as composer

args = './outfile.pdf', './infile1.pdf', './infile2.pdf'

kwargs = dict(title="My PDF", author="John Doe", 
            subject="My first PDF", creator="John Doe")

composer(*args, **kwargs)

# composes a PDF with the content of infile1.pdf then infile2.pdf
# sets the PDF info with the given kwargs
# writes the PDF to ./outfile.pdf


```




