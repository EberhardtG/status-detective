import requests

#GET /posts/1 - should succeed

response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
response.raise_for_status()
print(f"GET existing post:  {response.status_code} ({response.reason}) Description: Request succeeded — resource returned")

#GET /posts/99999 - nonexistent resource
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/99999",
        timeout=10
    )
    response.raise_for_status()
    print(f"GET nonexistent: {response.status_code} ({response.reason})")
    

except requests.exceptions.HTTPError as e:
    print(f"GET nonexistent: 404 Not Found — resource does not exist")
    print("Description:  Nonexistent resource- should return 404 request")
# raise_for_status() throws an HTTPError for 4xx/5xx responses.
# This is expected for nonexistent resources (404). Wrapping the call
# in try/except allows the script to continue and print a friendly message.


#DELETE /posts/1 - should succeed

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1", timeout=10)

print(f"DELETE /posts/1")
response.raise_for_status()
print(f"Status: {response.status_code} ({response.reason})")
print("Deleted post 1 successfully (JSONPlaceholder simulates deletion).")
print("Description:  deletes post- should return successful message")

#GET /invalidendpoint - bad URI
try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalidendpoint", timeout=10)
    response.raise_for_status()
    print(f"GET bad endpoint:   {response.status_code} ({response.reason})")
    
except requests.exceptions.HTTPError as e:
    print(f"GET nonexistent: 404 Not Found — resource does not exist")
    print("Description:  bad URI- should return 404 request")


#GET /users/1/todos - nested resource
#GET /users/1/todos - nested resource
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos", timeout=10)
    response.raise_for_status()
    print(f"GET /users/1/todos: {response.status_code} ({response.reason})")
    print("Description: Request succeeded — returned todos for user 1")

except requests.exceptions.HTTPError:
    print("GET /users/1/todos: Request failed — could not retrieve nested resource")



import requests

def make_request(method, url, data=None):
    """
    Sends an HTTP request using the given method and URL.
    Returns a formatted status report string.
    """

    try:
        if method == "GET":
            response = requests.get(url, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=10)
        elif method == "PATCH":
            response = requests.patch(url, json=data, timeout=10)
        elif method == "PUT":
            response = requests.put(url, json=data, timeout=10)
        elif method == "DELETE":
            response = requests.delete(url, timeout=10)
        else:
            return f"{method} {url}\nDescription: Unsupported HTTP method"

        response.raise_for_status()

        return (
            f"{method} {url}\n"
            f"Status: {response.status_code} ({response.reason})\n"
            f"Description: Request succeeded"
        )

    except requests.exceptions.HTTPError:
        return (
            f"{method} {url}\n"
            f"Status: {response.status_code} ({response.reason})\n"
            f"Description: Request failed — {response.reason}"
        )

    except requests.exceptions.RequestException as e:
        return (
            f"{method} {url}\n"
            f"Description: Request error — {str(e)}"
        )


#why:
# The make_request() function centralizes all HTTP logic into one reusable place.
# Instead of writing separate GET/POST/DELETE blocks, the function handles:
#   - timeout enforcement
#   - raise_for_status() error detection
#   - method selection
#   - formatted status reporting
# This reduces duplication, improves readability, and ensures consistent behavior
# across all API calls.

#design:
# The function accepts a method and URL so it can perform ANY request the assignment
# requires. Using try/except ensures the script never crashes on 404 or network
# errors. Returning formatted strings keeps output consistent and easy to read.
# This design mirrors real-world API client utilities.


# ---------------------------------------------------------
# Now use the function for all required assignment requests
# ---------------------------------------------------------

print(make_request("GET", "https://jsonplaceholder.typicode.com/posts/1"))
print()

print(make_request("GET", "https://jsonplaceholder.typicode.com/posts/99999"))
print()

print(make_request("DELETE", "https://jsonplaceholder.typicode.com/posts/1"))
print()

print(make_request("GET", "https://jsonplaceholder.typicode.com/invalidendpoint"))
print()

print(make_request("GET", "https://jsonplaceholder.typicode.com/users/1/todos"))
print()
