#%% #some preparation:
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
#%%



#plt.title("Tree Image")
#plt.xlabel("X pixel scaling")
#plt.ylabel("Y pixels scaling")


image = mpimg.imread("Resources/single_pink_tree_with_trunk.jpeg")
plt.imshow(image)
plt.axis('off')
plt.show()

#plt.savefig("test.png", bbox_inches='tight')

#%%

# Add to my streamlit app

st.title("La Bonne Fortune :sweat_drops: :sunny: :seedling:", anchor=None)
st.image(image)
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
