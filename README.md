# A+ Path Maze -- BFS Solver

This project was created as part of the **Fundamentals of AI (2023)**
course.\
It implements an **AI path‑finding agent** using **Breadth‑First Search
(BFS)** to navigate a maze and reach the goal.

------------------------------------------------------------------------

## 🎮 Game Description

In this maze game:

-   **Player path is shown using +**
-   **Start point is A+**
-   **Goal point is X**
-   \*\*Walls are @*\*
-   **Free spaces are blank (" ")**

Your agent explores all valid moves using **BFS** until it finds the
shortest path to the goal.

------------------------------------------------------------------------

## 🧠 AI Technique Used: BFS (Breadth‑First Search)

BFS explores all paths equally level‑by‑level, guaranteeing:

-   **Shortest path to the goal**
-   **No revisiting invalid or blocked nodes**
-   **Systematic exploration**

It works by using a **queue** of movement possibilities:\
`L = Left`, `R = Right`, `U = Up`, `D = Down`.

------------------------------------------------------------------------

## 🗺️ Maze Structure

The maze is stored in a 2D list:

    @ @ @ @ @ A+ @ @ @
    @               @
    @   @ @   @ @   @
    @   @     @     @
    @   @ @   @     @
    @   @ @   @     @
    @   @ @   @ @   @
    @               @
    @ @ @ @ @ @ @ X @

------------------------------------------------------------------------

## 🚀 How It Works

1.  The BFS algorithm starts from **A+**.
2.  It tries moves in this order: `L, R, U, D`.
3.  Every valid move is added to the queue.
4.  BFS continues until the goal `X` is found.
5.  The full path is printed on the maze using `+`.

------------------------------------------------------------------------

## 🧩 Example Output

When the goal is found:

    The return path for A+: RDDDRRRUUUDDD...

    + + + @ @ A+ @ @ @
    @ + + + + + + + + @
    @   @ @ +   @ @ + @
    ...
    Great job, you have reached the goal :)

------------------------------------------------------------------------

## 📦 Files Included

-   `main.py` -- BFS maze solver\
-   README.md -- project documentation

------------------------------------------------------------------------

## ▶️ How to Run

1.  Make sure you have **Python 3** installed.
2.  Run the script:

``` bash
python3 main.py
```

You will see the maze, the found path, and the success message.

------------------------------------------------------------------------

## 🧑‍💻 Authors

-   **Raghad Khaled Almutairi -- 2110409**\
-   **Ryouf Bander Alghamdi -- 2110489**\
-   **Amatulrahman Alsubhi**

------------------------------------------------------------------------

## 📘 Course

**CCAI‑221 -- Fundamentals of AI (2023)**\
**Path‑Finding AI Project (BFS)**

------------------------------------------------------------------------

## ⭐ Notes

This project demonstrates how simple search algorithms can solve
real‑world navigation problems, making it an excellent example for
introductory AI concepts.
