import pandas as pd
from pathlib import Path


def main():
    print(f"Welcome to module {__name__}.")
    print(f"Location:{__file__}")
    print(f"We are working with pandas version {pd.__version__}.")

    file_name = "comics.csv"

    # Create path for the data file that we are going to load
    data_folder = Path(__file__).resolve().parent / "data"
    file_to_open = data_folder / file_name

    print(f"Loading {file_to_open}...")

    comics = pd.read_csv(file_to_open)
    print(comics.head(10))


def initialise():
    print(f"Initialising {__name__}...")
    print("DONE!\n\n")


print(f"\nYou have imported {__name__}.")
print(f"Running the initialise function...\n")
initialise()

if __name__ == "__main__":
    main()
