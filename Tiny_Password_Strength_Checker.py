


import string

def password_strength_checker():
    password = input("Enter password to check: ")

    length = lambda p: len(p) >= 8
    has_uppercase = lambda p: any(c.isupper() for c in p)
    has_lowercase = lambda p: any(c.islower() for c in p)
    has_number = lambda p: any(c.isdigit() for c in p)
    has_symbol = lambda p: any(c in string.punctuation for c in p)

    # RULE NAME : RULE FUNCTION
    rules_functions = {
        "length": length,
        "uppercase": has_uppercase,
        "lowercase": has_lowercase,
        "number": has_number,
        "symbol": has_symbol
    }

    # dictionary comprehension
    results = {name: func(password) for name, func in rules_functions.items()}

    # list comprehension
    score = sum(1 for r in results.values() if r)

    print("\nRule Results\n")
    for i, (name, result) in enumerate(results.items()):
        print(f"{i}. {name}: {result}")

    if score <= 2:
        print("\nPassword strength: Password needs work")
    elif score <= 4:
        print("\nPassword strength: Password ok")
    else:
        print("\nPassword strength: You have a strong Password")

if __name__ == "__main__":
    password_strength_checker()