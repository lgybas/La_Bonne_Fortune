#%% #some preparation:
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import datetime
import os
import glob
  





#import x

#%%



#with st.sidebar:
#    selected = option_menu("Étincelle de vie", ["Instants de Bonheur", 'Courants'], 
#        icons=['house', 'gear'], menu_icon="cast", default_index=1)
#    selected

#droplet
#magic
#moon-stars
#moisture
#music-note
#wind
#wallet2
#plus-circle-dottet
#cloud-plus
#clock-history
#clock
#chat-right-heart
#0-circle-fill
#1-circle-fill
#2-circle-fill
#arrow-down-circle-fill
#arrow-up-circle-fill


#### get all happy moments


#%%
# Add to my streamlit app
st.title("La Bonne Fortune :sweat_drops: :sunny: :seedling:", anchor=None)







image_tree = mpimg.imread("Resources/single_pink_tree_with_trunk.jpeg")
st.image(image_tree)
st.caption( "Encore et encore l'arbre m'a dit: **»I love you«** ")

# Quote für mich


st.header("Schöpferische Kreativität braucht einen guten Boden")

st.markdown(
"""
**Mein Reichtum ist meine schöpferische Kreativität.**   
    
_Schöpferisch kreativ sein_ heißt, dass ich aus mir selbst heraus Neues erschaffen kann.    
Dass ich Ideen _wahr_ nehme und _ernst_ nehme, die in mir schlummern.    
Und dass ich mich traue     
und dass ich mir Zeit und Raum gebe,   
diese Ideen wachsen zu lassen.

Dazu brauche ich einen guten und gesunden Boden. Mit _Boden_ meine ich insbesondere meinen Alltag aber auch meine Lebensumstände. 
Ich brauche einen Boden der mich trägt, der mich versorgt, der auch in einer ungewissen Zukunft leitet.   
Vor allem braucht dieser Boden einen wirksamen Zersetzungsprozess :cyclone: um Altes zu Zersetzen und brauchbare Nährstoffe zu extrahieren.
      
Wie merke ich dass mein Boden sich gesund entwickelt? 
Im täglichen und im längerfristigen möchte ich mehr Mut und Zeit haben um schöpferisch kreativ tätig zu sein. 
Um aus mir heraus Neues zu schaffen. Und den schlummernden Ideen Raum zum entfalten und Tun zu geben. 

Welche Landschaft aus diesem Reichtum wohl erwächst?

I love you.    
Liane
""")



st.code("""
In kurz:
1. Ich bin reich, wenn ich aus mir selbst heraus Neues erschaffen kann.
2. Der Boden bestimmt was auf ihm wachsen kann.
3. Um Neues aus mir erschaffen zu können, brauche ich einen guten, gesunden Boden  
""")



st.header("Projet minimal: Bien-être")

st.subheader("Courage")
esprit = st.slider("Un Esprit Clair", max_value=3, value=1)
libido = st.slider("Libido / Moteur interne", max_value=3, value=1)
profonde_satisfaction = st.slider("Sentiment d'être à la Bonne Place", max_value=3, value=1)

st.button("soumettre courage")

st.subheader("Temps")
time = st.slider("Temps Bien Dépensé (heures)", max_value=12, value=1)

st.button("soumettre temps")



#now show the output....

#seed_1.heic
image_seed = mpimg.imread("Resources/seed_1.jpg")
st.image(image_seed)



#Drei Töpfe
st.header("Projet minimal: Finances")
#Big decisions
st.subheader("Décisions Majeures")
#Topf 1 in grau + Summe, Topf 2 + Summe, Topf 3 + Summe

if "major_decisions" not in st.session_state:
    st.session_state.major_decisions = {
        "Prio":[],
        "Description":[],
         "Pot 2":[],
        "Pot 3":[],
         }

pot_3_init = 25000

if "pot_2_ideas_sum" not in st.session_state:
    st.session_state.pot_2_ideas_sum = 0

if "pot_3_ideas_sum" not in st.session_state:
    st.session_state.pot_3_ideas_sum = pot_3_init





col1, col2, col3 = st.columns(3)
col1.metric("Pot 1", "2,000 €", "+2%", delta_color="inverse")
col2.metric("Pot 2", st.session_state.pot_2_ideas_sum, "-8%", delta_color="inverse")
col3.metric("Pot 3", st.session_state.pot_3_ideas_sum, "+4%", delta_color="inverse")

st.markdown("""**Déclaration:**   
 **Pot 1** - la moyenne des dépenses bihebdomadaires    
 **Pot 2** - le total des dépenses annuelles  
 **Pot 3** - le total des investissements annuels""")


#Add a new major decision:
if st.checkbox("Nouveau Idée"):
    c1, c2, c3, c4 = st.columns(4)
    prio = c1.number_input("Prio", 0, 10)
    desc = c2.text_input("Description")
    pot_2 = c3.number_input("Pot 2", 0, 15000)
    pot_3 = c4.number_input("Pot 3", 0, 50000)

    if st.button("Ajouter"):
        st.session_state.major_decisions["Prio"].append(prio)
        st.session_state.major_decisions["Description"].append(desc)
        st.session_state.major_decisions["Pot 2"].append(pot_2)
        st.session_state.major_decisions["Pot 3"].append(pot_3)

        st.session_state.pot_2_ideas_sum += pot_2 
        st.session_state.pot_3_ideas_sum -= pot_2 

        


st.dataframe(st.session_state.major_decisions)

button_c1, button_c2 = st.columns(2)
button_c1.button("rafraichir")

today = datetime.datetime.today().strftime("%A")

file_name_major_dec = "Major_Decisions_" + today

button_c2.download_button("Save", data=pd.DataFrame(st.session_state.major_decisions).to_csv().encode('utf-8'), file_name=file_name_major_dec)


#wie füllt sich der topf 2
# unklare Übersicht



#Liste wo man decisions hinzufügen kann + Summe



# die Summen werden dann aus dem Topf 2 oder 3 abgezogen


#Drei Töpfe revisited
#Small decisions
st.subheader("Décisions Mineures")

#st.markdown(
#"""
#**Mein Reichtum ist meine schöpferische Kreativität**   
#_Schöpferisch kreativ sein_ heißt, dass ich aus mir selbst heraus Neues erschaffen kann.    
#Dass ich Ideen _wahr_ nehme und _ernst_ nehme, die in mir schlummern.    
#Und dass ich mich traue     
#und dass ich mir Zeit und Raum gebe,   
#diese Ideen wachsen zu lassen.
#    
#Dazu brauche ich einen guten und gesunden Boden. Mit _Boden_ meine ich insbesondere meinen Alltag aber auch meine Lebensumstände. 
#Ich brauche einen Boden der mich trägt, der mich versorgt, der auch in einer ungewissen Zukunft leitet.   
#Vor allem braucht dieser Boden einen wirksamen Zersetzungsprozess :cyclone: um Altes zu Zersetzen und noch brauchbare Nährstoffe zu extrahieren.
#   
#Mit dieser Übersicht verhelfe ich mir zu einem guten, gesunden Boden.   
#Sie lenkt meinen Blick auf die kleinen Details des Alltags, 
#um genau zu hin zu schauen, ob das was ich tue mir den Boden bereitet den ich suche. 
#   
#I love you.
#""")
#   
#- ob das was ich tue     
#- auch mit dem was ich brauche    
#- und mit dem was in mir     
#in Einklang ist.   


#st.markdown(
#"""
#Mein Reichtum ist meine schöpferische Kreativität   
#* dass ich Neues erschaffen kann, aus mir selbst heraus.  
#* dass ich Ideen ernst nehme, die in mir schlummern.  
#* dass ich mich traue, diese Ideen in Handlungen umzusetzen.  
#  
#Um Neues aus mir selbst erschaffen zu können, brauche ich einen guten und gesunden Boden.   
#Diese Übersicht hilft mir, einen guten gesunden Boden zu schaffen.   
#Wie sich meine schöpferische Kreativität dann im Alltag ausdrückt, das bleibt mir überlassen.  
  
#Let's get the facts right, to create a healthy soil.
#""")

#st.markdown(
#"""
#Mein Reichtum ist meine schöpferische Kreativität - dass ich Neues erschaffen kann, aus mir selbst heraus.  
#Mein Reichtum ist meine schöpferische Kreativität - dass ich Ideen ernst nehme, die in mir schlummern.  
#Mein Reichtum ist meine schöpferische Kreativität - dass ich mich traue, diese Ideen in Handlungen umzusetzen.  
#  
#Um Neues aus mir selbst erschaffen zu können, brauche ich einen guten und gesunden Boden. 
#""")#
#
#st.markdown("""Reichtum ist, wenn ich aus mir selbst heraus Neues erschaffen kann.  
#Der Boden bestimmt, was darauf wachsen kann.  
#Um Neues aus mir erschaffen zu können, brauche ich guten und gesunden Boden.  
#Und einen guten Zersetzungsprozess :cyclone:   
#I love you too.
#""")


#st.markdown("""Mein Reichtum ist, wenn ich aus mir selbst heraus Neues erschaffen kann.  
#Ob und was wachsen kann, wird von dem Boden bestimmt, in dem es Wurzeln schlägt.
#
#Um Neues aus mir erschaffen zu können, brauche ich guten und gesunden Boden.  
#Und einen guten Zersetzungsprozess :cyclone:   
#I love you too.
#""")

#st.markdown(""" Ich bin reich, wenn ich aus mir selbst heraus Neues erschaffen kann.
#Doch die Landschaft, die wachsen kann, wird durch die Bodenbeschaffenheit bestimmt. 


#Reichtum ist, wenn ich aus mir selbst heraus Neues erschaffen kann.  
#Der Boden bestimmt, was darauf wachsen kann.  
#Um Neues aus mir erschaffen zu können, brauche ich guten und gesunden Boden.  
#Und einen guten Zersetzungsprozess :cyclone:   
#I love you too.
#""")

#st.markdown("""
#Mein Reichtum ist meine schöpferische Kreativität - dass ich aus mir selbst heraus Neues erschaffen kann 
#und dass ich mich traue, die Potentiale und Ideen auszuschöpfen, die in mir schlummern. 
#Und gleichzeitig dafür sorge, dass ich auch morgen und übermorgen Zugang zu meiner schöpferischen Kreativität
#""")#




# Wellbeing
# Add title
# Add inputfield / Add Schieber
# Add 2 more inputfields


# Create a graph



#%%

# For later:

# Connect to database
# Save values to Database
# * Value1, value2, value3, name, datetimestamp, location (?)









# %%
