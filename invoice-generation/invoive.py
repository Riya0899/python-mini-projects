import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Smart Invoice Dashboard", layout="wide")

# UI DESIGN
st.markdown("""
<style>
.stApp {
    background: black;
    color: white;
}
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# LOGIN
def load_users():
    return pd.read_csv("user.csv")

def login(u, p):
    users = load_users()
    return not users[(users["username"] == u) & (users["password"] == p)].empty

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(u, p):
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")
    st.stop()
    
st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

# HEADER
st.markdown("""
<div style="
    background: linear-gradient(135deg, #ff4b4b, #ff6b6b);
    padding: 25px;
    border-radius: 20px;
    text-align:center;
    color:white;
">
    <h1>🧾 Smart Invoice Dashboard</h1>
</div>
""", unsafe_allow_html=True)

# LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("r-data.csv")

    df["total"] = df["price"] * df["qty"]
    df["profit"] = df["total"] * 0.3

    if "date" not in df.columns:
        df["date"] = pd.date_range(start="2024-01-01", periods=len(df))

    df["date"] = pd.to_datetime(df["date"])
    df["day_name"] = df["date"].dt.day_name()

    return df

df = load_data()

# FILTERS
st.sidebar.header("🔍 Filters")

search = st.sidebar.text_input("Search Item")

category = st.sidebar.multiselect("Category", df["category"].unique(), df["category"].unique())
customer = st.sidebar.multiselect("Customer", df["customer"].unique(), df["customer"].unique())

price = st.sidebar.slider("Price", int(df.price.min()), int(df.price.max()),
                         (int(df.price.min()), int(df.price.max())))

rating = st.sidebar.slider("Rating", float(df.rating.min()), float(df.rating.max()),
                          (float(df.rating.min()), float(df.rating.max())))

qty = st.sidebar.slider("Quantity", int(df.qty.min()), int(df.qty.max()),
                       (int(df.qty.min()), int(df.qty.max())))

profit_range = st.sidebar.slider("Profit", int(df.profit.min()), int(df.profit.max()),
                                (int(df.profit.min()), int(df.profit.max())))

start_date, end_date = st.sidebar.date_input(
    "Date Range",
    [df["date"].min(), df["date"].max()]
)

# APPLY FILTERS
filtered = df[
    (df["category"].isin(category)) &
    (df["customer"].isin(customer)) &
    (df["price"].between(price[0], price[1])) &
    (df["rating"].between(rating[0], rating[1])) &
    (df["qty"].between(qty[0], qty[1])) &
    (df["profit"].between(profit_range[0], profit_range[1])) &
    (df["date"].between(pd.to_datetime(start_date), pd.to_datetime(end_date)))
]

if search:
    filtered = filtered[filtered["item"].str.contains(search, case=False)]

# NAVIGATION
page = st.radio("", ["Billing", "Analytics", "Customers"], horizontal=True)


# BILLING

if page == "Billing":

    st.subheader("🍽️ Menu")

    items_list = filtered["item"].unique()
    cart = []
    total = 0

    cols = st.columns(3)

    for i, item in enumerate(items_list):

        col = cols[i % 3]
        item_df = filtered[filtered["item"] == item]

        price = int(item_df["price"].mean())
        rating = float(item_df["rating"].mean())

        with col:
            st.markdown(f"""
            <div class="glass">
                <h3>🍴 {item}</h3>
                <p>💰 Price: ₹{price}</p>
                <p>⭐ Rating: {rating:.1f}</p>
            </div>
            """, unsafe_allow_html=True)

            qty = st.number_input(f"Qty ({item})", 0, 10, key=f"{item}")

            if qty > 0:
                amount = price * qty
                total += amount
                cart.append((item, qty, amount))

    st.markdown("---")

    if st.button("Generate Invoice"):

        if not cart:
            st.warning("Please select at least one item")
        else:
            st.success("✅ Invoice Generated Successfully")

            final = total * 0.9

            st.markdown('<div class="glass">', unsafe_allow_html=True)

            st.write(f"Invoice ID: {np.random.randint(1000,9999)}")
            st.write(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}")

            invoice_df = pd.DataFrame(cart, columns=["Item", "Qty", "Amount"])
            st.dataframe(invoice_df)

            st.write(f"Total: ₹{total}")
            st.success(f"Final (10% off): ₹{final}")

            st.markdown('</div>', unsafe_allow_html=True)
            # st.balloons()

            csv = invoice_df.to_csv(index=False).encode()  # converts string into bytes
            st.download_button("Download Invoice", csv, "invoice.csv")

# ANALYTICS

elif page == "Analytics":

    st.subheader("Analytics")

    total_revenue = filtered["total"].sum()
    total_orders = len(filtered)
    avg_rating = filtered["rating"].mean()
    total_profit = filtered["profit"].sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"""<div class="glass"><h4>💰 Revenue</h4><h2>₹{total_revenue:,.0f}</h2></div>""", unsafe_allow_html=True)
    col2.markdown(f"""<div class="glass"><h4>📦 Orders</h4><h2>{total_orders}</h2></div>""", unsafe_allow_html=True)
    col3.markdown(f"""<div class="glass"><h4>⭐ Rating</h4><h2>{avg_rating:.1f}</h2></div>""", unsafe_allow_html=True)
    col4.markdown(f"""<div class="glass"><h4>💸 Profit</h4><h2>₹{total_profit:,.0f}</h2></div>""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Daily Trend")
    st.line_chart(filtered.groupby("date")["total"].sum())

    st.markdown("### Category")
    st.bar_chart(filtered.groupby("category")["total"].sum())

    st.markdown("### Top Items")
    st.bar_chart(filtered.groupby("item")["total"].sum())

    st.markdown("### Customers")
    st.bar_chart(filtered.groupby("customer")["total"].sum())

    st.markdown("### Day-wise Sales")
    st.bar_chart(filtered.groupby("day_name")["total"].sum())

# CUSTOMERS

elif page == "Customers":

    st.subheader("Customer Insights")

    cust = filtered.groupby("customer")["total"].sum().reset_index()
    st.dataframe(cust)

# DOWNLOAD DATA
csv = filtered.to_csv(index=False).encode()
st.download_button("Download Data", csv, "filtered_data.csv")