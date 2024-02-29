# Nama    : Rizaldi Febriansyah
# NIM     : 221402126
# Soal 5

sumNumber = 0
inputNumber = 0

while inputNumber != -1:
    inputNumber = int(input("Input a Number (input -1 to finish) :"))
    if inputNumber != -1:
        sumNumber += inputNumber
    
print(sumNumber)