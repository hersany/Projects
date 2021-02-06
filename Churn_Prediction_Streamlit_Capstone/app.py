import streamlit as st
import pandas as pd
import numpy as np
import pickle

html_temp = """
<div style="background-color:rgba(127, 90, 127, 0.3);padding:7px">
<h2 style="border:2px solid white;color:white;text-align:center;">Employee Churn Prediction Model</h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

model = pickle.load(open("model", "rb"))

satisfaction_level = st.slider("What is the satisfaction level of the employee?", 0.0, 1.0, step = 0.01)
last_evaluation = st.slider("What is the last evaluation of the employee?", 0.0, 1.0, step = 0.01)
number_project = st.slider("How many of projects assigned to the employee?", 0, 10, step = 1)
average_montly_hours = st.slider("How many hours in average the employee worked in a month?", 50, 350, step = 1)
time_spend_company = st.slider("How many years spent by the employee in the company?"
                               , 0, 15, step = 1)
Work_accident = st.selectbox("Is the employee has had a work accident?", ('Yes', 'No'))
promotion_last_5years = st.selectbox("Is the employee has had a promotion in the last 5 years?", ('Yes', 'No'))
departments = st.selectbox("Select the employee's working department/division.", ("sales", "technical", "support", "IT", "product_mng", "marketing", "RandD", "accounting", "hr", "management"))
salary = st.selectbox("Select salary level of the employee.", ("low", "medium", "high"))

my_dict = {
    "satisfaction_level": satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": number_project,
    "average_montly_hours": average_montly_hours,
    "time_spend_company": time_spend_company,
    "Work_accident": Work_accident,
    "promotion_last_5years": promotion_last_5years,
    "departments": departments,
    "salary":salary
    
}

df = pd.DataFrame.from_dict([my_dict])

df['salary'] = df['salary'].map({'low' : 0, 'medium' : 1, 'high' : 2})

df['Work_accident'] = df['Work_accident'].map({'No' : 0, 'Yes' : 1})

df['promotion_last_5years'] = df['promotion_last_5years'].map({'No' : 0, 'Yes' : 1})

columns = ['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident',
       'promotion_last_5years', 'departments_IT',
       'departments_RandD', 'salary', 'departments_accounting', 'departments_hr',
       'departments_management', 'departments_marketing',
       'departments_product_mng', 'departments_sales', 'departments_support',
       'departments_technical']

df2 = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

st.table(df)

pred = model.predict(df2)

st.warning(pred)

if pred[0] == 1.0:
    st.warning("Bad news! This employee will terminate the contract.")
else:
    st.success("Good news! This employee is happy with the company")



