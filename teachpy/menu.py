import cmd
import teachpy_utils as utils

def run():

    c = TeachPyCLI()
    c.run()


class TeachPyCLI(cmd.Cmd):
    def __init__(self):

        self.intro = "Welcome to Teach Python.\nType help for assistance."
        self.prompt = "What next?"

        super(TeachPyCLI, self).__init__()


    def do_start(self, arg : str):
        """Start a module"""

        modules = {1:"Basic Stuff", 2:"Getting going", 3:"Heating up!", 4:"On fire!!!"}

        if len(arg) == 0:
            print("You didn't specify a module to start!")

            selection = utils.pick("Module", list(modules.values()))

            utils.type_text(f"Starting {selection}...\n")

        else:
            print(f"Starting module {arg[0]}...")

    def run(self):
        self.cmdloop()


if __name__ == "__main__":
    run()



