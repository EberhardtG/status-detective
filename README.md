# 🧪 Status Detective — HTTP Status Code Exploration with JSONPlaceholder

A Python project that explores common HTTP status codes using the JSONPlaceholder REST API.

The script performs multiple API requests against valid and invalid endpoints, examines the returned status codes, categorizes the responses, and prints a formatted status report for each request. This project provides hands-on practice with REST APIs, HTTP methods, and understanding how web servers communicate success and failure to clients.

---

## 🚀 Features

- GET existing resource
- GET nonexistent resource
- POST new resource with valid data
- DELETE existing resource
- GET invalid endpoint
- GET nested resource
- Automatic HTTP status categorization
- Human-readable status descriptions
- Reusable request reporting function
- Clean, formatted console output

---

## 📁 Project Structure

```text
status_detective.py   # Main application
README.md             # Project documentation
```

---

## 🔧 Technologies Used

- Python 3
- requests
- JSONPlaceholder API

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/status-detective.git
cd status-detective
```

Install dependencies:

```bash
pip install requests
```

Run the program:

```bash
python status_detective.py
```

---

## 🧠 What the Program Tests

### 1. GET /posts/1

Retrieves a valid post from the API.

Expected Status:

```text
200 OK
```

Category:

```text
Success
```

---

### 2. GET /posts/99999

Attempts to retrieve a post that does not exist.

Expected Status:

```text
404 Not Found
```

Category:

```text
Client Error
```

---

### 3. POST /posts

Creates a new post using valid JSON data.

Example Data:

```json
{
  "title": "Test Post",
  "body": "Assignment Submission",
  "userId": 1
}
```

Expected Status:

```text
201 Created
```

Category:

```text
Success
```

---

### 4. DELETE /posts/1

Sends a DELETE request to remove a resource.

Expected Status:

```text
200 OK
```

Category:

```text
Success
```

---

### 5. GET /invalidendpoint

Attempts to access an endpoint that does not exist.

Expected Status:

```text
404 Not Found
```

Category:

```text
Client Error
```

---

### 6. GET /users/1/todos

Retrieves a nested resource showing todos associated with User 1.

Expected Status:

```text
200 OK
```

Category:

```text
Success
```

---

## 📊 Status Categories

The application automatically classifies status codes:

| Range | Category |
|---------|------------|
| 200-299 | Success |
| 400-499 | Client Error |
| 500-599 | Server Error |
| Other | Unknown/Other |

---

## 🔄 Reusable Status Report Function

The project includes a reusable function that accepts:

- HTTP Method
- Endpoint
- Optional JSON Data

The function:

- Sends the request
- Retrieves the returned status code
- Categorizes the response
- Generates a user-friendly description
- Prints a formatted report

This reduces duplicate code and follows good software development practices.

---

## 📝 Example Output

```text
GET /posts/1
  Status: 200 (Success)
  Description: Request succeeded — resource returned

GET /posts/99999
  Status: 404 (Client Error)
  Description: Resource not found

POST /posts
  Status: 201 (Success)
  Description: Resource created successfully
```

---

## 🎯 Learning Outcomes

Through this project, I gained experience with:

- REST API fundamentals
- HTTP request methods
  - GET
  - POST
  - DELETE
- HTTP status codes
- API testing and troubleshooting
- Python requests library
- Writing reusable functions
- Response validation
- Clean console output formatting

---

## 📚 API Resource

This project uses the free test API provided by JSONPlaceholder:

https://jsonplaceholder.typicode.com

---

## 📄 License

This project is provided for educational purposes as part of Python and API development coursework.
