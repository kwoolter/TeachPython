import cmd


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
        if len(arg) == 0:
            print("You didn't specify a module to start!")
        else:
            print(f"Starting module {arg[0]}...")

    def run(self):
        self.cmdloop()







