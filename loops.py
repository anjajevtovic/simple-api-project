
#FOR LOOPS#

numbers = [1,2,3,4,5]

for number in numbers:
    print(number)
print(number)

list1 = list(range(0,5))
print(list1)

ran = range(4,9)
for n in ran:
    print(n)

# 5 is step
ran2 = range(45, 65, 5)
for n in ran2:
    print(n)

#looping in dict
hashes = {"bebe":12343534, "calw":984742974, "shapa":832783278}

for brand, brand_hash in hashes.items():
    print(f"\n{brand} - {brand_hash}")