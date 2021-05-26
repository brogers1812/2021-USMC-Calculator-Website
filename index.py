import pandas as pd
import numpy as np
import streamlit as st


def pftfunc(gender,age,get_altitude,get_pull,get_event1,get_push,get_event2,get_crunch,get_plank,get_event3,get_run,get_row):
	#read and setup male pullup CSV file
	age = str(age)
	pull = str(get_pull)
	push = str(get_push)
	crunch = str(get_crunch)
	plank = str(get_plank)
	run = str(get_run)
	row = str(get_row)

# Determine if the string has a range between XX.50 to XX.59
	run = [character for character in run if character.isalnum()]
	run = int("".join(run))
	run = str(run)
	if run.endswith("0"):
		run = int(run)
		if(run % 10 !=0):
			run = (run - run % 10) + 10
		run = str(run) + "0"

	if run.endswith("5", 2,3):
		run = int(run)
		run = round(run,-2)
		run = str(run)

	elif run.endswith("0", 2,3):
		run = int(run)
		if(run % 10 !=0):
			run = (run - run % 10) + 10
		run = str(run)

	elif run.endswith("1", 2,3) or run.endswith("2", 2,3) or run.endswith("3", 2,3) or run.endswith("4", 2,3):
		run = int(run)
		if(run % 10 !=0):
			run = (run - run % 10) + 10
			get_run = str(run)
		run = str(run)

	else:
		get_run = 0

	get_run = run


	# Determine if the string has a range between XX.50 to XX.59
	row = [character for character in row if character.isalnum()]
	row = int("".join(row))
	row = str(row)
	if row.endswith("0"):
		row = int(row)
		if(row % 10 !=0):
			row = (row - row % 10) + 10
		row = str(row) + "0"

	if row.endswith("5", 2,3):
		row = int(row)
		row = round(row,-2)
		row = str(row)

	elif row.endswith("0", 2,3):
		row = int(row)
		if(row % 10 !=0):
			row = (row - row % 10) + 10
		row = str(row)

	elif row.endswith("1", 2,3) or row.endswith("2", 2,3) or row.endswith("3", 2,3) or row.endswith("4", 2,3):
		row = int(row)
		if(row % 10 !=0):
			row = (row - row % 10) + 10
			get_row = str(row)
		row = str(row)

	else:
		get_row = 0

	get_row = row


	if gender == "Male" and get_event1 == "Pull-ups":
		m_pullup_df=pd.read_csv("lookup_records/csv/pft/m_pull.csv",index_col=0)
		pull_pts = m_pullup_df.loc[[pull],[age]].values[0]
		event1 = pull_pts

	elif gender == "Male" and get_event1 == "Push-ups":
		m_pushup_df=pd.read_csv("lookup_records/csv/pft/m_push.csv",index_col=0)
		pushup_pts = m_pushup_df.loc[[push],[age]].values[0]
		event1 = pushup_pts

	elif gender == "Female" and get_event1 == "Push-ups":
		m_pushup_df=pd.read_csv("lookup_records/csv/pft/f_push.csv",index_col=0)
		pushup_pts = m_pushup_df.loc[[push],[age]].values[0]
		event1 = pushup_pts

	else:
		f_pullup_df=pd.read_csv("lookup_records/csv/pft/f_pull.csv",index_col=0)
		pull_pts = f_pullup_df.loc[[pull],[age]].values[0]
		event1 = pull_pts

	if gender == "Male" and get_event2 == "Crunches":
		#read and setup male crunches CSV file
		m_crunch_df=pd.read_csv("lookup_records/csv/pft/m_crunch.csv",index_col=0)
		crunch_pts = m_crunch_df.loc[[crunch],[age]].values[0]
		event2 = crunch_pts

	elif gender == "Female" and get_event2 == "Crunches":
		#read and setup female crunches CSV files
		f_crunch_df=pd.read_csv("lookup_records/csv/pft/f_crunch.csv",index_col=0)
		crunch_pts = f_crunch_df.loc[[crunch],[age]].values[0]
		event2 = crunch_pts
	else:
		
		plank = str(get_plank)
		plank = [character for character in plank if character.isalnum()]
		plank = int("".join(plank))
		plank = str(plank)
		if plank.endswith("0"):
			plank = int(plank)
			if(plank % 10 !=0):
				plank = (plank - plank % 10) + 10
				plank = str(plank) + "0"

		#read and setup plank file
		plank_df=pd.read_csv("lookup_records/csv/pft/plank.csv",index_col=0)
		plank_pts = plank_df.loc[[plank],[age]].values[0]
		event2 = plank_pts

	if get_altitude == "No":
		if gender == "Male" and get_event3 == "Run":
			m_run_no_alt_df=pd.read_csv("lookup_records/csv/pft/m_run_no_alt.csv",index_col=0)
			run_pts = m_run_no_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Male" and get_event3 == "Row":
			m_row_no_alt_df=pd.read_csv("lookup_records/csv/pft/m_row_no_alt.csv",index_col=0)
			row_pts = m_row_no_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts
		elif gender == "Female" and get_event3 == "Run":
			f_run_no_alt_df=pd.read_csv("lookup_records/csv/pft/f_run_no_alt.csv",index_col=0)
			run_pts = f_run_no_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Female" and get_event3 == "Row":
			f_row_no_alt_df=pd.read_csv("lookup_records/csv/pft/f_row_no_alt.csv",index_col=0)
			row_pts = f_row_no_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts
	else:
		if gender == "Male" and get_event3 == "Run":
			m_run_alt_df=pd.read_csv("lookup_records/csv/pft/m_run_alt.csv",index_col=0)
			run_pts = m_run_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Male" and get_event3 == "Row":
			m_row_alt_df=pd.read_csv("lookup_records/csv/pft/m_row_alt.csv",index_col=0)
			row_pts = m_row_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts
		elif gender == "Female" and get_event3 == "Run":
			f_run_alt_df=pd.read_csv("lookup_records/csv/pft/f_run_alt.csv",index_col=0)
			run_pts = f_run_alt_df.loc[[get_run],[age]].values[0]
			event3 = run_pts
		elif gender == "Female" and get_event3 == "Row":
			f_row_alt_df=pd.read_csv("lookup_records/csv/pft/f_row_alt.csv",index_col=0)
			row_pts = f_row_alt_df.loc[[get_row],[age]].values[0]
			event3 = row_pts

		
	pftfunc = int(event1) + int(event2) + int(event3)

	return pftfunc

def cftfunc(gender,age,altitude,get_mtc,get_acl,get_muf):
	#read and setup male pullup CSV file
	age = str(age)
	mtc = str(get_mtc)
	acl = str(get_acl)
	muf = str(get_muf)

	# Determine if the string has a range between XX.50 to XX.59
		
	#MTC lookup records
	mtc = mtc.replace(".", "")
	if len(mtc) == 3:
		mtc = int(mtc)
	elif len(mtc) == 2:
		mtc = float(mtc)
		mtc = int(mtc * 10)
	mtc = str(mtc)

	if gender == "Male" and altitude == "No":
		m_mtc_df=pd.read_csv("lookup_records/csv/cft/m_mtc_no_alt.csv",index_col=0)
		mtc_pts = m_mtc_df.loc[[mtc],[age]].values[0]
		event1 = mtc_pts
	elif gender == "Male" and altitude == "Yes":
		m_mtc_df=pd.read_csv("lookup_records/csv/cft/m_mtc_alt.csv",index_col=0)
		mtc_pts = m_mtc_df.loc[[mtc],[age]].values[0]
		event1 = mtc_pts
	elif gender == "Female" and altitude == "No":
		f_mtc_df=pd.read_csv("lookup_records/csv/cft/f_mtc_no_alt.csv",index_col=0)
		mtc_pts = f_mtc_df.loc[[mtc],[age]].values[0]
		event1 = mtc_pts
	elif gender == "Female" and altitude == "Yes":
		f_mtc_df=pd.read_csv("lookup_records/csv/cft/f_mtc_alt.csv",index_col=0)
		mtc_pts = f_mtc_df.loc[[mtc],[age]].values[0]
		event1 = mtc_pts
	#ACL record looup
	if gender == "Male":
		m_acl_df=pd.read_csv("lookup_records/csv/cft/m_acl.csv",index_col=0)
		acl_pts = m_acl_df.loc[[acl],[age]].values[0]
		event2 = acl_pts
	elif gender == "Female":
		f_acl_df=pd.read_csv("lookup_records/csv/cft/f_acl.csv",index_col=0)
		acl_pts = f_acl_df.loc[[acl],[age]].values[0]
		event2 = acl_pts
	#MUF record lookup
	muf = muf.replace(".", "")
	if len(muf) == 3:
		muf = int(muf)
	elif len(muf) == 2:
		muf = float(muf)
		muf = int(muf * 10)
	muf = str(muf)

	if gender == "Male" and altitude == "No":
		m_muf_df=pd.read_csv("lookup_records/csv/cft/m_muf_no_alt.csv",index_col=0)
		muf_pts = m_muf_df.loc[[muf],[age]].values[0]
		event3 = muf_pts
	elif gender == "Male" and altitude == "Yes":
		m_muf_df=pd.read_csv("lookup_records/csv/cft/m_muf_alt.csv",index_col=0)
		muf_pts = m_muf_df.loc[[muf],[age]].values[0]
		event3 = muf_pts
	elif gender == "Female" and altitude == "No":
		f_muf_df=pd.read_csv("lookup_records/csv/cft/f_muf_no_alt.csv",index_col=0)
		muf_pts = f_muf_df.loc[[muf],[age]].values[0]
		event3 = muf_pts
	elif gender == "Female" and altitude == "Yes":
		f_muf_df=pd.read_csv("lookup_records/csv/cft/f_muf_alt.csv",index_col=0)
		muf_pts = f_muf_df.loc[[muf],[age]].values[0]
		event3 = muf_pts

	cftfunc = int(event1) + int(event2) + int(event3) 
	return cftfunc
		
def main():
	st.title("2021 USMC PFT/CFT Calculator")
	html_temp="An updated calculator that complies with MCO 6100.13A with CH-3 dated 23 February 2021.<br> By. Beau Rogers "
	st.markdown(html_temp,unsafe_allow_html = True)
	get_type = st.radio("Did you perform the PFT or CFT?",("PFT","CFT"))
	get_Gender = st.radio("Select your gender",("Male","Female"))
	get_Altitude = st.radio("Did you conduct the PFT at an elevation above 4500 ft mean sea level?",("No","Yes"))
	get_age = st.slider("How old are you?",value=25, min_value=17, max_value=51, step=1)
	if get_type == "PFT":
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
		get_event2 = st.radio("Did you crunches or plank?",("Crunches","Plank"))
		if get_event2 == "Crunches" and get_Gender == "Male":	
			get_crunch = st.slider("How many crunches did you perform?",value=70,min_value=40,max_value=115)
			get_plank = 0
		elif get_event2 == "Crunches" and get_Gender == "Female":	
			get_crunch = st.slider("How many crunches did you perform?",value=70,min_value=40,max_value=110)
			get_plank = 0
		elif get_event2 == "Plank":
			get_plank = st.number_input('Enter your plank time:',value=3.05,min_value=1.03,max_value=4.20,step=.01)
			get_crunch = 0
		get_event3 = st.radio("Did you perform the 3 mile run or 5k row?",("Run","Row"))
		if get_Altitude == "Yes":
			if get_event3 == "Run" and get_Gender == "Male":
				get_run = st.number_input('Enter your runtime:',value=22.00,min_value=19.30,max_value=34.30,step=.01)
				get_row = 0
			elif get_event3 == "Row" and get_Gender == "Male":
				get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.40,max_value=26.40,step=.01)
				get_run = 0
			elif get_event3 == "Run" and get_Gender == "Female":
				get_run = st.number_input('Enter your runtime:',value=24.00,min_value=22.30,max_value=37.30,step=.01)
				get_row = 0
			elif get_event3 == "Row" and get_Gender == "Female":
				get_row = st.number_input('Enter your rowtime:',value=24.00,min_value=21.40,max_value=29.40,step=.01)
				get_run = 0
			else:
				get_row=0
				get_run=0
		elif get_Altitude == "No":
			if get_event3 == "Run" and get_Gender == "Male":
				get_run = st.number_input('Enter your runtime:',value=22.00,min_value=18.00,max_value=33.15,step=.01)
				get_row = 0
			elif get_event3 == "Row" and get_Gender == "Male":
				get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.00,max_value=26.00,step=.01)
				get_run = 0
			elif get_event3 == "Run" and get_Gender == "Female":
				get_run = st.number_input('Enter your runtime:',value=22.00,min_value=21.00,max_value=36.00,step=.01)
				get_row = 0
			elif get_event3 == "Row" and get_Gender == "Female":
				get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=21.00,max_value=29.00,step=.01)
				get_run = 0
			else:
				get_row=0
				get_run=0
		else:
			get_row = 0
			get_run = 0
	else:
		if get_Altitude == "No" and get_Gender == "Male":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=3.15,min_value=2.38,max_value=5.07,step=.01)
		elif get_Altitude == "No" and get_Gender == "Female":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=4.00,min_value=3.10,max_value=5.52,step=.01)
		elif get_Altitude == "Yes" and get_Gender == "Male":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=3.15,min_value=2.44,max_value=5.11,step=.01)
		elif get_Altitude == "Yes" and get_Gender == "Female":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=4.00,min_value=3.16,max_value=5.58,step=.01)
		if  get_Gender == "Male":
			get_acl = st.slider('How many ammo can lifts did you perform?',value=90,min_value=16,max_value=120,step=1)
		elif get_Gender == "Female":
			get_acl = st.slider('How many ammo can lifts did you perform?',value=50,min_value=6,max_value=75,step=1)
		if get_Altitude == "No" and get_Gender == "Male":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=3.15,min_value=2.04,max_value=6.09,step=.01)
		elif get_Altitude == "No" and get_Gender == "Female":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=4.00,min_value=2.42,max_value=6.33,step=.01)
		elif get_Altitude == "Yes" and get_Gender == "Male":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=3.15,min_value=2.12,max_value=6.17,step=.01)
		elif get_Altitude == "Yes" and get_Gender == "Female":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=4.00,min_value=2.50,max_value=6.41,step=.01)
	
	if st.button("Calculate"):
		if get_type == "PFT":
			totalscore=pftfunc(get_Gender,get_age,get_Altitude,get_pull,get_event1,get_push,get_event2,get_crunch,get_plank,get_event3,get_run,get_row)
			st.title('PFT results')
			st.markdown("You inputted that you are a {} year old {}".format(int(get_age),get_Gender),unsafe_allow_html = True)
			if get_pull >= 1:
				st.markdown("Pullups:  {}".format(int(get_pull)))		
			else:
				st.markdown("Pushups:  {}".format(int(get_push)))
			if get_crunch >=1:
				st.markdown("Crunches:  {}".format(int(get_crunch)))
			else:
				st.markdown("Plank:  {}".format(float(get_plank)))
			if get_run >=1:
				st.markdown("Run:  {}".format(float(get_run)))
			else:
				st.markdown("Row:  {}".format(float(get_row)))
			if totalscore >= 235:
				pftclass = "first"
				st.text("Your total PFT score is {} out of 300 points.You earned a {} class PFT!".format(int(totalscore), pftclass))
			elif totalscore <= 235 and totalscore >= 200:
				pftclass = "second"
				st.text("Your total PFT score is {} out of 300 points.\nYou earned a {} class PFT!".format(int(totalscore), pftclass))
			elif totalscore <=200 and totalscore >= 120:
				pftclass = "third"
				st.markdown("Your total PFT score is **_{}_** out of 300 points.\nYou earned a **_{}_** class PFT!".format(int(totalscore), pftclass))
			else:
				pftclass = "Failed"
				st.write("Your total PFT score is {} out of 300 points.\nYou failed the PFT!".format(int(totalscore)))
		elif get_type == "CFT":
			totalscore=cftfunc(get_Gender,get_age,get_Altitude,get_mtc,get_acl,get_muf)
			st.title('CFT results')
			st.markdown("You inputted that you are a {} year old {}".format(int(get_age),get_Gender),unsafe_allow_html = True)
			st.markdown("Maneuver To Contact:  {}".format(float(get_mtc)))
			st.markdown("Ammo Can Life:  {}".format(int(get_acl)))
			st.markdown("Maneuver Under Fire:  {}".format(float(get_muf)))
			if totalscore >= 235:
				pftclass = "first"
				st.markdown("Your total CFT score is {} out of 300 points.You earned a {} class PFT!".format(int(totalscore), pftclass))
			elif totalscore <= 234 and totalscore >= 200:
				pftclass = "second"
				st.markdown("Your total CFT score is {} out of 300 points.\nYou earned a {} class PFT!".format(int(totalscore), pftclass))
			elif totalscore <=199 and totalscore >= 150:
				pftclass = "third"
				st.markdown("Your total CFT score is **_{}_** out of 300 points.\nYou earned a **_{}_** class PFT!".format(int(totalscore), pftclass))
			else:
				pftclass = "Failed"
				st.markdown("Your total CFT score is {} out of 300 points.\nYou failed the CFT!".format(int(totalscore)))



if __name__=='__main__':
	main()