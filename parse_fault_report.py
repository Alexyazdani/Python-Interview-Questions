r'''
Alex Yazdani
29 June 2024

parse_fault_report.py
Write a function parse_fault_report(file_contents) that takes the text contents of a DFT fault report as input. The report contains lines like "Detected Faults : 180200" and "Fault Coverage : 97.4%". Your function should extract these values and return a summary string, and include a warning if fault coverage is below 98%.
'''

def parse_fault_report(filein, fileout):
    with open((filein), "r") as fin:
        file_contents = fin.read()
    data = {}
    for line in file_contents.splitlines():
        info = line.replace(" ", "").split(":")
        data[info[0]] = info[1]
    with open((fileout), "w") as fout:
        fout.write(f"Detected {data['DetectedFaults']} out of {data['TotalFaultsAnalyzed']} faults.\n")
        FC = data['FaultCoverage']
        fout.write(f"Fault coverage is {FC}.\n")
        if float(FC.rstrip('%')) < 98:
            fout.write("WARNING: Fault coverage below threshold!\n")


if __name__ == "__main__":
    filepath_in = "input_files/"
    filenames_in = ["DFT_report1.txt", "DFT_report2.txt"]
    filepath_out = "output_files/"
    filenames_out = ["DFT_summary1.txt", "DFT_summary2.txt"]
    for i, filename_in in enumerate(filenames_in):
        filein = filepath_in+filename_in
        fileout = filepath_out+filenames_out[i]
        parse_fault_report(filein, fileout)
