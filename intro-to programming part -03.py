# Function to convert salary to corresponding currency
def convertSalary(salary, country):
    if country == "Canada":
        converted_salary = salary * 1.47 / 1.0
        currency_name = "CAD"
        avg_salary = 64000
    elif country == "USA":
        converted_salary = salary * 1.18 / 1.0
        currency_name = "USD"
        avg_salary = 56516
    elif country == "Cambodia":
        converted_salary = salary * 4847.38 / 1.0
        currency_name = "Cambodian Riel"
        avg_salary = 5649856
    elif country == "United Kingdom":
        converted_salary = salary * 0.91 / 1.0
        currency_name = "Pound Sterling"
        avg_salary = 35423
    else:
        converted_salary = None
        currency_name = None
        avg_salary = None
        print("Invalid country entered")
    return converted_salary, currency_name, avg_salary

# Take inputs from user
salary = float(input("Enter your salary per annum in Euros: "))
country = input("Enter the country you want to migrate to: ")

# Convert salary to corresponding currency and get currency name and average salary of country
converted_salary, currency_name, avg_salary = convertSalary(salary, country)

# Compare converted salary with average salary of country and print result
if converted_salary is not None:
    if converted_salary > avg_salary:
        print("You will be rich in {} with a salary of {} {}".format(country, converted_salary, currency_name))
    else:
        print("You will be poor in {} with a salary of {} {}".format(country, converted_salary, currency_name))
