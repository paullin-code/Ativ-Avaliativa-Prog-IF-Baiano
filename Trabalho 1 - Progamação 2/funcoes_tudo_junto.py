# 1 - Adicionar
# 2 - Editar
# 3 - Remover
# 4 - Listar
# 5 - Pesquisar contato

# ids = [0, 1, 2, 3]
# nomes = ["Paulo", "Lucas", "Paulo","Luiz"]
# emails = ["aaaaa", "bbbbb", "ccccc", "ddddd"]
# telefones = [111111, 222222, 333333, 444444]


ids = []
nomes = []
emails = []
telefones = []

# funcao para adicionar contato
def adicionar(nome, email, telefone):
    ids.append(len(ids))
    nomes.append(nome)
    emails.append(email)
    telefones.append(telefone)

# funcao para editar contato
def editar(var_edit, id_edit):

    if var_edit == "nome":
        # solicitando novo nome
        novo_nome = input("Digite o novo nome: ").capitalize()
        nomes[id_edit] = novo_nome
        print("----------Contato Editado----------")
        print(f"ID: {id_edit} | Nome: {nomes[id_edit]} | Email: {emails[id_edit]} | Telefone: {telefones[id_edit]}")

    elif var_edit == "email":
        # solicitando novo email
        novo_email = input("Digite o novo email: ")
        emails[id_edit] = novo_email
        print("----------Contato Editado----------")
        print(f"ID: {id_edit} | Nome: {nomes[id_edit]} | Email: {emails[id_edit]} | Telefone: {telefones[id_edit]}")

    elif var_edit == "telefone":
        # solicitando novo telefone
        novo_tele = int(input("Digite o novo telefone: "))
        telefones[id_edit] = novo_tele
        print("----------Contato Editado----------")
        print(f"ID: {id_edit} | Nome: {nomes[id_edit]} | Email: {emails[id_edit]} | Telefone: {telefones[id_edit]}")

# funcao para remover contato
def remover(id_remov):
    ids.pop(id_remov)
    nomes.pop(id_remov)
    emails.pop(id_remov)
    telefones.pop(id_remov)

    for i in range(len(ids)):
        if ids[i] >= id_remov:
            ids[i] -= 1

    print("----------Agenda Editada----------")
    for ordem in ids:
        print(f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}")

# funcao para listar contatos
def listar():
    resposta = ""
    print("----------Lista de Contatos----------")
    for ordem in ids:
        if ordem != ids[-1]:
            texto = f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}\n"
        else:
            texto = f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}"
        resposta += texto
    return resposta

# funcao para pesquisar contato
def pesquisar(nome_pes):
    if nome_pes in nomes:
        # verificacao para garantir se nao tem nome repetidos na lista
        # se houver ele ira printar todos
        print("----------Contato Encontrado----------")
        for id,item in enumerate(nomes):
            if item == nome_pes:
                print(f"ID: {ids[id]} | Nome: {nomes[id]} | Email: {emails[id]} | Telefone: {telefones[id]}")
        input("Pressione Enter para continuar...")
        return None
    else:
        print(f'Não há ninguém com o nome "{nome_pes}" na agenda!')
        resp = input("Deseja tentar novamente: (s/n): ").lower()
        return resp

