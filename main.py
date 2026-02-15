import pytest
import datetime

if __name__ == "__main__":
    print(f"--- Starting Full Test Suite at {datetime.datetime.now()} ---")
    
    # This command automatically finds ANY file starting with "test_" and runs it.
    exit_code = pytest.main(["-v", "-s", "--durations=0"])
    
    if exit_code == 0:
        print("\n--- SUITE EXECUTION SUCCESSFUL ---")
    else:
        print("\n--- SUITE EXECUTION FAILED ---")