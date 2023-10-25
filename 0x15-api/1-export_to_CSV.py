#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
from requests import get
from sys import argv

# Define a function to retrieve data from the API and export it to CSV
def export_todo_list_to_csv(employee_id):
    # Define the base URL of the REST API
    api_base_url = "https://jsonplaceholder.typicode.com/"

    # Make an API request to fetch employee information
    employee_info = get(api_base_url + "users/{}".format(employee_id)).json()

    # Make an API request to fetch the employee's TODO list
    todo_list = get(api_base_url + "todos?userId={}".format(employee_id)).json()

    # Open a CSV file for writing, using the employee_id as the filename
    with open("todo_list_{}.csv".format(employee_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the CSV file with relevant data
        for task in todo_list:
            csv_writer.writerow([employee_id, employee_info.get("username"),
                                  task.get("completed"),
                                  task.get("title")])


# Check if the script is run as the main program
if __name__ == "__main__":
    # Parse the command-line argument as the employee_id
    employee_id = int(argv[1])
    export_todo_list_to_csv(employee_id)
