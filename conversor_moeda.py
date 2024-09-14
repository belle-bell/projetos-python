'''
Conversor de moeda
'''

import requests

def converter_moeda():
    moeda_inicial = input('Digite a moeda inicial (ex: USD): ')
    moeda_alvo = input('Digite a moeda alvo (ex: EUR): ')

    while True:
        try:
            valor = float(input('Digite o valor a ser convertido: '))
        except ValueError:
            print('O valor deve ser um número!')
            continue

        if valor <= 0:
            print('O valor deve ser maior que 0')
            continue
        else:
            break


# foi utilizado api de currency do site https://apilayer.com

    url = ('https://api.apilayer.com/fixer/convert?to='
           + moeda_alvo + '&from=' + moeda_inicial +
           '&amount=' + str(valor))

    payload = {}
    headers = {'apikey': 'api-key'}
    resposta = requests.request('GET', url, headers=headers, data=payload)
    codigo_status = resposta.status_code

    if codigo_status != 200:
        print('Ocorreu um problema. Tente novamente mais tarde')
        quit()

    resultado = resposta.json()
    print('Resultado da conversão: ' + str(resultado['result']))

if __name__ == '__main__':
    converter_moeda()