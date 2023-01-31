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

# Quote für mich
st.text( ' /"I love you./", dit Fred ')
st.text("Reichtum ist, wenn ich aus mir selbst heraus Neues erschaffen kann.")
st.text("Der Boden bestimmt, was darauf wachsen kann.")
st.text("Um Neues aus mir erschaffen zu können, brauche ich guten und gesunden Boden.")
st.text('Und einen guten Zersetzungsprozess :cyclone: ')


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
