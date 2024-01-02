import numpy as np

def main():

    a = np.zeros((5,10))
    a[0][1] = 1
    a[1][0] = 2
    a[-1][-1] = 99
    a[-2][:] = 5

    print(a)
    a_as_list = a.tolist()
    print(f"a is {len(a)} by {len(a[0])}")


if __name__ == "__main__":
    main()
