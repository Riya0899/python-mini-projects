import streamlit as st 
import pandas as pd
import numpy as np

st.set_page_config(page_title="Invoice Management System", layout="wide")

st.title("🧾 INVOICE MANAGEMENT SYSTEM")
st.write("---")

# load data
@st.cache_data
def load_data():
    invoice_df = pd.read_csv("r-data.csv")
    invoice_df["total"] = invoice_df["price"] * invoice_df["qty"]
    return invoice_df

invoice_df = load_data()

# filters
st.sidebar.header("🔍CHOOSE YOUR OPTIONS")

category_filter = st.sidebar.multiselect(
    "category",invoice_df["category"].unique(),default=invoice_df["category"].unique())

item_filter = st.sidebar.multiselect("Items",invoice_df["item"].unique(), default=list(invoice_df["item"].unique()))

price_range = st.sidebar.slider(
    "Price Range",
    int(invoice_df["price"].min()),
    int(invoice_df["price"].max()),
    (int(invoice_df["price"].min()), int(invoice_df["price"].max())))

filtered = invoice_df[
    invoice_df["category"].isin(category_filter) &
    invoice_df["item"].isin(item_filter) &
    (invoice_df["price"] >= price_range[0]) &
    (invoice_df["price"] <= price_range[1])]

# navigation
page = st.radio("NAVIGATIONS",["🧾 Billing", "📦 Orders", "📊 Analytics", "👥 Customers"],horizontal=True)
st.markdown("---")
# billing
if page == "🧾 Billing":

    st.subheader("INVOICE GENERATION")
    items = st.multiselect("Select Items", filtered['item'].unique())
    total = 0
    cart = []
    for i in items:
        price = filtered[filtered["item"] == i]["price"].mean()
        qty = st.number_input(i, 1, 10, 1, key=i)
        value = price * qty
        total += value
        cart.append((i, qty, value))
    if st.button("Generate Invoice"):
        if len(cart) == 0:
            st.warning("Please select items first")
        else:
            st.success("Invoice Generated")
            # invoive generation
            st.subheader("🧾 Invoice Receipt")

            cols = st.columns([3, 1, 2])
            cols[0].write("**Item**")
            cols[1].write("**Qty**")
            cols[2].write("**Amount**")

            st.markdown("---")

            for item, qty, value in cart:
                cols = st.columns([3, 1, 2])
                cols[0].write(item)
                cols[1].write(qty)
                cols[2].write(f"₹{value:.0f}")

            st.markdown("---")

            # discount
            discount = 0.10 if total > 1000 else 0.05
            final = total - total * discount

            cols = st.columns([3, 2])
            cols[0].write("**Subtotal**")
            cols[1].write(f"{total:.0f}")

            cols = st.columns([3, 2])
            cols[0].write("**Discount**")
            cols[1].write(f"{int(discount*100)}%")

            cols = st.columns([3, 2])
            cols[0].write("## PAYMENT")
            cols[1].success(f"₹{final:.0f}")

# download
            invoice_df_dl = pd.DataFrame(cart, columns=["Item", "Qty", "Amount"])

            summary_df = pd.DataFrame({
                "Item": ["", "Subtotal", "Discount %", "Total Payable"],
                "Qty": ["", "", "", ""],
                "Amount": ["", total, f"{int(discount*100)}%", final]})
            
            final_invoice = pd.concat([invoice_df_dl, summary_df], ignore_index=True)
            st.download_button(label="📥 Download Invoice",data=final_invoice.to_csv(index=False),file_name="invoice.csv",mime="text/csv")

# orders
elif page == "📦 Orders":
    st.subheader("Order Overview")
    orders = filtered.groupby("item").agg({
        "qty": "sum",
        "total": "sum",
        "rating": "mean"
    }).reset_index()
    st.dataframe(orders, use_container_width=True)
    
# analytics
elif page=="📊 Analytics":
    st.subheader("Analytical Dashboard")
    vals = filtered["total"].values
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Avg Order", f"₹{np.mean(vals):.0f}")
    c2.metric("Max Order", f"₹{np.max(vals):.0f}")
    c3.metric("Min Order", f"₹{np.min(vals):.0f}")
    c4.metric("Revenue", f"₹{np.sum(vals):,.0f}")
    
    st.markdown("### 📈 Revenue Trend")
    st.line_chart(filtered.groupby("day")["total"].sum())

    st.markdown("### 🏆 Top Items")
    st.bar_chart(filtered.groupby("item")["total"].sum())

    st.markdown("### 🍽️ Category Performance")
    st.bar_chart(filtered.groupby("category")["total"].sum())

# customers
elif page=="👥 Customers":
    st.subheader("Customer Insights")
    cust = filtered.groupby("customer").agg({
        "total": "sum",
        "qty": "sum",
        "rating": "mean"
    }).reset_index()

    spend = cust["total"].values
    cust["segment"] = np.where(
        spend > np.percentile(spend, 75), "High Value",
        np.where(spend < np.percentile(spend, 25), "Low Value", "Mid Value"))
    st.dataframe(cust, use_container_width=True)