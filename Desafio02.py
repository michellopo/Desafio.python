pin = 1212
senha = int(input("Digite sua senha: "))
rep = 1
while pin != senha and rep < 3:
    senha = int(input("Senha Ínvalida! Digite sua senha novamente: "))
    rep += 1
if senha != pin and rep >=3:
    print("Senha Bloqueada!")
else:
    print("Compra efetuada com Sucesso!!")