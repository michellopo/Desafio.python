h1 = int(input("Digite a hora: "))
m1 = int(input("Digite os minutos: "))
h2 = int(input("Digite a hora: "))
m2 = int(input("Digite os minutos: "))

hrtotal = h1 + h2
mintotal = m1 + m2

if mintotal >= 60:
    hrtotal = hrtotal + 1
    mintotal = mintotal - 60
if hrtotal >= 12 and hrtotal < 24:
    hrtotal = hrtotal - 12
    print(f"{hrtotal} : {mintotal}")
elif hrtotal >=24 and hrtotal < 36:
    hrtotal = hrtotal - 24
    print(f"{hrtotal} : {mintotal}")
elif hrtotal >= 36:
    hrtotal = hrtotal - 36
    print(f"{hrtotal} : {mintotal}")
else:
    hrtotal = hrtotal + 12
    print(f"{hrtotal} : {mintotal}")
