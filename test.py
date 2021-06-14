import streamlit as st


def agefunc(wt,ht):
	basic_ht = float(ht)
	wt = float(wt)
	
	if basic_ht == 52 and 73 <= wt <= 100 or basic_ht == 53 and 76 <= wt <= 104


	if basic_ht == 52 and 73 <= wt <= 106 or basic_ht == 53 and 110 >= wt >= 76:
			st.markdown("You are within height and weight standards")
			overweight = 0
	elif basic_ht == 52 and 73 > wt or basic_ht == 53 and 76 > wt:
			st.markdown("You are underweight")
			overweight = 0
	elif basic_ht == 52 and wt > 106 or basic_ht == 53 and 110 > wt:
			overweight = 1
	

	return 


def main():
	st.title("Are you within standards??")
	wt = st.slider("Weight",value=185, min_value=60, max_value=289, step=1)
	ht = st.slider("Height?",value=68, min_value=52, max_value=86, step=1)
	


	
	st.markdown(agefunc(wt,ht))






if __name__=='__main__':
	main()