#Não são necessarias dependencias, é um programa simples. Assim que for iniciado irá pedir para digitar um número (que será especificado o que fará)
#Ao digitar o numero, será redirecionado para a função escolhida, e sempre irá passar o nome de algum pokemon, para que as alterações possam ser feitas

#função para validar se o pokemon existe no dicionario
def validar_pokemon(dicionario, nome):
    if nome in dicionario:
        return False
    return True

#função reutilizavel de nome do pokemon
def solicitar_nome():
    return input("Digite o nome do pokemon: ")

#função reutilizavel de nivel do pokemon
def solicitar_nivel():
    while True:
        try:
            nivel = int(input("Digite o nivel do pokemon: "))
            if 1 <= nivel <= 100:
                return nivel
        
            else: 
                print("Nivel invalido, digite um valor entre 1 e 100")
        except ValueError:
            print("Digite apenas numeros inteiros")
            continue

#função reutilizavel de quantidade de capturas
def solicitar_quantidade():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de capturas: "))
            if quantidade > 0:
                return quantidade
            else:
                print("Quantidade deve ser maior que 0.")
        except ValueError:
            print("Digite um número válido.")


#Função principal
def main():

    #Dicionario que guarda os pokemons
    dicionario = {}

    #lista que guarda as capturas
    capturas = []

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
            continue

        if escolha == 1:
            adicionar_pokemon(dicionario)

        elif escolha == 2:
            listar_pokemons(dicionario)

        elif escolha == 3:
            remover_pokemon(dicionario)

        elif escolha == 4:
            atualizar_nivel(dicionario)

        elif escolha == 5:
            registrar_captura(dicionario, capturas)

        elif escolha == 6:
           exibir_capturas(capturas)

        #Encerra o programa
        elif escolha == 7:
            return

        else: 
            print("Escolha uma opção válida")


 #Aqui os pokemons são adicionados
def adicionar_pokemon(dicionario):
    nome = solicitar_nome()

    if not validar_pokemon(dicionario, nome): #Só uma anotação para mim mesmo, a função validar_pokemon() confere se o nome existe no dicionario, caso exista, ele retorna false, ou seja, se fosse um 'if validar_pokemon()' e o pokemon não existisse, o return seria executado e encerraria a função, por isso é um if not
        print(f"{nome} já existe na pokedex")
        return
    
    tipo = input("Digite o tipo do pokemon ")
    nivel = solicitar_nivel()

    dicionario[nome] = {
        "tipo": tipo,
        "nivel": nivel
    }
    print(f"{nome} adicionado com sucesso")


#Aqui os pokemons são listados
def listar_pokemons(dicionario):
    if not dicionario:
        print("Não existe nenhum pokemon")
        return

    for nome in sorted(dicionario):
        print(f"{nome}: {dicionario[nome]}")

#Aqui os pokemons são removidos do dicionario
def remover_pokemon(dicionario):
    nome = solicitar_nome()

    if validar_pokemon(dicionario, nome):
        print(f"{nome} não existe na sua pokedex")
        return
    
    del dicionario[nome]
    print(f"{nome} removido com sucesso.")

#Aqui o nivel dos pokemons são atualizados
def atualizar_nivel(dicionario):
    while True:
        nome = solicitar_nome()

        if validar_pokemon(dicionario, nome):
            print(f"{nome} não existe na pokedex")
            return
        
        nivel = solicitar_nivel()
        dicionario[nome]["nivel"] = nivel
        print("Nivel alterado com sucesso")
        return

#Aqui registramos as capturas dos pokemons
def registrar_captura(dicionario, capturas):
    while True:
        nome = solicitar_nome()

        if validar_pokemon(dicionario, nome):
            print(f"{nome} não existe na sua pokedex, então não é possivel adicionar capturas a ele")
            return
        
        try:
            qnt_capturas = solicitar_quantidade()

            for i, captura in enumerate(capturas):
                if captura[0] == nome:
                    capturas[i][1] += qnt_capturas
                    return

            capturas.append([nome, qnt_capturas])
            return
            
        except ValueError:
            print("Digite apenas numeros inteiros")
            continue 

#Aqui listamos as capturas dos pokemons
def exibir_capturas(capturas):
     if not capturas:
        print("Nenhuma captura registrada ainda.")
        return

     print("Histórico de capturas:")
     for nome, qtd in capturas:
        print(f"{nome}: {qtd} vezes capturado")


main()


