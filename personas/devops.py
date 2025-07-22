# personas/devops.py

import streamlit as st

def devops_interface():
    # Create vertical space to help center
    st.markdown('<div style="height: 33vh;"></div>', unsafe_allow_html=True)

    # Center the sentence and dropdown horizontally
    st.markdown(
        """
        <div style="display:flex; justify-content:center; align-items:center;">
            <h2 style="margin-right:16px;">I want to</h2>
        """,
        unsafe_allow_html=True,
    )
    # Dropdown (Streamlit cannot be truly inside HTML: render below and hide the label)
    selected_action = st.selectbox(
        '',
        ['Learn', 'Resolve a Query', 'Have it done for me with AI'],
        key='devops_action',
        label_visibility='collapsed'
    )

    st.markdown("</div>", unsafe_allow_html=True)
    return selected_action
