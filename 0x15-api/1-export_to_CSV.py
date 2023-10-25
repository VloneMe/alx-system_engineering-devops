#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
from requests import get
from sys import argv

"""
A function to fetch data from the API and export it to a CSV file
"""
def api_to_csv(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(user_id)).json()
    tasks = get(url + "todos?userId={}".format(user_id)).json()

    """
    # Create a new CSV file with the user's ID as the filename
    """
    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        file_stream = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        """
        # Write the CSV header row
        """
        file_stream.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        """
        # Iterate through tasks and write each task's information to the CSV file
        """
        for task in tasks:
            file_stream.writerow([user_id, user.get("username"), task.get("completed"), task.get("title")])


if __name__ == "__main__":
    """
    # Extract the employee ID from the command-line arguments
        and call the 'api_to_csv' function """
    api_to_csv(int(argv[1]))
