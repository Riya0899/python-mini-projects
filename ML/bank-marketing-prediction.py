import streamlit as st
import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib


st.set_page_config(page_title="Bank ML App", layout="wide")
st.title("Bank Marketing Prediction Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("bank.csv")
    return df

df = load_data()


features = [
    "age", "job", "marital", "education",
    "balance", "housing", "loan",
    "duration", "campaign"
]

target = "deposit"

missing = [col for col in features + [target] if col not in df.columns]
if missing:
    st.error(f"Missing columns in dataset: {missing}")
    st.stop()

df = df[features + [target]]


@st.cache_resource
def preprocess(df):
    df = df.copy()
    encoders = {}

    for col in df.select_dtypes(include="object").columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    X = df[features]
    y = df[target]

    return X, y, encoders

X, y, encoders = preprocess(df)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "KNN": KNeighborsClassifier()
}

page = st.sidebar.radio(
    "Navigation",
    ["Dataset Preview", "Data Analysis",
     "Model Training", "Prediction", "Model Comparison"]
)

if page == "Dataset Preview":

    st.subheader("Dataset Preview")
    st.dataframe(df.head(20), use_container_width=True)

    st.subheader("Dataset Info")
    st.write(df.describe())


elif page == "Data Analysis":
    st.subheader("Data Visualization")
    col1, col2 = st.columns(2)

    with col1:
        st.bar_chart(df["job"].value_counts())
        st.caption("Job Distribution")

    with col2:
        st.bar_chart(df["education"].value_counts())
        st.caption("Education Distribution")

    st.bar_chart(df["deposit"].value_counts())
    st.caption("Target Distribution")


elif page == "Model Training":

    st.subheader("Train Models")

    model_name = st.selectbox("Choose Model", list(models.keys()))

    use_scaled = model_name in ["Logistic Regression", "KNN"]

    X_tr = X_train_scaled if use_scaled else X_train

    if st.button("Train Model"):

        model = models[model_name]
        model.fit(X_tr, y_train)

        os.makedirs("models", exist_ok=True)
        joblib.dump((model, scaler if use_scaled else None),
                    f"models/{model_name}.pkl")

        st.success(f"{model_name} trained successfully!")

elif page == "Prediction":
    st.subheader(" Predict Customer Deposit")
    age = st.number_input("Age", 18, 100, 30)
    job = st.selectbox("Job", df["job"].unique())
    marital = st.selectbox("Marital", df["marital"].unique())
    education = st.selectbox("Education", df["education"].unique())
    balance = st.number_input("Balance", value=1000)
    housing = st.selectbox("Housing Loan", df["housing"].unique())
    loan = st.selectbox("Personal Loan", df["loan"].unique())
    duration = st.number_input("Duration", value=100)
    campaign = st.number_input("Campaign", value=1)
    model_choice = st.selectbox("Model", list(models.keys()))

    if st.button("Predict"):

        model_path = f"models/{model_choice}.pkl"

        if not os.path.exists(model_path):
            st.error("Please train model first!")
        else:

            model, saved_scaler = joblib.load(model_path)

            input_data = {
                "age": age,
                "job": encoders["job"].transform([job])[0],
                "marital": encoders["marital"].transform([marital])[0],
                "education": encoders["education"].transform([education])[0],
                "balance": balance,
                "housing": encoders["housing"].transform([housing])[0],
                "loan": encoders["loan"].transform([loan])[0],
                "duration": duration,
                "campaign": campaign
            }

            input_df = pd.DataFrame([input_data], columns=X.columns)

            use_scaled = model_choice in ["Logistic Regression", "KNN"]

            if use_scaled:
                input_df = saved_scaler.transform(input_df)

            prediction = model.predict(input_df)[0]

            if prediction == 1:
                st.success("Customer WILL open deposit")
            else:
                st.error("Customer will NOT open deposit")

elif page == "Model Comparison":

    st.subheader("Model Accuracy Comparison")

    results = []

    for name, model in models.items():

        use_scaled = name in ["Logistic Regression", "KNN"]

        X_tr = X_train_scaled if use_scaled else X_train

        model.fit(X_tr, y_train)
        preds = model.predict(X_test_scaled if use_scaled else X_test)

        acc = accuracy_score(y_test, preds)
        results.append((name, acc))

    results_df = pd.DataFrame(results, columns=["Model", "Accuracy"])

    st.dataframe(results_df)
    st.bar_chart(results_df.set_index("Model"))