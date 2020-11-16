from random import randint

NUMBER = randint(0, 10)
ATTEMPTS = 3
C = 0

# repetir enquanto houver tentativas
while C < 3:

    KICK = int(input('Em que número de 1 a 10 o computador pensou?'))
    C += 1
    ATTEMPTS -= 1

    if KICK == NUMBER:
        print("Parabêns você acertou")
        break

    elif KICK != NUMBER:
        print("Você errou!!Você tem {} chances".format(ATTEMPTS))

print("O número é: {}\n FIM".format(NUMBER))
