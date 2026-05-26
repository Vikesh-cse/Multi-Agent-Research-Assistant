import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 AI Research Assistant")
st.caption("Powered by Multi-Agent AI • Tavily • Groq • LangChain")

st.divider()

topic = st.text_input(
    "Research Topic",
    placeholder="Future of AI Agents in Healthcare"
)

col1, col2 = st.columns([1, 4])

with col1:
    run_btn = st.button(
        "🚀 Start Research",
        use_container_width=True
    )

if run_btn:

    if not topic:
        st.warning("Please enter a research topic.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    status.info("🌐 Search Agent working...")
    progress.progress(25)

    result = run_research_pipeline(topic)

    progress.progress(100)
    status.success("✅ Research Complete")

    tab1, tab2 = st.tabs([
        "📑 Report",
        "🧐 Critic Review"
    ])

    with tab1:
        st.markdown(result["report"])

    with tab2:
        st.markdown(result["review"])