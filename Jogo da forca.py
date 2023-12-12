import random
import os
## from unidecode import unidecode

# Importando um arquivo txt com as palavras que eu quero pro jogo e separando cada palavra pelo tab (\n)
arquivo = r"C:\PythonDSA\Cap 7\palavras da forca.txt"
try:
    with open(arquivo, 'r', encoding = 'utf-8') as lista:
        palavras = lista.read().split('\n')

    ## palavras = [unidecode(palavra.lower()) for palavra in palavras]
    palavras = [palavra.lower() for palavra in palavras]

    with open(arquivo, 'w', encoding = 'utf-8') as lista:
        lista.write('\n'.join(palavras))

    # Funcao para limpar a tela
    def limpa_tela():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def game():
        limpa_tela()

        print("#### Olá, bem-vindo(a) ao jogo da forca da Thalyta! ####")
        
        while True:
            try:
                resp = int(input("Você deseja iniciar o jogo?\n1 - Sim\n2 - Não\n"))
                if resp not in (1, 2):
                    print("Escolha uma opção válida!")
                    continue
            except ValueError:
                print("Verifique se o que você digitou está condizente com o tipo de resposta válida!")
                continue
            else:
                if resp == 1:
                    print("Adivinhe a palavra abaixo:\n")
                    palavra = random.choice(palavras)
                    letras_tela = ["_" if letra.isalpha() else ' ' for letra in palavra]
                    chances = 7
                    letras_erradas = []

                    while chances > 0:
                        print(" ".join(letras_tela))
                        print("\nChances restantes:", chances)
                        print("Letras erradas:", " ".join(letras_erradas))
                        
                        tentativa = input("\nDigite uma letra: ").lower()
                        if not tentativa.isalpha() or len(tentativa) > 1:
                            print("Por gentiliza, digite apenas letras do alfabeto e apenas uma por vez!")
                            chances += 1

                        if tentativa in palavra:
                            if tentativa in letras_tela:
                                print("Você já digitou essa letra")
                            index = 0
                            for letra in palavra:
                                if tentativa == letra:
                                    letras_tela[index] = letra
                                index += 1
                        elif tentativa in letras_erradas:
                            print("Você já digitou essa letra")

                        else:
                            chances -= 1
                            letras_erradas.append(tentativa)
                        
                        if "_" not in letras_tela:
                            print("\nVocê venceu, a palavra era:", palavra)
                            break

                    if "_" in letras_tela:
                        print("\nVocê perdeu, a palavra era:", palavra)
                else:
                    print("Programa finalizado!")
                    break

except FileNotFoundError: 
    print("Verifique se o arquivo importado está correto")

except Exception as e:
    print(f"Meu amigo, o que foi que tu já fez errado? {e}")

# Bloco main
if __name__ == "__main__":
    game()
