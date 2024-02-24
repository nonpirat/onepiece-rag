import helper as h
import streamlit as st

st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))

pet_color = st.sidebar.text_area("What color is your {}?".format(animal_type), max_chars=15)

number = st.sidebar.text_area("How many names do you want?", max_chars=2)

if animal_type:
    if pet_color:
        if number:
            response = h.generate_pet_name(n=number, animal=animal_type, pet_color=pet_color)
            st.text(response)