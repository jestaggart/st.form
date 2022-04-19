import streamlit as st

st.title('st.form')

st.header('Declared using the `with` statement')
with st.form('my_form'):
    st.write('**Order your coffee**')
    
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    cofee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    milk_val = st.checkbox('Milk')

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Coffee bean: ', coffee_bean_val)
        st.write('Coffee roast: ', coffee_roast_val)
        st.write('Brewing: ', brewing_val)
        st.write('Milk: ', milk_val)

st.write('Outside the form')
st.write(brewing_val)

#st.header('Declared using object notation')
#form = st.form('my_form_2')
