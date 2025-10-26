import streamlit as st
import queue

# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="Hospital PMS", page_icon="🏥", layout="wide")

st.title("🏥 Hospital Patient Management System")
st.markdown("""
This application manages hospital patients using **Queues and Priority Queues**.  
- Critical and Serious patients go into a **Priority Queue (treated first)**  
- Normal patients go into a **Normal Queue (FIFO order)**  
""")

# ---------- INITIALIZE QUEUES ----------
if "priority_queue" not in st.session_state:
    st.session_state.priority_queue = queue.PriorityQueue()
if "normal_queue" not in st.session_state:
    st.session_state.normal_queue = queue.Queue()

# ---------- ADMIT PATIENT ----------
st.divider()
st.subheader("➕ Admit New Patient")

with st.form("admit_form"):
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0)
    condition = st.text_area("Condition / Symptoms")
    priority = st.radio(
        "Select Priority",
        (1, 2, 3),
        format_func=lambda x: {1: "Critical", 2: "Serious", 3: "Normal"}[x]
    )
    submitted = st.form_submit_button("Admit Patient")

    if submitted:
        if not name or not condition:
            st.warning("⚠️ Please fill all required fields.")
        else:
            patient = (priority, f"{name} | Age: {age} | Condition: {condition} | Priority: {priority}")
            if priority == 3:
                st.session_state.normal_queue.put(patient)
            else:
                st.session_state.priority_queue.put(patient)
            st.success(f"✅ Patient **{name}** admitted successfully!")

# ---------- TREAT PATIENT ----------
st.divider()
st.subheader("🩹 Treat Next Patient")

if st.button("Treat Patient"):
    if not st.session_state.priority_queue.empty():
        patient = st.session_state.priority_queue.get()[1]
        st.info(f"👨‍⚕️ Treating **Priority Patient**:\n\n{patient}")
    elif not st.session_state.normal_queue.empty():
        patient = st.session_state.normal_queue.get()[1]
        st.info(f"👩‍⚕️ Treating **Normal Patient**:\n\n{patient}")
    else:
        st.warning("No patients are waiting in the queue!")

# ---------- DISPLAY QUEUES ----------
st.divider()
st.subheader("📋 Current Patient Queues")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧾 Priority Queue (Critical / Serious)")
    if st.session_state.priority_queue.empty():
        st.write("No priority patients.")
    else:
        for p in list(st.session_state.priority_queue.queue):
            st.write("•", p[1])

with col2:
    st.markdown("### 🧾 Normal Queue")
    if st.session_state.normal_queue.empty():
        st.write("No normal patients.")
    else:
        for p in list(st.session_state.normal_queue.queue):
            st.write("•", p[1])

st.divider()
st.caption("Developed by Aryan Singh — Data Structures Internal Assessment Project")
