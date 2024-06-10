import teachpy
import logging

def main():

    logging.basicConfig(level=logging.WARN)
    try:
        teachpy.run()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()