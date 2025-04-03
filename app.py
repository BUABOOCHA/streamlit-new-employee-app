import streamlit as st
import pandas as pd

st.title("New employee")

report_pattama_df = pd.read_excel('Daily report_20250115_Pattama_Sooksan.xlsx')
report_raewwadee_df = pd.read_excel('Daily report_20250115_Raewwadee_Jaidee.xlsx')
new_employee_df = pd.read_excel('New Employee_202502.xlsx')

passed_raewwadee = report_raewwadee_df[
    (report_raewwadee_df["Interview"] == "Yes") & (report_raewwadee_df["Status"] == "Pass")
].copy()
passed_pattama = report_pattama_df[
    (report_pattama_df["Interview"] == "Yes") & (report_pattama_df["Status"] == "Pass")
].copy()

passed_raewwadee["Team Member"] = "Raewwadee Jaidee"
passed_pattama["Team Member"] = "Pattama Sooksan"

interview_passed = pd.concat([passed_raewwadee, passed_pattama])

final_df = pd.merge(
    new_employee_df,
    interview_passed,
    how="inner",
    left_on=["Employee Name"],
    right_on=["Candidate Name"]
)
output_df = final_df[["Employee Name", "Join Date", "Role_x", "Team Member"]]
output_df.columns = ["Employee Name", "Join Date", "Role", "Team Member"]

#print(output_df)
st.dataframe(output_df)