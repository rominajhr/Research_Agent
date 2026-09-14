# 🧠 AI Research Agent

An AI-powered research assistant that helps analyze research papers and generate structured research insights from a given topic.

The system uses a **multi-agent architecture** in which specialized agents handle different stages of the research workflow — from finding a relevant paper to analyzing it, generating a summary, identifying limitations, proposing research ideas, and producing a final report.

## ✨ Features

* 🔎 **Paper Search** — finds a relevant research paper based on a given topic
* 📄 **Paper Analysis** — analyzes the selected paper and extracts its main components
* 📝 **Summarization** — generates an executive summary of the research
* 🔍 **Critical Analysis** — identifies technical and experimental limitations
* 💡 **Research Ideas** — suggests potential future research directions
* 📊 **Structured Report** — combines all generated insights into a final research report
* 📥 **Markdown Export** — allows the generated report to be downloaded as a `.md` file
* 🖥️ **Streamlit Interface** — provides a simple web-based interface for interacting with the system

## 🏗️ Architecture

The project follows a multi-agent pipeline coordinated by a central `Coordinator`.

```text
                    Research Topic
                          │
                          ▼
                 ┌─────────────────┐
                 │   Search Agent  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Paper Analysis  │
                 │     Agent       │
                 └────────┬────────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
       ┌──────────┐ ┌──────────┐ ┌──────────┐
       │ Summary  │ │  Critic  │ │   Idea   │
       │  Agent   │ │  Agent   │ │  Agent   │
       └────┬─────┘ └────┬─────┘ └────┬─────┘
            │            │            │
            └────────────┼────────────┘
                         ▼
                ┌─────────────────┐
                │  Report Agent   │
                └────────┬────────┘
                         │
                         ▼
                  Research Report
                         │
                         ▼
                   Markdown (.md)
```

## 🤖 Agents

The system is composed of specialized agents, each responsible for a specific part of the research workflow:

| Agent                | Responsibility                                           |
| -------------------- | -------------------------------------------------------- |
| `SearchAgent`        | Finds a relevant research paper for the given topic      |
| `PaperAnalysisAgent` | Analyzes the selected paper                              |
| `SummaryAgent`       | Produces a concise research summary                      |
| `CriticAgent`        | Identifies technical and experimental limitations        |
| `IdeaAgent`          | Generates potential research ideas and future directions |
| `ReportAgent`        | Combines the results into a final structured report      |

The `Coordinator` manages the overall workflow and passes the output of each stage to the next agent.

## 📁 Project Structure

```text
Research_Agent/
│
├── agents/
│   ├── search_agent.py
│   ├── paper_analysis_agent.py
│   ├── summary_agent.py
│   ├── critic_agent.py
│   ├── idea_agent.py
│   └── report_agent.py
│
├── models/
│   └── ...
│
├── app.py
├── coordinator.py
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rominajhr/Research_Agent.git
cd Research_Agent
```

### 2. Create a virtual environment

It is recommended to use a virtual environment to keep the project dependencies isolated.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

If a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

### 4. Configure your model/API credentials

The agents require the appropriate model configuration and API credentials used by the project's model implementations.

Keep private credentials outside the repository and **never commit API keys or secrets to GitHub**.

### 5. Run the application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Then open the local URL provided by Streamlit in your browser.

## 🖥️ Usage

1. Enter a research topic in the **Research Topic** field.
2. Click **Analyze Paper**.
3. The system runs the research pipeline.
4. The interface displays:

   * Paper information
   * Research problem
   * Method
   * Results
   * Keywords
   * Executive summary
   * Technical limitations
   * Experimental limitations
   * Future directions
   * Research ideas
5. Download the generated report as a Markdown file.

### Example

```text
Research Topic:
Vision Transformer
```

The system then processes the topic through the multi-agent pipeline and generates a structured research report.

## 📄 Generated Report

The final report contains several sections designed to provide a quick but structured understanding of the selected research paper:

* **Paper Information**
* **Problem**
* **Method**
* **Results**
* **Keywords**
* **Executive Summary**
* **Technical Limitations**
* **Experimental Limitations**
* **Future Directions**
* **Research Ideas**

The report can be downloaded directly from the Streamlit interface as:

```text
research_report.md
```

## 🛠️ Technology Stack

* **Python**
* **Streamlit** — web interface
* **LLM-based Agents** — research and analysis
* **Multi-Agent Architecture** — task decomposition and specialization
* **Markdown** — report generation

## 🎯 Project Goal

The goal of this project is to explore how **LLM-based multi-agent systems can support academic research workflows**.

Instead of relying on a single model to perform every task, the system separates the research process into specialized stages. This makes it possible to independently improve different parts of the workflow, such as paper search, analysis, critique, and research idea generation.

## 🔮 Future Improvements

Potential directions for extending the project include:

* [ ] Support analysis of multiple papers
* [ ] Add paper comparison capabilities
* [ ] Add citation/reference extraction
* [ ] Improve paper search and retrieval
* [ ] Add structured literature-review generation
* [ ] Add experiment/reproduction assistance
* [ ] Add persistent research history
* [ ] Improve agent evaluation and reliability
* [ ] Add configurable LLM providers
* [ ] Add automated tests for individual agents
* [ ] Add support for exporting reports to PDF or LaTeX

## 📌 Status

This project is currently under development and is intended as an experimental implementation of an AI-assisted academic research workflow.

## 👤 Author

**Romina Johari**

GitHub: [@rominajhr](https://github.com/rominajhr)
