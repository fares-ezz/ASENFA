import os, sys, time

def draw(word="ASENFA", speed=0.015):
    """
    Draws a smooth animated word made of yellow stars (*) in the terminal.
    Each letter is spaced for readability.
    And I Used AI To Create That Animation
    """
    # Enable ANSI colors on Windows
    if os.name == "nt":
        os.system("")

    YELLOW = "\033[33m"
    RESET = "\033[0m"

    # 5x5 pixel font for each character
    LETTERS = {
        'A': [" *** ", "*   *", "*****", "*   *", "*   *"],
        'S': [" ****", "*    ", " *** ", "    *", "**** "],
        'E': ["*****", "*    ", "**** ", "*    ", "*****"],
        'N': ["*   *", "**  *", "* * *", "*  **", "*   *"],
        'F': ["*****", "*    ", "**** ", "*    ", "*    "],
        'H': ["*   *", "*   *", "*****", "*   *", "*   *"],
        'L': ["*    ", "*    ", "*    ", "*    ", "*****"],
        'O': [" *** ", "*   *", "*   *", "*   *", " *** "],
        'W': ["*   *", "*   *", "* * *", "** **", "*   *"],
        'R': ["**** ", "*   *", "**** ", "*  * ", "*   *"],
        'D': ["**** ", "*   *", "*   *", "*   *", "**** "],
        ' ': ["     ", "     ", "     ", "     ", "     "],
    }

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    # Build word with spacing between characters
    grid = [""] * 5
    for ch in word:
        letter = LETTERS.get(ch.upper(), LETTERS[' '])
        for i in range(5):
            # Add extra spaces for better separation between letters
            grid[i] += letter[i] + "   "

    # Animation
    clear()
    height, width = len(grid), len(grid[0])
    frame = [[" " for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if grid[i][j] == "*":
                frame[i][j] = YELLOW + "*" + RESET
                clear()
                for r in range(height):
                    print("".join(frame[r]))
                sys.stdout.flush()
                time.sleep(speed)

    # Final static display
    clear()
    for r in range(height):
        print("".join(frame[r]))
    print()
    time.sleep(1.5)


