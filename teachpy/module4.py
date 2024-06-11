import pandas as pd


def main():
    print(f"Welcome to module {__name__}.")
    print(f"Location:{__file__}")

    print(f"We are working with pandas version {pd.__version__}.")

    file_name = "comics.csv"
    file_location = ".\\data"

    print(f"Loading {file_location}\\{file_name}")

    comics = pd.read_csv(f"{file_location}\\{file_name}")
    print(comics.describe())


def initialise():
    print(f"Initialising {__name__}")


print(f"\nYou have imported {__name__}...\n")
initialise()

if __name__ == "__main__":
    main()
