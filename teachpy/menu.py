import cmd
from . import teachpy_utils as utils


def run():
    c = TeachPyCLI()
    c.run()


class TeachPyCLI(cmd.Cmd):
    """ Command Line interface to run teh Tech Python menu"""

    def __init__(self):

        self.intro = "Welcome to Teach Python.\nType help for assistance."
        self.prompt = "What next?"

        super(TeachPyCLI, self).__init__()

        return

    def do_start(self, arg: str):
        """Start a module"""

        modules = ("Basic Stuff", "Getting going", "Heating up!", "On fire!!!")

        if len(arg) == 0:
            print("You didn't specify a module to start!")

            selection = utils.pick("Module", modules)
            module_number = modules.index(selection) + 1

            utils.type_text(f"Starting module {module_number}. {selection}...\n")


        else:
            selection = arg

            try:
                module_number = modules.index(arg) + 1
                utils.type_text(f"Starting module {module_number}. {selection}...\n")

            except ValueError:
                print(f"Module '{selection}' not found")
                return

        if module_number == 1:
            from . import module1
            pass
        elif module_number == 2:
            from . import module2

        return

    def run(self):

        self.cmdloop()

        return


if __name__ == "__main__":
    run()
