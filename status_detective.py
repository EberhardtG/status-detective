# status_detective.py

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_status_category(status_code):
    if 200 <= status_code < 300:
        return "Success"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
    else:
        return "Other"


def get_description(status_code):
    descriptions = {
        200: "Request succeeded — resource returned",
        201: "Resource created successfully",
        404: "Resource not found",
    }
    return descriptions.get(status_code, "Status code description unavailable")


def status_report(method, endpoint, data=None):
    url = BASE_URL + endpoint

    if method.upper() == "GET":
        response = requests.get(url)

    elif method.upper() == "POST":
        response = requests.post(url, json=data)

    elif method.upper() == "DELETE":
        response = requests.delete(url)

    else:
        print(f"Unsupported method: {method}")
        return

    print(f"{method.upper()} {endpoint}")
    print(
        f"  Status: {response.status_code} "
        f"({get_status_category(response.status_code)})"
    )
    print(f"  Description: {get_description(response.status_code)}")
    print()


# Request 1
status_report("GET", "/posts/1")

# Request 2
status_report("GET", "/posts/99999")

# Request 3
status_report(
    "POST",
    "/posts",
    {
        "title": "Test Post",
        "body": "Assignment Submission",
        "userId": 1,
    },
)

# Request 4
status_report("DELETE", "/posts/1")

# Request 5
status_report("GET", "/invalidendpoint")

# Request 6
status_report("GET", "/users/1/todos")
