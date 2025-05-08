def main ():
    banco = ""
    nome = ""
    opcao = 0

    while True:
        print ("MENU BANCÁRIO")
        print ("1 - Cadastro de Banco")
        print ("2 - Cadastro do Cliente")
        print ("3 - Sair do Sistema")
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            banco=(input("Digite o nome do seu Banco: "))
            print ("Seu banco:", banco ,  " foi cadastrado com sucesso")

        elif opcao == 2:
            nome=(input("Digite o seu nome para efetuar cadastro: "))
            print ("Seja bem vindo," , nome,"!" , " Cliente efetivado.")

        elif opcao == 3:
            print ("Menu encerrado, obrigado!")

        else:
            print ("Opção inválida, tente novamente.")

        break
if __name__=="__main__":
    main()
