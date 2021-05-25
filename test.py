import pandas as pd
import numpy as np
import streamlit as st


def initial():
	st.title("2021 USMC PFT Calculator")
	html_temp="An updated calculator that complies with MCO 6100.13A with CH-3 dated 23 February 2021.<br> By. Beau Rogers "
	st.markdown(html_temp,unsafe_allow_html = True)	
	if st.button("PFT"):
		gender = st.radio("Select your gender",("Male","Female"), key=1)
		altitude = st.radio("Did you conduct the PFT at an elevation above 4500 ft mean sea level?",("Yes","No"))
		age = st.slider("How old are you?",value=25, min_value=17, max_value=51, step=1)
		pfttotal = str(gender) + str(altitude) + str(age)
		st.title('PFT stats')
		st.write(pfttotal)
	if st.button("CFT"):
		a = 4
		b = 4
		y = a + b
		st.write(y)
		
	if st.button("BCP"):
		a = 5
		b = 10
		z = a + b
		st.write(z)
		

		


initial()
