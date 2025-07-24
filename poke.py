#Exibir histórico de capturas: O histórico de capturas deve ser armazenado em uma lista, onde cada entrada consiste no nome do Pokémon e a quantidade de vezes que foi capturado. Quando o usuário escolher exibir o histórico de capturas, o programa deve mostrar todas as entradas feitas.

def main():

    dicionario = {}

    capturas = {}


    while True:
        print("1 - Adicionar pokemon\n" \
        "2- Listar pokemon\n" \
        "3- Remover pokemon\n" \
        "4- Atualizar nivel\n" \
        "5- Registrar captura\n" \
        "6- Exibir histórico capturas\n" \
        "7- Sair\n")

        try:
            escolha = int(input("Escolha a opção desejada\n"))  
        except ValueError:
            print("Escolha um número inteiro")

        if escolha == 1:
            nome = input("Digite o nome do pokemon que deseja adicionar\n")
            tipo = input("Agora digite o tipo do pokemon que deseja adicionar\n")
            try:
                nivel = int(input("Por ultimo, o nivel do pokemon (de 1 a 100)\n"))
            except ValueError:
                print("Escolha un número inteiro")

            if nome not in dicionario:
                if nivel >= 1 and nivel <= 100:

                    dicionario[nome] = {
                    "tipo": tipo,
                    "level": nivel
                    }
                
                else:
                    print("Nível inválido")
            
            else:
                print("Esse pokemon ja existe")


        elif escolha == 2:
            if not dicionario:
                print("Não existe nenhum pokemon")

            for nome in sorted(dicionario):
                print(f"{nome}: {dicionario[nome]}")

        elif escolha == 3:
            deletar = input("Digite o nome do pokemon que deseja remover\n")

            if deletar in dicionario:
                del dicionario[deletar]

            else:
                print("Pokemon não encontrado")

        elif escolha == 4:
            nome = input("Digite o nome do pokemon que deseja atualizar o nivel\n")

            if nome in dicionario:
                try:
                    novo_nivel = int(input("Digite o novo nivel de 1 a 100\n"))
                except ValueError:
                    print("Digite um numero inteiro")

                if novo_nivel >= 1 and novo_nivel <= 100:
                    dicionario[nome]["level"] = novo_nivel

                else:
                    print("Nivel inválido")
            
            else:
                print("Esse pokemon não existe na sua pokedex")

        elif escolha == 5:
            capturar = input("Digite o nome do pokemon para registrar a captura\n")

            if capturar in dicionario:
                try:
                    quantidade = int(input("Digite a quantidade de vezes que foi capturado\n"))
                except ValueError:
                    print("Digite um numero inteiro")
                    
                if capturar not in capturas:
                    capturas[capturar] = quantidade
            
                else:
                    capturas[capturar] += quantidade

            else:
                print("O pokemon não existe")

        elif escolha == 6:
            if not capturas:
                print("Nenhuma captura registrada ainda.")

            else:
                print("Histórico de capturas:")
            for nome, qtd in capturas.items():
                print(f"{nome}: {qtd} vezes")

        elif escolha == 7:
            return

        else: 
            print("Escolha uma opção válida")














main()