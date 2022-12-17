import unittest

from gumshoe_pdf_composer.__main__ import compose


class TestCompose(unittest.TestCase):
    def test_compose(self):
        actual = compose('outfilename.pdf', *['infilename1.pdf', 'infilename2.pdf'])
        expected = None
        self.assertEqual(actual, expected)
