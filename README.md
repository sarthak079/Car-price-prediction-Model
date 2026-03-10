# Car Price Prediction Model
An end-to-end Machine Learning pipeline to predict vehicle market value using historical data.

## 🛠 Tech Stack
* **Language:** Python 3.9+
* **ML Framework:** Scikit-learn, Pandas, NumPy
* **API Framework:** FastAPI
* **Frontend/UI:** Streamlit
* **Infrastructure:** GitHub (Version Control)

## 🚀 Key Features
* **Predictive Analytics:** Implements a regression model to estimate car prices based on features like year, mileage, and fuel type.
* **RESTful API:** Developed a backend using **FastAPI** for seamless integration and model serving.
* **Interactive UI:** Built a real-time testing dashboard with **Streamlit** to demonstrate model inference.
* **Standardized Pipeline:** Includes modular scripts for model training, schema validation, and API deployment.

Quick Start
Install requirements:
pip install -r car-price-api/requirements.txt

Start the API:
uvicorn car-price-api.main:app --reload

Launch the Dashboard:
streamlit run car-price-api/streamlit_app.py

Bachend is deployes using Render and 
Frontend is deployed using Streamlit

project access: https://car-price-prediction-model-nab9kag6bqyyzidmwxvs6k.streamlit.app/
