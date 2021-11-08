import sys

print(sys.argv)

sum = 0

for value in sys.argv[1:]:
    sum = sum + int(value)

print(sum)