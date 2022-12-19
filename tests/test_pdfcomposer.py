import pathlib
import unittest
from unittest.mock import patch
from io import StringIO

from pdfcomposer import Api


MOC_DATA_DIR = pathlib.Path.cwd().parent.parent.parent.joinpath('mockdata')
print('mock data dir: ', MOC_DATA_DIR)

class TestPdfComposer(unittest.TestCase):
    @patch('sys.stdin', StringIO('pdfcomposer --outputer default'))
    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.stderr', new_callable=StringIO)
    def test_main(self, stderr, stdout):
        # Expect stderr
        err = ''

        # Expect stdout
        expected = ''

        # Check stdout and stderr
        self.assertEqual(stdout.getvalue(), expected)
        self.assertEqual(stderr.getvalue(), err)

    def test_api(self):
        api = Api()
        api(*[str(MOC_DATA_DIR.joinpath('output.pdf')),
              str(MOC_DATA_DIR.joinpath('infile1.pdf')),
              str(MOC_DATA_DIR.joinpath('infile1.pdf'))],
            **dict(path='compose'))

        self.assertTrue(MOC_DATA_DIR.joinpath('output.pdf').exists())
