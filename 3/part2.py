import re

with open("3/input.txt") as inpt:
    memory = inpt.read()

products = []
enabled = True
instruction: str
for instruction in re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", memory):
    if instruction.startswith("mul"):
        if enabled:
            factors = [int(i) for i in re.findall(r"\d+", instruction)]
            products.append(factors[0] * factors[1])
    elif instruction.startswith("don"):
        enabled = False
    else:
        enabled = True
    print(instruction, sum(products))

print(sum(products))
