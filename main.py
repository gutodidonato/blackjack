import random as r


pontos_jogador= 0
pontos_pc = 0
lista_de_cartas = [1,2,3,4,5,6,7,8,9,10,11]

def pegar_carta():
    carta = lista_de_cartas[0, r.randint(0, len(lista_de_cartas))]
    return carta



def blackjack():
    primeira_carta = pegar_carta
    segunda_carta = pegar_carta
    print(f"Você recebeu {primeira_carta} e um {segunda_carta}")
    