import streamlit as st

from coordinator import Coordinator

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Research Assistant")
st.caption("Search, Analyze and Generate Research Insights")

topic = st.text_input(
    "Research Topic",
    placeholder="Vision Transformer"
)

if st.button("Analyze Paper"):

    try:

        with st.spinner("Analyzing..."):

            coordinator = Coordinator()
            report = coordinator.run(topic)

    except Exception as e:

        st.error(str(e))
        st.stop()
    paper = report["paper"]

    st.success("Analysis completed!")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Authors", paper["num_authors"])

    with col2:
        st.metric("Published", paper["published"])

    with col3:
        st.metric("Field", report["research_field"])

    st.subheader("📄 Paper")

    st.write(f"**Title:** {paper['title']}")

    st.write(
        f"**Authors:** {', '.join(paper['authors'])}"
    )

    st.divider()

    st.subheader("🎯 Problem")

    st.write(report["problem"])

    st.subheader("⚙️ Method")

    st.write(report["method"])

    st.subheader("📈 Results")

    st.write(report["results"])

    st.subheader("🏷️ Keywords")

    st.write(", ".join(report["keywords"]))

    st.divider()

    st.subheader("📝 Executive Summary")

    st.write(report["summary"])

    st.divider()

    with st.expander("⚠️ Technical Limitations"):

        for item in report["technical_limitations"]:
            st.markdown(f"- {item}")

    with st.expander("🧪 Experimental Limitations"):

        for item in report["experimental_limitations"]:
            st.markdown(f"- {item}")

    with st.expander("🚀 Future Directions"):

        for item in report["future_directions"]:
            st.markdown(f"- {item}")

    with st.expander("💡 Research Ideas"):

        for item in report["research_ideas"]:
            st.markdown(f"- {item}")

    st.divider()

    st.download_button(
        "📥 Download Report",
        report["markdown"],
        file_name="research_report.md",
        mime="text/markdown"
    )