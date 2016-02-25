


def molarMassCalc(num_of_elements):
    i = 0
    molar_mass = 0
    while i < num_of_elements:
        amount = float(input("Number of atoms: "))
        amu = float(input("Element amu: "))
        molar_mass += (amount * amu)
        i += 1
    print(str(molar_mass) + "g")
