import re

with open("3/input.txt") as inpt:
    memory = inpt.read()

products = []
for instruction in re.findall(r"mul\(\d+,\d+\)", memory):
    factors = [int(i) for i in re.findall(r"\d+", instruction)]
    products.append(factors[0] * factors[1])

print(sum(products))
