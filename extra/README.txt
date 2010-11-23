501.txt through 509.txt are pages straight from the opcode description table
in the SH-1/SH-2/SH-DSP Software Manual from Renesas.

sh7052.csv and sh7055.csv are CSV files from the on-chip peripheral module
register tables and interrupt vector tables in the SH7052 and SH7055 F-ZTAT
Hardware Manuals. filter-vec.awk and filter-reg.awk convert the CSVs into
importable Python modules.

page_parse.py takes the data in the manual pages and turns it into a useful
CSV of opcode instructions.

csv_to_py.py converts the output of page_parse.py into an importable module
with a single data structure: "opcodes".
