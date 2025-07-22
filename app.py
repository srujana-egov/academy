import streamlit as st

# Persona options
personas = ['DevOps Engineer', 'Data Scientist', 'Product Manager']

# Second step options
actions = ['Learn', 'Resolve a query', 'Have it done for me with AI']

def main():
    # Page 1: Choose persona
    st.title("Persona Selector")
    st.write("I am a", end=" ")

    # Keep persona in session state
    if 'persona' not in st.session_state:
        st.session_state.persona = None
    if 'action' not in st.session_state:
        st.session_state.action = None

    persona = st.selectbox("Select your persona:", personas, 
        key='persona', label_visibility='collapsed')

    # Continue button
    if st.button("Continue »", key="continue_1"):
        st.session_state.persona = persona

    # If persona selected, show the second page
    if st.session_state.persona:
        st.write(f"### You are a: {st.session_state.persona}")
        st.write("I want to", end=" ")
        action = st.selectbox("Select your action:", actions, key='action', label_visibility='collapsed')
        if st.button("Go »", key="continue_2"):
            st.session_state.action = action

    # If action selected, show final result
    if st.session_state.action:
        st.success(f"Persona: **{st.session_state.persona}**\n\nAction: **{st.session_state.action}**")
        # You can render the specific interface for the persona and action here

if __name__ == "__main__":
    main()
