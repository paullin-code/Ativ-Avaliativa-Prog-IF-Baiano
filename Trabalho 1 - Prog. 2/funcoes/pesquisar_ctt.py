# importando as listas
from listas.listas_ctt import *

# funcao para pesquisar contato
def pesquisar(nome_pes):
    if nome_pes in nomes:
        # verificacao para garantir se nao tem nome repetidos na lista
        # se houver ele ira printar todos
        print("----------Contato Encontrado----------")
        for id,item in enumerate(nomes):
            if item == nome_pes:
                print(f"ID: {ids[id]} | Nome: {nomes[id]} | Email: {emails[id]} | Telefone: {telefones[id]}")
        return None
    else:
        print(f'Não há ninguém com o nome "{nome_pes}" na agenda!')
        resp = input("Deseja tentar novamente: (s/n): ").lower()
        return resp