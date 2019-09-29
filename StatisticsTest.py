from unittest import TestCase

from Statistics import Statistics


class StatisticsTest(TestCase):
    def test_values(self):
        self.assertEqual(Statistics().values(""), [], "Cadena Vacía")

    def test_values_one_number(self):
        self.assertEqual(Statistics().values("1"), [1], "Un Número")
        self.assertEqual(Statistics().values("2"), [2], "Un Número")
        self.assertEqual(Statistics().values("3"), [3], "Un Número")

    def test_values_two_numbers(self):
        self.assertEqual(Statistics().values("1,2"), [1, 2], "Dos Números")
