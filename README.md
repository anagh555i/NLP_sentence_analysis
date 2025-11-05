# NLP Sentence Analysis
A Jupyter‐Notebook based exploratory project analysing sentences using NLP techniques.

## 🧠 Overview
This project performs sentence‐level analysis on a given corpus of sentences (see `Sentences.csv`). It uses Python (in Jupyter notebooks) to explore, visualise, and extract insights from the text.  
It’s ideal for:
- Learning or demonstrating basic NLP workflows (tokenisation, POS, simple statistics).
- Rapid prototyping of sentence‐analysis pipelines.
- Educational or proof‐of‐concept usage.

## 📁 Repository Structure
```
/ (root)
│   .gitignore
│   INFO.txt
│   Sentences.csv             ← the main input dataset (sentences)
│   srs.csv                   ← secondary dataset / SRS annotations
│   srsCorpus.csv             ← corpus derived from SRS dataset
│
├── Main.ipynb                ← primary notebook: load data, analyse, visualise
├── TESTING.ipynb             ← notebook for experiments, tests, prototyping
└── SRS/                      ← folder containing “SRS” documentation or assets
    └── … 
```

## ✅ Features
- Load a sentence dataset and perform cleaning/pre‐processing.
- Exploratory data analysis (EDA): sentence length distributions, token counts, maybe POS tag counts.
- Visualisations embedded within Jupyter (histograms, bar charts etc).
- Modular notebook design: main pipeline + testing/experimentation notebook.
- Simple, clear structure so newcomers can follow and extend.

## 🚀 Getting Started
### Prerequisites
- Python 3.x installed
- Jupyter Notebook (or JupyterLab)
- Common NLP/data libraries (you can install via `pip`):
  ```bash
  pip install pandas numpy matplotlib seaborn nltk spacy
  ```

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/anagh555i/NLP_sentence_analysis.git
   cd NLP_sentence_analysis
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
3. Install dependencies (see above).
4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
   then open `Main.ipynb` and run the cells.

### Usage
- In `Main.ipynb`, cells walk you through: loading the CSV (`Sentences.csv`), inspecting the data, pre‑processing (tokenisation, cleaning), generating basic statistics, visualising distributions.
- In `TESTING.ipynb`, you can explore further ideas or test modifications (e.g., different tokenisers, POS tagging, named entities).
- Extend the project by adding new analyses (e.g., sentiment, clustering, topic modelling) or by applying to your own sentence corpus.

## 📐 Customisation & Extending
- Replace `Sentences.csv` with your own dataset of sentences (ensure similar format).
- Add new notebook(s) for advanced NLP tasks (e.g., using the spaCy library, word embeddings, transformer models).
- Modularise code (e.g., move common functions into `.py` modules) for reuse.
- Allow interactive dashboards (e.g., using Streamlit or Dash) on top of the analysis.

## 🔍 Insights & Findings
*(You can fill this section after you’ve run the analysis—mention interesting patterns you found, e.g., “Average sentence length is 12 words”, “Most common POS tag: noun”, etc.)*

## 🎓 Use Cases
- Academic/learning: Understand how sentence‐level NLP workflows work.
- Prototype for larger projects: Use as a starting point for text analytics.
- Data journalism: Quick snapshot of sentence characteristics in a dataset.

## 🤝 Contributing
If you’d like to contribute:
1. Fork the repo.
2. Create a branch: `git checkout -b feature/your‐feature`.
3. Make your changes, test them, commit.
4. Open a Pull Request describing your addition/improvement.
5. Ensure you update this README if you add major functionality.

## 📜 Licence
*(If you haven’t selected a licence yet, you might choose one – e.g., MIT License. Then mention it here.)*

---

**Author**: Anagh  
**Repository**: https://github.com/anagh555i/NLP_sentence_analysis
