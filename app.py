import streamlit as st
from personas import devops_interface

personas = ['DevOps Engineer', 'Data Scientist', 'Product Manager']

def main():
    if "step" not in st.session_state:
        st.session_state.step = 1
    if "persona" not in st.session_state:
        st.session_state.persona = None
    if "action" not in st.session_state:
        st.session_state.action = None

    # PAGE 1: Persona selection
    if st.session_state.step == 1:
        st.markdown(
            """
            <div style="height:20vh;"></div>
            <div style="display: flex; justify-content: center; align-items: center;">
                <span style="font-size:400%; font-weight: bold; margin-right: 20px;">
                    I am a
                </span>
                <div>
            """,
            unsafe_allow_html=True,
        )
        persona = st.selectbox(
            "",
            personas,
            key="persona_select",
            label_visibility="collapsed"
        )
        st.markdown("</div></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([4, 2, 4])
        with col2:
            if st.button("Continue »", use_container_width=True, key="continue1"):
                st.session_state.persona = persona
                st.session_state.step = 2

    # PAGE 2: Action selection—"I want to" big and centered, dropdown directly below
    elif st.session_state.step == 2:
        st.markdown(
            """
            <div style="height:20vh;"></div>
            <div style="display: flex; flex-direction: column; align-items: center;">
                <span style="font-size:400%; font-weight: bold;">I want to</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.session_state.persona == "DevOps Engineer":
            selected_action = devops_interface()
        else:
            selected_action = st.selectbox(
                "",
                ["Learn", "Resolve a Query", "Have it done for me with AI"],
                key="generic_action",
                label_visibility="collapsed"
            )
        col1, col2, col3 = st.columns([4, 2, 4])
        with col2:
            if st.button("Continue »", use_container_width=True, key="action_continue"):
                st.session_state.action = selected_action
                st.session_state.step = 3

    # PAGE 3: Optional summary/final step
    elif st.session_state.step == 3:
        st.markdown("<div style='height:15vh;'></div>", unsafe_allow_html=True)
        st.markdown(
            f"<h3 style='text-align:center;'>Persona: <b>{st.session_state.persona}</b></h3>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h3 style='text-align:center;'>Action: <b>{st.session_state.action}</b></h3>",
            unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns([4, 2, 4])
        with col2:
            if st.button("Start Over", use_container_width=True):
                st.session_state.step = 1
                st.session_state.persona = None
                st.session_state.action = None

if __name__ == "__main__":
    main()
