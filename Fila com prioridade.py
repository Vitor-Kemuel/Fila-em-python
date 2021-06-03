print("Atividade - FILA COM PRIORIDADES (MODO 1: INSERÇÃO COM BUSCA, REMOÇÃO NORMAL)")

# Modulo que mostra como está a fila


def show_list(names, priorities):
    print("A fila segue com a seguinte sequencia:\n")

    for i in range(len(names)):
        print(f"{i+1}º | {names[i]}, prioridade {priorities[i]}")
        print("--------------------------------")

# Modulo que define se serão removidos mais nomes da lista


def remove_more():
    while True:
        end = input("Deseja remover mais alguem? (S/N) ").lower()
        if end == 's':
            return True
        elif end == 'n':
            return False
        else:
            continue

# Modulo que define se deseja tentar digitar as informações para a busca novamente


def try_again():
    while True:
        end = input(
            "Nome não encontrado!! Deseja tentar novamente? (S/N) ").lower()
        if end == 's':
            return True
        elif end == 'n':
            return False
        else:
            continue

# Modulo que "atende" alguém especifico na fila


def remove_specifc_name(names, priorities):
    if len(names) == 0:
        print("A fila está vazia!!")
        return names, priorities

    repeat = True

    while repeat == True:
        name = input("Qual o nome da pessoa que deseja atender? ").lower()
        priority = int(input("Qual é o nivel de prioridade da pessoa? "))

        name = name.replace(' ', '')

        index = len(names) + 1

        for i in range(len(names)):
            name_list = names[i].replace(' ', '')
            if name == name_list.lower() and priority == priorities[i]:
                index = i
                break

        if index > len(names):
            again = try_again()
            if again == False:
                break

        else:
            print(
                f"{names.pop(index)} Com a prioridade {priorities.pop(index)} foi atendido")

            if len(names) == 0:
                print("Todos foram atendidos!!")
                break

            show_list(names, priorities)

            repeat = remove_more()

    return names, priorities

# Modulo que "Atende" o primeiro da lista


def remove_name(names, priorities):
    repeat = True

    try:
        while repeat == True:
            print(
                f"{names.pop(0)} Com a prioridade {priorities.pop(0)} foi atendido\n")

            if len(names) == 0:
                print("Todos foram atendidos!!")
                break

            show_list(names, priorities)

            repeat = remove_more()

    except:
        print("A fila está vazia!!")

    return names, priorities

# Modulo que defini o que ocorrerá no fim do ciclo


def defining_the_end():
    while True:
        end = int(input("Digite (0) para adicionar nomes a fila" +
                        "\nDigite (1) para atender o primeiro da fila" +
                        "\nDigite (2) para atender alguém especifico" +
                        "\nDigite (3) para encerrar o Programa\n"))

        if end == 0 or end == 1 or end == 2 or end == 3:
            break

    return end

# Modulo de leitura novos dados


def new_priority():
    name = input('Digite o nome! ')

    while True:
        try:
            priority = int(input("Digite a prioridade! "))
            break
        except:
            print("Digite apenas numeros!!")

    return name, priority

# Modulo para definir se os dados anteriores serão apagados


def last_data():
    while True:
        last_bd = input("Deseja utilizar os ultimos dados inseridos? (S/N)" +
                        " (Caso não, o programa apagara os dados e fara a coleta de novos dados!!) ").lower()
        if last_bd == 'n':
            return True

        elif last_bd == 's':
            return

        else:
            continue

# Modulo que pergunta se deseja inserir novos dados ou apenas ler os existentes


def new_data():
    while True:
        reading = input("Deseja inserir novos dados? (S/N)" +
                        " (Caso não, o programa ira mostrar os dados inseridos) ").lower()
        if reading == 'n':
            return False, False

        elif reading == 's':
            repeat = last_data()
            return True, repeat

        else:
            continue

# Modulo que pergunta se deseja adicionar mais alguem após a digitação de um dado
# Sera ativo caso tenha selecionado para adicionar novos dados


def repeat_question():
    while True:
        question = input("Deseja adicionar mais alguém? (S/N) ").lower()

        if question == 'n':
            return False

        elif question == 's':
            return True
        else:
            continue

# Modulo que insere novos dados na lista em suas respectivas prioridades


def add(names, priorities, name, priority):
    if len(names) == 0:
        names.append(name)
        priorities.append(priority)

    elif priorities[-1] <= priority:
        names.append(name)
        priorities.append(priority)

    else:
        for i in range(len(names)):
            if priority < priorities[i]:
                priorities.insert(i, priority)
                names.insert(i, name)
                break

    return names, priorities

# Modulo controlador da coleta de informações
# chama os modulos de leitura, inserção
# e questiona sobre inserir mais dados


def control_add(names, priorities, repeat):
    while repeat == True:
        name, priority = new_priority()
        names, priorities = add(names, priorities, name, priority)
        repeat = repeat_question()

    return names, priorities

# modulo para chamar as funçoes reponsaveis por
# adicionar elementos, "atender" elementos e encerrar o programa


def functionalities(list_name, list_priority):
    while True:
        end = defining_the_end()

        if end == 0:
            repeat = True
            control_add(list_name, list_priority, repeat)
            show_list(list_name, list_priority)

        elif end == 1:
            list_name, list_priority = remove_name(list_name, list_priority)

        elif end == 2:
            list_name, list_priority = remove_specifc_name(
                list_name, list_priority)

        else:
            print("Encerrando o programa!!")
            end == False
            return False

# modulo principal responsavel por charmar as funções


def main():
    end = True

    # Bloco de comando responsaveis para chamar as funçoes
    while end == True:
        reset = False
        repeat = True

        # Bloco de comando que declara as listas caso for a primeira execução
        if 'list_name' in locals() and 'list_priority' in locals():
            print("Iniciando o sistema")
            repeat, reset = new_data()
            if reset == True:
                list_name = []
                list_priority = []

        else:
            print("Executando criação das variaveis!!")
            list_name = []
            list_priority = []

        end = functionalities(list_name, list_priority)


# programa principal
main()
