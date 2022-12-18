import unittest

from pdfcomposer.__main__ import compose


class TestCompose(unittest.TestCase):
    def test_compose(self):
        actual = compose('output_file_path.pdf', *['input_file_1_path.pdf', 'input_file_2_path.pdf'])
        expected = None
        self.assertEqual(actual, expected)
