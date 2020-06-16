print("\nZakładamy, że adresy to dowolne liczby o formacie XX-XXX.\n")


def number_to_postal_code(postal_code):
    postal_code = str(postal_code)
    return postal_code[:2] + '-' + postal_code[2:]


address_1 = "79-900"
address_2 = "80-155"

start = int("".join(address_1.split('-')))
end = int("".join(address_2.split('-')))

print(f"Kody pomiędzy {address_1} a {address_2} to:\n{[number_to_postal_code(x) for x in range(start + 1, end)]}")
