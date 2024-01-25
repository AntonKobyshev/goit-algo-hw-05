mgs_FileNotFound = """
❌ Error type: {}
Run the script from the directory where the file task_03.py is located
"""

mgs_WrongEncoding = """
❌ Error type: {}
Wrong file encoding type
"""

output_head = (
    "| {:^20}|".format("Algorithm types")
    + "{:^10}|\n".format("Speed")
    + "|" + "-" * 21 + "|" + "-" * 10 + "|\n"
)

fastest_result = "\nFastest algorithm: {} with total time: {}\n"
