#!/usr/bin/python3
"""
A script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

def get_employee_todo_list(employee_id):
    # Define the API URL
    base_url = 'https://jsonplaceholder.typicode.com'
    endpoint = f'/users/{employee_id}/todos'
    url = base_url + endpoint

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            todos = response.json()

            # Print the response to inspect its structure
            print("API Response:")
            print(todos)

            # You can then adapt your code based on the actual structure of the response.

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
