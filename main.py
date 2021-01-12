import random as rd
class Board:
    def __init__(self):
        self.board = [[0 for col in range(3)] for row in range(3)]

    def player_sign(self, sign):
        signs = ["-", "X", "O"]
        return signs[sign]

    def print_board(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                print(self.player_sign(self.board[x][y]), end=" ")
            print()

    def make_move(self, player_sign, move):
        # Checks if input is valid and then put player_sign on board
        if(len(move) != 2 or type(move[0]) != int 
           or type(move[1]) != int 
           or move[0] < 0 or move[0] > 2
           or move[1] < 0 or move[1] > 2
           or self.board[move[0]][move[1]] != 0):
            print("Invalid move!")
            return False
        else:
            self.board[move[0]][move[1]] = player_sign
            return True

    def is_board_full(self):
        for x in self.board:
            for y in x:
                if(y == 0):
                    return False

    def is_game_over(self, player_win):
        if(player_win or self.is_board_full()):
            return True

    def win_indexes(self, n):
        for r in range(n):
            yield [(r, c) for c in range(n)]
        for c in range(n):
            yield [(r, c) for r in range(n)]
        yield [(i, i) for i in range(n)]
        yield [(i, n - 1 - i) for i in range(n)]

    def is_winner(self, decorator):
        n = len(self.board)
        for indexes in self.win_indexes(n):
            if all(self.board[r][c] == decorator for r, c in indexes):
                return True
        return False
    

    # not yet filled position
    def valid_positions(self):
        valid_positions = []
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if(self.board[x][y] == 0):
                    valid_positions.append((x,y))
        return valid_positions
    
    def ai(self):
        pos = self.valid_positions()
        rd_num = rd.randint(0,len(pos)-1)
        return pos[rd_num]

    def ai_hard(self, decorator):
        player = 0
        ai = 0
        # my positions
        for i,x in enumerate(self.board):
            for j,y in enumerate(x):
                if y == 1:
                    player += 2**(i+j)
                elif y == 2:
                    ai += 2**(i+j)

        # magic C AI function
        return 1

class Player:
    def __init__(self, name, is_ai, sign):
        self.ai = is_ai
        self.name = name
        self.sign = sign

    def play(self, board):
        if not self.ai:
            valid_move = False
            while(not valid_move):
                board.print_board()
                print("{} is playing: (eg: 2,1)".format(self.name))
                val = input("> ")
                try:
                    x, y = map(lambda x: int(x), val.split(","))
                    valid_move = board.make_move(self.sign, (x, y))
                except:
                    valid_move = False
                
            return board

        else:
            board.print_board()
            position = board.ai()
            board.make_move(self.sign, position)
            print("AI is playing")
            print(">",position)
            return board


    def is_winner(self, board):
        return board.is_winner(self.sign)


board = Board()
print("1. Player vs Player")
print("2. Player vs AI")

gamemode = input("[1/2]")
print("Player1 - name")
player1_name = input("> ")
player1 = Player(player1_name, False, 1)

if gamemode == "2":
    player2 = Player("AI", True, 2)

else:
    print("Player2 - name")
    player2_name = input("> ")
    player2 = Player(player2_name, False, 2)

end = False
while not end:
    board = player1.play(board)
    p1win = player1.is_winner(board)
    end = board.is_game_over(p1win)
    if(end and not p1win):
        print("Its a tie")
        print(board.print_board())
        break
    if(p1win):
        print("{} win!".format(player1.name))
        print(board.print_board())
        break

    board = player2.play(board)
    p2win = player2.is_winner(board)
    end = board.is_game_over(p2win)
    if(end and not p2win):
        print("Its a tie")
        print(board.print_board())
        break
    if(p2win):
        print("{} win!".format(player2.name))
        print(board.print_board())
