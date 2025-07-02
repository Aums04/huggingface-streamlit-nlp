import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")
st.write("Welcome to my first Streamlit app!")

# st.header("Header Example")
# st.subheader("Subheader Example")
# st.markdown("**Markdown** and _formatting_ supported!")
# st.code("print('Hello, World!')", language="node")
# st.latex(r"E=a^2+b^2")

# st.text_input("Text Input", key="text_input")
# st.text_area("Text Area", key="text_area")
# st.number_input("Number Input", min_value=0, max_value=100, key="number_input")
# st.date_input("Date Input", key="date_input")
# st.time_input("Time Input", key="time_input")
# st.file_uploader("Upload a file", key="file_uploader")
# st.checkbox("Check me!", key="checkbox")
# st.radio("Choose one", ["Option 1", "Option 2", "Option 3"], key="radio")
# st.selectbox("Select an option", ["A", "B", "C"], key="selectbox")
# st.multiselect("Select multiple", ["X", "Y", "Z"], key="multiselect")
# st.slider("Slide me!", 0, 10, 5, key="slider")
# st.button("Click Me!", key="button")
# st.color_picker("Pick a color", key="color_picker")

# st.success("This is a success message!")
# st.info("This is an info message.")
# st.warning("This is a warning message.")
# st.error("This is an error message.")
# st.exception(Exception("This is an exception message."))

data = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
st.dataframe(data)
st.table(data.head())
st.line_chart(data)
st.map()  # Shows a blank map

st.sidebar.title("Sidebar Title")
st.sidebar.button("Sidebar Button")