import streamlit as st
from currency_converter import CurrencyConverter
import pycountry

st.image("logo.png", use_column_width = True)
st.title("Currency Converter")

converter = CurrencyConverter()

currencies = converter.currencies

currency_to_country = {currency: pycountry.currencies.get(alpha_3=currency).name for currency in currencies if pycountry.currencies.get(alpha_3=currency)}

amount = st.number_input("Enter amount:", min_value=0.0)
from_currency = st.selectbox("From currency:", options=list(currency_to_country.keys()))
from_country = currency_to_country.get(from_currency,"Unknown")
st.write(f"From country:{from_country}")
to_currency = st.selectbox("To currency:", options=list(currency_to_country.keys()))
to_country = currency_to_country.get(to_currency, "Unknown")
st.write(f"To country: {to_country}")



converted_amount = converter.convert(amount, from_currency, to_currency)
if st.button('Convert Currency'):
    st.subheader('Your Currency has been converted')
    st.write(f"Converted amount: {converted_amount:.2f} {to_currency}")
    st.image("currency converter.png", use_column_width = False)

