r'''
Alex Yazdani
29 June 2024

parse_fault_report.py
Write a function parse_fault_report(file_contents) that takes the text contents of a DFT fault report as input. The report contains lines like "Detected Faults : 180200" and "Fault Coverage : 97.4%". Your function should extract these values and return a summary string, and include a warning if fault coverage is below 98%.
'''

def parse_fault_report(file_contents):
    data = {}
    for line in file_contents.splitlines():
        info = line.replace(" ", "").split(":")
        data[info[0]] = info[1]
    print(f"Detected {data['DetectedFaults']} out of {data['TotalFaultsAnalyzed']} faults.")
    FC = data['FaultCoverage']
    print(f"Fault coverage is {FC}.")
    if float(FC.rstrip('%')) < 98:
        print("WARNING: Fault coverage below threshold!")
    return ""

if __name__ == "__main__":
    filepath = "input_files/"
    filenames = ["DFT_report1.txt", "DFT_report2.txt"]
    for filename in filenames:
        with open((filepath+filename), "r") as f:
            file_contents = f.read()
        print(parse_fault_report(file_contents))
        print("---")
