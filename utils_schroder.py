"""
Module: utils_schroder_healthcare_analytics.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Justin Schroder

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
#Is the hospital considered excellent?/Is the emergency department open?
is_hospital_excellent: bool = True
is_emergency_department_open: bool = False

# Integer variable: Number of patients served
number_of_patients: int = 15000

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.7

# declare a list of strings
# List of strings: Healthcare departments 
departments: list = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics"]

# declare a list of numbers so we can illustrate statistics skills
# List of floats: Patient satisfaction scores (out of 5)
patient_satisfaction_scores: list = [4.8, 4.7, 4.9, 5.0, 4.6, 4.8]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Hospital Excellent:             {is_hospital_excellent}
Emergency Department Open:     {is_emergency_department_open}
Number of Patients:            {number_of_patients}
Departments:                   {departments}
Patient Satisfaction Scores:   {patient_satisfaction_scores}
Minimum Satisfaction Score:   {min_satisfaction}
Maximum Satisfaction Score:   {max_satisfaction}
Mean Satisfaction Score:      {mean_satisfaction:.2f}
Standard Deviation of Satisfaction Scores: {stdev_satisfaction:.2f}
---------------------------------------------------------
Delivering actionable insights to improve healthcare outcomes.
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.


