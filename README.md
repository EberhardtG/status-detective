
# 🧪 Status Detective — HTTP Status Exploration with JSONPlaceholder  
A Python project that explores HTTP status codes using the JSONPlaceholder REST API.  
This script performs multiple API calls—including valid requests, nonexistent resources, deletion, invalid endpoints, and nested resources—and prints formatted status reports for each.

It also includes a reusable **`make_request()`** function that accepts any HTTP method and URL, performs the request safely, and returns a consistent, human‑readable status summary.

---

## 🚀 Features  
- **GET existing resource**  
- **GET nonexistent resource**  
- **DELETE existing resource**  
- **GET invalid endpoint**  
- **GET nested resource**  
- Centralized request handler (`make_request`)  
- Safe error handling using `try/except`  
- `timeout=10` to prevent hanging requests  
- `raise_for_status()` for professional error detection  
- Clean, formatted status output  

---

## 📁 Project Structure  
```
status_detective.py   # Main script performing all API tests
README.md             # Project documentation
```

---

## 🔧 Technologies Used  
- Python 3  
- requests library  
- JSONPlaceholder API  

---

## 📦 Installation  
Clone the repository:

```
git clone https://github.com/yourusername/status-detective.git
cd status-detective
```

Install dependencies:

```
pip install requests
```

Run the script:

```
python status_detective.py
```

---

## 🧠 How It Works  

### 1️⃣ GET `/posts/1` — Valid Resource  
Retrieves an existing post.  
Prints status code, reason, and a description confirming success.

### 2️⃣ GET `/posts/99999` — Nonexistent Resource  
Triggers a `404 Not Found`.  
Handled safely using `try/except` and prints a friendly explanation.

### 3️⃣ DELETE `/posts/1` — Successful Delete  
JSONPlaceholder simulates deletion and returns a success status.  
The script prints a confirmation message.

### 4️⃣ GET `/invalidendpoint` — Bad URI  
Demonstrates how invalid endpoints return `404`.  
Handled gracefully with descriptive output.

### 5️⃣ GET `/users/1/todos` — Nested Resource  
Retrieves all todos belonging to user 1.  
Shows how REST APIs expose hierarchical relationships.

### 6️⃣ Reusable Request Function  
The `make_request()` function accepts:

- HTTP method  
- URL  
- Optional JSON data  

It performs the request with:

- `timeout=10`  
- `raise_for_status()`  
- formatted status reporting  
- safe error handling  

This eliminates repeated code and mirrors real‑world API client design.

---

## 📝 Example Output  
Each request prints:

- HTTP method  
- URI  
- Status code  
- Reason phrase  
- Human‑readable description  

This makes the script ideal for learning how APIs behave under different conditions.

---

## 🎯 Learning Outcomes  
By completing this project, you gain experience with:

- REST API fundamentals  
- HTTP status codes  
- Defensive programming  
- Error handling with `raise_for_status()`  
- Timeouts and network reliability  
- Writing reusable API utilities  
- Understanding nested resources  
- Producing clean, consistent output  

---

## 📄 License  
This project is open‑source under the MIT License.

