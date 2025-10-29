import os
from multiprocessing import Pool
from src.log_analyzer.extra_functions import messages_analysis

class LogAnalyzer:

    file_name : str
    processes : int
    
    def __init__(self, file_name, processes = 4):
        self.file_name = file_name
        self.processes = processes

        self.lines = []
        self.fragments = []
        self.partial_results = []
        self.results = {}

    # 'Self' is used to indicate the current instance

    # 1. load_file() -> This function is used to load a file and get some information about it

    def load_file(self):
        file_path = self.file_name

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Log file not found: {file_path}")
        
        loaded = 0
        valid_lines = []

        with open(file_path, 'r') as f:
            for row in f:
                line = row.rstrip('\n').strip()
                parts = line.split(';')
                valid_lines.append(line)
                loaded += 1

        self.lines = valid_lines

        return {'path': file_path, 'loaded': loaded}
    
    # 2. split_work() -> It divide the log file content in equals parts

    def split_work(self):
        total_lines = len(self.lines)
        processes = self.processes
        fragment_size = total_lines // processes
        fragments = []

        start = 0

        # This loop calculate de final index of current fragment ('end')

        for i in range(processes):
            end = start + fragment_size
            if i == processes - 1:
                fragments.append(self.lines[start:])
            else:
                fragments.append(self.lines[start:end])
            start = end

        self.fragments = fragments

        return {
            "total_lines": total_lines,
            "fragments": len(fragments),
            "lines_per_fragment": fragment_size,
            "last_fragment_lines": len(fragments[-1])
        }
    
    # 3. analyze_parallel() -> It creates 4 process by using Pool from multiproccesing

    def analyze_parallel(self):
        processes = self.processes
        with Pool(processes) as pool:
            results = pool.map(messages_analysis, self.fragments)
        
        self.partial_results = results
        return self.partial_results

    # 4. combine_results() -> It takes each dictionary with the counters and it will calculate final measures

    def combine_results(self):
        
        raise;

    def show_report(self):
        raise;

    def run_analysis(self):
        raise;