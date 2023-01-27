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

# %%
