import pickle

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

def adicionar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    novo_contato = Contato(nome, telefone, email)
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")

def listar_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for i, contato in enumerate(contatos, start=1):
            print(f"{i}. Nome: {contato.nome}, Telefone: {contato.telefone}, E-mail: {contato.email}")

def salvar_contatos_arquivo(contatos, nome_arquivo):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(contatos, arquivo)

def ler_contatos_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            contatos = pickle.load(arquivo)
            return contatos
    except FileNotFoundError:
        return []

def main():
    nome_arquivo = "contatos.bin"
    contatos = ler_contatos_arquivo(nome_arquivo)

    while True:
        print("\nOpções:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato(contatos)
        elif escolha == '2':
            listar_contatos(contatos)
        elif escolha == '3':
            salvar_contatos_arquivo(contatos, nome_arquivo)
            print("Contatos salvos. Adeus!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
