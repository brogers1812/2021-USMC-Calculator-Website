import pandas as pd
# import streamlit as st

# def bcp(get_ht,get_wt,get_gender,get_neck_circum,get_ab_circum,get_wt_circum,get_hip_circum):
ht=int(73.0)
wt=str(250)
gender = "Male"
	# neck = get_neck_circum
	# ab = get_ab_circum
	# waist = get_wt_circum
	# hip = get_hip_circum
	
if gender == "Male":
		m_ht_wt_df=pd.read_csv("lookup_records/csv/bcp/male_ht_wt_chart.csv",index_col=0)
		m_ht_wt = m_ht_wt_df.loc[[wt],[ht]].values[0]
		if m_ht_wt == 1:
			print("You are within standards")
		else:
			print("You are not within standards")
else:
		f_ht_wt_df=pd.read_csv("lookup_records/csv/bcp/female_ht_wt_chart.csv",index_col=0)
		f_ht_wt = f_ht_wt_df.loc[[wt],[ht]].values[0]
		if f_ht_wt == 1:
			print("You are within standards")
		else:
			print("You are not within standards")





		# st.write("BCP Calculator in progress!")
		# get_ht = st.slider('Select your height in inches',value=70,min_value=52,max_value=86,step=.5)
		# if get_gender == "Male":
		# 	get_wt = st.number_input('Enter your weight in pounds',value=210,min_value=73,max_value=289,step=1)
		# 	get_neck_circum = st.number_input('Enter your neck circumference',value=15,min_value=12,max_value=18,step=1)
		# 	get_ab_circum = st.number_input('Enter your abdomen circumference',value=30,min_value=27,max_value=42,step=1)
		# 	get_wt_circum = 0
		# 	get_hip_circum = 0
		# elif get_gender == "Female":
		# 	get_wt = st.number_input('Enter your weight in pounds',value=150,min_value=73,max_value=274,step=1)
		# 	get_wt_circum = st.number_input('Enter your waist circumference',value=15,min_value=12,max_value=18,step=1)
		# 	get_hip_circum = st.number_input('Enter your hip circumference',value=15,min_value=12,max_value=18,step=1)
		# 	get_neck_circum = 0
		# 	get_ab_circum = 0