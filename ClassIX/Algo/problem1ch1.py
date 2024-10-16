def main():
    numberOne = int(input("Enter the first number"))
    numberTwo = int(input("Enter the second number"))
    numberOfRationalNum = int(input("Enter the number of rational number required"))
    baseNumerator = numberOne*(numberOfRationalNum + 1)
    baseDenominator = numberOfRationalNum + 1

    for i in range(numberOfRationalNum):
        baseNumerator = baseNumerator + 1
        print(f"{baseNumerator} / {baseDenominator}")

if __name__ == "__main__":
    main()