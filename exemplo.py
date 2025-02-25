import json
import os

# Nome do arquivo que servirá como "banco de dados"
DATABASE_FILE = "banco.json"

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    if os.path.exists(DATABASE_FILE):  # Verifica se o arquivo existe
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)  # Carrega os dados do JSON
            except json.JSONDecodeError:
                return {"usuarios": []}  # Retorna um banco vazio se houver erro no JSON
    return {"usuarios": []}  # Se o arquivo não existir, cria um banco vazio

# Função para salvar os dados no arquivo JSON
def salvar_dados(dados):
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)  # Salva os dados formatados

# Função para adicionar um novo usuário ao "banco"
def adicionar_usuario(id, nome, email):
    dados = carregar_dados()  # Carrega os dados atuais

    # Verifica se o ID já existe
    if any(usuario["id"] == id for usuario in dados["usuarios"]):
        print("❌ Erro: ID já cadastrado!")
        return

    novo_usuario = {"id": id, "nome": nome, "email": email}  # Cria um dicionário do usuário
    dados["usuarios"].append(novo_usuario)  # Adiciona o novo usuário à lista
    salvar_dados(dados)  # Salva os dados atualizados no JSON
    print(f"✅ Usuário {nome} cadastrado com sucesso!")

# Função para listar todos os usuários
def listar_usuarios():
    dados = carregar_dados()
    if not dados["usuarios"]:
        print("📂 Nenhum usuário cadastrado.")
    else:
        print("\n📋 Lista de Usuários:")
        for usuario in dados["usuarios"]:
            print(f'🆔 {usuario["id"]} | 👤 {usuario["nome"]} | ✉️ {usuario["email"]}')
    print()

# Função para buscar um usuário pelo ID
def buscar_usuario(id):
    dados = carregar_dados()
    for usuario in dados["usuarios"]:
        if usuario["id"] == id:
            print(f'🔍 Usuário encontrado: {usuario}')
            return usuario
    print("❌ Usuário não encontrado.")
    return None

# Função para atualizar o nome ou email de um usuário
def atualizar_usuario(id, novo_nome=None, novo_email=None):
    dados = carregar_dados()
    for usuario in dados["usuarios"]:
        if usuario["id"] == id:
            if novo_nome:
                usuario["nome"] = novo_nome
            if novo_email:
                usuario["email"] = novo_email
            salvar_dados(dados)
            print(f"✅ Usuário {id} atualizado com sucesso!")
            return
    print("❌ Usuário não encontrado.")

# Função para excluir um usuário pelo ID
def excluir_usuario(id):
    dados = carregar_dados()
    nova_lista = [u for u in dados["usuarios"] if u["id"] != id]

    if len(nova_lista) == len(dados["usuarios"]):
        print("❌ Usuário não encontrado.")
    else:
        dados["usuarios"] = nova_lista
        salvar_dados(dados)
        print(f"✅ Usuário {id} excluído com sucesso!")

# TESTES
if __name__ == "__main__":
    while True:
        print("\n📌 MENU")
        print("1️⃣ Adicionar Usuário")
        print("2️⃣ Listar Usuários")
        print("3️⃣ Buscar Usuário")
        print("4️⃣ Atualizar Usuário")
        print("5️⃣ Excluir Usuário")
        print("0️⃣ Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id = int(input("🆔 ID: "))
            nome = input("👤 Nome: ")
            email = input("✉️ Email: ")
            adicionar_usuario(id, nome, email)

        elif escolha == "2":
            listar_usuarios()

        elif escolha == "3":
            id = int(input("🔍 Digite o ID para buscar: "))
            buscar_usuario(id)

        elif escolha == "4":
            id = int(input("🆔 ID do usuário a atualizar: "))
            novo_nome = input("👤 Novo nome (pressione Enter para manter o mesmo): ")
            novo_email = input("✉️ Novo email (pressione Enter para manter o mesmo): ")
            atualizar_usuario(id, novo_nome if novo_nome else None, novo_email if novo_email else None)

        elif escolha == "5":
            id = int(input("🗑️ Digite o ID do usuário a excluir: "))
            excluir_usuario(id)

        elif escolha == "0":
            print("🚪 Saindo...")
            break

        else:
            print("❌ Opção inválida! Tente novamente.")
