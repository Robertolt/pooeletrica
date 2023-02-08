"""Leia 3 números e mostre-os em ordem na tela usando apenas condicionais"""

num1 = int(input(''))
num2 = int(input(''))
num3 = int(input(''))

if (num1 > num2) and (num1 > num3):
    if num2 > num3:
        print(num3, num2, num1)
    else:
        print(num2, num3, num1)
elif (num2 > num3) and (num2 > num1):
    if num1 > num3:
        print(num3, num1, num2)
    else:
        print(num1, num3, num2)
elif (num3 > num2) and (num3 > num1):
    if num2 > num1:
        print(num1, num2, num3)
    else:
        print(num2, num1, num3)
else:
    print(num1, num2, num3)
