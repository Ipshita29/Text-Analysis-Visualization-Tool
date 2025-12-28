# Text Analysis & Visualization Tool

A beginner-friendly Python project that analyzes user-entered text, extracts simple textual statistics, and optionally visualizes numeric data using Matplotlib.

---

## ✨ Features

### 📊 Text Analysis
The tool extracts the following information from the input text:

- Sentence count  
- Word count  
- Average sentence length  
- Tone detection (Excited / Neutral)  
- Number detection (checks if the text contains numbers)  

### 📈 Visualization
- If numbers are present, they can be visualized using a simple graph.
- The graph is displayed directly (no file saving).

---

## 🛠️ Tech Stack

- Python 3  
- Matplotlib

No machine learning libraries are used. All logic is rule-based and fully explainable.

---

## 📁 Project Structure

```text
text-visualization-tool/
│
├── main.py            # Entry point
├── text_parser.py     # Text analysis logic
├── analyzer.py        # Numeric analysis
├── visualizer.py      # Data visualization
└── README.md
