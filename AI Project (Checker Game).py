import copy
import random
board = []
player = "red"
for i in range(6):
    board.append([" ", " ", " ", " ", " ", " "])
print(board)


def board_creator():
    for i in range(len(board)):
        if i == 0 or i == 1:

            for j in range(len(board)):
                if i % 2 == 0 and j % 2 == 0:
                    board[i][j] = "B"
                elif i % 2 == 1 and j % 2 == 1:
                    board[i][j] = "B"
        if i == 4 or i == 5:

            for j in range(len(board[i])):
                if i % 2 == 0 and j % 2 == 0:
                    board[i][j] = "R"
                elif i % 2 == 1 and j % 2 == 1:
                    board[i][j] = "R"
    for place in board:
        print(place, end='')
        print('')
    return board


def switchCurrentPlayer():


    global player

    if player == "red":
        player = "black"
    elif player == "black":
        player = "red"


def is_position_within_board(row, col):
    if col < 0 or col > 5:
        return False
    else:
        if row < 0 or row > 5:
            return False
        else:
            return True
def all_black_moves(board):

        all_black_moves=[]
        for i in range(6):
            for j in range(6):
                new_board = copy.deepcopy(board)
                if new_board[i][j] == "B":
                    if is_position_within_board(i + 1, j + 1):
                        if board[i+1][j+1] == "R":
                            if is_position_within_board(i + 2, j + 2):
                                if new_board[i + 2][j + 2] == " ":
                                    new_board[i + 2][j + 2] = 'B'
                                    new_board[i + 1][j + 1] = ' '
                                    new_board[i][j] = " "
                                    all_black_moves.append(new_board)
                                    new_board = copy.deepcopy(board)
                        if board[i+1][j+1] == " ":
                            if new_board[i + 1][j + 1] == " ":
                                new_board[i + 1][j + 1] = 'B'
                                new_board[i][j] = " "
                                all_black_moves.append(new_board)
                                new_board = copy.deepcopy(board)


                    if is_position_within_board(i + 1, j - 1):
                        if board[i+1][j-1] == "R":
                            if is_position_within_board(i + 2, j - 2):
                                if new_board[i + 2][j - 2] == " ":
                                    new_board[i + 2][j - 2] = 'B'
                                    new_board[i + 1][j - 1] = ' '
                                    new_board[i][j] = " "
                                    all_black_moves.append(new_board)
                                    new_board = copy.deepcopy(board)
                        if board[i+1][j-1] == " ":
                            if new_board[i + 1][j - 1] == " ":
                                new_board[i + 1][j - 1] = 'B'
                                new_board[i][j] = " "
                                all_black_moves.append(new_board)
                                new_board = copy.deepcopy(board)
        return all_black_moves


def all_red_moves(board):
    all_red_moves = []
    for i in range(6):
        for j in range(6):
            new_board = copy.deepcopy(board)
            if new_board[i][j] == "R":
                if is_position_within_board(i - 1, j - 1):
                    if board[i - 1][j - 1] == "B":
                        if is_position_within_board(i - 2, j - 2):
                            if new_board[i - 2][j - 2] == " ":
                                new_board[i - 2][j - 2] = 'R'
                                new_board[i - 1][j - 1] = ' '
                                new_board[i][j] = " "
                                all_red_moves.append(new_board)
                                new_board = copy.deepcopy(board)
                    if board[i - 1][j - 1] == " ":
                        if new_board[i - 1][j - 1] == " ":
                            new_board[i - 1][j - 1] = 'R'
                            new_board[i][j] = " "
                            all_red_moves.append(new_board)
                            new_board = copy.deepcopy(board)

                if is_position_within_board(i - 1, j + 1):
                    if board[i - 1][j + 1] == "B":
                        if is_position_within_board(i - 2, j + 2):
                            if new_board[i - 2][j + 2] == " ":
                                new_board[i - 2][j + 2] = 'R'
                                new_board[i - 1][j + 1] = ' '
                                new_board[i][j] = " "
                                all_red_moves.append(new_board)
                                new_board = copy.deepcopy(board)
                    if board[i - 1][j + 1] == " ":
                        if new_board[i - 1][j + 1] == " ":
                            new_board[i - 1][j + 1] = 'R'
                            new_board[i][j] = " "
                            all_red_moves.append(new_board)
                            new_board = copy.deepcopy(board)
    return all_red_moves

def eval1(board):
        number_of_red_pieces = 0
        number_of_black_pieces = 0
        red_pieces_across = 0
        black_pieces_across = 0
        for row in range(len(board)):
            if row == 0:
                red_pieces_across += board[row].count("R")
                number_of_black_pieces += board[row].count("B")
            elif row == len(board)-1:
                black_pieces_across += board[row].count("B")
                number_of_red_pieces += board[row].count("R")
            else:
                number_of_red_pieces += board[row].count("R")
                number_of_black_pieces += board[row].count("B")
        red_points = number_of_red_pieces + 3 * red_pieces_across
        black_points = number_of_black_pieces + black_pieces_across * 3
        return black_points - red_points


def eval2(board):
    number_of_red_pieces = 0
    number_of_black_pieces = 0
    red_pieces_in_black_territory = 0
    black_pieces_in_red_territory = 0
    for row in range(len(board)):
        if row <3:
            black_pieces_in_red_territory += board[row].count("B")
            number_of_red_pieces += board[row].count("R")
        else:
            number_of_black_pieces += board[row].count("B")
            red_pieces_in_black_territory += board[row].count("R")

    red_points = number_of_red_pieces + 1.5 * red_pieces_in_black_territory
    black_points = number_of_black_pieces + black_pieces_in_red_territory * 1.5
    return black_points - red_points
def minimax( player_rn, board, depth,min,max):

            if (not bool(all_red_moves(board))) or (not bool(all_black_moves(board))) or depth == 0:
                return eval1(board), board


            if player_rn == "black":

                best_eval = min
                best_move = None
                for move in all_black_moves(board):
                    evaluation = minimax("red", board, depth - 1, best_eval, max)[0]
                    if evaluation > best_eval:
                        best_eval = evaluation
                        best_move = move
                    if evaluation == best_eval:
                        ran = random.randint(1, 2)
                        if ran == 1:
                            best_move = move
                    if best_eval >= max:
                        print("Pruning Done")
                        return max, move

                return best_eval, best_move
            else:

                best_eval = max
                best_move = None
                for move in all_red_moves(board):
                    evaluation = minimax("black", board, depth - 1, min, best_eval)[0]
                    if evaluation < best_eval:
                        best_eval = evaluation
                        best_move = move
                    if best_eval == best_eval:
                        ran = random.randint(1, 2)
                        if ran == 1:
                            best_move = move
                    if best_eval <= min:
                        print("Pruning Done")
                        return min, move

                return best_eval, best_move
def play_game(depth,depth2):
        global player,board
        board=board_creator()


        possible_moves = all_red_moves(board)
        count = 0

        while  bool(all_red_moves(board)) and bool(all_black_moves(board)) :
            count += 1

            if player == "red":

                val, b2 = minimax("red", board, depth, -999, 999)
            else:

                val, b2 = minimax("black", board, depth2, -999, 999)

            board = copy.deepcopy(b2)
            for place in board:
                print(place, end='')
                print('')
            print("*************")
            switchCurrentPlayer()

        return eval1(board),player

def play_game2(depth):
    global player, board
    board = board_creator()
    print(board)

    possible_moves = all_red_moves(board)
    count = 0

    while not bool(all_red_moves(board)) or not bool(all_black_moves(board)) is False:
        count += 1
        if player == "red":
            val, board2 = minimax("red", board, depth, -999, 999)
        else:

            temp_board = copy.deepcopy(board)
            all_moves = all_black_moves(temp_board, "black")
            board2 = all_moves[random.randint(0, len(all_moves) - 1)]

        board = copy.deepcopy(board2)
        print("player {0}".format(player))
        for place in board:
            print(place, end='')
            print('')
        print("*************")
        switchCurrentPlayer()
    print(player)

    print(eval1(board))
    print("count {0}".format(count))
    return eval1(board), player
play_game(2,2)