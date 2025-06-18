
import streamlit as st

st.title("Sheispot Health Check App")
st.markdown("### A Demo App for Patient Assessment using Sheispot + SheiX Logic")

# Patient Information
st.header("🧍 Patient Info")
name = st.text_input("Patient Name")
age = st.number_input("Patient Age", min_value=0, max_value=120, value=30)
patient_id = st.text_input("Patient ID")

# Initial Measurements Input
st.header("📏 Input Initial Measurements")
m1 = st.number_input("Measurement 1 (e.g., blood pressure systolic)", value=120)
m2 = st.number_input("Measurement 2 (e.g., blood pressure diastolic)", value=80)

# Generate Sequence like Sheispot Pattern
def sheispot_sequence(a, b):
    seq = [a, b]
    for _ in range(5):
        seq.append(seq[-1] + seq[-2])
    return seq

sequence = sheispot_sequence(m1, m2)
measured_7th = st.number_input("Measured 7th Value (real-world reading)", value=sequence[6])
predicted_total = measured_7th * 11

# Display Output
st.header("📊 Result")
st.write(f"Sequence Generated: {sequence}")
st.write(f"Predicted Total (7th × 11): **{predicted_total}**")
