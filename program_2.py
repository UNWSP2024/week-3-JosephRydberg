#Age Category Output Joseph Rydberg 9/16/24
def categorize_age(age):
    ageCategory = "NA"
    if age <= 1:
        ageCategory = "Infant"
    elif age > 1 and age < 13:
        ageCategory = "Child"
    elif age > 13 and age < 20:
        ageCategory = "Teenager"
    elif age >= 20:
        ageCategory = "Adult"


    return ageCategory

if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print ("They are a " + ageBucket)