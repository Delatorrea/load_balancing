import unittest
from load.core import Input


class TestInput(unittest.TestCase):

    def test_deve_retornar_arquivo_input(self):
        data = Input()
        archive = open('input.txt', 'r')
        self.assertEqual(archive, data.archive)
        archive.close()


if __name__ == '__main__':
    unittest.main()
