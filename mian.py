import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder


# features = ['Location', 'Category', 'Type', 'MPrice', 'Month', 'day']
model = joblib.load('lin_final.pkl')
le = LabelEncoder()

Location = st.text_input('Местоположение (Eng) (Library, university и т.д.)')
Category = st.text_input('Категория преобладающего товара (Eng) (Food, carbonated и т.д.)')
Type = st.text_input('Тип оплаты (Eng) (Credit, cash)')
MPrice = st.text_input('Средняя цена товара (Например, 3.5)')

if MPrice != "":
    MPrice = float(MPrice)

Month = st.text_input('Месяц (№)')
if Month != "":
    Month = int(Month)

Day = st.text_input('День (№)')
if Day != "":
    Day = int(Day)


if Location != "" and Category != "" and Type != "" and MPrice != "" and Month != "" and Day != "":
    data = pd.DataFrame({'Location': [Location], 'Category': [Category],
                         'Type': Type, 'MPrice': MPrice, 'Month': Month,
                         'day': Day})

    data['Location'] = le.fit_transform(data['Location'])
    data['Category'] = le.fit_transform(data['Category'])
    data['Type'] = le.fit_transform(data['Type'])

medium_count = st.text_input('Средний поток посетителей за день: ')
if medium_count != "":
    medium_count = int(medium_count)

metrics = [Location, Category, MPrice, Type, Month, Day, medium_count]
conds = [cond != "" for cond in metrics]


if all(conds):
    st.write(data)
    pred = model.predict(data)

if medium_count != "" and pred is not None:
    st.write("Предполагаемая выручка за день: ")
    st.write(int(medium_count)*pred)
