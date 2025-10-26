# 🏥 Hospital Patient Management System (Streamlit + Queues)

This project is a **simple web-based Hospital Patient Management System** built using **Python and Streamlit**.  
It uses **Queues and Priority Queues** (from Python’s `queue` module) to simulate patient handling.

## 🎯 Features
- Admit patients with name, age, condition, and priority.
- Priority Queue for Critical/Serious cases.
- Normal Queue for FIFO handling.
- Treat next patient with one click.
- View current queues live on browser.

## 🚀 How to Run Locally
1. Install Python 3.8 or later.
2. Run:
   ```bash
   pip install streamlit
   streamlit run app.py
   ```

## 🌐 Deploy on Streamlit Cloud
1. Upload this folder to GitHub.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click “New App” and choose your GitHub repo.
4. Select `app.py` as main file.
5. Click “Deploy”.

Your app will be live at:
`https://your-username-hospital-pms.streamlit.app`
