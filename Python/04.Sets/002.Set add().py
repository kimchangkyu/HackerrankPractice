number = int(input())
countries = []

for num in range(number):
    country = input()
    countries.append(country)

print(len(set(countries)))