from model import Location
import random
import copy
from model import Direction


class GameCoreController:

    def __init__(self):
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4
        ]

        self.__list_merge = []

        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def zore_to_end(self):
        for item in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[item] == 0:
                del self.__list_merge[item]
                self.__list_merge.append(0)

    def merge(self):
        self.zore_to_end()
        for item in range(len(self.__list_merge) - 1):
            if self.__list_merge[item] == self.__list_merge[item + 1]:
                self.__list_merge[item], self.__list_merge[item + 1] = self.__list_merge[item] + self.__list_merge[
                    item + 1], 0
        self.zore_to_end()

    def __move_left(self):
        for item in range(len(self.__map)):
            self.__list_merge[:] = self.__map[item]
            self.merge()
            self.__map[item][:] = self.__list_merge

    def __move_right(self):
        for item in range(len(self.__map)):
            self.__list_merge[:] = self.__map[item][::-1]
            self.merge()
            self.__map[item][::-1] = self.__list_merge

    def __move_up(self):
        for c in range(len(self.__map)):
            self.__list_merge.clear()
            for r in range(len(self.__map[c])):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(len(self.__map[c])):
                self.__map[r][c] = self.__list_merge[r]

    def __move_down(self):
        for c in range(len(self.__map)):
            self.__list_merge.clear()
            for r in range(len(self.__map[c]) - 1, -1, -1):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(len(self.__map[c]) - 1, -1, -1):
                self.__map[r][c] = self.__list_merge[len(self.__map[c]) - 1 - r]

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map)):
                if self.__map[r][c] == 0:
                    loc = Location(r, c)
                    self.__list_empty_location.append(loc)

    def generate_new_number(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_location.clear()

    def move(self, dir):
        original_map = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()
        self.is_change = original_map != self.__map

    def is_game__over(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r]) - 1):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c + 1][r]:
                    return False
        return True
