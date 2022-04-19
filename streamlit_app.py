import streamlit as st

st.title('st.form')

st.header('Declared using the `with` statement')
with st.form('my_form'):
    st.write('**Order your coffee**')
    
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.markdown(f'''
        - Coffee bean: {coffee_bean_val}
        - Coffee roast: {coffee_roast_val}
        - Brewing: {brewing_val}
        - Milk: {milk_val}
        ''')

st.write('Outside the form')

#st.header('Declared using object notation')
#form = st.form('my_form_2')
