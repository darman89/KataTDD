from unittest import TestCase

from Statistics import Statistics


class StatisticsTest(TestCase):
    def test_values(self):
        self.assertEqual(Statistics().values(""), [], "Cadena Vacía")

    def test_values_one_number(self):
        self.assertEqual(Statistics().values("1"), [1], "Un Número")
