# 💸 SpendingSpy: Personal Finance Analyzer

SpendingSpy is a simple yet powerful web app that lets you upload your bank/exported transaction CSV and automatically:

- 🔍 Categorize transactions into spending categories
- 📊 Visualize your expenses (pie, bar, trend, merchant charts)
- 🧠 Cluster spending patterns using KMeans
- 📥 Download a clean, categorized, and clustered CSV

Built with **Python**, **Streamlit**, **pandas**, and **scikit-learn**.

---

## 🚀 Features

- Upload transaction CSV
- Auto-categorization based on keywords
- Spending breakdown (pie & bar)
- Monthly and cumulative trend analysis
- Top merchants visual
- ML-based clustering on amount + merchant
- Download cleaned CSV output

---

## 📁 File Structure

```
SpendingSpy/
├── streamlit_app.py          # Streamlit UI script
├── spending_spy.py           # Core logic: categorize, cluster, visualize
├── sample_spending_spy.csv   # Demo input file
├── categorized_output.csv    # Sample generated output
└── assets/                   # (optional) screenshots or GIFs
```

---

## 📷 Preview

### 🧾 Categorized Transactions
![Transactions](https://via.placeholder.com/800x300?text=Sample+Table)

### 📊 Visualizations
![Charts](https://via.placeholder.com/800x400?text=Spending+Charts)

---

## 🛠️ How to Run

1. Install dependencies:

```bash
pip install streamlit pandas matplotlib scikit-learn
```

2. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

3. Upload your CSV and explore your financial insights!

---

## 🧪 Sample CSV Format

```csv
date,description,amount
2024-03-01,Uber Eats,22.5
2024-03-02,Walmart,56.9
...
```

---

## 📥 Output (CSV)

The downloaded file includes:
- `date`, `description`, `amount`
- Auto-generated `category`
- ML-assigned `cluster`
- Derived `month`

---

## 🏷️ Tags

`#fintech` `#streamlit` `#python` `#ml` `#data-viz`

---

