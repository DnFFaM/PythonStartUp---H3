import base64

"Øvelese 1"

print("1 plus 1 equals " + str(1+1))

name = input("give me your name: ")
print("Hello " + name)

Loop = ["Hello", "Hello", "Hello", "Bye!"]
for x in Loop:
  print(x) 

"Øvelese 2"

a = 1

print (a)

b = "some text"

print (b)

print ("a is of type " + str(type(a).__name__))

print ("b is of type " + str(type(b).__name__))

c = 0 + 2j

print (c * c)

cc = 1 + 0j

resultat = cc * cc

print (resultat)

s = "Hello, World!"

hex_string = ":".join("{:02x}".format(ord(c)) for c in s)
print(hex_string)

decimal_string = " ".join(str(ord(c)) for c in s)
print (decimal_string)

binary = " ".join(format(ord(c), "b") for c in s)
print (binary) 

octal_string = " ".join("{:03o}".format(ord(c)) for c in s)
print(octal_string)

base64_string = base64.b64encode(s.encode()).decode()
print(base64_string)

unicode_string = " ".join(f"U+{ord(c):04X}" for c in s)
print(unicode_string)

"Øvelse 3 "


print()

print("Øvelse 5.1 (list)")

Fruits = ["Apple", "Banana", "Cherry", "Date"]

print(*Fruits)

Fruits.extend(["Elderberry", "Fig"])

size = len(Fruits)
print(size)

Fruits.remove("Cherry")

print(Fruits)

First = [Fruits[0]]
Last = [Fruits[-1]]
res = First + Last
print (res)

for fruit in Fruits:
    print(fruit)

Fruits.sort()
print(Fruits)


print()

print("Øvelse 5.2 (tuple)")

TFruits =("Apple", "Banana", "Cherry","Date")
print (TFruits)

Tsize = len(TFruits)
print (Tsize)

First = [TFruits[0]]
Last = [TFruits[-1]]
res = First + Last
print (res)

for tfruit in TFruits:
    print(tfruit)

my_list = list(TFruits)
my_list.extend(["Elderberry", "Fig"])

TFruits = tuple(my_list)
print(TFruits)


print()

print("Øvelse 5.3 (sets)")

SFruits = {"Apple", "Banana", "Cherry", "Date"}
print(SFruits)

SFruits.update({"Elderberry", "Fig"})
print(SFruits)

print(len(SFruits))

SFruits.remove("Cherry")
print(SFruits)

if "Banana" in SFruits:
    print("Yes, Banana is in this set")

for sfruit in SFruits:
    print(sfruit)

SFruits.clear()
print(SFruits)


print()

print("Øvelse 5.4 (dictionary)")

fruit_prices = {
    "Apple" : 0.99,
    "Banana" : 0.59,
    "Cherry" : 2.99,
    "Date" : 3.49
}
print(fruit_prices)

fruit_prices["Elderberry"] = 1.99
fruit_prices["Fig"] = 2.49

print(fruit_prices)

print(len(fruit_prices))

removed_value = fruit_prices.pop("Cherry")
print(removed_value)
print(fruit_prices)

print(fruit_prices["Banana"])

for key, values in fruit_prices.items():
    print(f"{key}: {values}")

fruit_prices.update({"Apple" : 1.09})

print(fruit_prices)

print(" En List er ensimple data storage. " "|" " En tuple er en samling, som er ordnet og uforanderlig. " "|" " Et sæt er en samling, som er uordnet, uforanderlig* og uindekseret. " "|" " En Dictionary er en samling, som er ordnet*, kan ændres og gemmeer key-value. ")