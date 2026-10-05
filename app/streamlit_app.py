import streamlit as st
from app.llm_service import analyze_call
from app.rag_service import retrieve_knowledge


st.set_page_config(
    page_title="Enterprise IT Support Intelligence",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI-Powered Enterprise IT Support Intelligence")

st.markdown(
    """
    **Enterprise IT Support Intelligence Platform**

    Analyze employee IT support requests using a hybrid AI pipeline
    combining rule-based NLP, ChromaDB retrieval, and Ollama-powered
    Gemma 3 recommendations.
    """
)

st.divider()


# --------------------------------------------------
# Request Input
# --------------------------------------------------

st.subheader("🎫 Employee IT Support Request")

sample_issues = {
    "VPN Issue":
        "My company VPN keeps disconnecting while I am working from home.",

    "Outlook Issue":
        "My Outlook is not opening and I need access to my email for an important meeting.",

    "Password Issue":
        "I forgot my company password and my account is locked after several failed login attempts.",

    "Wi-Fi Issue":
        "My office Wi-Fi is not connecting while other employees are connected."
}


selected_issue = st.selectbox(
    "Try a sample enterprise IT issue",
    ["Custom Request"] + list(sample_issues.keys())
)


if selected_issue != "Custom Request":
    default_text = sample_issues[selected_issue]
else:
    default_text = ""


conversation = st.text_area(
    "IT Support Request",
    value=default_text,
    placeholder="Describe the employee's IT issue...",
    height=140
)


# --------------------------------------------------
# Analyze Request
# --------------------------------------------------

if st.button("🔍 Analyze IT Issue", type="primary"):

    if not conversation.strip():

        st.warning("Please enter an IT support request.")

    else:

        with st.spinner("Analyzing request with AI..."):

            result = analyze_call(conversation)

            retrieved_knowledge = retrieve_knowledge(
                conversation,
                n_results=2
            )


        st.success("Analysis completed successfully.")


        # --------------------------------------------------
        # KPI Cards
        # --------------------------------------------------

        st.subheader("📊 Ticket Analysis")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Intent",
                result["intent"]
            )

        with col2:
            st.metric(
                "Sentiment",
                result["sentiment"]
            )

        with col3:
            st.metric(
                "Priority",
                result["priority"]
            )

        with col4:
            st.metric(
                "Support Queue",
                result["queue"]
            )


        # --------------------------------------------------
        # AI / RAG Status
        # --------------------------------------------------

        st.subheader("🧠 AI Intelligence")

        col1, col2 = st.columns(2)

        with col1:
            st.info(
                "🤖 **Gemma 3 AI Recommendation**\n\n"
                "Recommendation generated using Ollama."
            )

        with col2:
            st.success(
                "📚 **RAG Knowledge Grounding**\n\n"
                f"{len(retrieved_knowledge)} relevant knowledge documents retrieved."
            )


        # --------------------------------------------------
        # Ticket Summary
        # --------------------------------------------------

        st.subheader("📝 Ticket Summary")

        st.write(
            result["summary"]
        )


        # --------------------------------------------------
        # Support Routing
        # --------------------------------------------------

        st.subheader("🎯 Support Routing")

        st.info(
            f"Recommended Support Queue: **{result['queue']}**"
        )


        # --------------------------------------------------
        # Baseline Recommendation
        # --------------------------------------------------

        st.subheader("🛠️ Baseline Recommendation")

        st.write(
            result["recommendation"]
        )


        # --------------------------------------------------
        # AI Recommendation
        # --------------------------------------------------

        st.subheader("🤖 AI Recommendation")

        st.success(
            result["ai_recommendation"]
        )


        # --------------------------------------------------
        # Retrieved Knowledge
        # --------------------------------------------------

        st.subheader("📚 Retrieved Knowledge")

        st.caption(
            "Knowledge retrieved from the enterprise IT support knowledge base "
            "and provided to the Gemma 3 model."
        )


        for index, document in enumerate(
            retrieved_knowledge,
            start=1
        ):

            with st.expander(
                f"Knowledge Source {index}"
            ):

                st.code(
                    document,
                    language="text"
                )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "AI-Powered Enterprise IT Support Intelligence | "
    "Python • NLP • ChromaDB • RAG • Ollama • Gemma 3 • Streamlit"
)
