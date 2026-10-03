# 🚀 PitchDeck AI — Startup Pitch Deck Analyzer

An AI-powered web application that analyzes startup pitch decks in PDF format and provides structured insights using **Google Gemini**.

The application extracts information from each slide, sends the content to Gemini for analysis, and presents the results through an interactive **Streamlit** dashboard.

---

## 📌 Project Overview

Evaluating a startup pitch deck manually can take significant time. PitchDeck AI automates the initial analysis process by extracting the content from a pitch deck and generating a structured report.

The application analyzes areas such as:

* 📋 Overall Assessment
* 🎯 Problem
* 💡 Solution
* 📈 Target Market
* 💰 Business Model
* ⚔️ Competition
* 👥 Team
* 💵 Financial Information
* 💪 Strengths
* ⚠️ Weaknesses
* 🔧 Recommendations
* 📊 Overall Score

If information is not available in the pitch deck, the application identifies it instead of inventing information.

---

## ✨ Features

### 📄 PDF Upload

Upload a startup pitch deck directly through the Streamlit interface.

### 🔍 Slide Text Extraction

The application extracts text from individual PDF pages using `pdfplumber`.

### 🤖 AI-Powered Analysis

Google Gemini analyzes the extracted pitch deck content and generates structured insights.

### 📊 Structured Results

The analysis is presented in clearly organized sections covering important startup and business areas.

### 📑 Slide-by-Slide Breakdown

Users can view:

* Individual slides
* Extracted text
* Slide previews when available

### 📥 Download Analysis

The generated analysis can be downloaded as a text report.

### 🎨 Interactive UI

The application uses a dark-themed Streamlit interface with:

* Upload section
* File information
* Analysis dashboard
* Tabs
* Slide expanders
* Download functionality

---

## 🛠️ Tech Stack

| Technology        | Purpose                        |
| ----------------- | ------------------------------ |
| Python            | Core programming language      |
| Streamlit         | Web application interface      |
| Google Gemini API | AI-powered pitch deck analysis |
| pdfplumber        | PDF text extraction            |
| Google GenAI SDK  | Gemini API integration         |

---

## 🏗️ Project Structure

```text
pitch-deck-analyzer/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

### `app.py`

Contains the Streamlit user interface, file upload functionality, analysis display, slide breakdown, and report download.

### `analyzer.py`

Handles:

* PDF processing
* Slide text extraction
* Gemini API communication
* Pitch deck analysis

### `requirements.txt`

Contains the Python packages required to run the application.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/pitch-deck-analyzer.git
```

### 2. Navigate to the project

```bash
cd pitch-deck-analyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Configuration

Create a `.streamlit` folder in the project directory:

```text
.streamlit/
└── secrets.toml
```

Inside `secrets.toml`, add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

### ⚠️ Important

Never upload your actual API key to GitHub.

Add this to `.gitignore`:

```text
.streamlit/secrets.toml
__pycache__/
*.pyc
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔄 How It Works

```text
        Upload PDF
            ↓
     Extract PDF Content
            ↓
      Extract Slide Text
            ↓
     Build AI Prompt
            ↓
      Google Gemini API
            ↓
     Analyze Pitch Deck
            ↓
   Structured AI Results
            ↓
      Streamlit Dashboard
            ↓
     Download Report
```

---

## 🧠 Analysis Workflow

### Step 1 — Upload

The user uploads a startup pitch deck in PDF format.

### Step 2 — PDF Processing

`pdfplumber` processes the PDF and extracts text from each page.

### Step 3 — Slide Organization

Each page is treated as an individual slide and stored with its slide number and extracted text.

### Step 4 — AI Analysis

The extracted content is sent to Google Gemini with instructions to analyze the startup pitch deck.

### Step 5 — Structured Output

Gemini generates an analysis covering the startup's:

* Problem
* Solution
* Market
* Business model
* Competition
* Team
* Financial information
* Strengths
* Weaknesses
* Recommendations

### Step 6 — Visualization

The results are displayed in the Streamlit dashboard.

---

## 📊 Example Output

The application generates sections such as:

```text
1. Overall Assessment

2. Problem

3. Solution

4. Target Market

5. Business Model

6. Competition

7. Team

8. Financial Information

9. Strengths

10. Weaknesses

11. Specific Recommendations

12. Overall Score
```

---

## 🎯 Use Cases

PitchDeck AI can be useful for:

* Startup founders
* Entrepreneurs
* Investors
* Startup analysts
* Business students
* Incubators and accelerators
* Early-stage startup evaluation

It can be used as an initial analysis tool before performing deeper business or financial due diligence.

---

## 🚀 Future Improvements

Possible future enhancements include:

* 📷 Visual analysis of slide layouts
* 📊 Automatic charts and scoring dashboards
* 💼 Investor-readiness analysis
* 📈 Market-size analysis
* 🏆 Startup scoring dashboard
* 🔎 Competitor research
* 📄 PDF report generation
* 💬 Chat with the pitch deck
* 🧠 RAG-based document question answering
* 📑 Support for PowerPoint files
* ☁️ Cloud deployment

---



Built as an AI/ML project to demonstrate practical skills in:

* Python
* Generative AI
* Gemini API
* Prompt Engineering
* PDF Processing
* Streamlit
* AI Application Development

---

## ⭐ Project Highlights

This project demonstrates an end-to-end Generative AI application workflow:

**PDF → Data Extraction → Prompt Engineering → Gemini API → AI Analysis → Streamlit UI**

If you found this project useful, consider giving the repository a ⭐.
