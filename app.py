import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="AI Movie Success Predictor",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------
# LOAD MODELS
# ---------------------------

box_model = joblib.load(r"C:\Users\DELL\OneDrive\Desktop\Movie_success_prediction\models\box_office_prediction_model.pkl")
success_model = joblib.load(r"C:\Users\DELL\OneDrive\Desktop\Movie_success_prediction\models\success_prediction_model.pkl")

# Replace with MAE from notebook
MAE = 25000000


# ---------------------------
# CUSTOM UI STYLE
# ---------------------------

st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.big-font {
    font-size:40px !important;
    font-weight:700;
}

.metric-card {
    background-color: #1e222a;
    padding: 25px;
    border-radius: 12px;
    text-align:center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}

.metric-title{
    font-size:18px;
    color:white;
}

.metric-value{
    font-size:32px;
    font-weight:700;
    color:#ff4b4b;
            
}

</style>
""", unsafe_allow_html=True)


# ---------------------------
# HEADER
# ---------------------------

st.markdown("<p class='big-font'>🎬 AI Movie Success Predictor</p>", unsafe_allow_html=True)

st.write(
"""
Predict **Box Office Revenue** and **Movie Success Probability**
using Machine Learning.
"""
)

st.divider()

# ---------------------------
# SIDEBAR INPUTS
# ---------------------------

st.sidebar.header("🎛 Movie Inputs")

genre = st.sidebar.selectbox(
    "Genre",
    ["Action","Comedy","Drama","Thriller","Romance","Horror"]
)

imdb_score = st.sidebar.slider(
    "Expected IMDb Score",
    1.0,10.0,7.0
)

running_time = st.sidebar.slider(
    "Running Time (minutes)",
    60,200,120
)

movie_age = st.sidebar.slider(
    "Movie Age (years)",
    0,20,1
)

total_awards = st.sidebar.slider(
    "Total Awards / Nominations",
    0,50,5
)

director_level = st.sidebar.selectbox(
    "Director Reputation",
    ["Beginner","Experienced","Elite"]
)

cast_level = st.sidebar.selectbox(
    "Cast Popularity",
    ["Unknown","Recognizable","A-List Stars"]
)

# ---------------------------
# LEVEL MAPPINGS
# ---------------------------

director_map = {
    "Beginner": 20000000,
    "Experienced": 100000000,
    "Elite": 300000000
}

cast_map = {
    "Unknown": 30000000,
    "Recognizable": 120000000,
    "A-List Stars": 350000000
}

director_avg = director_map[director_level]
actor_avg = cast_map[cast_level]

# ---------------------------
# PREDICT BUTTON
# ---------------------------

if st.sidebar.button("Predict Movie Performance"):

    # Prepare dataframe
    input_df = pd.DataFrame({

        "running_time":[float(running_time)],
        "genre":[genre],
        "imdb_score":[float(imdb_score)],
        "movie_age":[int(movie_age)],
        "total_awards":[int(total_awards)],
        "director_avg_box_office":[float(director_avg)],
        "actor_1_avg_box_office":[float(actor_avg)],
        "actor_2_avg_box_office":[float(actor_avg)],
        "actor_3_avg_box_office":[float(actor_avg)],
        "cast_popularity":[float(actor_avg)]

    })

    # ---------------------------
    # BOX OFFICE PREDICTION
    # ---------------------------

    revenue = box_model.predict(input_df)[0]

    lower = max(0, revenue - MAE)
    upper = revenue + MAE

    # ---------------------------
    # SUCCESS PREDICTION
    # ---------------------------

    success_prob = success_model.predict_proba(input_df)[0][1]

    success_label = "Likely Successful" if success_prob > 0.5 else "High Risk"


    # ---------------------------
    # DISPLAY RESULTS
    # ---------------------------

    st.header("Prediction Results")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">Predicted Box Office</div>
        <div class="metric-value">${revenue:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
        )

    with col2:
        st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">Revenue Range</div>
        <div class="metric-value">${lower:,.0f} - ${upper:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
        )

    with col3:
        st.markdown(
        f"""
        <div class="metric-card">
        <div class="metric-title">Success Probability</div>
        <div class="metric-value">{success_prob*100:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True
        )

    st.divider()

    st.subheader("Model Prediction")

    if success_prob > 0.5:
        st.success("This movie is likely to be successful 🎉")
    else:
        st.error("This movie has a higher risk of failing ⚠️")

    st.progress(float(success_prob))

# ---------------------------
# FOOTER
# ---------------------------

st.divider()

st.write(
"""
Built with **Machine Learning + Streamlit**

Features used in prediction:

• Genre  
• IMDb Score  
• Running Time  
• Awards  
• Director Reputation  
• Cast Popularity  
"""
)