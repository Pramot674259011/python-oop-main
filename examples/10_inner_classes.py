class Computer:
    class CPU:
        def __init__(self, model):
            self.model = model

        def info(self):
            print(f"CPU model: {self.model}")


if __name__ == "__main__":
    cpu = Computer.CPU("Example CPU")
    cpu.info()
