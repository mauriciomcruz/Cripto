from rsa_func import (
    primos,
    gerar_chaves,
    criptografar,
    descriptografar,
    verificar_numero)

def main():
    print("=== RSA - Criptografia de Caracteres ===")
    
    p, q = primos()
    chave_publica, chave_privada = gerar_chaves(p, q)

    print("\nChave Pública (e, n):", chave_publica)
    print("Chave Privada (d, n):", chave_privada)

    texto = input("\nDigite um texto curto para criptografar: ")

    if not verificar_numero(chave_publica[1], texto):
        print("Escolha primos maiores para gerar um n maior.")
        exit(1)

    criptografado = [criptografar(c, chave_publica) for c in texto]
    print("\nTexto criptografado (valores numéricos):", criptografado)

    descriptografado = ''.join(descriptografar(c, chave_privada) for c in criptografado)
    print("Texto descriptografado:", descriptografado)

if __name__ == "__main__":
    main()
