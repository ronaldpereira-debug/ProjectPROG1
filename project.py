import json
import shutil
import os


ARQUIVO = "produtos.json"
BACKUP = "backup_produtos.json"


# ==========================================
# Classe Produto
# ==========================================

class Produto: #Define uma classe chamada Produto.

    def __init__(self, codigo, descricao, valor, deletado=" "): #Método executado automaticamente quando um objeto é criado.
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        self.deletado = deletado

    def para_dict(self): #Transforma o objeto em um dicionário.
        return { #O parâmetro self representa o próprio objeto.
            "codigo": self.codigo,
            "descricao": self.descricao,
            "valor": self.valor,
            "deletado": self.deletado
        }


# ==========================================
# Funções auxiliares
# ==========================================

def carregar_produtos(): #Responsável por carregar os produtos armazenados.

    if not os.path.exists(ARQUIVO): #Verifica se o arquivo existe.
        return [] #Retorna uma lista vazia caso o arquivo não exista.

    with open(ARQUIVO, "r", encoding="utf-8") as arq: #open() abre um arquivo; "r" Modo leitura, utf-8, Permite utilizar caracteres acentuados.

        return json.load(arq) #Lê todo o conteúdo JSON e retorna uma lista de produtos.


def salvar_produtos(produtos): #Recebe uma lista e grava os dados no arquivo.

    with open(ARQUIVO, "w", encoding="utf-8") as arq: #Abre um arquivo com modo escrita "w", caso não exista será criado
        json.dump(produtos, arq, indent=4, ensure_ascii=False) # Formata o JSON com identação para facilitar a leitura.
        #dump() pertence à biblioteca json e serve para gravar dados Python em um arquivo no formato JSON.
        #2 parâmetros o primeiro produtos é o objeto que será salvo, todo conteúdo do produto é convertido para json.
        #e o segundo parâmetro arq é uma referência ao arquivo produtos.json.
        #Sem o ident tudo ficaria em 1 única linha, quando foi escrito ident=4 ficará todas as informações do produtos separados em 4 linhas, em ordem.
        #ensure_ascii=False permite alguns caracteres como o ^, se não tivesse ou fosse = True iria sair \u00e2

# ==========================================
# Menu
# ==========================================

def menu():

    while True: #Executa indefinidamente. O encerramento ocorre através de: return opcao

        print("\n=== MENU PARA CADASTRO DE PRODUTOS ===\n")

        print("1. Incluir")
        print("2. Listar")
        print("3. Consultar")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Organizar Arquivo")
        print("7. Backup")
        print("8. Restore")
        print("0. Sair")

        try: #Tenta executar um bloco de código.

            opcao = int(input("\nDigite sua opção: "))

            if 0 <= opcao <= 8:
                return opcao
                #Se a opção escrita pelo usuário estiver entre 0 e 8 retorna o valor de opcao, se opcao for = 3 então return 3
                #Isso será armazenado em op = menu()

            print("Opção inválida!")

        except ValueError: #Captura erros de conversão. Se o usuário digitar errado, o programa não encerra.
                            #Nesse caso, se o usuário digita um texto ao invés de número.
            print("Digite apenas números!")


# ==========================================
# Inclusão
# ==========================================

def inclusao(): #Realiza o cadastro de novos produtos.

    produtos = carregar_produtos() #Obtém os produtos já existentes.

    codigo = int(input("Código do produto: "))
    descricao = input("Descrição do produto: ")
    valor = float(input("Valor do produto: "))

    novo = Produto(codigo, descricao, valor) #Instancia um objeto Produto.

    produtos.append(novo.para_dict())# append adiciona um elemento ao final da lista.
                                     #para_dict converte o objeto em um dicionário.

    salvar_produtos(produtos)#Atualiza o arquivo. Salva e atualiza.

    print("\nProduto cadastrado com sucesso!")


# ==========================================
# Listagem
# ==========================================

def listar(): #Exibe todos os produtos.

    produtos = carregar_produtos() # = não significa que é igual.
                                   #guarde o resultado retornado por carregar_produtos() dentro da variável produtos.
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for p in produtos: #Percorre cada elemento da lista.

        print( #f-string f"Cod {p['codigo']}" Permite inserir variáveis diretamente no texto.
            f"Cod {p['codigo']} --- " #p["codigo"] Acessa o campo código do dicionário.
            f"Descrição: {p['descricao']} --- "
            f"Valor R$ {p['valor']:.2f} --- "
            f"Deletado? ({p['deletado']})"
        )


# ==========================================
# Consulta
# ==========================================

def consultar(): #Pesquisa um produto pelo código.

    produtos = carregar_produtos()

    codigo = int(input("Digite o código: "))

    for p in produtos:

        if p["codigo"] == codigo and p["deletado"] != "*":#Verifica se os códigos são iguais.
                                                          #and p["deletado"] != "*"
                                                          #Ignora registros marcados como excluídos.

            print(
                f"\nCod {p['codigo']} "
                f"--- Descrição: {p['descricao']} "
                f"--- Valor R$ {p['valor']:.2f}"
            )

            return

    print("\nCódigo não cadastrado!")


# ==========================================
# Alteração
# ==========================================

def alterar(): #Permite modificar dados existentes.

    produtos = carregar_produtos()

    codigo = int(input("Digite o código que deseja alterar: "))

    for p in produtos:

        if p["codigo"] == codigo:#Substitui o valor atual.

            print(
                f"\nCod {p['codigo']} "
                f"--- Descrição: {p['descricao']} "
                f"--- Valor R$ {p['valor']:.2f}"
            )

            p["descricao"] = input("Nova descrição: ")
            p["valor"] = float(input("Novo valor: "))

            salvar_produtos(produtos)#Salva as alterações.

            print("\nProduto alterado com sucesso!")

            return

    print("\nCódigo não cadastrado!")


# ==========================================
# Exclusão Lógica
# ==========================================

def excluir():#Implementa exclusão lógica.
#Conceito
#O produto não é removido.
#Apenas recebe uma marcação.
#Isso permite recuperar dados, posteriormente.

    produtos = carregar_produtos()

    codigo = int(input("Digite o código que deseja excluir: "))

    for p in produtos:

        if p["codigo"] == codigo:

            print(
                f"\nCod {p['codigo']} "
                f"--- Descrição: {p['descricao']} "
                f"--- Valor R$ {p['valor']:.2f}"
            )

            certeza = input(
                "\nTem certeza que deseja excluir? (s/n): "
            ).lower()

            if certeza == "s":

                p["deletado"] = "*"

                salvar_produtos(produtos)

                print("\nProduto excluído com sucesso!")

            return

    print("\nCódigo não cadastrado!")


# ==========================================
# Organizar Arquivo
# Exclusão Física
# ==========================================

def organizar():#Executa a exclusão física.

    produtos = carregar_produtos()

    ativos = []#Armazena somente produtos válidos.

    for p in produtos:

        if p["deletado"] != "*":#Mantém apenas registros ativos.
            ativos.append(p)

    salvar_produtos(ativos)#A nova lista substitui o arquivo anterior.

    print("\nArquivo organizado com sucesso!")


# ==========================================
# Backup
# ==========================================

def backup():#Cria uma cópia de segurança.

    if not os.path.exists(ARQUIVO):

        print("Arquivo inexistente!")
        return

    shutil.copy(ARQUIVO, BACKUP)#Copia o arquivo original para o backup.

    print("\nBackup realizado com sucesso!")


# ==========================================
# Restore
# ==========================================

def restore():#Recupera os dados do backup.

    if not os.path.exists(BACKUP):

        print("Backup inexistente!")
        return

    shutil.copy(BACKUP, ARQUIVO)#Substitui o arquivo principal pelo backup.

    print("\nRestore realizado com sucesso!")


# ==========================================
# Programa Principal
# ==========================================

def main():#Controla o fluxo principal do programa.

    while True:

        op = menu()#Obtém a opção escolhida.

        match op:#Equivalente ao switch do C.
                 #Exemplo: Se a opção for 1, executa a função de inclusão.

            case 1:
                inclusao()

            case 2:
                listar()

            case 3:
                consultar()

            case 4:
                alterar()

            case 5:
                excluir()

            case 6:
                organizar()

            case 7:
                backup()

            case 8:
                restore()

            case 0:
                print("\nPrograma encerrado.")
                break


# ==========================================
# Início do Programa
# ==========================================

if __name__ == "__main__":#Verifica se o arquivo está sendo executado diretamente.
    main()#Inicia o sistema.
