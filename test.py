import streamlit as st


def agefunc(wt,ht):
	ht = float(ht)
	wt = float(wt)

	if ht == 52 and 73 <= wt <= 106:
		st.markdown("You are within height and weight standards")
	elif ht == 52 and 73 > wt:
		st.markdown("You are underweight")
	elif ht == 52 and wt > 106:
		st.markdown("You are overweight")

	return 


def main():
	st.title("Are you within standards??")
	wt = st.slider("Weight",value=185, min_value=60, max_value=289, step=1)
	ht = st.slider("Height?",value=68, min_value=52, max_value=86, step=1)
	


	
	st.markdown(agefunc(wt,ht))






if __name__=='__main__':
	main()