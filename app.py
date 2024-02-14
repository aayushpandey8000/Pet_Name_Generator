import langchain_helper as lh
import streamlit as st

# Display the GIF before the title


col1, col2 = st.columns([2, 8])  # Adjust the width ratio as needed
with col1:
    # Display the GIF with adjusted size
    st.image('pet-dog.gif', use_column_width=True,)

with col2:
    # Display the title
    st.title("Pet Name Generator")

# now sidebar and other components
user_pet=st.sidebar.selectbox("What is your pet?",("Cat","Dog","Cow","Parrot"))
if user_pet=='Cat':
    pet_color=st.sidebar.text_area(label="What colot is your Cat?",max_chars=15
    )
if user_pet=='Dog':
    pet_color=st.sidebar.text_area(label="What color is your Dog?",max_chars=15)

if user_pet=='Cow':
    pet_color=st.sidebar.text_area(label="What color is your Cow?",max_chars=15)

if user_pet=='Parrot':
    pet_color=st.sidebar.text_area(label="What color is your Parrot?",max_chars=15)



submit_button = st.sidebar.button("Generate Pet Name")

if submit_button:
    if pet_color:
        response = lh.generate_pet_name(user_pet, pet_color)
        st.write(response['name_pet'])