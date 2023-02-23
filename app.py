import streamlit as st
import openai
import os


def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=10,
        )["choices"][0]["text"]
    except Exception as e:
        # alert exception message to streamlit
        st.write(e)
        


# initialize openai api key
openai.api_key = os.getenv('OPENAI_KEY')

try:
    st.title("Text Summarizer")

    # initialize state variable 
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    input_text = st.text_area(label='Enter full text:', value="", height=250)

    # st.button("submit")
    st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )


    # configure text area to populate with current state of summary
    output_text = st.text_area(label='Summarized text:', value=st.session_state["summary"], height=250)
except:
    st.write("Error")
    st.write("Please check your internet connection and try again.")
    st.write("If the problem persists, please contact support.")
