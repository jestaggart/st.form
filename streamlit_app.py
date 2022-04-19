import streamlit as st

st.title('st.form')

st.header('Declared using the `with` statement')
with st.form('my_form'):
    st.write('Inside the form')
    cofee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark])
    checkbox_val = st.checkbox('Form checkbox')

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Coffee roast: ', coffee_roast_val)

st.write('Outside the form')

#st.header('Declared using object notation')
#form = st.form('my_form_2')
