Pilha = []
fila = []
quantPilha = 5
opcao = ""
filmes = ""
opcao2 = ""

while opcao != "9" or len(Pilha) <= quantPilha:

    if opcao == "":
        filmes = input(
            "Digite um filme e posteriormente\nescolha a opção PUSH para adicionar à Pilha:")


    else:
        while opcao2 != "9":

            if len(Pilha) < quantPilha:
                opcao2 = input("[1] Adicionar outro\n[9]Voltar para o menu\n")
                if opcao2 == "1":
                    filmes = input(
                        "Digite outro Filme e posteriormente\nescolha QUALQUER opção:")
                    print(f"\nA opçao Push adiciona um valor no topo da pilha\n")
                    Pilha.append(filmes)

                    print(f"Você adicionou o filme {filmes.upper()} a nossa Pilha\n")
                    filmes = ""
            else:

                print("Infelizmente sua Pilha encheu. \nVolte ao menu e use a opção POP")
                opcao2 = input("\n[9]Voltar para o menu\n")

    opcao = input(
        "[1]--> PUSH\n[2]--> POP\n[3]--> Peek\n[4]--> Isfull\n[5]--> IsEmpity\n[6]--> Mostrar PILHA\n[7]--> Mostrar Fila\n[8]--> Remover da Fila\n[9]--> Encerrar:\n ")

    if opcao == "1":

        if filmes == "":
            if len(Pilha) < quantPilha:
                filmes = input(
                    "Digite outro Filme e posteriormente\nescolha QUALQUER opção:")
                print(f"\nA opçao Push adiciona um valor no topo da  pilha\n")
                Pilha.append(filmes)
                print(f"Você adicionou o filme {filmes.upper()} a nossa Pilha\n")
                filmes = "",

        else:
            print(
                f"\nA opçao Push adiciona um valor no topo da pilha\n")
            Pilha.append(filmes)

            print(f"Você adicionou o filme {filmes.upper()} a nossa Pilha\n")


    elif opcao == "2":
        if len(Pilha) != 0:
            aux = Pilha.pop()
            fila.append(aux)
            print(
                f"A opção POP remove o último valor\nNesse caso você retirou '{aux}'\n ")
        else:
            print("ERRO!\nVocê não possui dados na PILHA para ser retirado")

    elif opcao == "3":

        print(
            f"A Opção Peek mostra o Topo da Pilha\nNesse caso o topo é {Pilha[-1]}\n")

    elif opcao == "4":
        if len(Pilha) < quantPilha:
            print(f"Sua pilha ainda possui {quantPilha - len(Pilha)} espaços restantes p9ara PREENCHER.")
        else:
            print("Sua Pilha está cheia")

    elif opcao == "5":

        if len(Pilha) == 0:
            print(
                f"Sua pilha ainda possui {quantPilha - len(Pilha)} espaços restantes.\nPor favor vá ao comando POP para remover")
        else:
            print("Sua pilha está vazia\n")

    elif opcao == "6":
        if len(Pilha) < quantPilha:
            print("Por favor preencha toda a PILHA para melhorar os exemplos")
        else:
            print(f"{Pilha[-1], Pilha[-2], Pilha[-3], Pilha[-4], Pilha[-5]}"),

    elif opcao == "7":
        if len(fila) == 0:
            print("SUA LISTA AINDA ESTÁ VAZIA\nUse o comando POP")
        else:
            print(f"SUA FILA É\nfila\n{fila}")

    elif opcao == "8":

        del fila[0]
        print(f"Você removeu uma valor da fila")


    elif opcao == "9":
        print("obrigado a todos! FIMMM")
    else:
        print(
            f"Erro!\nVocê digitou ({opcao}) e é uma opção inválida ou não existe.\n")

else:
    raise Exception('Excedeu o máximo de tamanho permitido')