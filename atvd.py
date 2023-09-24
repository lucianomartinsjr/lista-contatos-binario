import pickle

def salvar_contatos_arquivo(contatos, nome_arquivo):
    try:
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(contatos, arquivo)2
    except Exception as e:
        print(f"Erro ao salvar os contatos: {str(e)}")

def ler_contatos_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            contatos = pickle.load(arquivo)
            return contatos
    except FileNotFoundError:
        return []

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

def adicionar_contato(contatos,nome_arquivo):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    novo_contato = Contato(nome, telefone, email)
    contatos.append(novo_contato)
    
    salvar_contatos_arquivo(contatos, nome_arquivo)
    print("\nContato adicionado com sucesso!")
    

def listar_contatos(contatos):
    if not contatos:
        print("\nNenhum contato cadastrado.")
    else:
        for i, contato in enumerate(contatos, start=1):
            print(f"{i}. Nome: {contato.nome}, Telefone: {contato.telefone}, E-mail: {contato.email}")

def remover_contato(contatos,nome_arquivo):
    listar_contatos(contatos)
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato que deseja remover: ")) - 1
        if 0 <= indice < len(contatos):
            contato_removido = contatos.pop(indice)
            print(f"Contato {contato_removido.nome} removido com sucesso!")
            
            salvar_contatos_arquivo(contatos, nome_arquivo)
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite o número do contato que deseja remover.")


def main():
    nome_arquivo = "contatos.bin"
    contatos = ler_contatos_arquivo(nome_arquivo)

    while True:
        print("\nOpções:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Remover Contato")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato(contatos,nome_arquivo)
        elif escolha == '2':
            listar_contatos(contatos)
        elif escolha == '3':
            remover_contato(contatos,nome_arquivo)
        elif escolha == '4':
            salvar_contatos_arquivo(contatos, nome_arquivo)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
