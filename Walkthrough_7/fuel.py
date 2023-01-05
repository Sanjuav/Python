try:
    fuel = int(input("Enter in litres: "))
    consumption = int(input("Enter consumption per minute: "))
    endurance = fuel//consumption
    print("Endurance:", endurance)
except ValueError:
    print("Kindly enter integer value")
