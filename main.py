# main.py
class App:
    
    import src.log_generator.generator as gen
    
    def __init__(self):
        print("Inicializando la aplicación...")

    def run(self):
        file_name = input("Enter the file name: ")
        print(f"Creando archivo: {file_name}")
        # Aquí podrías llamar a tus módulos, por ejemplo:
        gen.create_file(file_name)


if __name__ == "__main__":
    app = App()   # se crea la instancia
    app.run()     # se ejecuta el programa
