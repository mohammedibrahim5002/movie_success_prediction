# 🎬 Movie Box Office Prediction & Analytics System

A **Machine Learning + Data Analytics project** that predicts movie box office revenue and analyzes factors influencing movie success.

This project combines **predictive modeling, business analytics, and an interactive web application** to help understand how factors like **genre, IMDb score, runtime, awards, and cast popularity** impact movie performance.

The system provides **two key capabilities**:

• **Box Office Prediction Model** – Estimates expected movie revenue
• **Success Classification Model** – Predicts whether a movie will likely be successful

---

## Live Demo

Try the deployed app here:
https://movie-success-prediction-model.streamlit.app/

---

# 📊 Project Objectives

The main goals of this project are:

• Predict movie **box office revenue** using machine learning
• Classify movies as **Successful or Unsuccessful**
• Identify **key drivers of movie success**
• Build **data visualizations for decision making**
• Deploy a **professional web application**

---

# 🧠 Machine Learning Models

Two models were developed:

### 1️⃣ Box Office Prediction (Regression)

Predicts expected revenue for a movie.

**Model Used**

Random Forest Regressor

**Evaluation Metrics**

• R² Score
• Mean Absolute Error (MAE)
• Mean Squared Error (MSE)

---

### 2️⃣ Movie Success Classifier

Predicts whether a movie will be:

• Successful
• Unsuccessful

**Model Used**

Random Forest Classifier

**Evaluation Metrics**

• Precision
• Recall
• Accuracy
• F1 Score

---

# 📈 Features Used

The models use several movie characteristics:

| Feature        | Description                  |
| -------------- | ---------------------------- |
| Genre          | Type of movie                |
| Running Time   | Movie duration               |
| IMDb Score     | Audience rating              |
| Movie Age      | Years since release          |
| Total Awards   | Awards won by the movie      |
| Director Level | Director popularity level    |
| Cast Level     | Actor popularity level       |
| Success Label  | Whether movie performed well |

These features help the model capture **both creative and commercial factors**.

---

# 📊 Movie Analysis

Key insights include:

### Revenue Distribution

Shows how movie earnings are distributed across the industry.

### Genre Performance

Identifies the **most profitable genres**.

### Budget vs Revenue

Explores how production budget affects earnings.

### IMDb Score vs Revenue

Analyzes relationship between audience ratings and revenue.

### Success Probability by Genre

Highlights which genres have **higher chances of success**.

### Top Grossing Movies

Benchmarks industry blockbusters.

---

# 🖥 Interactive Web Application

An interactive **Streamlit web app** allows users to:

• Input movie characteristics
• Predict expected box office revenue
• Estimate success probability

Example inputs:

• Genre
• IMDb Score
• Total Awards
• Movie Age
• Director Level
• Cast Popularity

The application then generates **data-driven predictions**.

---

# 🛠 Tech Stack

### Programming

Python

### Data Analysis

Pandas
NumPy

### Machine Learning

Scikit-learn

### Visualization

Matplotlib
Seaborn

### Web Application

Streamlit

---

# 📂 Project Structure

```
MOVIE_SUCCESS_PREDICTION/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── box_office_prediction_model.pkl
│   └── success_prediction_model.pkl
│
├── data/
│   └── movies_data.csv
│
├── notebooks/
    ├── movie_analysis.ipynb
    └── success_prediction.ipynb
```

---

# 🚀 Running the Project Locally

### 1 Install dependencies

```
pip install -r requirements.txt
```

### 2 Run the web app

```
streamlit run app.py
```

The application will launch in your browser.

---

# 🌐 Deployment

The application can be deployed using:

• Streamlit Cloud
• Hugging Face Spaces
• Render

```

---

# 📊 Example Insights

Some key findings from the analysis:

• Most movies generate **under $100M revenue**
• A small number of **blockbusters dominate the industry**
• Certain genres consistently outperform others
• Higher IMDb ratings correlate with better revenue
• Budget increases potential earnings but increases risk

---

# 🔮 Future Improvements

Possible improvements to the project:

• Incorporate **NLP analysis of movie plots**
• Use **deep learning models for prediction**
• Integrate **real-time movie datasets**
• Add **interactive business dashboards**

---
