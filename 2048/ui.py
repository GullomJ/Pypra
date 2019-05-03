from bill import GameCoreController
from model import Direction


class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        print('------------------------------')
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c], end='\t')
            print()

    def update(self):
        while True:
            self.__move_map()
            if self.__controller.is_change:
                self.__controller.generate_new_number()
                self.__print_map()
            if self.__controller.is_game__over():
                print('Game Over')
                break

    def __move_map(self):
        dir = input('Direction of movement（w,s,a,d）:')
        if dir == 'w':
            self.__controller.move(Direction.up)
        elif dir == 's':
            self.__controller.move(Direction.down)
        elif dir == 'a':
            self.__controller.move(Direction.left)
        elif dir == 'd':
            self.__controller.move(Direction.right)
