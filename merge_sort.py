'''
Merge sort
'''

def merge_sort(lista):
    print("Dividindo ", lista)
  
    if len(lista) > 1:
        ponto_medio = len(lista) // 2
        metade_esquerda = lista[:ponto_medio]
        metade_direita = lista[ponto_medio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = 0
        j = 0
        k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] <= metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else:
                lista[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1
  
    print("Mesclando ", lista)

def obter_numeros():
    while True:
        try:
            tamanho = int(input("Escolha o tamanho da lista (entre 5 e 10): "))
            if tamanho < 5 or tamanho > 10:
                print("Por favor, escolha um número entre 5 e 10.")
                continue
            
            lista = []
            for i in range(tamanho):
                while True:
                    try:
                        numero = int(input(f"Digite o número {i + 1} (entre 1 e 99): "))
                        if 1 <= numero <= 99:
                            lista.append(numero)
                            break
                        else:
                            print("Número fora do intervalo. Digite um número entre 1 e 99.")
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro.")
            
            return lista
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

if __name__ == '__main__':
    lista = obter_numeros()
    print("Lista original:", lista)
    merge_sort(lista)
    print("Lista ordenada:", lista)
