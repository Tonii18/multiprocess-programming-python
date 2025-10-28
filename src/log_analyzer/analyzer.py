import os

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
    
    # 2. split_work() ->

    def split_work(self, lines_per_fragment):
        raise;

    def analyze_parallel(self):
        raise;

    def combine_results(self):
        raise;

    def show_report(self):
        raise;

    def run_analysis(self):
        raise;