import sqlite3
import pandas as pd
import gradio as gr
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# ============================================================
# 🚀 Load SQLCoder model
# ============================================================
model_id = "defog/sqlcoder-7b-2"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto"
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    do_sample=False
)

sqlcoder_llm = HuggingFacePipeline(pipeline=pipe)

# ============================================================
# 🧠 Define query function
# ============================================================
def ask_question(user_db, question):
    """Takes an uploaded SQLite database + a question, returns SQL + result"""
    if not user_db:
        return "❌ Please upload a database file.", None

    conn = sqlite3.connect(user_db.name)
    cursor = conn.cursor()

    # Create a Text-to-SQL prompt
    prompt = f"Translate this question into an SQLite query:\nQuestion: {question}\nSQL:"
    sql_query = sqlcoder_llm(prompt)

    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=columns)
        conn.close()
        return sql_query, df
    except Exception as e:
        conn.close()
        return f"❌ Error executing query: {e}", None

# ============================================================
# 🎨 Gradio UI
# ============================================================
demo = gr.Interface(
    fn=ask_question,
    inputs=[
        gr.File(label="Upload SQLite Database (.db)"),
        gr.Textbox(label="Ask your question")
    ],
    outputs=[
        gr.Textbox(label="Generated SQL Query"),
        gr.Dataframe(label="Query Result")
    ],
    title="🧠 Text-to-SQL on Your Own Database",
    description="Upload your SQLite database and ask natural language questions."
)

if __name__ == "__main__":
    demo.launch()
