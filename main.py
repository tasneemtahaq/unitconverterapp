import streamlit as st

# Unit conversion dictionary
conversion_rates = {
    "Meters to Kilometers": 0.001,
    "Kilometers to Meters": 1000,
    "Centimeters to Meters": 0.01,
    "Meters to Centimeters": 100,
    "Inches to Feet": 1 / 12,
    "Feet to Inches": 12,
    "Meters to Feet": 3.28084,
    "Feet to Meters": 0.3048,
}

# Streamlit app
st.title("🔄 Simple Unit Converter")

# Input section
conversion_type = st.selectbox("Choose conversion type:", list(conversion_rates.keys()))
value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1)

# Convert button
if st.button("Convert"):
    result = value * conversion_rates[conversion_type]
    st.success(f"✅ Result: {value} → {round(result, 4)} ({conversion_type})")
