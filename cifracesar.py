#@author: João Gabriel Abreu 21/10/25


def cifra_cesar(mensagem, chave, modo):
    resultado = ''
    
    for letra in mensagem:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            if modo == 'criptografar':
                nova_letra = chr((ord(letra) - base + chave) % 26 + base)
            elif modo == 'descriptografar':
                nova_letra = chr((ord(letra) - base - chave) % 26 + base)
            resultado += nova_letra
        else:
            resultado += letra  # mantém espaços e pontuação independente 

    return resultado

# interface completamente simples e funcional
def main():
    print("=== Cifra de César ===")
    mensagem = input("Digite a mensagem: ")
    chave = int(input("Digite a chave (número de deslocamento): "))
    modo = input("Deseja criptografar ou descriptografar? ").lower()

    resultado = cifra_cesar(mensagem, chave, modo)
    print(f"\nResultado: {resultado}")

if __name__ == "__main__":
    main()
