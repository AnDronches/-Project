from random import*
print("Введите количество чифр в числе:")
n = int(input())
c = randrange(10**(n-1), 10**n )

def igra(a):
    cow, bull = 0, 0 
    list_a = []
    list_b = []
    for i in range(n):
        list_a.append((a//10**(n-1-i))%10)
        list_b.append((c//10**(n-1-i))%10)
    for i in range(n):
        if list_b[i] == list_a[i]:
            bull += 1
        elif list_b[i] in list_a:
            cow += 1
    print(bull,"быков и",cow,"коров")
    return(bull)
print("Введите число")
f = int(input())
while igra(f) != n:
    print("Введите число")
    f = int(input())
print("Поздраляю, ты победил!!!!:)")