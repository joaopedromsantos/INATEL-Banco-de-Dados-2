class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class LivroCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        titulo = input("Enter the title: ")
        autor = input("Enter the author: ")
        ano = int(input("Enter the year: "))
        preco = float(input("Enter the price: "))
        self.livro_model.create_livro(titulo, autor, ano, preco)

    def read_livro(self):
        id = input("Enter the id: ")
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"Title: {livro.get('titulo')}")
            print(f"Author: {livro.get('autor')}")
            print(f"Year: {livro.get('ano')}")
            print(f"Price: {livro.get('preco')}")

    def update_livro(self):
        id = input("Enter the id: ")
        titulo = input("Enter the new title: ")
        autor = input("Enter the new author: ")
        ano = int(input("Enter the new year: "))
        preco = float(input("Enter the new price: "))
        self.livro_model.update_livro(id, titulo, autor, ano, preco)

    def delete_livro(self):
        id = input("Enter the id: ")
        self.livro_model.delete_livro(id)

    def run(self):
        print("Welcome to the Livro CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()

