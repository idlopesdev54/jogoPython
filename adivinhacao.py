import random

def jogar():

    print("*****************************")
    print("Bem vindo jogo de Adivinhação Numérica!")
    print("*****************************")

    secret_number = random.randrange(1,11)
    total_de_tentativas = 0
    pontos = 50

    print("Choose difficulty level?")
    print("(1)-Easy (2)-Medium (3)- Hard")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 5
    elif(nivel == 2):
        total_de_tentativas = 3
    else:
        total_de_tentativas = 1


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite o seu numero 1 e 10! ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 16 ):
            print("Você deve digitar um número entre 1 e 10!")
            continue

        acertou = chute == secret_number
        maior = chute > secret_number
        menor = chute < secret_number

        if(acertou):
            print('Voce acertou e ganhou {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o numero secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o numero secreto")
            pontos_perdidos = abs(secret_number - chute)
            pontos = pontos - pontos_perdidos


    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()




