import PySimpleGUI as sg
from rsa_func import primo, gerar_chaves, verificar_numero, criptografar, descriptografar

def main():
    sg.theme('DarkBlue3')

    layout = [
        [sg.Text('Digite dois números primos diferentes')],
        [sg.Text('Primo p:', size=(8,1)), sg.Input(key='-P-')],
        [sg.Text('Primo q:', size=(8,1)), sg.Input(key='-Q-')],
        [sg.Text('Texto para criptografar:')],
        [sg.Input(key='-TEXTO-', size=(40,1))],
        [sg.Button('Gerar chaves'), sg.Button('Criptografar'), sg.Button('Descriptografar'), sg.Button('Sair')],
        [sg.Text('Chave Pública (e, n):'), sg.Text('', key='-CHAVE_PUB-')],
        [sg.Text('Chave Privada (d, n):'), sg.Text('', key='-CHAVE_PRIV-')],
        [sg.Text('Texto Criptografado (números):')],
        [sg.Multiline('', key='-CRIPTOGRAFADO-', size=(60,5), disabled=True)],
        [sg.Text('Texto Descriptografado:')],
        [sg.Multiline('', key='-DESCRIPTOGRAFADO-', size=(60,3), disabled=True)],
        [sg.Text('', key='-ERRO-', text_color='red')]
    ]

    window = sg.Window('RSA Criptografia Simples', layout)

    chave_publica = None
    chave_privada = None
    criptografado = []

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Sair'):
            break

        elif event == 'Gerar chaves':
            try:
                p = int(values['-P-'])
                q = int(values['-Q-'])
                if p == q:
                    window['-ERRO-'].update('Erro: p e q devem ser diferentes.')
                    continue
                if not (primo(p) and primo(q)):
                    window['-ERRO-'].update('Erro: p e q devem ser primos.')
                    continue

                chave_publica, chave_privada = gerar_chaves(p, q)

                window['-CHAVE_PUB-'].update(str(chave_publica))
                window['-CHAVE_PRIV-'].update(str(chave_privada))
                window['-ERRO-'].update('')
                criptografado = []
                window['-CRIPTOGRAFADO-'].update('')
                window['-DESCRIPTOGRAFADO-'].update('')

            except ValueError:
                window['-ERRO-'].update('Digite valores inteiros válidos para p e q.')

        elif event == 'Criptografar':
            if chave_publica is None:
                window['-ERRO-'].update('Antes, gere as chaves com p e q válidos.')
                continue

            texto = values['-TEXTO-']
            n = chave_publica[1]

            if not verificar_numero(n, texto):
                window['-ERRO-'].update(f'Erro: algum caractere tem valor >= n ({n}). Use primos maiores.')
                continue

            criptografado = [criptografar(c, chave_publica) for c in texto]
            window['-CRIPTOGRAFADO-'].update(str(criptografado))
            window['-ERRO-'].update('')

        elif event == 'Descriptografar':
            if chave_privada is None:
                window['-ERRO-'].update('Antes, gere as chaves com p e q válidos.')
                continue
            if not criptografado:
                window['-ERRO-'].update('Criptografe o texto primeiro.')
                continue

            descriptografado = ''.join(descriptografar(c, chave_privada) for c in criptografado)
            window['-DESCRIPTOGRAFADO-'].update(descriptografado)
            window['-ERRO-'].update('')

    window.close()

if __name__ == '__main__':
    main()
