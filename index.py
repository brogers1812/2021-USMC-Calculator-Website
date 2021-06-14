import pandas as pd
import numpy as np
import math
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



def bcpfunc(get_ht,get_wt,get_age,get_gender,get_extra_point,get_circum_value):
	basic_ht = math.ceil(get_ht)
	advanced_ht = float(get_ht)
	wt = float(get_wt)
	age = get_age
	gender = str(get_gender)
	circum_value = str(get_circum_value)

	if gender == "Male":
		if basic_ht == 52 and 73 <= wt <= 106:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 52 and 73 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 52 and wt > 106:
			overweight = 1
		elif basic_ht == 53 and 110 >= wt >= 76:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 53 and 76 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 53 and wt > 110:
			overweight = 1
		elif basic_ht == 54 and 114 >= wt >= 79:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 54 and 79 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 54 and wt > 114:
			overweight = 1
		elif basic_ht == 55 and 118 >= wt >= 82:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 55 and 82 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 55 and wt > 118:
			overweight = 1
		elif basic_ht == 56 and 122 >= wt >= 85:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 56 and 85 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 56  and wt > 122:
			overweight = 1
		elif basic_ht == 57 and 127 >= wt >= 88:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 57 and 88 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 57 and wt > 127:
			overweight = 1
		elif basic_ht == 58 and 131 >= wt >= 91:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 58 and 91 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 58 and wt > 131:
			overweight = 1
		elif basic_ht == 59 and 136 >= wt >= 94:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 59 and 94 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 59 and wt > 136:
			overweight = 1    
		elif basic_ht == 60 and 141 >= wt >= 97:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 60 and 97 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 60 and wt > 141:
			overweight = 1
		elif basic_ht == 61 and 145 >= wt >= 100:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 61 and 100 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 61 and wt > 145:
			overweight = 1
		elif basic_ht == 62 and 150 >= wt >= 104:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 62 and 104 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 62 and wt > 150:
			overweight = 1
		elif basic_ht == 63 and 155 >= wt >= 107:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 63 and 107 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 63 and wt > 155:
			overweight = 1
		elif basic_ht == 64 and 160 >= wt >= 110:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 64 and 110 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 64 and wt > 160:
			overweight = 1
		elif basic_ht == 65 and 165 >= wt >= 114:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 65 and 114 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 65 and wt > 165:
			overweight = 1
		elif basic_ht == 66 and 170 >= wt >= 117:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 66 and 117 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 66 and wt > 170:
			overweight = 1
		elif basic_ht == 67 and 175 >= wt >= 121:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 67 and 121 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 67 and wt > 175:
			overweight = 1
		elif basic_ht == 68 and 180 >= wt >= 125:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 68 and 125 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 68 and wt > 180:
			overweight = 1
		elif basic_ht == 69 and 186 >= wt >= 128:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 69 and 128 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 69 and wt > 186:
			overweight = 1
		elif basic_ht == 70 and 191 >= wt >= 132:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 70 and 132 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 70 and wt > 191:
			overweight = 1
		elif basic_ht == 71 and 197 >= wt >= 136:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 71 and 136 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 71 and wt > 197:
			overweight = 1
		elif basic_ht == 72 and 202 >= wt >= 140:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 72 and 140 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 72 and wt > 202:
			overweight = 1
		elif basic_ht == 73 and 208 >= wt >= 144:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 73 and 144 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 73 and wt > 208:
			overweight = 1
		elif basic_ht == 74 and 214 >= wt >= 148:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 74 and 148 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 74 and wt > 214:
			overweight = 1
		elif basic_ht == 75 and 220 >= wt >= 152:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 75 and 152 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 75 and wt > 220:
			overweight = 1
		elif basic_ht == 76 and 225 >= wt >= 156:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 76 and 156 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 76 and wt > 255:
			overweight = 1
		elif basic_ht == 77 and 231 >= wt >= 160:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 77 and 160 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 77 and wt > 231:
			overweight = 1
		elif basic_ht == 78 and 237 >= wt >= 164:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 78 and 164 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 78 and wt > 237:
			overweight = 1
		elif basic_ht == 79 and 244 >= wt >= 168:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 79 and 168 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 79 and wt > 244:
			overweight = 1
		elif basic_ht == 80 and 250 >= wt >= 173:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 80 and 173 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 80 and wt > 250:
			overweight = 1
		elif basic_ht == 81 and 256 >= wt >= 177:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 81 and 177 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 81 and wt > 256:
			overweight = 1
		elif basic_ht == 82 and 263 >= wt >= 182:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 82 and 182 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 82 and wt > 263:
			overweight = 1
		elif basic_ht == 83 and 269 >= wt >= 186:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 83 and 186 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 83 and wt > 269:
			overweight = 1
		elif basic_ht == 84 and 276 >= wt >= 191:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 84 and 191 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 84 and wt > 276:
			overweight = 1
		elif basic_ht == 85 and 283 >= wt >= 195:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 85 and 195 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 85 and wt > 283:
			overweight = 1
		elif basic_ht == 86 and 289 >= wt >= 200:
			st.markdown("You are within height and weight standards.")
			overweight = 0
		elif basic_ht == 86 and 200 > wt:
			st.markdown("You are underweight")
			overweight = 0
		elif basic_ht == 86 and wt > 289:
			overweight = 1

		if 17 <= age <= 25:
			max_bcp_percent = 18
			if get_extra_point == 'Yes':
				max_bcp_percent = 19
		elif 26 <= age <= 35:
			max_bcp_percent = 19
			if get_extra_point == 'Yes':
				max_bcp_percent = 20
		elif 36 <= age <= 45:
			max_bcp_percent = 20
			if get_extra_point == 'Yes':
				max_bcp_percent = 21
		elif 46 <= age <= 51:
			max_bcp_percent = 21
			if get_extra_point == 'Yes':
				max_bcp_percent = 22

		if 52 <= advanced_ht <=54.5 and overweight == 1:
			st.markdown("You are a height that is not considered for the Body Composition Program.")
			m_body_fat_lookup = 0.0

		elif 55.0 <= advanced_ht <= 59.5 and overweight == 1:
			ht = str(advanced_ht)
			m_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_55-595_chart.csv",index_col=0)
			m_body_fat_lookup = m_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if m_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif m_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 60 <= advanced_ht <= 64.5 and overweight == 1:
			ht = str(advanced_ht)
			m_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_60-645_chart.csv",index_col=0)
			m_body_fat_lookup = m_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if m_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif m_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 65 <= advanced_ht <= 69.5 and overweight == 1:
			ht = str(advanced_ht)
			m_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_65-695_chart.csv",index_col=0)
			m_body_fat_lookup = m_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if m_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif m_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 70 <= advanced_ht <= 74.5 and overweight == 1:
			ht = str(advanced_ht)
			m_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_70-745_chart.csv",index_col=0)
			m_body_fat_lookup = m_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if m_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif m_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 75 <= advanced_ht <= 79.5 and overweight == 1:
			ht = str(advanced_ht)
			m_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_75-795_chart.csv",index_col=0)
			m_body_fat_lookup = m_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if m_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif m_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")
			
		if overweight == 0:
			body_fat = 0.0
		else:
			body_fat = float(m_body_fat_lookup)
		

	else:
		if basic_ht == 52 and 100 >= wt >= 73:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 52 and wt < 73:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 52 and wt > 100:
			overweight = 1
		elif basic_ht == 53 and 104 >= wt >= 76:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 53 and wt < 76:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 53 and wt > 104:
			overweight = 1
		elif basic_ht == 54 and 108 >= wt >= 79:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 54 and wt < 73:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 54 and wt > 108:
			overweight = 1
		elif basic_ht == 55 and 112 >= wt >= 82:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 55 and wt < 82:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 55 and wt > 112:
			overweight = 1
		elif basic_ht == 56 and 115 >= wt >= 85:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 56 and wt < 85:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 56 and wt > 115:
			overweight = 1
		elif basic_ht == 57 and 120 >= wt >= 88:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 57 and wt < 88:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 57 and wt > 120:
			overweight = 1
		elif basic_ht == 58 and 124 >= wt >= 91:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 58 and wt < 91:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 58 and wt > 124:
			overweight = 1
		elif basic_ht == 59 and 129 >= wt >= 94:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 59 and wt < 94:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 59 and wt > 129:
			overweight = 1
		elif basic_ht == 60 and 133 >= wt >= 97:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 60 and wt < 73:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 60 and wt > 133:
			overweight = 1
		elif basic_ht == 61	and 137	>= wt >= 100:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 61 and wt < 100:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 61 and wt > 137:
			overweight = 1
		elif basic_ht == 62	and 142	>= wt >= 104:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 62 and wt < 104:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 62 and wt > 142:
			overweight = 1
		elif basic_ht == 63	and 146	>= wt >= 107:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 63 and wt < 107:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 63 and wt > 146:
			overweight = 1
		elif basic_ht == 64	and 151	>= wt >= 110:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 64 and wt < 110:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 64 and wt > 151:
			overweight = 1
		elif basic_ht == 65	and 156	>= wt >= 114:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 65 and wt < 114:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 65 and wt > 156:
			overweight = 1
		elif basic_ht == 66	and 161	>= wt >= 117:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 66 and wt < 117:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 66 and wt > 161:
			overweight = 1
		elif basic_ht == 67	and 166	>= wt >= 121:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 67 and wt < 121:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 67 and wt > 166:
			overweight = 1
		elif basic_ht == 68	and 171	>= wt >= 125:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 68 and wt < 125:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 68 and wt > 171:
			overweight = 1
		elif basic_ht == 69	and 176	>= wt >= 128:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 69 and wt < 128:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 69 and wt > 176:
			overweight = 1
		elif basic_ht == 70	and 181	>= wt >= 132:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 70 and wt < 132:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 70 and wt > 181:
			overweight = 1
		elif basic_ht == 71	and 186	>= wt >= 136:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 71 and wt < 136:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 71 and wt > 186:
			overweight = 1
		elif basic_ht == 72	and 191	>= wt >= 140:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 72 and wt < 140:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 72 and wt > 191:
			overweight = 1
		elif basic_ht == 73	and 197	>= wt >= 144:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 73 and wt < 144:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 73 and wt > 197:
			overweight = 1
		elif basic_ht == 74	and 202	>= wt >= 148:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 74 and wt < 148:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 74 and wt > 202:
			overweight = 1
		elif basic_ht == 75	and 208	>= wt >= 152:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 75 and wt < 152:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 75 and wt > 208:
			overweight = 1
		elif basic_ht == 76	and 213	>= wt >= 156:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 76 and wt < 156:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 76 and wt > 213:
			overweight = 1
		elif basic_ht == 77	and 219	>= wt >= 160:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 77 and wt < 160:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 77 and wt > 219:
			overweight = 1
		elif basic_ht == 78	and 225	>= wt >= 164:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 78 and wt < 164:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 78 and wt > 225:
			overweight = 1
		elif basic_ht == 79	and 230	>= wt >= 168:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 79 and wt < 168:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 79 and wt > 230:
			overweight = 1
		elif basic_ht == 80	and 236	>= wt >= 173:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 80 and wt < 173:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 80 and wt > 236:
			overweight = 1
		elif basic_ht == 81	and 242	>= wt >= 177:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 81 and wt < 177:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 81 and wt > 242:
			overweight = 1
		elif basic_ht == 82	and 248	>= wt >= 182:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 82 and wt < 182:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 82 and wt > 248:
			overweight = 1
		elif basic_ht == 83	and 255	>= wt >= 186:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 83 and wt < 186:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 83 and wt > 255:
			overweight = 1
		elif basic_ht == 84	and 261	>= wt >= 191:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 84 and wt < 191:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 84 and wt > 261:
			overweight = 1
		elif basic_ht == 85	and 267	>= wt >= 195:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 85 and wt < 195:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 85 and wt > 267:
			overweight = 1
		elif basic_ht == 86	and 274	>= wt >= 200:
			st.markdown("You are within height and weight standards")
			overweight = 0
		elif basic_ht == 86 and wt < 200:
			st.markdown("You are underweight.")
			overweight = 0
		elif basic_ht == 86 and wt > 274:
			overweight = 1


		if 17 <= age <= 25:
			max_bcp_percent = 26
			if get_extra_point == 'Yes':
				max_bcp_percent = 27
		elif 26 <= age <= 35:
			max_bcp_percent = 27
			if get_extra_point == 'Yes':
				max_bcp_percent = 28
		elif 36 <= age <= 45:
			max_bcp_percent = 28
			if get_extra_point == 'Yes':
				max_bcp_percent = 29
		elif 46 <= age <= 51:
			max_bcp_percent = 29
			if get_extra_point == 'Yes':
				max_bcp_percent = 30



		if 52 == advanced_ht and overweight == 1:
			st.markdown("You are a height that is not considered for the Body Composition Program.")
			f_body_fat_lookup = 0.0

		elif 53.0 <= advanced_ht <= 57.5 and overweight == 1:
			ht = str(advanced_ht)
			f_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_55-595_chart.csv",index_col=0)
			f_body_fat_lookup = f_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if f_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif f_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 58 <= advanced_ht <= 62.5 and overweight == 1:
			ht = str(advanced_ht)
			f_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_60-645_chart.csv",index_col=0)
			f_body_fat_lookup = f_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if f_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif f_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 63 <= advanced_ht <= 67.5 and overweight == 1:
			ht = str(advanced_ht)
			f_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_65-695_chart.csv",index_col=0)
			f_body_fat_lookup = f_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if f_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif f_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 68 <= advanced_ht <= 72.5 and overweight == 1:
			ht = str(advanced_ht)
			f_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_70-745_chart.csv",index_col=0)
			f_body_fat_lookup = f_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if f_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif f_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")

		elif 73 <= advanced_ht <= 77.5 and overweight == 1:
			ht = str(advanced_ht)
			f_body_fat_lookup_df=pd.read_csv("lookup_records/csv/bcp/male_75-795_chart.csv",index_col=0)
			f_body_fat_lookup = f_body_fat_lookup_df.loc[[circum_value],[ht]].values[0]
			if f_body_fat_lookup <= max_bcp_percent:
				st.markdown("You are within standards")
			elif f_body_fat_lookup > max_bcp_percent:
				st.markdown("You are not within standards. 3rd option. ")
			
		if overweight == 0:
			body_fat = 0.0
		else:
			body_fat = float(f_body_fat_lookup)
		
	return body_fat
		
def main():
	st.title("2021 USMC PFT/CFT Calculator")
	html_temp="An updated calculator that complies with MCO 6100.13A with CH-3 dated 23 February 2021.<br> By. Beau Rogers "
	st.markdown(html_temp,unsafe_allow_html = True)
	get_type = st.radio("Did you perform the PFT or CFT?",("PFT","CFT","BCP"))
	get_gender = st.radio("Select your gender",("Male","Female"))
	if get_type == "PFT":
		get_Altitude = st.radio("Did you conduct the PFT/CFT at an elevation above 4500 ft mean sea level?",("No","Yes"))
		get_age = st.slider("How old are you?",value=25, min_value=17, max_value=51, step=1)
		get_event1 = st.radio("Did you perform pullups or pushups?",("Pull-ups","Push-ups"))
		if get_event1 == 'Pull-ups' and get_gender == "Male":
			get_pull = st.slider("How many pullups did you perform?",value=15, min_value=3, max_value=23, step=1)
			get_push = 0
		elif get_event1 == 'Push-ups' and get_gender == "Male":
			get_push = st.slider("How many pushups did you perform?",value=50, min_value=20, max_value=87, step=1)
			get_pull = 0
		elif get_event1 == 'Pull-ups' and get_gender == "Female":
			get_pull = st.slider("How many pullups did you perform?",value=8, min_value=1, max_value=12, step=1)
			get_push = 0
		elif get_event1 == 'Push-ups' and get_gender == 'Female':
			get_push = st.slider("How many pushups did you perform?",value=30, min_value=10, max_value=50, step=1)
			get_pull = 0
		else:
			get_pull = 0
			get_push = 0
		get_event2 = st.radio("Did you crunches or plank?",("Crunches","Plank"))
		if get_event2 == "Crunches" and get_gender == "Male":	
			get_crunch = st.slider("How many crunches did you perform?",value=70,min_value=40,max_value=115)
			get_plank = 0
		elif get_event2 == "Crunches" and get_gender == "Female":	
			get_crunch = st.slider("How many crunches did you perform?",value=70,min_value=40,max_value=110)
			get_plank = 0
		elif get_event2 == "Plank":
			get_plank = st.number_input('Enter your plank time:',value=3.05,min_value=1.03,max_value=4.20,step=.01)
			get_crunch = 0
		if get_age >= 46:
			get_event3 = st.radio("Did you perform the 3 mile run or 5k row?",("Run","Row"))
			if get_Altitude == "Yes":
				if get_event3 == "Run" and get_gender == "Male":
					get_run = st.number_input('Enter your runtime:',value=22.00,min_value=19.30,max_value=34.30,step=.01)
					get_row = 0
				elif get_event3 == "Row" and get_gender == "Male":
					get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.40,max_value=26.40,step=.01)
					get_run = 0
				elif get_event3 == "Run" and get_gender == "Female":
					get_run = st.number_input('Enter your runtime:',value=24.00,min_value=22.30,max_value=37.30,step=.01)
					get_row = 0
				elif get_event3 == "Row" and get_gender == "Female":
					get_row = st.number_input('Enter your rowtime:',value=24.00,min_value=21.40,max_value=29.40,step=.01)
					get_run = 0
				else:
					get_row=0
					get_run=0
			elif get_Altitude == "No":
				if get_event3 == "Run" and get_gender == "Male":
					get_run = st.number_input('Enter your runtime:',value=22.00,min_value=18.00,max_value=33.15,step=.01)
					get_row = 0
				elif get_event3 == "Row" and get_gender == "Male":
					get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=18.00,max_value=26.00,step=.01)
					get_run = 0
				elif get_event3 == "Run" and get_gender == "Female":
					get_run = st.number_input('Enter your runtime:',value=22.00,min_value=21.00,max_value=36.00,step=.01)
					get_row = 0
				elif get_event3 == "Row" and get_gender == "Female":
					get_row = st.number_input('Enter your rowtime:',value=22.00,min_value=21.00,max_value=29.00,step=.01)
					get_run = 0
				else:
					get_row=0
					get_run=0
			else:
				get_row = 0
				get_run = 0
		elif get_age < 46:
			st.markdown("Due to your age, you're only authorized to perform the run.")
			get_event3 = "Run"
			if get_Altitude == "Yes":
				if get_gender == "Male":
					get_run = st.number_input('Enter your runtime:',value=22.00,min_value=19.30,max_value=34.30,step=.01)
					get_row = 0
				elif get_gender == "Female":
					get_run = st.number_input('Enter your runtime:',value=24.00,min_value=22.30,max_value=37.30,step=.01)
					get_row = 0
				else:
					get_row=0
					get_run=0
			elif get_Altitude == "No":
				if  get_gender == "Male":
					get_run = st.number_input('Enter your runtime:',value=22.00,min_value=18.00,max_value=33.15,step=.01)
					get_row = 0
				elif get_gender == "Female":
					get_run = st.number_input('Enter your runtime:',value=22.00,min_value=21.00,max_value=36.00,step=.01)
					get_row = 0
				else:
					get_row=0
					get_run=0
			else:
				get_row = 0
				get_run = 0
	elif get_type == "CFT": 
		get_Altitude = st.radio("Did you conduct the PFT/CFT at an elevation above 4500 ft mean sea level?",("No","Yes"))
		get_age = st.slider("How old are you?",value=25, min_value=17, max_value=51, step=1)
		if get_Altitude == "No" and get_gender == "Male":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=3.15,min_value=2.38,max_value=5.07,step=.01)
		elif get_Altitude == "No" and get_gender == "Female":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=4.00,min_value=3.10,max_value=5.52,step=.01)
		elif get_Altitude == "Yes" and get_gender == "Male":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=3.15,min_value=2.44,max_value=5.11,step=.01)
		elif get_Altitude == "Yes" and get_gender == "Female":
			get_mtc = st.number_input('Enter your time for movement to contact:',value=4.00,min_value=3.16,max_value=5.58,step=.01)
		if  get_gender == "Male":
			get_acl = st.slider('How many ammo can lifts did you perform?',value=90,min_value=16,max_value=120,step=1)
		elif get_gender == "Female":
			get_acl = st.slider('How many ammo can lifts did you perform?',value=50,min_value=6,max_value=75,step=1)
		if get_Altitude == "No" and get_gender == "Male":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=3.15,min_value=2.04,max_value=6.09,step=.01)
		elif get_Altitude == "No" and get_gender == "Female":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=4.00,min_value=2.42,max_value=6.33,step=.01)
		elif get_Altitude == "Yes" and get_gender == "Male":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=3.15,min_value=2.12,max_value=6.17,step=.01)
		elif get_Altitude == "Yes" and get_gender == "Female":
			get_muf = st.number_input('Enter your time for maneuver under fire:',value=4.00,min_value=2.50,max_value=6.41,step=.01)
	
	else:
		get_ironman = st.radio("Did you score a 285 of higher on the PFT & CFT?",("No","Yes"))
		if get_ironman == "Yes":
			st.markdown('You are exempt from the Marine Corps height and weight standards.')
		else:
			get_extra_point = st.radio('Did you score a 250 or higher on the PFT & CFT',("No","Yes"))
			if get_extra_point == "Yes":
				st.markdown("You earned an extra body fat percentage. I.e. 18% --> 19%")
			get_age = st.slider("How old are you?",value=25, min_value=17, max_value=51, step=1)
			get_ht = st.slider('Select your height in inches',value=70.5,min_value=52.0,max_value=86.0,step=.5)
			if get_gender == "Male":
				get_wt = st.number_input('Enter your weight in pounds',value=210,min_value=60,max_value=300,step=1)
				get_neck_circum = st.number_input('Enter your neck circumference',value=15.5,min_value=12.0,max_value=18.0,step=.5)
				get_ab_circum = st.number_input('Enter your abdomen circumference',value=31.5,min_value=25.0,max_value=42.0,step=.5)
				get_circum_value = get_ab_circum - get_neck_circum
			elif get_gender == "Female":
				get_wt = st.number_input('Enter your weight in pounds',value=140,min_value=60,max_value=300,step=1)
				get_neck_circum = st.number_input('Enter your neck circumference',value=15.5,min_value=12.0,max_value=18.0,step=.5)
				get_wt_circum = st.number_input('Enter your waist circumference',value=15,min_value=12,max_value=18,step=1)
				get_hip_circum = st.number_input('Enter your hip circumference',value=15,min_value=12,max_value=18,step=1)
				get_circum_value = get_wt_circum + get_hip_circum - get_neck_circum


	if st.button("Calculate"):
		if get_type == "PFT":
			totalscore=pftfunc(get_gender,get_age,get_Altitude,get_pull,get_event1,get_push,get_event2,get_crunch,get_plank,get_event3,get_run,get_row)
			st.title('PFT results')
			st.markdown("You inputted that you are a {} year old {}".format(int(get_age),get_gender),unsafe_allow_html = True)
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
			totalscore=cftfunc(get_gender,get_age,get_Altitude,get_mtc,get_acl,get_muf)
			st.title('CFT results')
			st.markdown("You inputted that you are a {} year old {}".format(int(get_age),get_gender),unsafe_allow_html = True)
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
		elif get_type == "BCP":
			bcp_value=bcpfunc(get_ht,get_wt,get_age,get_gender,get_extra_point,get_circum_value)
			st.title('BCP results')
			st.markdown("Body Fat Percentage:  {}".format(float(bcp_value)))
			st.markdown("Your circumference value is: {}".format(float(get_circum_value)))
			

if __name__=='__main__':
	main()