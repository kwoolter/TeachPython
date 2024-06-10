from . teachpy_utils.kwtext import *

def main():

    print(f"Welcome to {__name__}")

    t = KWTextView()
    t.initialise()

    print(Fore.GREEN + "Welcome to Teach Python - Module 2")
    print(Fore.BLUE + "Hello World")

    colour_map = {"X": Fore.RED + Back.BLUE + Style.BRIGHT,
                  " ": Back.YELLOW,
                  "#": Fore.GREEN + Back.BLACK + Style.BRIGHT}

    rows = 3
    columns = 10

    g = t.new_grid(rows=rows, columns=columns, fill="0")
    colours = t.new_colour_mask(rows, columns, Fore.RED, Back.YELLOW, style=Style.NORMAL)

    g[2][2] = "X"
    g[5][2] = "X"
    colours[0][0] = Fore.YELLOW + Back.BLACK + Style.BRIGHT

    t.print_grid(g, colours, override=colour_map)


    print(Fore.RED + "Bye")


if __name__ == "__main__":
    main()