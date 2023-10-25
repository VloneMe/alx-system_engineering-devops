#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
from requests import get
from sys import argv


def get_data_api(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(user_id)).json()
    tasks = get(url + "todos?userId={}".format(user_id)).json()

    # Create a CSV file with the user's ID as the filename
    filename = "{}.csv".format(user_id)
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row to the CSV file
        csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                )

        for task in tasks:
            # Extract task information
            task_id = task.get("id")
            task_title = task.get("title")
            task_completed = task.get("completed")

            # Write task information to the CSV file
            csv_writer.writerow(
                    [user_id, user["name"], task_completed, task_title]
                    )

    print("Data exported to {}.csv".format(user_id))


if __name__ == "__main__":
    user_id = int(argv[1])
    get_data_api(user_id)
