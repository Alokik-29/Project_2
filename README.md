# 🧠 Text-to-SQL RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** powered chatbot that converts natural language questions into **SQL queries** and returns data-driven answers from a connected database.
Built using **LangChain**, **SQLCoder**, and **Gradio**, this project demonstrates how LLMs can automate structured data access without writing manual SQL queries.

---

## 🚀 Features

* 🔍 **Natural Language to SQL** – Converts user input into valid SQL queries.
* 🧩 **RAG Pipeline** – Uses retrieval techniques to enhance query understanding.
* 🗂️ **Dynamic Database Support** – Works with any uploaded SQLite database (e.g., Chinook).
* 💬 **Interactive Gradio Interface** – Simple UI for question-answering over your data.
* ⚙️ **Deployed on Hugging Face Spaces** for real-time interaction.

---

## 🏗️ Tech Stack

* **Python**
* **LangChain & LangChain-Community**
* **Transformers (SQLCoder Model)**
* **SQLAlchemy**
* **Gradio**
* **Hugging Face Hub**

---

## 📂 Project Structure

```
├── app.py                # Main Gradio application
├── requirements.txt       # Required dependencies
├── README.md              # Project documentation
└── (optional) database.db # User-uploaded SQLite database
```

---

## ⚙️ How It Works

1. The user uploads a **SQLite database file**.
2. Enters a natural language question like:

   > “Show me all customers who purchased more than 5 tracks.”
3. The LLM (SQLCoder) generates a **SQL query**.
4. The app executes the query and displays the **resulting table**.

---

## 💻 Demo

Try the live app here:
👉 [**Hugging Face Space – Text-to-SQL Chatbot**](https://huggingface.co/spaces/alokik29/Text-to-SQL-RAG)


---

## 📚 Example Queries

| User Question                         | Generated SQL                                           | Result                        |
| ------------------------------------- | ------------------------------------------------------- | ----------------------------- |
| “List top 5 selling artists”          | `SELECT Artist, COUNT(*) ...`                           | Returns artist names & counts |
| “How many customers are from Canada?” | `SELECT COUNT(*) FROM Customers WHERE Country='Canada'` | Returns 8                     |

---

## 🧩 Future Improvements

* Add context-aware query refinement
* Support for MySQL/PostgreSQL
* Integrate with an AI Agent for automatic data exploration

---

## 🧑‍💻 Author

**Alokik Gour**
B.Tech, NSUT | Machine Learning & Deep Learning Enthusiast

* 📘 [LinkedIn](www.linkedin.com/in/alokik29)

---

⭐ **If you like this project, don’t forget to star the repo!**
