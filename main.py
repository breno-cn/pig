from Game import Game

def main():
    game = Game()
    results = [0, 0]

    print('rodando 1000 jogos, forçando o jogador 1 a ganhar, fazendo ele ter uma estratégia e o segundo jogando aleatório')
    for _ in range(1000):
        game.reset()
        while not game.should_stop():
            game.player1_win()
        
        winner = game.winner()
        results[winner] += 1
    print(results)

    results = [0, 0]
    print('rodando 1000 jogos, forçando o jogador 2 a ganhar, fazendo ele ter uma estratégia e o segundo jogando aleatório')
    for _ in range(1000):
        game.reset()
        while not game.should_stop():
            game.player2_win()
        
        winner = game.winner()
        results[winner] += 1
    print(results)

    results = [0, 0]
    print('rodando mil jogos aleatórios')
    for _ in range(1000):
        game.reset()
        while not game.should_stop():
            game.play_random()
        
        winner = game.winner()
        results[winner] += 1
    print(results)

    print('vale notar que se ambos usarem essa estratégia, targets mais razoáveis tendem a vencer mais')
    results = [0, 0]
    print('rodando mil jogos aleatórios')
    for _ in range(1000):
        game.reset()
        while not game.should_stop():
            game.tough_victory()
        
        winner = game.winner()
        results[winner] += 1
    print(results)
if __name__ == '__main__':
    main()
