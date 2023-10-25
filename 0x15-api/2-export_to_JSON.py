#!/usr/bin/python3
# This script uses a REST API to fetch information about an employee's TODO list progress
# and exports the data in JSON format.

# Import necessary libraries
import json
from requests import get
from sys import argv

# Define a function to fetch data from the REST API and export it as JSON
def fetch_and_export_todo_data(employee_id):
    # Create an empty list to store task information
    todo_list = []
    
    # Define the base URL for the JSONPlaceholder API
    api_base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch employee information using the provided employee_id
    employee_data = get(api_base_url + "users/{}".format(employee_id)).json()
    
    # Fetch TODO tasks associated with the employee
    tasks = get(api_base_url + "todos?userId={}".format(employee_id)).json()
    
    # Iterate through the tasks and create dictionaries for each task
    for task in tasks:
        task_info = {}
        task_info["task"] = task.get("title")
        task_info["completed"] = task.get("completed")
        task_info["employee_username"] = employee_data.get("username")
        todo_list.append(task_info)
    
    # Open a JSON file with the employee_id as the filename and write the data
    with open("{}.json".format(employee_id), 'w', newline='') as json_file:
        json.dump({argv[1]: todo_list}, json_file)

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the fetch_and_export_todo_data function with the employee ID provided as a command-line argument
    fetch_and_export_todo_data(int(argv[1]))
