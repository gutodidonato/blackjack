import random as r


pontos_jogador= 0
pontos_pc = 0
lista_de_cartas = [1,2,3,4,5,6,7,8,9,10,10,10]

def pegar_carta():
    carta = lista_de_cartas[r.randint(0, len(lista_de_cartas)) - 1]
    return carta

def primeira_jogada(jogador):
    primeira_carta = pegar_carta()
    segunda_carta = pegar_carta()
    print(f"{jogador} recebeu {primeira_carta} e um {segunda_carta}")
    if primeira_carta == 1:
        primeira_carta = 11
    if segunda_carta == 1 and primeira_carta != 11:
        segunda_carta = 11
    print(f"{jogador} está com {primeira_carta + segunda_carta} pontos \n")
    return primeira_carta + segunda_carta
    
def pedir(jogador):
    carta = lista_de_cartas[r.randint(0, len(lista_de_cartas)) - 1]
    print(f"{jogador} recebeu uma carta de {carta} pontos")
    return carta

def frase_derrota(jogador):
    print(f"{jogador} você perdeu")


def comprar_ou_parar(jogador, pontos):
    decisao = input("Deseja comprar ou parar? ").lower()
    print("\n")
    if decisao == "comprar" or decisao == "comp" or decisao == "sim":
        pontos += pedir(jogador)
        if pontos <= 21:
            return comprar_ou_parar(jogador, pontos)
    return pontos
    
def atualizar(acumulador, jogador):
    print(f"O {jogador} está com {acumulador} pontos")
    

def blackjack(jogador):
     # First two cards for both players
    acumuladora = 0 
    acumuladora2 = 0
    acumuladora += primeira_jogada(jogador)
    acumuladora2 += primeira_jogada("CPU")
     # Player`s turn
    acumuladora = comprar_ou_parar(jogador, acumuladora)
    atualizar(acumuladora, jogador)
    print("\n")
    
    # Lógica computador    
    while acumuladora2 < 17:
        acumuladora2 += pedir("CPU")

    atualizar(acumuladora2, "CPU")
    
    # Lógica final de game
    if acumuladora > 21 or (acumuladora2 <= 21 and acumuladora2 >= acumuladora):
        frase_derrota(jogador)
    else:
        print(f"{jogador} venceu!")

    print(f"Fim do jogo. \n")
    continuar = input(f"Deseja continuar?")
    if continuar == "sim" or continuar == "s" or continuar == "yes":
        blackjack(jogador)
    
    
    
blackjack("Luis")