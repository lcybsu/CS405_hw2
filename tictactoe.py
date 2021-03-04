from copy import deepcopy
from mcts import *

class Board():
    def __init__(self, board=None):
        # define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_square = '-'
        # define board position
        self.position = {}
        # init (reset) board
        self.init_board()
        # create a copy of a previous board state if available
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)
    # init (reset) board
    def init_board(self):
        for row in range(4):
            for col in range(4):
                self.position[row, col] = self.empty_square
    # make move
    def make_move(self, row, col):
        board = Board(self)
        board.position[row, col] = self.player_1
        # swap players
        (board.player_1, board.player_2) = (board.player_2, board.player_1)
        return board
    # get whether the game is drawn
    def is_draw(self):
        for row, col in self.position:
            if self.position[row, col] == self.empty_square:
                return False
        return True

    def is_win(self):
        for col in range(4): # vertical
            winning_pattern = []
            for row in range(4):
                if self.position[row, col] == self.player_2:
                    winning_pattern.append((row, col))
                if len(winning_pattern) == 3:
                    if abs(max(winning_pattern)[0]-min(winning_pattern)[0]) < 3:
                        return True

        for row in range(4): # horizontal
            winning_pattern = []
            for col in range(4):
                if self.position[row, col] == self.player_2:
                    winning_pattern.append((row, col))
                if len(winning_pattern) == 3:
                    if abs(max(winning_pattern)[1] - min(winning_pattern)[1]) < 3:
                        return True

        winning_pattern = [] # diagonal left to right
        for row in range(4):
            col = row
            if self.position[row, col] == self.player_2:
                winning_pattern.append((row, col))
            if len(winning_pattern) == 3:
                if abs(max(winning_pattern)[1] - min(winning_pattern)[1]) < 3:
                    return True

        winning_pattern = []  # [0,3][1,2][2,1][0,3] # diagonal right to left
        for row in range(4):
            col = 3 - row
            if self.position[row, col] == self.player_2:
                winning_pattern.append((row, col))
            if len(winning_pattern) == 3:
                if abs(max(winning_pattern)[1] - min(winning_pattern)[1]) < 3:
                    return True

        winning_pattern = [] # diagonal left to right higher than the center line
        for row in range(0,3): #[0,1][1,2][2,3]
            col = row+1
            if self.position[row, col] == self.player_2:
                winning_pattern.append((row, col))
            if len(winning_pattern) == 3:
                return True

        winning_pattern = [] # diagonal left to right lower than the center line
        for row in range(1,4): #[1,0][2,1][3,2]
            col = row - 1
            if self.position[row, col] == self.player_2:
                winning_pattern.append((row, col))
            if len(winning_pattern) == 3:
                return True

        winning_pattern = [] # diagonal right to left higher than the center line
        for row in range(3):  #[0,2][1,1][2,0]
            col = 2 - row
            if self.position[row, col] == self.player_2:
                winning_pattern.append((row, col))
            if len(winning_pattern) == 3:
                return True

        winning_pattern = [] # diagonal right to left lower than the center line
        for row in range(1,4): #[1,3][2,2][3,1]
            col = 4 - row
            if self.position[row, col] == self.player_2:
                winning_pattern.append((row, col))
            if len(winning_pattern) == 3:
                return True
        return False

    def generate_states(self):
        actions = []
        for row in range(4):
            for col in range(4):
                if self.position[row, col] == self.empty_square:
                    actions.append(self.make_move(row, col))
        return actions

    def AI_vs_AI(self):
        print('\n  Tic Tac Toe uses Monte Carlo Tree Search\n')
        print('Type "exit" to quit')
        print('Move format [row,column]')
        mcts = MCTS()
        self = self.make_move(1, 2)
        print(self)
        while True:
            try:
                best_move1 = mcts.search(self)
                try:
                    self = best_move1.board
                except:
                    pass
                print(self)
                (board.player_1, board.player_2) = (board.player_2, board.player_1)

                best_move = mcts.search(self)
                try:
                    self = best_move.board
                except:
                    pass
                print(self)
                (board.player_1, board.player_2) = (board.player_2, board.player_1)
                if self.is_win():
                    print('player "%s" won!\n' % self.player_2)
                    break
                elif self.is_draw():
                    print('Drawn!\n')
                    break
            except Exception as e:
                print('  Error:', e)
                print('Move format [row,column]')

    def play_saved_game(self):
        print('\n  Tic Tac Toe uses Monte Carlo Tree Search\n')
        print('  Type "exit" to quit')
        print('Play the saved game')
        mcts = MCTS()
        self = self.make_move(1, 1)
        self = self.make_move(1, 2)
        self = self.make_move(2, 2)
        self = self.make_move(2, 1)
        print(self)
        while True:
            try:
                best_move1 = mcts.search(self)
                try:
                    self = best_move1.board
                except:
                    pass
                print(self)
                (board.player_1, board.player_2) = (board.player_2, board.player_1)
                best_move = mcts.search(self)
                try:
                    self = best_move.board
                except:
                    pass
                print(self)
                (board.player_1, board.player_2) = (board.player_2, board.player_1)
                if self.is_win():
                    print('player "%s" won!\n' % self.player_2)
                    break
                elif self.is_draw():
                    print('Drawn!\n')
                    break
            except Exception as e:
                print('  Error:', e)
                print('Move format [row,column]')

    def human_AI(self):
        print('\n  Tic Tac Toe uses Monte Carlo Tree Search \n')
        print('Type "exit" to quit')
        print('Move format [row,column]')

        print(self)
        mcts = MCTS()
        while True:
            # get user input
            user_input = input('Input[row,col]: ')
            if user_input == 'exit': break
            if user_input == '': continue
            try:
                row = int(user_input.split(',')[0]) - 1
                col = int(user_input.split(',')[1]) - 1

                if self.position[row, col] != self.empty_square:
                    print(' Illegal move!')
                    continue
                self = self.make_move(row, col)
                print(self)
                best_move = mcts.search(self)
                try:
                    self = best_move.board
                except:
                    pass
                print(self)
                if self.is_win():
                    print('player "%s" won!\n' % self.player_2)
                    break
                elif self.is_draw():
                    print('Game is drawn!\n')
                    break
            except Exception as e:
                print('  Error:', e)
                print('  Move format [x,y]: 1,2 where 1 is row and 2 is column')

    def __str__(self):
        board_string = ''
        for row in range(4):
            for col in range(4):
                board_string += ' %s' % self.position[row, col]
            board_string += '\n'
        if self.player_1 == 'x':
            board_string = '\n--------------\n "x" turn:\n--------------\n\n' + board_string
        elif self.player_1 == 'o':
            board_string = '\n--------------\n "o" turn:\n--------------\n\n' + board_string
        return board_string

if __name__ == '__main__':
    board = Board()
    # board.human_AI()
    # board.AI_vs_AI()
    board.play_saved_game()