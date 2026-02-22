import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

"""
Centralized Configuration and Fixture Management
This file handles the Setup and Teardown phases for all test scripts.
"""

# The scope="function" ensures the browser starts and closes for EACH individual test.
# This guarantees test isolation and independence, allowing them to run in any order.
@pytest.fixture(scope="function")
def driver(request):
    test_name = request.node.name
    print(f"\n[SETUP] Starting Browser for: {test_name}")
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-popup-blocking") # Mitigates some intrusive UI elements
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver # Test executes here
    
    print(f"\n[TEARDOWN] Closing Browser for: {test_name}")
    driver.quit()


# Add this to the very bottom of your conftest.py file

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    Generates a custom execution summary table in the console.
    This fulfills the assignment requirement to measure execution times
    without breaking the chronological setup/teardown logging.
    """
    terminalreporter.write_sep("=", "CUSTOM EXECUTION SUMMARY TABLE")
    terminalreporter.write_line(f"{'Test Case Name':<30} | {'Status':<10} | {'Time (s)':<10}")
    terminalreporter.write_line("-" * 55)
    
    # Loop through passed and failed tests
    for status in ('passed', 'failed'):
        reports = terminalreporter.stats.get(status, [])
        for rep in reports:
            if rep.when == 'call':  # Only get the actual test execution time
                test_name = rep.nodeid.split('::')[-1]
                terminalreporter.write_line(f"{test_name:<30} | {status.upper():<10} | {rep.duration:.2f}s")    