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

        # TODO:
        """
        1. Create a results folder and export analysis data to a json file X
        2. Monitoring results by using psutil
        3. Create feature to analyze a named file entered by the user
        4. Clean main.py
        """

        # 1. Enter file name

        file_name = input("Enter the file name: ")
        print(f"Creating file: {file_name}")
        full_name = gen.create_file(file_name)
        print('File created succesfully!')

        # 2. Create analyzer instance and run full analysis

        analyzer = LogAnalyzer(full_name)
        final_results = analyzer.run_analysis()

        # 3. Show resume

        print("--- Final Results ---")
        print("Total lines analyzed:", {final_results['total_lines']})
        print("Message types count:", final_results["messages"])
        print("\nTop 10 active IPs:")
        for ip, count in final_results["top_ips"]:
            print(f"{ip}: {count} times")

        print("\nErrors by hour:")
        for hour, count in final_results["errors_by_hour"].items():
            print(f"{hour}:00 -> {count} errors")

        print("\n==============================")
        print("Analysis completed successfully ✅")

        # 4. Save results

        try:
            report_path = analyzer.save_results(out_dir="results")
            print(f"\nSaved analysis report to: {report_path}")
        except Exception as e:
            print("Warning: could not save results:", e)


# Run main

if __name__ == "__main__":
    app = App()   # Create an instance
    app.run()     # Run the program
