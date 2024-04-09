import random

class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increase_score(self, points):
        self.score += points

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board, self.bomb_locations = self.make_new_board()

    def make_new_board(self):
        board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bomb_locations = []
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bomb_locations.append((row, col))
            bombs_planted += 1
        return board, bomb_locations

    def print_board(self):
        board = [[' ' if (row, col) not in self.dug_positions else self.board[row][col] for col in range(self.dim_size)] for row in range(self.dim_size)]
        for row in board:
            print('|'.join(row))
            print('-' * (len(row) * 2 - 1))

    def dig(self, row, col):
        if (row, col) in self.bomb_locations:
            return False
        self.dug_positions.add((row, col))
        return True
    
    def play_game(self):
        self.dug_positions = set()
        print("Welcome to Minesweeper!")
        self.print_board()

        # Create answer tuples
        answers = ("C", "D", "A", "A", "B")
        guesses = []  # Empty guess list 
        score = 0

        questions = ("How many elements are in the periodic table?: ",
                     "Which animal lays the largest eggs?: ",
                     "What is the most abundant gas in Earth's atmosphere?: ",
                     "How many bones are in the human body?: ",
                     "Which planet in the solar system is the hottest?: ")
        # Create option tuples
        options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

        for i, question in enumerate(questions):
            while True:
                row = int(input("Enter row to dig: "))
                col = int(input("Enter column to dig: "))

                if not (0 <= row < self.dim_size and 0 <= col < self.dim_size):
                    print("Invalid position. Please enter row and column within the board dimensions.")
                    continue

                if not self.dig(row, col):
                    # ask question
                    # Shuffle the list
                    questions_list = list(questions)
                    random.shuffle(questions_list)

                    # Choose one element from the shuffled list
                    chosen_element = random.choice(questions)

                    # print question
                    print(chosen_element)

                    # loop through options and print for the specified index for specific question
                    for option in options[i]:
                        print(option)

                    guess = input("Enter (A, B, C, D): ").upper()
                    guesses.append(guess)
                    if guess != answers[i]:  # Add guess to empty guess list 
                        print("Game Over! You hit a bomb!")
                        return
                else:
                    print("You dug safely!")
                    self.print_board()
                    if len(self.dug_positions) == self.dim_size**2 - self.num_bombs:
                        print("Congratulations! You've cleared the board!")
                        return

# Test the game
user1 = User("Player 1")
print("Welcome,", user1.name)
board = Board(5, 5)
board.play_game()
