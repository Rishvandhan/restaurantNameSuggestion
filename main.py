import helper
import streamlit as st

st.title("Restaurant Name Generator")

# Sidebar cuisine selection
# Add an image from a local file
st.sidebar.image("Resources/logo.jpg", caption="Large Language Models", use_container_width=True)
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Select a Cuisine", "Indian", "Italian", "Mexican", "Arabic", "American"))



# Wait until a valid cuisine is selected
if cuisine and cuisine != "Select a Cuisine":  # Check to avoid default state
    if cuisine == "Indian":
        st.sidebar.image("Resources/India.jpg", caption="Indian Cuisine", use_container_width=True)
        st.image("Resources/Indian_food.jpg", caption="Delicious Dishes", use_container_width=True)
    elif cuisine == "Italian":
        st.sidebar.image("Resources/Itali.jpg", caption="Italian Cuisine", use_container_width=True)
        st.image("Resources/Italian_food.jpg", caption="Delicious Dishes", use_container_width=True)
    elif cuisine == "Mexican":
        st.sidebar.image("Resources/Mexico.jpg", caption="Mexican Cuisine", use_container_width=True)
        st.image("Resources/Mexican_food.jpg", caption="Delicious Dishes", use_container_width=True)
    elif cuisine == "Arabic":
        st.sidebar.image("Resources/Arabia.jpg", caption="Arabic Cuisine", use_container_width=True)
        st.image("Resources/Arabic_food.jpg", caption="Delicious Dishes", use_container_width=True)
    elif cuisine == "American":
        st.sidebar.image("Resources/America.jpg", caption="American Cuisine", use_container_width=True)
        st.image("Resources/Amreican_food.jpg", caption="Delicious Dishes", use_container_width=True)

    
    with st.spinner("Generating restaurant name and menu items... This website has been built with free resources, so free things take time in this world. Please wait for about a minute."):
        response = helper.generate_name_items(cuisine)  # Call your helper function
    st.success("Done!")
    
    # Display restaurant name and menu items
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    for item in menu_items:
        st.write("-", item)
else:
    st.write("Please select a cuisine from the dropdown menu.")
    st.write(helper.dummy())