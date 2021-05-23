import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image


def welcome():
    return 'welcome all'

def prediction(gender,age,get_altitude,get_pull,get_event1,get_push,get_event2,get_event3,get_run,get_row):
	#read and setup male pullup CSV file
	get_pull = str(get_pull)
	age = str(age)
	get_pull = str(get_pull)
	get_push = str(get_push)
	get_crunch = str(get_event2)
	run = str(get_run)
		#Start run - remove . from user input
	run = [character for character in run if character.isalnum()]
	run = int("".join(run))
	if(run % 10 !=0):
		run = (run - run % 10) + 10
	#End run - remove . from user input
	get_run = str(run)

	row = str(get_row)
	# 	#Start row - remove . from user input
	# row = [character for character in row if character.isalnum()]
	# row = int("".join(row))
	# if(row % 5 !=0):
	# 	row = (row - row % 5) + 5
	# #End row - remove . from user input
	# get_row=str(row)

	if gender == "Male" and get_event1 == "Pull-ups":
		m_pullup_df=pd.read_csv("lookup_records\csv\m_pull.csv",index_col=0)
		pull_pts = m_pullup_df.loc[[get_pull],[age]].values[0]
		event1 = pull_pts

	elif gender == "Male" and get_event1 == "Push-ups":
		m_pushup_df=pd.read_csv("lookup_records\csv\m_push.csv",index_col=0)
		pushup_pts = m_pushup_df.loc[[get_push],[age]].values[0]
		event1 = pushup_pts

	elif gender == "Female" and get_event1 == "Push-ups":
		m_pushup_df=pd.read_csv("lookup_records\csv\\f_push.csv",index_col=0)
		pushup_pts = m_pushup_df.loc[[get_push],[age]].values[0]
		event1 = pushup_pts

	else:
		f_pullup_df=pd.read_csv("lookup_records\csv\\f_pull.csv",index_col=0)
		pull_pts = f_pullup_df.loc[[get_pull],[age]].values[0]
		event1 = pull_pts

	if gender == "Male":
		#read and setup male crunches CSV file
		m_crunch_df=pd.read_csv("lookup_records\csv\m_crunch.csv",index_col=0)
		crunch_pts = m_crunch_df.loc[[get_crunch],[age]].values[0]
		event2 = crunch_pts

	else:
		#read and setup female crunches CSV files
		f_crunch_df=pd.read_csv("lookup_records\csv\\f_crunch.csv",index_col=0)
		crunch_pts = f_crunch_df.loc[[get_crunch],[age]].values[0]
		event2 = crunch_pts

	if get_altitude == "No":
		if gender == "Male" and get_event3 == "Run":
			m_run_no_alt_df=pd.read_csv("lookup_records\csv\\m_run_no_alt.csv",index_col=0)
			run_pts = m_run_no_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Male" and get_event3 == "Row":
			m_row_no_alt_df=pd.read_csv("lookup_records\csv\\m_row_no_alt.csv",index_col=0)
			row_pts = m_row_no_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts
		elif gender == "Female" and get_event3 == "Run":
			f_run_no_alt_df=pd.read_csv("lookup_records\csv\\f_run_no_alt.csv",index_col=0)
			run_pts = f_run_no_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Female" and get_event3 == "Row":
			f_row_no_alt_df=pd.read_csv("lookup_records\csv\\f_row_no_alt.csv",index_col=0)
			row_pts = f_row_no_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts
	else:
		if gender == "Male" and get_event3 == "Run":
			m_run_alt_df=pd.read_csv("lookup_records\csv\\m_run_alt.csv",index_col=0)
			run_pts = m_run_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Male" and get_event3 == "Row":
			m_row_alt_df=pd.read_csv("lookup_records\csv\\m_row_alt.csv",index_col=0)
			row_pts = m_row_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts
		elif gender == "Female" and get_event3 == "Run":
			f_run_alt_df=pd.read_csv("lookup_records\csv\\f_run_alt.csv",index_col=0)
			run_pts = f_run_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Female" and get_event3 == "Row":
			f_row_alt_df=pd.read_csv("lookup_records\csv\\f_row_alt.csv",index_col=0)
			row_pts = f_row_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts

	
	
	
	
	prediction = int(event1) + int(event2) + int(event3)

	return prediction
		
def main():
	st.title("2021 USMC PFT Calculator")
	html_temp=""
	ans=0
	st.markdown(html_temp,unsafe_allow_html = True)
	get_Gender = st.radio("Select your gender",("Male","Female"))
	get_Altitude = st.radio("Did you conduct the PFT at an elevation above 4500 ft mean sea level?",("Yes","No"))
	get_age = st.slider("How old are you?",value=25, min_value=17, max_value=51, step=1)
	get_event1 = st.radio("Did you perform pullups or pushups?",("Pull-ups","Push-ups"))
	if get_event1 == 'Pull-ups' and get_Gender == "Male":
		get_pull = st.slider("How many pullups did you perform?",value=15, min_value=3, max_value=23, step=1)
		get_push = 0
	elif get_event1 == 'Push-ups' and get_Gender == "Male":
		get_push = st.slider("How many pushups did you perform?",value=50, min_value=20, max_value=87, step=1)
		get_pull = 0
	elif get_event1 == 'Pull-ups' and get_Gender == "Female":
		get_pull = st.slider("How many pullups did you perform?",value=8, min_value=1, max_value=12, step=1)
		get_push = 0
	elif get_event1 == 'Push-ups' and get_Gender == 'Female':
		get_push = st.slider("How many pushups did you perform?",value=30, min_value=10, max_value=50, step=1)
		get_pull = 0
	else:
		get_pull = 0
		get_push = 0
	if get_Gender == "Male":	
		get_event2 = st.slider("How many crunches did you perform?",value=70,min_value=40,max_value=115)
	else:
		get_event2 = st.slider("How many crunches did you perform?",value=70,min_value=40,max_value=110)
	get_event3 = st.radio("Did you perform the 3 mile run or 5k row?",("Run","Row"))
	if get_Altitude == "Yes":
		if get_event3 == "Run" and get_Gender == "Male":
			get_run = st.number_input('Enter your runtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_row = 0
		elif get_event3 == "Row" and get_Gender == "Male":
			get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_run = 0
		elif get_event3 == "Run" and get_Gender == "Female":
			get_run = st.number_input('Enter your runtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_row = 0
		elif get_event3 == "Row" and get_Gender == "Female":
			get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_run = 0
		else:
			get_row=0
			get_run=0
	elif get_Altitude == "No":
		if get_event3 == "Run" and get_Gender == "Male":
			get_run = st.number_input('Enter your runtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_row = 0
		elif get_event3 == "Row" and get_Gender == "Male":
			get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_run = 0
		elif get_event3 == "Run" and get_Gender == "Female":
			get_run = st.number_input('Enter your runtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_row = 0
		elif get_event3 == "Row" and get_Gender == "Female":
			get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.00,max_value=30.00,step=.05)
			get_run = 0
		else:
			get_row=0
			get_run=0
	else:
		get_row = 0
		get_run = 0
	get_total = get_pull + get_push + get_event2 + get_run + get_row

	if st.button("Predict"):
		
		if get_total == get_pull + get_push + get_event2 + get_run + get_row:
			ans=prediction(get_Gender,get_age,get_Altitude,get_pull,get_event1,get_push,get_event2,get_event3,get_run,get_row)
		else:
			ans = "Were still working on it."
		st.sidebar.text(int(ans))
		# if ans==0:
		# 	st.success('You have no chance of getting stroke😊')
		# 	st.image('stroke_detection/images/happy_heart.jfif')
		# else:
		# 	st.success('You are at risk of getting stroke😥')
		# 	st.image('stroke_detection/images/damaged_heart.jfif')

if __name__=='__main__':
	main()