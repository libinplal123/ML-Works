import streamlit as st
st.title(":red[Calculator]")
num1 = st.number_input("enter number 1")
num2 = st.number_input("enter number 2")
choice = st.selectbox("select your option",['ADD','SUB','DIV'])
if st.button("CALCULATE"):
    if choice=="ADD":
        result = num1+num2
        st.success(f"addition result {result}")
    elif choice=="SUB":
        result = num1-num2
        st.success(f"subtraction result {result}")
    elif choice=="DIV":
        result = num1/num2
        st.success(f"division result {result}")
