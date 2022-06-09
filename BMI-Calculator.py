def result():
    if bmi <= 18.4:
        return "Underweight"

    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal weight"

    elif bmi >= 25.0 and bmi <= 29.9:
        return "Preadiposity"

    elif bmi >= 30.0 and bmi <= 34.9:
        return "Obesity grade 1 'moderate obesity'"

    elif bmi >= 35.0 and bmi <= 39.9:
        return "besity grade 2 'severe obesity'"

    elif bmi >= 40.0:
        return "Adipositas Grad 3 'extreme Adipositas'"

if __name__ == "__main__":
    try:
        print("--BMI RECHNER--")
    
        weight: float = float(input("Your weight in kilograms: "))
        size: float = float(input("Your size in meters: "))
        bmi: float = weight/size/size
        weight_classes: str = result()
        
        print("Your BMI value is " + str(int(bmi)) + " " + str(weight_classes))
    except ValueError:
        print("Invalid input!")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt STRG-C")
