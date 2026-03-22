# 🏙️ Dubai Property Price Predictor

> Predict residential property prices in Dubai using machine learning — live web app included.

[![Live Demo](https://img.shields.io/badge/Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://dubaipropertytrends.streamlit.app/)
[![Streamlit App Repo](https://img.shields.io/badge/Streamlit_App_Repo-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Harishdaga/DubaiPropertyTrendsStreamlit)

---

## 📌 Overview

This repository contains the **data analysis and model training** code for the Dubai Property Price Predictor project.

The Dubai real estate market is one of the fastest-growing in the world. This project analyses historical transaction data to identify key price drivers and builds a machine learning model to predict property prices based on location, size, and amenities.

---

## 📊 What's Inside

| File / Folder | Description |
|---|---|
| `notebook/dubai_data_analysis.ipynb` | Full EDA — data cleaning, visualisation, feature analysis |
| `notebook/data/` | Raw and processed dataset |
| `src/` | Pipeline modules (data ingestion, transformation, model training) |
| `app.py` | Flask app entry point |

---

## 🔍 Project Workflow

1. **Data Collection & Cleaning** — Dubai residential property transactions dataset; handled missing values, removed outliers, standardised columns
2. **Exploratory Data Analysis (EDA)** — Distribution of prices by area, property type, size, amenities and finishing quality
3. **Feature Engineering** — Price per sq ft, location encoding, 29 amenity binary features
4. **Modelling** — Tested Linear Regression, Random Forest, XGBoost; **Gradient Boosting gave best results: 87% R² accuracy**
5. **Deployment** — Interactive Streamlit web app deployed on Streamlit Cloud

---

## 🎯 Key Results

- **87% R² accuracy** on test data
- **34 features** including area, bedrooms, bathrooms, and 29 amenity attributes
- Top price drivers identified: **location, property size, finishing quality, amenities**

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189AB4?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

---

## 🚀 Live App

The deployed Streamlit app lets users select property details and instantly see **AED + USD price estimates**.

👉 **[dubaipropertytrends.streamlit.app](https://dubaipropertytrends.streamlit.app/)**

The app code lives in a separate repo: [DubaiPropertyTrendsStreamlit](https://github.com/Harishdaga/DubaiPropertyTrendsStreamlit)

---

## 👤 Author

**Harish Daga** — Data Analyst
[harish.cv](https://harish.cv) · [LinkedIn](https://linkedin.com/in/harishdaga)
