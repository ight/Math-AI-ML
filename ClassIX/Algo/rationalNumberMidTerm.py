def main():
    numberOne = int(input("Enter the first number"))
    numberTwo = int(input("Enter the second number"))
    numberOfRationalNum = int(input("Enter the number of rational number required"))
    baseNumerator = (numberOne + numberTwo)
    baseDenominator = 2
    print(f"{baseNumerator} / {baseDenominator}")
    for i in range(numberOfRationalNum):
        baseDenominator = baseDenominator * 2
        baseNumerator = baseDenominator + baseNumerator
        print(f"{baseNumerator} / {baseDenominator}")

if __name__ == "__main__":
    main()