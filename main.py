import streamlit as st

st.set_page_config(page_title="Universal Unit Converter", layout="centered")

st.title("🔄 Universal Unit Converter")

# Categories
category = st.selectbox("Select a category:", ["Length", "Weight", "Temperature", "Time"])

# Conversion options based on category
conversion_options = {
    "Length": {
        "Meters to Kilometers": lambda x: x / 1000,
        "Kilometers to Meters": lambda x: x * 1000,
        "Centimeters to Meters": lambda x: x / 100,
        "Meters to Centimeters": lambda x: x * 100,
        "Inches to Feet": lambda x: x / 12,
        "Feet to Inches": lambda x: x * 12,
        "Meters to Feet": lambda x: x * 3.28084,
        "Feet to Meters": lambda x: x / 3.28084
    },
    "Weight": {
        "Kilograms to Grams": lambda x: x * 1000,
        "Grams to Kilograms": lambda x: x / 1000,
        "Pounds to Kilograms": lambda x: x * 0.453592,
        "Kilograms to Pounds": lambda x: x / 0.453592
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9,
        "Celsius to Kelvin": lambda x: x + 273.15,
        "Kelvin to Celsius": lambda x: x - 273.15
    },
    "Time": {
        "Minutes to Hours": lambda x: x / 60,
        "Hours to Minutes": lambda x: x * 60,
        "Seconds to Minutes": lambda x: x / 60,
        "Minutes to Seconds": lambda x: x * 60
    }
}

# Get conversion list for the chosen category
conversion_list = list(conversion_options[category].keys())
conversion_type = st.selectbox(f"Select {category} conversion:", conversion_list)

# Input value
value = st.number_input("Enter value to convert:", step=0.1)

# Convert button
if st.button("Convert"):
    result = conversion_options[category][conversion_type](value)
    st.success(f"✅ Result: {value} → {round(result, 4)} ({conversion_type})")
