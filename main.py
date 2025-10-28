# App entry point

from src.log_analyzer.analyzer import LogAnalyzer
import src.log_generator.generator as gen
import time

file_name : str

class App:
    
    def __init__(self):
        print("Initialising aaplication")

    def run(self):
        # TODO 1: Ask for the file´s lines number
        file_name = input("Enter the file name: ")
        print(f"Creating file: {file_name}")
        full_name = gen.create_file(file_name)
        print('File created succesfully!')

        analyzer = LogAnalyzer(full_name)
        summary = analyzer.load_file()

        # TODO: Debugging the input, delete later

        print(f"\n✅ Log file loaded successfully!")
        print(f"Path: {summary['path']}")
        print(f"Total lines loaded: {summary['loaded']}")
        print(f"Example line: {analyzer.lines[0] if analyzer.lines else 'No lines loaded'}")



if __name__ == "__main__":
    app = App()   # Create an instance
    app.run()     # Run the program
