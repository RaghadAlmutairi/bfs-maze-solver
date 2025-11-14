import queue

print("**************************")
print("WELCOME TO +A PATH MAZE :)")
print("**************************")

print("\nGame Description:\n**THE PLAYER IS -> + \n**THE GOAL ARE-> A+\n")
print("***PATH KEYS***\n  L = Left\n  R = Right\n  U = Up\n  D = Down\n")


def createMazeForTheGoal():
    maze = []
    maze.append(["@", "@", "@", "@", "@", "A+", "@", "@", "@"])
    maze.append(["@", " ", " ", " ", " ", " ", " ", " ", " @"])
    maze.append(["@", " ", "@", "@", " ", "@", "@", " ", " @"])
    maze.append(["@", " ", "@", " ", " ", " ", "@", " ", " @"])
    maze.append(["@", " ", "@", " ", "@", " ", "@", " ", " @"])
    maze.append(["@", " ", "@", " ", "@", " ", "@", " ", " @"])
    maze.append(["@", " ", "@", " ", "@", " ", "@", "@", " @"])
    maze.append(["@", " ", " ", " ", " ", " ", " ", " ", " @"])
    maze.append(["@", "@", "@", "@", "@", "@", "@", "X", " @"])

    return maze


def printPathMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "A+":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "A+":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "@"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "A+":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("The return path for A+: " + moves)
        print("")
        printPathMaze(maze, moves)
        print("\n\nGreat job, you have reached the goal :)\nContinue to progress in this way in real life to reach your goals.")
        return True

    return False


# MAIN BFS ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze = createMazeForTheGoal()

while not findEnd(maze, add):
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)