
#x = "hallo\nwelt"
x = "\"hallo\"\tweltöäüß\\"

print(x)
print("123\t12")
print("50\t12")
print("1234\t12")

print("1234", "5678", sep="\t")

print('"H"allo')

print(x.replace("allo", "ALLO"))
print(x.upper())
print(x.lower())
print(x.casefold())

print(x.upper() == "HALLO")

print(len(x))
print("Hallo".casefold() in x.casefold())

a = 12345

print(f"Variable a ist {a}")
print(f"Variable a ist {a=}")
print(f"Variable a ist {a:,}".replace(",", "'"))

