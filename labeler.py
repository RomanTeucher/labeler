import json

import streamlit as st

st.title("Data Preparation")
if "data" not in st.session_state:
    st.session_state["data"] = []


def save(title, text, source):
    if len(title.strip()) == 0:
        st.warning("Title cannot be empty")
        return
    if len(text.strip()) == 0:
        st.warning("Text cannot be empty")
        return
    if len(source.strip()) == 0:
        st.warning("Source cannot be empty")
        return

    #st.session_state["title"] = ""
    st.session_state["text"] = ""
    #st.session_state["source"] = ""

    st.session_state["data"] += [
        {"text": text, "source_document": source, "title": title}
    ]


def load():
    st.markdown(
        """
        <style>
  
            div[data-testid="column"]:nth-of-type(3)
            {
                
                text-align: end;
            } 
        </style>
        """,
        unsafe_allow_html=True,
    )

    title = st.text_input(label="Title", key="title")
    text = st.text_area(label="Text", key="text")
    source = st.text_input(label="Source", key="source")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.button(label="Submit", on_click=save, args=(title, text, source))
    with col3:
        st.download_button(
            label="Download",
            data=json.dumps(st.session_state["data"], indent=4),
            file_name="labeled.json",
            mime="application/json",
        )


if __name__ == "__main__":
    load()
