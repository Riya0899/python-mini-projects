import streamlit as st
import numpy as np

st.title("🌦️ Weather Forecast System (NumPy Project)")


st.subheader("Enter Temperature Data (3 Weeks)")
temps = []
for i in range(3):
    row = st.text_input(f"Week {i+1} (7 values separated by space)", "")
    
    if row:
        values = list(map(float, row.split()))
        if len(values) == 7:
            temps.append(values)


if len(temps) == 3:
    temps = np.array(temps)

    st.write("### 📊 Temperature Matrix")
    st.write(temps)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

  
    st.subheader("📅 Weekly Average")
    weekly_avg = np.mean(temps, axis=1)
    for i, avg in enumerate(weekly_avg):
        st.write(f"Week {i+1}: {avg:.2f}°C")

  
    st.subheader("📆 Daily Average")
    daily_avg = np.mean(temps, axis=0)
    for d, val in zip(days, daily_avg):
        st.write(f"{d}: {val:.2f}°C")


    st.subheader("🌡️ Overall Stats")
    st.write(f"Min Temp: {np.min(temps)}°C")
    st.write(f"Max Temp: {np.max(temps)}°C")


    st.subheader("🔮 Next Week Forecast")
    last_2_weeks = temps[-2:]
    forecast = np.mean(last_2_weeks, axis=0)

    for d, val in zip(days, forecast):
        st.write(f"{d}: {val:.2f}°C")

    st.subheader("📉 Temperature Variation (Std Dev)")
    std_dev = np.std(temps, axis=0)

    for d, val in zip(days, std_dev):
        st.write(f"{d}: {val:.2f}")

else:
    st.warning("Please enter all 3 weeks correctly (7 values each).")