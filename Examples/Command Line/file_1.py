print("File 1 Name " + __name__)

if __name__ == "__main__":
    print("File 1 inside if")

a = 1

for i in range(3):
    b = 1 + a

    a = b + 2

print(a)