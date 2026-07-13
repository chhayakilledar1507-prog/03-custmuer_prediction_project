import streamlit as st
import pandas as pd
import pickle


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD MODEL ----------------

with open("customer_churn_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- PREMIUM CSS ----------------

st.markdown("""
<style>

/* Background */

.stApp{
    background:linear-gradient(135deg,#eef4ff,#dbeafe,#f8fbff);
}

/* Main Container */

.block-container{
    background:white;
    padding:2rem;
    border-radius:20px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.12);
}

/* Hide Streamlit Menu */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Headings */

h1{
    color:white;
    text-align:center;
    font-weight:bold;
}

h2,h3{
    color:#0d6efd;
}

/* Input Labels */

label{
    font-weight:600;
}

/* Button */

.stButton>button{

    width:100%;
    height:55px;

    background:linear-gradient(90deg,#0d6efd,#00b4ff);

    color:white;

    border:none;

    border-radius:15px;

    font-size:20px;

    font-weight:bold;

    transition:.3s;

}

.stButton>button:hover{

    transform:scale(1.02);

    box-shadow:0 8px 20px rgba(0,123,255,.4);

}

/* Metric Cards */

div[data-testid="metric-container"]{

    background:white;

    border:1px solid #d9e7ff;

    border-radius:15px;

    padding:15px;

    box-shadow:0 5px 15px rgba(0,0,0,.08);

}

/* Success */

div[data-testid="stSuccess"]{

    border-radius:15px;

}

/* Error */

div[data-testid="stError"]{

    border-radius:15px;

}

/* Info */

div[data-testid="stInfo"]{

    border-radius:15px;

}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""

<div style="
background:linear-gradient(90deg,#0d6efd,#00b4ff);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:25px;
">

<h1>📊 Customer Churn Prediction System</h1>

<h4>
Machine Learning Based Customer Retention Analysis
</h4>

</div>

""", unsafe_allow_html=True)

st.info("Fill all customer details and click **Predict Customer Churn**.")

st.markdown("---")

st.subheader("📝 Customer Information")
# ---------------- CUSTOMER INPUTS ----------------

col1, col2 = st.columns(2)

with col1:

    gender = st.radio(
        "👤 Gender",
        ["Male", "Female"],
        horizontal=True
    )

with col2:

    senior = st.radio(
        "🧓 Senior Citizen",
        [0,1],
        horizontal=True
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    partner = st.radio(
        "💍 Partner",
        ["Yes","No"],
        horizontal=True
    )

with col2:

    dependents = st.radio(
        "👨‍👩‍👧 Dependents",
        ["Yes","No"],
        horizontal=True
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    tenure = st.slider(
        "📅 Tenure (Months)",
        0,
        72,
        12
    )

with col2:

    phone_service = st.radio(
        "📞 Phone Service",
        ["Yes","No"],
        horizontal=True
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    multiple_lines = st.selectbox(
        "☎ Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
        ]
    )

with col2:

    internet_service = st.selectbox(
        "🌐 Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    online_security = st.selectbox(
        "🔒 Online Security",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

with col2:

    online_backup = st.selectbox(
        "💾 Online Backup",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    device_protection = st.selectbox(
        "🛡 Device Protection",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

with col2:

    tech_support = st.selectbox(
        "🛠 Tech Support",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    streaming_tv = st.selectbox(
        "📺 Streaming TV",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

with col2:

    streaming_movies = st.selectbox(
        "🎬 Streaming Movies",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    contract = st.selectbox(
        "📄 Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

with col2:

    paperless = st.radio(
        "🧾 Paperless Billing",
        [
            "Yes",
            "No"
        ],
        horizontal=True
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    payment = st.selectbox(
        "💳 Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col2:

    monthly = st.number_input(
        "💰 Monthly Charges",
        min_value=0.0,
        value=50.0,
        step=1.0
    )

# ------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    total = st.number_input(
        "💵 Total Charges",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

with col2:

    st.markdown("<br><br>", unsafe_allow_html=True)

    predict = st.button(
        "🚀 Predict Customer Churn",
        use_container_width=True
    )

st.markdown("---")
# ---------------- PREDICTION ----------------

if predict:

    input_data = pd.DataFrame({

        "gender":[gender],
        "SeniorCitizen":[senior],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[phone_service],
        "MultipleLines":[multiple_lines],
        "InternetService":[internet_service],
        "OnlineSecurity":[online_security],
        "OnlineBackup":[online_backup],
        "DeviceProtection":[device_protection],
        "TechSupport":[tech_support],
        "StreamingTV":[streaming_tv],
        "StreamingMovies":[streaming_movies],
        "Contract":[contract],
        "PaperlessBilling":[paperless],
        "PaymentMethod":[payment],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]

    })

    with st.spinner("🔄 Predicting Customer Churn..."):
         prediction = model.predict(input_data)
       

    st.markdown("---")

    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:

        st.error("⚠️ Customer is likely to Churn")

        st.warning("### 💡 Recommendation")
        st.write("""
✔ Offer attractive discounts
✔ Contact customer personally
✔ Improve customer support
✔ Provide better subscription plans
✔ Give loyalty rewards
""")

    else:

        st.success("✅ Customer is likely to Stay")
        st.balloons()

        st.success("### 🎉 Recommendation")
        st.write("""
✔ Customer is satisfied
✔ Maintain current service quality
✔ Continue loyalty benefits
✔ Offer premium plans
✔ Keep regular communication
""")


    report = pd.DataFrame({
        "Prediction": [
            "Stay" if prediction[0] == 0 else "Churn"
        ]
    })

    st.download_button(
        "📥 Download Prediction Report",
        report.to_csv(index=False),
        "prediction_report.csv",
        "text/csv"
    )
# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""

<div style='text-align:center;'>

<h3 style='color:#0d6efd;'>
📊 Customer Churn Prediction System
</h3>

<p>
Machine Learning Project using Logistic Regression
</p>

<p>
Developed with ❤️ by <b>Chhaya Killedar</b>
</p>

</div>

""", unsafe_allow_html=True)
