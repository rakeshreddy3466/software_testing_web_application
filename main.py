import pytest
import datetime

"""
Main Suite Executor
This script triggers the entire test suite automatically.
It generates a self-contained HTML report for clear test result documentation.
"""

if __name__ == "__main__":
    print(f"--- Starting Full Test Suite at {datetime.datetime.now()} ---")
    
    # -v: Verbose output (shows each test name)
    # -s: Allows print statements to show in the console
    # --html/--self-contained-html: Generates the standalone HTML report
    exit_code = pytest.main([
        "-v", 
        "-s", 
        "--html=report.html", 
        "--self-contained-html"
    ])
    
    if exit_code == 0:
        print("\n--- SUITE EXECUTION SUCCESSFUL ---")
        print("--- Please open 'report.html' in your browser to view the results ---")
    else:
        print("\n--- SUITE EXECUTION FAILED ---")