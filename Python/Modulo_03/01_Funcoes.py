"""
                        Funções em Python

        Função nada mais é que um bloco de códigos para realizar uma tarefa. 
        
        Varias vezes durante nosso curso nós utilizamos funções que a linguagem
    python deixa disponibilizada par anós, como por exemplo, len(), append(),
    strip(), print()... Etc..

        Podemos fácilmente perceber que todas elas possuem parenteses, este serve
    para passar informações para dentro desta função, afim de trabalhar essas
    informações, porem, nem sempre é obrigatório receber algum argumento para
    pode ser utilizada, cada função, tem uma caracteristicas específica para seu
    uso.

        Neste capitulo não será estudado as funções disponíveis no Python, isso 
    já foi realizado aula a aula conforme o contexto de aprendizagem na aula
    em específico, porem, apartir de agora vamos aprender a criar nossas proprias
    funções, seu uso e a importancia de usarmos funções personalizadas.

        A ideia principal na utilização de uma função personalizada é a reutilização 
    desta função em vários trechos do código para assim, ele ficar mais fácil de 
    ser entendido, mais enchuto e fácil de organizar.

    O exemplo abaixo mostra a estrutura de uma função
    
    def nome_funcao():
        faça algo
        faça outra coisa
        return valor_final

"""
print()

# O trecho de código abaixo recebe a entrada do usuário para cadastrar um produto.
# A linha dois deixa todos os caracteres digitados em letras minusculas
# A linha três imprime em tela a confirmação com o nome do produto cadastrado
produto = input('Digite o nome do produto: ')
produto = produto.casefold()
print('Produto {} cadastrado com sucesso '.format(produto))

# A principio não há nada errado com o código acima, o único problema é quando
# for necessário a impressão do mesmo código em outros trechos do programa, caso
# um dia seja necessário realizar alterações, o programador precisará percorrer
# todo o código fonte atrás deste trecho de código para realizar alterações ou
# manutenções. Nessa hora é idicado usar funções, pois, em caso de manutenção e 
# alterações, o programador só precisará alterar um único ponto para que haja 
# atualização em todo o sistema. Fora isso, você não precisará, a cada vez que
# precisar cadastrar um produto, realizar a digitação de todo o código novamente.

print()
# Abaixo, criamos a função casdastrar()
def cadastrar():
    produto = input('Digite o nome do produto: ')
    produto = produto.casefold()
    print('Produto {} cadastrado com sucesso '.format(produto))

# A função criada nada fará até que a mesma seja chamada no código para acina-la

cadastrar()


