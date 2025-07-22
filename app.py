import streamlit as st
from personas import devops_interface

# Persona options
personas = ['DevOps Engineer', 'Data Scientist', 'Product Manager']

def main():
    # App title
    #st.title("Persona Selector")

    if "step" not in st.session_state:
        st.session_state.step = 1
    if "persona" not in st.session_state:
        st.session_state.persona = None
    if "action" not in st.session_state:
        st.session_state.action = None

    # Step 1: Persona selection
    if st.session_state.step == 1:
        st.write("I am a", end=" ")
        persona = st.selectbox(
            "Select your persona:",
            personas,
            key="persona_select",
            label_visibility="collapsed"
        )
        if st.button("Continue »"):
            st.session_state.persona = persona
            st.session_state.step = 2

    # Step 2: Persona-specific screen
    if st.session_state.step == 2:
        # Call the appropriate persona module
        if st.session_state.persona == "DevOps Engineer":
            selected_action = devops_interface()
        else:
            st.write(f"I want to", end=" ")
            selected_action = st.selectbox(
                "",
                ["Learn", "Resolve a Query", "Have it done for me with AI"],
                key="generic_action",
                label_visibility="collapsed"
            )
        if st.button("Continue »", key="action_continue"):
            st.session_state.action = selected_action
            st.session_state.step = 3

    # Step 3: Show summary (optional)
    if st.session_state.step == 3:
        st.success(f"Persona: **{st.session_state.persona}**\n\nAction: **{st.session_state.action}**")
        if st.button("Start Over"):
            st.session_state.step = 1
            st.session_state.persona = None
            st.session_state.action = None

if __name__ == "__main__":
    main()
