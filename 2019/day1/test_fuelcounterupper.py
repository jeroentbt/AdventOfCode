import fuelcounterupper
import unittest


class TestFuelCounterUpper(unittest.TestCase):

    def test_fuel_for_mass(self):
        testSet = [(12, 2),
                   (14, 2),
                   (1969, 654),
                   (100756, 33583)]
        for thisSet in testSet:
            moduleMass, fuel = thisSet
            self.assertEqual(fuelcounterupper.fuelForMass(moduleMass), fuel)

    def test_fuel_for_module(self):
        testSet = [(12, 2),
                   (14, 2),
                   (1969, 966),
                   (100756, 50346)]
        for thisSet in testSet:
            moduleMass, fuel = thisSet
            self.assertEqual(fuelcounterupper.fuelForModule(moduleMass), fuel)

        
    def test_fuel_requirement_all_modules(self):
        massList = [12, 14, 1969, 100756]
        self.assertEqual(fuelcounterupper.fuelForAll(massList),
                         sum([2, 2, 966, 50346]))


if __name__ == '__main__':
    unittest.main()
