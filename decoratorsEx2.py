# Decorators Example 2 - formatting phone number
def format(func):
    def inner(num):
        print(f"+{num[:-10]} {func(num)}")  # formats the phone number into country code & rest of the phone number
    return inner

@format
def phoneNum(phone):
    return phone[-10:] # returns only the phone number excluding the country code

phone = input("Enter your Phone Number: ")
phoneNum(phone)


