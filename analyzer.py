
import pdfplumber
import streamlit as st
from google import genai


# =========================================================
# EXTRACT SLIDES
# =========================================================

def extract_slides(pdf_file):
    """Extract both text and visual images from each PDF page."""

    slides = []

    with pdfplumber.open(pdf_file) as pdf:

        for i, page in enumerate(pdf.pages):

            # -----------------------------
            # Extract text
            # -----------------------------

            text = (
                page.extract_text(layout=True)
                or page.extract_text()
                or ""
            ).strip()

            # -----------------------------
            # Convert page to image
            # -----------------------------

            pil_image = None

            try:

                page_image = page.to_image(
                    resolution=120
                )

                pil_image = page_image.original

            except Exception:
                pil_image = None

            # -----------------------------
            # Store slide
            # -----------------------------

            slides.append({
                "number": i + 1,
                "text": text,
                "image": pil_image
            })

    return slides


# =========================================================
# ANALYZE DECK
# =========================================================

def analyze_deck(slides):
    """Analyze pitch deck using Gemini text + slide images."""

    # -----------------------------------------------------
    # API KEY
    # -----------------------------------------------------

    api_key = st.secrets.get(
        "GEMINI_API_KEY",
        ""
    )

    if not api_key:

        return """
⚠️ **Gemini API key is missing.**

Please check:

`.streamlit/secrets.toml`
"""


    # -----------------------------------------------------
    # GEMINI CLIENT
    # -----------------------------------------------------

    client = genai.Client(
        api_key=api_key
    )


    # -----------------------------------------------------
    # PROMPT
    # -----------------------------------------------------

    prompt = """
You are an expert startup pitch deck analyst.

Analyze the COMPLETE pitch deck using BOTH:

1. Extracted slide text
2. Visual information visible in the slide images

Important:
Charts, graphs, tables, logos, diagrams, screenshots,
numbers and visual elements may contain important information.

Do NOT assume information is missing just because it is
not available as extracted text.

Carefully inspect the visual slide content.

Provide the following:

# 1. Overall Assessment

Summarize what the startup does and the overall quality
of the pitch deck.

# 2. Problem

Identify the problem the startup is solving.

Include evidence from the slides.

# 3. Solution

Explain the product or solution.

# 4. Target Market

Identify:

- Target customers
- Market size
- TAM
- SAM
- SOM
- Geography

Only include values actually shown in the deck.

# 5. Business Model

Explain:

- How the company makes money
- Pricing
- Revenue model
- Customers
- Subscription or transaction model

Use information visible in the deck.

# 6. Competition

Identify:

- Competitors
- Competitive landscape
- Differentiation
- Competitive advantages

# 7. Team

Identify:

- Founders
- Key team members
- Their roles
- Relevant experience

# 8. Financial Information

Look carefully for:

- Revenue
- Growth
- Funding
- Valuation
- Expenses
- Projections
- Margins
- Financial charts
- Financial tables

# 9. Strengths

List the strongest aspects of the startup and pitch.

# 10. Weaknesses

Identify weaknesses, risks, missing information,
or unclear parts of the pitch.

# 11. Specific Recommendations

Give practical recommendations for improving the pitch deck.

# 12. Overall Score

Give an overall score from 0 to 100.

IMPORTANT RULES:

- Analyze BOTH text and images.
- Read charts and tables when possible.
- Do not invent facts.
- Do not assume information is missing until you have
  inspected the visual slide.
- If information truly cannot be found in either the text
  or visual content, say:
  "Not provided in the pitch deck."

Give detailed but easy-to-understand explanations.
"""


    # -----------------------------------------------------
    # BUILD CONTENT
    # -----------------------------------------------------

    contents = [prompt]


    # -----------------------------------------------------
    # ADD SLIDES
    # -----------------------------------------------------

    for slide in slides:

        slide_number = slide["number"]

        slide_text = slide.get(
            "text",
            ""
        )

        slide_image = slide.get(
            "image"
        )

        # Slide label

        contents.append(
            f"\n\n--- SLIDE {slide_number} ---"
        )

        # Text

        if slide_text:

            contents.append(
                f"\nExtracted text:\n{slide_text}"
            )

        else:

            contents.append(
                "\nNo selectable text was extracted."
            )

        # Image

        if slide_image:

            contents.append(
                slide_image
            )


    # -----------------------------------------------------
    # SEND TO GEMINI
    # -----------------------------------------------------

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=contents
        )

        if response.text:

            return response.text

        return """
⚠️ Gemini returned an empty response.
"""


    # -----------------------------------------------------
    # ERROR HANDLING
    # -----------------------------------------------------

    except Exception as e:

        error_message = str(e)

        if (
            "503" in error_message
            or "UNAVAILABLE" in error_message
        ):

            return """
⚠️ **Gemini is temporarily unavailable.**

The Gemini service returned a 503 error.

Please try the analysis again.
"""


        if (
            "429" in error_message
            or "RESOURCE_EXHAUSTED" in error_message
        ):

            return """
⚠️ **Gemini API limit reached.**

Please wait and try again.
"""


        if (
            "401" in error_message
            or "UNAUTHENTICATED" in error_message
        ):

            return """
⚠️ **Gemini authentication failed.**

Please check your API key.
"""


        return f"""
⚠️ **Gemini API error**

`{error_message}`
"""
