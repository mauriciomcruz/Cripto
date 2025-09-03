from random import randrange

def primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def escolher_e(z):
    while True:
        e = randrange(2, z)
        if mdc(e, z) == 1:
            return e

def inverso_mod(e, z):
    t, novo_t = 0, 1
    r, novo_r = z, e
    while novo_r != 0:
        quociente = r // novo_r
        t, novo_t = novo_t, t - quociente * novo_t
        r, novo_r = novo_r, r - quociente * novo_r
    if r > 1:
        raise Exception("e não tem inverso modular")
    if t < 0:
        t += z
    return t

def gerar_chaves(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    if z <= 2:
        raise ValueError("Primos muito pequenos. Escolha maiores.")
    e = escolher_e(z)
    d = inverso_mod(e, z)
    return (e, n), (d, n)

def criptografar(caractere, chave_publica):
    e, n = chave_publica
    m = ord(caractere)
    c = pow(m, e, n)
    return chr(c)

def descriptografar(c, chave_privada):
    d, n = chave_privada
    m = pow(ord(c), d, n)
    return chr(m)

def verificar_numero(n, texto):
    for c in texto:
        if ord(c) >= n:
            return False
    return True
