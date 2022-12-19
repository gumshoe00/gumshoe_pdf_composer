import pathlib
import unittest
from unittest.mock import patch
from io import StringIO

from pdfcomposer import Api



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
        _dir = pathlib.Path(__file__).parent.joinpath('mockdata')
        api = Api()
        print(api('compose', *[str(_dir.joinpath('output.pdf')), str(_dir.joinpath('infile1.pdf')), str(_dir.joinpath('infile1.pdf'))]))

        self.assertTrue(_dir.joinpath('output.pdf').exists())
