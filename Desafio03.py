cond = 1
opcao = 0
while cond !=6:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    opcao = int(input("Selecione a opção:\n"
                  "[1] Soma\n"
                  "[2] Subtração\n"
                  "[3] Multiplicação\n"
                  "[4] Divisão\n"
                  "[5] Digitar novo número\n"
                  "[6] Sair\n"))
    match opcao:
        case 1:
            soma = n1 + n2
            print(f"{soma:.2f}")
        case 2:
            soma = n1 - n2
            print(f"{soma:.2f}")
        case 3:
            soma = n1 * n2
            print(f"{soma:.2f}")
        case 4:
            soma = n1 / n2
            print(f"{soma:.2f}")
        case 5:
            cond = 1
        case 6:
            cond = 6
            print("Processo encerrado!")



