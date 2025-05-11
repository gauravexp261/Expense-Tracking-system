# 💰 Expense Tracker App

A full-stack expense tracker built with:

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: MySQL

This app allows users to record daily expenses, categorize them, and view summaries in a clean and interactive UI.

---

## 📂 Project Structure

expense-tracking-system/
│
├── backend/                      # FastAPI backend
│   ├── main.py                   # API endpoints
│   ├── db_helper.py              # MySQL connection logic
│   └── requirements.txt          # Python packages for backend
│
├── frontend/                     # Streamlit frontend
│   ├── app.py                    # Streamlit app entry point
│   ├── edit_tab.py               # Expense editing/viewing
│   ├── add_tab.py                # Add new expenses
│   ├── summary_tab.py            # Expense summaries
│   ├── .streamlit/
│   │   └── secrets.toml          # API & DB secrets for Streamlit Cloud
│   └── requirements.txt          # Python packages for frontend
│
├── README.md                     # Project documentation
└── .gitignore      

---

## 🚀 Features

- ✅ Add daily expenses with amount, category, and notes
- 📅 View or delete expenses by date
- 📊 Get expense summary by category
- 🌐 API-first architecture using FastAPI
- 🧑‍💻 UI built with Streamlit (can run locally or on cloud)


⚙️ Run the FastAPI Backend Locally
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

▶️ Run the Streamlit Frontend Locally
cd frontend
pip install -r requirements.txt
streamlit run app.py
