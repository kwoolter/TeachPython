
def main():

    print(f"Welcome to module {__name__}.")
    print(f"Location:{__file__}")


def initialise():
    print(f"Initialising {__name__}")


print(f"\nYou have imported {__name__}...\n")
initialise()

if __name__ == "__main__":
    main()
