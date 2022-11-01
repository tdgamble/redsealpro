import streamlit as sl
import pandas as pd

#remove the hamburger/footer
sl.markdown("""
<style>
.css-1rs6os.edgvbvh3, .css-1lsmgbg.egzxvld0 
{
	visibility: hidden;
}

</style>
""", unsafe_allow_html=True) 
sl.markdown("<h1 style='text-align: center;'>User Registration</h1>", unsafe_allow_html=True)

with sl.form("Form 2"):
	col1, col2=sl.columns(2)
	f_name=col1.text_input("First Name")
	l_name=col2.text_input("Last Name")
	email=sl.text_input("Email Address")
	password=sl.text_input("Password")
	password_confirm=sl.text_input("Confirm Password")
	
	#day,month,year=sl.columns(3)
	#day.text_input("Day")
	#month.text_input("Month")
	#year.text_input("Year")
	date_input=sl.date_input("What is the date?")


	s_state=sl.form_submit_button("Submit")
	if s_state:
		if f_name == "":
			sl.warning("Please fill in your first name")
		elif l_name == "":
			sl.warning("Please fill in your last name")
		elif email == "":
			sl.warning("Please fill in your email address")
		elif password == "":
			sl.warning("Please fill in password")
		elif password_confirm == "":
			sl.warning("Please confirm your password")
		else:
			sl.success("Submitted Succesfully")