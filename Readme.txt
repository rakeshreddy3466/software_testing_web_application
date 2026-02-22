============================================================
AUTOMATED GUI-BASED TESTING SUITE - ASSIGNMENT 2
============================================================
Student Name: Rakesh Reddy Karri
System Under Test: https://automationexercise.com/
Tools: Python 3.13.1, Selenium, Pytest, Pytest-HTML

------------------------------------------------------------
1. HOW TO RUN THE SUITE
------------------------------------------------------------
Prerequisites:
- Python 3.x and Chrome Browser installed.
- Install required packages using the terminal:
  pip install selenium pytest webdriver-manager pytest-html

To run the entire suite automatically (Single Click):
  python3 main.py

* NOTE: Running main.py will automatically generate a 'report.html' 
  file in the directory containing the full test execution results.

To run individual scripts:
  pytest test_01_homepage.py -v -s

------------------------------------------------------------
2. PROJECT ARCHITECTURE & TRACEABILITY
------------------------------------------------------------
- main.py: The Single Suite Executor required by the assignment. Generates HTML report.
- conftest.py: Centralized modular design handling browser Setup and Teardown.
  * Note: Fixture scope is set to "function" to ensure strict Setup -> Test -> Teardown 
    order for every single test case independently.
- test_01 to test_10: Individual test scripts mapped directly to Feature Requirements (FR01 - FR10).

------------------------------------------------------------
3. TECHNICAL ANNOTATIONS
------------------------------------------------------------
- Synchronization: Upgraded to use explicit Selenium waits (WebDriverWait) instead of static time.sleep() for optimal reliability.
- Reliability: Uses JavaScript Injection (execute_script) in specific instances to bypass aggressive dynamic overlays/ads that block standard Selenium clicks.
============================================================