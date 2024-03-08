from gameparts import Board

# Всё, что ниже этой инструкции, не будет импортироваться,
# но будет выполняться при запуске файла game.py.
def main():
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.display()

# А вот вызов этой функции.
if __name__ == '__main__':
    main()