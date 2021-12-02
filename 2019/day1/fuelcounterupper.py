import math


def fuelForMass(moduleMass):
    fuelRequired = math.floor(moduleMass / 3) - 2
    return fuelRequired


def fuelForModule(moduleMass):
    massToFuel = moduleMass
    fuelForModule = 0

    while massToFuel > 0:
        fuelForThisMass = fuelForMass(massToFuel)
        if fuelForThisMass >= 0:
            fuelForModule += fuelForThisMass
        massToFuel = fuelForThisMass
    return fuelForModule


def fuelForAll(massList):
    totalFuelRequirement = 0
    for moduleMass in massList:
        totalFuelRequirement += fuelForModule(int(moduleMass))
    return totalFuelRequirement


with open("moduleMassList.txt", "r") as moduleMassList:
    print(fuelForAll(moduleMassList))
