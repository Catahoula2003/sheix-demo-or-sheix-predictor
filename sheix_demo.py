
import streamlit as st

st.set_page_config(page_title="SheiX Prediction Demo", layout="centered")

st.title("🔮 SheiX Curve Prediction")
st.subheader("Predict the 10-point total using only 7 values")

st.markdown("""
Enter your 7 initial values from a sequence (e.g., stock prices, indicators).
The SheiX algorithm uses a deterministic scalar to predict the total of all 10 values.
""")

inputs = []
for i in range(1, 8):
    value = st.number_input(f"Value A{i}", key=f"A{i}", value=0.0)
    inputs.append(value)

if st.button("Predict Total"):
    A7 = inputs[6]
    scalar = 2.6144
    prediction = round(A7 * scalar, 4)
    error_margin = round(prediction * 0.003, 4)

    st.success(f"🎯 Predicted Total (A1–A10): {prediction}")
    st.info(f"🧪 Estimated Accuracy Range: ±{error_margin}")

st.markdown("""
---
**Invented by Jarod William McKelvey**  
SheiX™ and Sheispot™ are proprietary predictive models.  
© 2025 — All rights reserved.
""")
