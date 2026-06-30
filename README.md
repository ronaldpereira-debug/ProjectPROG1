# ProjectPROG1
CRUD
Integrantes do grupo: RONALD PEREIRA FIDELIS, ANNE PATRICIA BARROS DE SANTANA, LUCIO DOUGLAS LOPES DA SILVA.

Esse projeto é um CRUD - (Create, Read, Update e Delete) para cadastro de produtos utilizando Python.

As funcionalidades disponíveis são:
Inclusão de produtos
Listagem de produtos
Consulta por código
Alteração de dados
Exclusão lógica
Organização do arquivo (exclusão física)
Backup
Restore

Como funciona o projeto passo a passo?
Inicialmente o menu será apresentado ao usuário e ele terá 8 opções funcionais para escolher.

Função inclusao()
*Realiza o cadastro de novos produtos.*

Função listar()
*Exibe todos os produtos.*

Função consultar()
*Pesquisa um produto pelo código.*

Função alterar()
*Permite modificar dados existentes.*

Função excluir()
*Implementa exclusão lógica.*

Função organizar()
*Executa a exclusão física.*

Quando usamos a função excluir o produto não é exatamente excluido da lista diretamente, ele recebe o símbolo (*), exatamente como uma exclusão lógica.
Isso vai permitir recuperar os dados posteriormente.

A exclusão lógica permite recuperar dados porque o registro não é removido do armazenamento. Apenas recebe uma marcação indicando que está excluído.

Antes:

{
    "codigo": 1,
    "descricao": "Mouse",
    "valor": 50.0,
    "deletado": " "
}

Depois:

{
    "codigo": 1,
    "descricao": "Mouse",
    "valor": 50.0,
    "deletado": "*"
}

É possível listar os produtos, porém ele irá aparecer ao lado como (*).
Mas o detalhe é, se você tentar pesquisar o código desse produto ele não vai aparecer justamente por causa da linha 149 do código:

if p["codigo"] == codigo and p["deletado"] != "*"
O produto ainda está no arquivo, mas o sistema finge que ele não existe.

Dessa forma a exclusão lógica se torna reversível, basta remover o símbolo de * para trazer novamente o produto.

E a exclusão física que é feita pela função organizar(), remove completamente os produtos marcados com (*), tornando impossível reverter a exclusão, se não for feito o backup antes de organizar, o produto é removido completamente.

Função backup()
*Cria uma cópia de segurança.*

Função restore()
*Recupera os dados do backup.*

Função main()
*Controla o fluxo principal do programa.*

Dentro do main() existe o match() que é muito parecido com o switch usado em C.

Basicamente match(op) vai ler o valor de op 0-8 e comparar o valor com cada case e assim executar o bloco correspondente.


BLIBIOTECAS UTILIZADAS:

json
*Biblioteca responsável por salvar e ler dados no formato JSON.*

shutil
*Biblioteca utilizada para copiar arquivos.*

os
*Biblioteca que permite manipular arquivos e diretórios.*

O código foi contruído em etapas, cada função do código foi feita em ligação onde fomos pensando na lógica correta e consequentemente buscando a sintaxe para a lógica funcionar. Portanto, o código foi feito em conjunto em ligação em chamadas pelo Discord/Meet.

Nenhum integrante do grupo teve uma função específca, código foi feito em conjunto em em algumas chamadas.
