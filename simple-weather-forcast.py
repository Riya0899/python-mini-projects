import streamlit as st
import numpy as np

st.set_page_config(page_title="Weather Dashboard", layout="wide")


st.markdown("""
<style>

.main {
    background: skyblue;
}

/* Header */
.header {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Hero Card */
.hero {
    background: skyblue;
    color: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
     margin-bottom: 25px;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.6s;
    color:black;
    width:80%;
    margin:auto;
}

.card:hover {
    transform: translateY(-5px);
}

/* Forecast Cards */
.day-card {
    background: white;
    padding: 15px;
    border-radius: 14px;
    text-align: center;
    border: 1px solid #eee;
    color:black;
}

/* Small text */
.small {
    font-size: 13px;
    color: black;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">🌤️ Weather Dashboard</div>', unsafe_allow_html=True)


def generate_weather():
    temps = np.random.randint(20, 40, size=(3, 7))
    conditions_list = ["Clear", "Clouds", "Rain", "Thunderstorm"]
    conditions = np.random.choice(conditions_list, size=(3, 7))
    return temps, conditions

temps, conditions = generate_weather()
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def get_icon(c):
    return {"Clear":"☀️","Clouds":"☁️","Rain":"🌧️","Thunderstorm":"⛈️"}.get(c,"🌈")


avg_temp = int(np.mean(temps))
condition = conditions[-1][0]
icon = get_icon(condition)

st.markdown(f"""
<div class="hero">
    <h2>Current Weather</h2>
    <h1 style="font-size:60px;">{avg_temp}°C {icon}</h1>
    <p>{condition}</p>
</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

col1.markdown(f'<div class="card"><h3>Min</h3><h2>{np.min(temps)}°C</h2></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="card"><h3>Max</h3><h2>{np.max(temps)}°C</h2></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="card"><h3>Average</h3><h2>{np.mean(temps):.1f}°C</h2></div>', unsafe_allow_html=True)

st.subheader("7-Day Forecast")

cols = st.columns(7)

for i, col in enumerate(cols):
    temp = int(np.mean(temps[:, i]))
    icon = get_icon(conditions[-1][i])

    with col:
        st.markdown(f"""
        <div class="day-card">
            <div class="small">{days[i]}</div>
            <h2>{icon}</h2>
            <h4>{temp}°C</h4>
        </div>
        """, unsafe_allow_html=True)


st.subheader("Next Week Prediction")

forecast = np.mean(temps[-2:], axis=0)
cols = st.columns(7)

for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
        <div class="day-card">
            <div class="small">{days[i]}</div>
            <h4>{int(forecast[i])}°C</h4>
        </div>
        """, unsafe_allow_html=True)


c1, c2 = st.columns(2)

with c1:
    st.subheader("Temperature Trend")
    st.line_chart(temps.T)

with c2:
    st.subheader("Variation")
    st.line_chart(np.std(temps, axis=0))


if st.button("🔄 Refresh Data"):
    st.rerun()