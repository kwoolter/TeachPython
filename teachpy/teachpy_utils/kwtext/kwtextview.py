import colorama
from colorama import Fore, Back, Style

class KWTextView:

    def __init__(self):
        pass

    def initialise(self):
        colorama.init(autoreset=True)

    def new_grid(self, rows : int = 10, columns : int = 10, fill : str = " "):

        use_char = fill[0]
        grid = [[use_char] * rows for j in range(columns)]
        return grid

    def new_colour_mask(self, rows : int = 10, columns : int = 10, fg = Fore.WHITE, bg = Back.BLACK, style = Style.NORMAL):
        colour = fg + bg + style
        grid = [[colour] * rows for j in range(columns)]
        return grid

    def print_grid(self, grid : list, colours : list = None, override : dict = None):

        cols = len(grid)
        rows = len(grid[0])

        if colours is None:
            colours = self.new_colour_mask( columns = cols, rows = rows, style=Style.BRIGHT)


        for y in range(rows):
            for x in range(cols):
                char = grid[x][y]
                colour = colours[x][y]
                if override is not None:
                    colour = override.get(char, colour)
                print(colour + char,end="")
            print()



def test():

    t = KWTextView()
    t.initialise()

    print(Fore.RED + "\nHello World\n")

    colour_map = {"X": Fore.LIGHTWHITE_EX + Back.BLUE + Style.BRIGHT,
                  "Y" : Fore.BLACK + Back.RED,
                  " " : Back.YELLOW,
                  "#" : Fore.GREEN + Back.BLACK + Style.BRIGHT}

    rows = 4
    columns = 10

    g = t.new_grid(rows = rows, columns = columns, fill = "0")
    colours = t.new_colour_mask(rows, columns, Fore.RED, Back.LIGHTYELLOW_EX, style = Style.NORMAL)

    g[2][2] = "X"
    g[5][2] = "Y"
    colours[0][0] = Fore.GREEN + Back.LIGHTCYAN_EX + Style.BRIGHT

    t.print_grid(g, colours, override=colour_map)

    print("\n\n")

    rows = 15
    columns = 5

    g = t.new_grid( rows = rows, columns = columns, fill = "@")

    g[2][1] = "X"
    g[0][5] = " "
    g[0][0] = "#"

    t.print_grid(g, override=colour_map)

    print("\n\nBye")

if __name__ == "__main__":
    test()