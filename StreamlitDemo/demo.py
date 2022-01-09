import streamlit as st

def main():
    st.set_page_config(page_title="ENERGY DASHBOARD - Austin Texas", initial_sidebar_state="expanded", layout="wide")
    sections = {
        "Hola": 'hello.py',
        "Features": 'features.py'
    }
   
    apps = list(sections)
    key = st.sidebar.selectbox('Select an section',apps)
    st.sidebar.markdown('#')

    fname_to_run = sections[key]
    with open(fname_to_run, encoding="utf8") as f:
        filebody = f.read()
    exec(filebody,globals())

if __name__ == "__main__":
    main()