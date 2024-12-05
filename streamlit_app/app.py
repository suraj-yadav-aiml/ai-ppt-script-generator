import sys
import os

# Add the parent directory of the project to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import tempfile
from script_from_ppt import PowerPointProcessor,ScriptGenerator,Config

st.set_page_config(
    page_title="AI-Powered PPT Script Generator",
    page_icon=":robot_face:",
    layout="wide",
)


# Custom CSS for Enhanced Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f7fa;
        }
        h1, h2, h3 {
            color: #1f77b4; 
        }
        .stTextArea {
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 0.5rem;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
        }
        .stDownloadButton>button {
            background-color: #008CBA;
            color: white;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
        }
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1.5rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for file upload and settings
with st.sidebar:
    uploaded_file = st.file_uploader("Upload Your PowerPoint File (.pptx)", type=["pptx"])

    with st.expander(label="AI Model Settings"):
        model_name = st.selectbox(
            "Select AI Model",
            options=["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
            index=0,
            on_change=lambda: st.session_state.clear()
        )
        temperature = st.slider(
            "Set Model Creativity (Temperature)", min_value=0.0, max_value=1.0, value=0.8,
            on_change=lambda: st.session_state.clear()
        )

    Config.MODEL_NAME = model_name
    Config.TEMPERATURE = temperature

    st.markdown("---")
    st.markdown("Developed with ❤️ by **Suraj Yadav**")

if "context" not in st.session_state:
    st.session_state.context = None
if "generated_script" not in st.session_state:
    st.session_state.generated_script = None
if "generate_clicked" not in st.session_state:
    st.session_state.generate_clicked = False

st.title("🤖 AI-Powered PowerPoint Script Generator")
st.markdown("Upload your PowerPoint file and generate an engaging script for the slides!")


if uploaded_file:
    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        # Process PowerPoint only when "Generate Script" button is clicked
        if st.button("Generate Script"):
            st.session_state.generate_clicked = True
            processor = PowerPointProcessor(verbose=Config.VERBOSE)
            ppt_data = processor.extract_data(file_path=temp_file_path)

            # Generate context
            st.session_state.context = processor.build_context(ppt_data)
            st.session_state.generated_script = None  # Clear any previously generated script

        # Show extracted content if context is available
        if st.session_state.context:
            st.subheader("📖 Extracted Slide Content")
            st.text_area("Slide Content (Context)", st.session_state.context, height=300)

        # Generate the script only if button is clicked and context exists
        if st.session_state.generate_clicked and st.session_state.context:
            if st.session_state.generated_script is None:
                question = (
                    "For each PowerPoint slide provided above, write a 3-4 minute script "
                    "that effectively conveys the key points. Ensure a smooth flow between slides, "
                    "maintaining a clear and engaging narrative."
                )
                script_generator = ScriptGenerator()
                st.session_state.generated_script = script_generator.generate_script(
                    context=st.session_state.context, question=question
                )

            # Show the generated script
            st.subheader("🎬 Generated Script")
            st.text_area("Generated Script", st.session_state.generated_script, height=400)

            # Download Option
            st.download_button(
                label="📥 Download Script",
                data=st.session_state.generated_script,
                file_name="generated_script.txt",
                mime="text/plain",
            )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.warning("Please upload a PowerPoint file to start!")

