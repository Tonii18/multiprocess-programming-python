# App entry point

import src.log_generator.generator as gen
import time

class App:
    
    def __init__(self):
        print("Initialising aaplication")

    def run(self):
        file_name = input("Enter the file name: ")
        print(f"Creating file: {file_name}")
        gen.create_file(file_name)
        print('File created succesfully!')


if __name__ == "__main__":
    app = App()   # Create an instance
    app.run()     # Run the program
