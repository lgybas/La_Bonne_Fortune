import streamlit as st
import os
import glob
import pandas as pd
import datetime

st.markdown("# Instants de Bonheur")
#st.sidebar.markdown("# Page 2 ❄️")

#add the happy_moments variable to session_state
if "happy_moments" not in st.session_state:
    st.session_state.happy_moments = []
#    st.session_state.happy_moments = {
#        "moment_desc":[],
#        "moment_datetime":[],
#        "moment_loc":[]
#         }

# use glob to get all the csv files 
# in the folder
#st.button("load data", key="initial_load")

happy_moments_file_name = "Happy_Moments.csv"

if st.button("load data", key="initial_load"):
    path = "/Users/liane/Downloads"
    csv_files = glob.glob(os.path.join(path, happy_moments_file_name))
    if len(csv_files) > 0:
        st.session_state.happy_moments = pd.read_csv((path + "/" + happy_moments_file_name), index_col=False)

st.write(st.session_state.happy_moments)

happy_moment = pd.DataFrame()
happy_moment["moment_desc"] = st.text_area("moments de bonheur")
#mom_desc = st.text_area("moments de bonheur")

mom_col1, mom_col2, mom_col3 = st.columns(3)
happy_moment["moment_datetime"] = mom_col1.text_input("date and time") # add date time
happy_moment["moment_loc"]= mom_col2.text_input("location") # add location

#mom_datetime = mom_col1.text_input("date and time") # add date time
#mom_loc= mom_col2.text_input("location") # add location
# add people?
#mom_col3.button("Ajoute moment", key="moment add")

if mom_col3.button("Ajoute moment", key="moment add"):
    st.session_state.happy_moments = pd.concat([st.session_state.happy_moments, happy_moment], ignore_index = True)
    st.write(happy_moment)
#    st.session_state.happy_moments["moment_desc"].append(mom_desc)
#    st.session_state.happy_moments["moment_datetime"].append(mom_datetime)
#    st.session_state.happy_moments["moment_loc"].append(mom_loc)


mom_button_c1, mom_button_c2 = st.columns(2)
mom_button_c1.button("rafraichir")

today = datetime.datetime.today().strftime("%A")


mom_button_c2.download_button("Save", data=pd.DataFrame(st.session_state.happy_moments).to_csv(index=False).encode('utf-8'), file_name=happy_moments_file_name)


happy_moments = pd.DataFrame(st.session_state.happy_moments)
st.table(happy_moments)


