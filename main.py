# App entry point

from src.log_analyzer.analyzer import LogAnalyzer
from src.log_analyzer.extra_functions import messages_analysis
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

        split_summary = analyzer.split_work()
        print(split_summary)

        # TODO: Remove later this loop, just for tests

        print("\n--- Fragment check ---")
        for i, fragment in enumerate(analyzer.fragments):
            print(f"Fragment {i+1}: {len(fragment)} lines")
            print("  Example lines:")
            for example in fragment[:3]:
                print(f"    {example}")
                print("  ...")
        print("----------------------\n")

        # TODO: Remove later, just for tests

        example_fragment = analyzer.fragments[0]
        result = messages_analysis(example_fragment)
        print(result)

        print('==========================================')

        # TODO: Remove later, just for tests

        partial_results = analyzer.analyze_parallel()
        for i, res in enumerate(partial_results):
            print(f"Fragment {i+1} partial result: {res}")




        



if __name__ == "__main__":
    app = App()   # Create an instance
    app.run()     # Run the program
