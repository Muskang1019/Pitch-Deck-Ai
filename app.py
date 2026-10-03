
import streamlit as st
from analyzer import extract_slides, analyze_deck


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PitchDeck AI",
    page_icon="🚀",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* ===============================
   MAIN PAGE
   =============================== */

.stApp {
    background-color: #0b1120 !important;
}

.block-container {
    max-width: 1150px;
    padding-top: 35px;
    padding-bottom: 50px;
}


/* ===============================
   ALL NORMAL TEXT
   =============================== */

p {
    color: #f1f5f9 !important;
}

label {
    color: #f1f5f9 !important;
}


/* ===============================
   HEADINGS
   =============================== */

h1 {
    color: #ffffff !important;
    font-size: 42px !important;
}

h2 {
    color: #ffffff !important;
    font-size: 30px !important;
}

h3 {
    color: #ffffff !important;
    font-size: 22px !important;
}


/* ===============================
   MARKDOWN CONTENT
   THIS FIXES DARK TEXT
   =============================== */

[data-testid="stMarkdownContainer"] {
    color: #f8fafc !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #f8fafc !important;
    font-size: 16px !important;
    line-height: 1.7 !important;
}

[data-testid="stMarkdownContainer"] li {
    color: #f8fafc !important;
    font-size: 16px !important;
    line-height: 1.7 !important;
}

[data-testid="stMarkdownContainer"] strong {
    color: #ffffff !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4 {
    color: #ffffff !important;
    margin-top: 20px !important;
    margin-bottom: 10px !important;
}

[data-testid="stMarkdownContainer"] h1 {
    font-size: 30px !important;
}

[data-testid="stMarkdownContainer"] h2 {
    font-size: 26px !important;
}

[data-testid="stMarkdownContainer"] h3 {
    font-size: 22px !important;
}


/* ===============================
   UPLOAD BOX
   =============================== */

[data-testid="stFileUploader"] {
    background-color: #111827 !important;
    border: 1px solid #334155 !important;
    border-radius: 14px !important;
    padding: 12px !important;
}

[data-testid="stFileUploaderDropzone"] {
    background-color: #111827 !important;
    border: 1px dashed #475569 !important;
    border-radius: 10px !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: #f8fafc !important;
}

[data-testid="stFileUploaderDropzone"] button {
    background-color: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
}


/* ===============================
   BUTTON
   =============================== */

.stButton > button {
    width: 100%;
    height: 52px;
    background-color: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background-color: #1d4ed8 !important;
}


/* ===============================
   METRICS
   =============================== */

[data-testid="stMetric"] {
    background-color: #111827 !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 15px !important;
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
}


/* ===============================
   ANALYSIS CARD
   =============================== */

.analysis-card {
    background-color: #111827;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 25px;
    margin-top: 15px;
}


/* ===============================
   TABS
   =============================== */

button[data-baseweb="tab"] {
    color: #94a3b8 !important;
    font-size: 16px !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #ffffff !important;
}


/* ===============================
   EXPANDER
   =============================== */

[data-testid="stExpander"] {
    background-color: #111827 !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

[data-testid="stExpander"] summary {
    color: #ffffff !important;
}

[data-testid="stExpander"] * {
    color: #f8fafc !important;
}


/* ===============================
   DOWNLOAD
   =============================== */

.stDownloadButton > button {
    width: 100%;
    height: 48px;
    background-color: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #475569 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.title("🚀 PitchDeck AI")

st.write(
    "Analyze your startup pitch deck and get structured AI-powered insights."
)

st.write("")


# =========================================================
# UPLOAD
# =========================================================

st.subheader("📄 Upload Pitch Deck")

uploaded_file = st.file_uploader(
    "Choose your PDF pitch deck",
    type=["pdf"]
)


# =========================================================
# AFTER UPLOAD
# =========================================================

if uploaded_file:

    st.success(
        f"📄 Uploaded: {uploaded_file.name}"
    )

    file_size = uploaded_file.size / (1024 * 1024)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "File Type",
            "PDF"
        )

    with col2:
        st.metric(
            "File Size",
            f"{file_size:.2f} MB"
        )

    with col3:
        st.metric(
            "AI Engine",
            "Gemini"
        )

    st.write("")


    # =====================================================
    # ANALYZE
    # =====================================================

    if st.button("🚀 Analyze Pitch Deck"):

        try:

            with st.spinner(
                "📄 Extracting information from your pitch deck..."
            ):

                slides = extract_slides(
                    uploaded_file
                )


            with st.spinner(
                "🤖 Gemini is analyzing your pitch deck..."
            ):

                analysis = analyze_deck(
                    slides
                )


            st.session_state["slides"] = slides
            st.session_state["analysis"] = analysis
            st.session_state["filename"] = uploaded_file.name


            st.success(
                "✅ Pitch deck analysis completed!"
            )


        except Exception as e:

            st.error(
                f"❌ Error: {e}"
            )


# =========================================================
# RESULTS
# =========================================================

if "analysis" in st.session_state:

    st.write("")

    st.header("📊 Analysis Results")

    slides = st.session_state["slides"]
    analysis = st.session_state["analysis"]


    # =====================================================
    # SUMMARY
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📑 Slides Analyzed",
            len(slides)
        )

    with col2:
        st.metric(
            "🤖 AI Model",
            "Gemini"
        )

    with col3:
        st.metric(
            "✅ Status",
            "Completed"
        )


    st.write("")


    # =====================================================
    # TABS
    # =====================================================

    analysis_tab, slides_tab = st.tabs(
        [
            "🧠 AI Analysis",
            "📑 Slide Breakdown"
        ]
    )


    # =====================================================
    # AI ANALYSIS
    # =====================================================

    with analysis_tab:

        st.markdown(
            '<div class="analysis-card">',
            unsafe_allow_html=True
        )

        st.markdown(analysis)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    # =====================================================
    # SLIDE BREAKDOWN
    # =====================================================

    with slides_tab:

        for slide in slides:

            with st.expander(
                f"📄 Slide {slide['number']}"
            ):

                if slide.get("image"):

                    st.image(
                        slide["image"],
                        use_container_width=True
                    )


                if slide.get("text"):

                    st.markdown(
                        "### 📝 Extracted Text"
                    )

                    st.write(
                        slide["text"]
                    )

                elif not slide.get("image"):

                    st.info(
                        "No text or image found on this slide."
                    )


    # =====================================================
    # DOWNLOAD
    # =====================================================

    st.write("")

    st.subheader("📥 Download Report")

    report = f"""
PITCHDECK AI ANALYSIS
=====================

File:
{st.session_state["filename"]}

Total Slides:
{len(slides)}

ANALYSIS
--------

{analysis}
"""

    st.download_button(
        "📥 Download Analysis",
        data=report,
        file_name="pitch_deck_analysis.txt",
        mime="text/plain"
    )


# =========================================================
# BEFORE UPLOAD
# =========================================================

else:

    st.info(
        "👆 Upload your pitch deck above to start the analysis."
    )
