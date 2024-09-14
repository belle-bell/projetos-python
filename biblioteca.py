'''
Biblioteca
'''

class Biblioteca:
    def __init__(self, livros):
        self.livros = livros

    def mostrar_livros_disponiveis(self):
        print('Nossa biblioteca pode oferecer os seguintes livros: ')
        for livro, usuario in self.livros.items():
            if usuario == 'Grátis':
                print(livro)

    def emprestar_livro(self, livro_pedido, nome):
        if self.livros.get(livro_pedido) == 'Grátis':
            print(f'{livro_pedido} foi marcado como \'Emprestado\' por: {nome}')
            self.livros[livro_pedido] = nome
            return True
        else:
            print(f'Desculpe, o livro {livro_pedido} não está disponível.')
            return False

    def devolver_livro(self, livro_retornado):
        if livro_retornado in self.livros and self.livros[livro_retornado] != 'Grátis':
            self.livros[livro_retornado] = 'Grátis'
            print(f'Obrigado por devolver o livro {livro_retornado}.')
        else:
            print(f'O livro {livro_retornado} não foi encontrado ou não está emprestado.')

class Estudante:
    def __init__(self, nome, biblioteca):
        self.nome = nome
        self.livros = []
        self.biblioteca = biblioteca

    def livros_emprestados(self):
        if not self.livros:
            print('Você não tem nenhum livro emprestado no momento.')
        else:
            for livro in self.livros:
                print(livro)

    def pedir_livro(self):
        livro = input('Coloque o nome do livro que você gostaria de pegar >> ')
        if self.biblioteca.emprestar_livro(livro, self.nome):
            self.livros.append(livro)

    def devolver_livro(self):
        livro = input('Coloque o nome do livro que você gostaria de devolver >> ')
        if livro in self.livros:
            self.biblioteca.devolver_livro(livro)
            self.livros.remove(livro)
        else:
            print('Você não pegou esse livro, tente outro...')

def create_lib():
    livros = {
        'Jogos Vorazes': 'Grátis',
        'Crepúsculo': 'Grátis',
        '1984': 'Grátis'
    }
    biblioteca = Biblioteca(livros)
    estudante_ex = Estudante('Seu nome', biblioteca)

    while True:
        print('''
            ============== MENU DA BIBLIOTECA ==============
              1. Mostrar livros disponíveis
              2. Pegar um livro
              3. Devolver um livro
              4. Olhar seus livros
              5. Sair
              ''')
        
        escolha = int(input('Selecione a opção desejada: '))
        if escolha == 1:
            print()
            biblioteca.mostrar_livros_disponiveis()
        elif escolha == 2:
            print()
            estudante_ex.pedir_livro()
        elif escolha == 3:
            print()
            estudante_ex.devolver_livro()
        elif escolha == 4:
            print()
            estudante_ex.livros_emprestados()
        elif escolha == 5:
            print('Até depois!')
            break 

if __name__ == '__main__':
    create_lib()