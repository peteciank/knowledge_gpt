import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload Trained Data in these formats: pdf, docx, or txt file📄\n"
            "3. (1) Ask to Write User Stories, Features, Estimate Effort or (2) Ask Questions About Scrum and SAFe💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste OpenAI API key here (sk-...)",
            help="Get API Key from Offering https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "🥋 AgileCop allows you to ask questions about your "
            "SAFe and Scrum Guide, and Estimate, or write User Stories and Features. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/peteciank) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by Pete Ciank and [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        faq()
