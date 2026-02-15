============================================================
AUTOMATED GUI-BASED TESTING SUITE - ASSIGNMENT 2
============================================================
Student Name: Rakesh Reddy Karri
Date: February 15, 2026
System Under Test: https://automationexercise.com/
Tools: Python 3.13.1, Selenium, Pytest [cite: 96, 98]

------------------------------------------------------------
1. HOW TO RUN THE SUITE
------------------------------------------------------------
Prerequisites:
- Python 3.x and Chrome Browser installed[cite: 47, 48].
- Selenium and Pytest installed (pip install selenium pytest).

To run the entire suite automatically (Single Click): [cite: 29, 50]
    python3 main.py [cite: 152]

To run individual scripts:
    pytest test_01_homepage.py -v -s [cite: 190]

------------------------------------------------------------
2. PROJECT ARCHITECTURE & UNDERSTANDING
------------------------------------------------------------
- main.py: The Single Suite Executor required by the assignment[cite: 29].
- conftest.py: Centralized modular design handling browser Setup and Teardown[cite: 29, 216].
- test_01 to test_10: Individual test scripts mapped to the 10 requirements[cite: 50, 100].

------------------------------------------------------------
3. TECHNICAL ANNOTATIONS
------------------------------------------------------------
- Modularization: Follows architectural best practices by separating 
  logic from configuration[cite: 29, 219].
- Reliability: Uses JavaScript Injection (execute_script) to bypass 
  dynamic overlays and third-party ads[cite: 223].
- Credentials: Uses a dummy user for secure authentication testing[cite: 57, 122].
============================================================