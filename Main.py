from Cell import Cell
from Settings import Settings
from CellSim import CellSim

class Main:

    def __init__(self):
        self.running = True
        self.set = Settings()

    def run(self):
        while(self.running):
            self.cs = CellSim(self.set)
            self.cs.run_game()
            self.running = self.set.chgSettings(self)

main = Main()
main.run()
