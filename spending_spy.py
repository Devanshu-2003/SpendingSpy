import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Category keywords mapping
CATEGORY_KEYWORDS = {
    'Food': ['uber eats', 'swiggy', 'zomato', 'mcdonalds', 'pizza'],
    'Groceries': ['walmart', 'whole foods', 'trader joe', 'kroger'],
    'Rent': ['rent', 'apartment', 'lease'],
    'Entertainment': ['netflix', 'spotify', 'youtube'],
    'Utilities': ['electricity', 'gas', 'water', 'comcast', 'internet'],
    'Transport': ['uber', 'lyft', 'metro', 'gas station'],
    'Shopping': ['amazon', 'flipkart', 'target'],
    'Travel': ['airbnb', 'delta', 'hotel', 'make my trip'],
}

# Categorization function
def categorize(description):
    desc = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in desc for keyword in keywords):
            return category
    return "Other"

# Load and categorize CSV
def process_csv(file_input):
    # Make sure to rewind the file pointer if it's a file-like object (from Streamlit)
    if hasattr(file_input, 'seek'):
        file_input.seek(0)
    df = pd.read_csv(file_input)
    df.columns = [col.strip().lower() for col in df.columns]
    df['category'] = df['description'].apply(categorize)
    return df

# 🧠 Cluster using merchant + amount
def cluster_transactions(df, n_clusters=3):
    df_ml = df[['description', 'amount']].copy()
    df_ml['merchant_encoded'] = df_ml['description'].astype('category').cat.codes

    X = df_ml[['merchant_encoded', 'amount']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)

    print("\n🧠 Transaction Clustering Preview:")
    print(df[['description', 'amount', 'cluster']].head())

    return df

# 📊 Visualizations
def plot_category_summary(df):
    summary = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    summary.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax)
    ax.set_title('Spending Distribution by Category')
    ax.set_ylabel('')
    fig.tight_layout()
    return fig

def plot_bar_chart(df):
    summary = df.groupby('category')['amount'].sum().sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    summary.plot(kind='barh', color='skyblue', edgecolor='black', ax=ax)
    ax.set_xlabel('Total Amount Spent ($)')
    ax.set_title('Spending by Category (Bar Chart)')
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    fig.tight_layout()
    return fig

def analyze_monthly_spending(df):
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M').astype(str)
    monthly = df.groupby('month')['amount'].sum()
    fig, ax = plt.subplots(figsize=(6, 4))
    monthly.plot(kind='bar', color='orange', edgecolor='black', ax=ax)
    ax.set_title("Total Spending by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount ($)")
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    fig.tight_layout()
    return fig

def top_merchants(df, top_n=5):
    merchants = df.groupby('description')['amount'].sum().sort_values(ascending=False).head(top_n)
    fig, ax = plt.subplots(figsize=(6, 4))
    merchants.plot(kind='bar', color='green', edgecolor='black', ax=ax)
    ax.set_title(f"Top {top_n} Merchants by Total Spend")
    ax.set_xlabel("Merchant")
    ax.set_ylabel("Amount ($)")
    ax.tick_params(axis='x', rotation=30)
    fig.tight_layout()
    return fig

def cumulative_spending_trend(df):
    df['date'] = pd.to_datetime(df['date'])
    trend = df.groupby('date')['amount'].sum().cumsum()
    fig, ax = plt.subplots(figsize=(6, 4))
    trend.plot(kind='line', marker='o', color='purple', ax=ax)
    ax.set_title("Cumulative Spending Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Amount ($)")
    ax.grid(True, linestyle='--', alpha=0.7)
    fig.tight_layout()
    return fig

# 🔁 Main program
if __name__ == "__main__":
    file_path = "sample.csv"
    df = process_csv(file_path)

    print("\n🧾 Categorized Transactions:")
    print(df[['date', 'description', 'amount', 'category']])

    print("\n📊 Category Summary:")
    print(df.groupby('category')['amount'].sum().sort_values(ascending=False))

    plot_category_summary(df)
    plot_bar_chart(df)
    analyze_monthly_spending(df)
    top_merchants(df)
    cumulative_spending_trend(df)
    df = cluster_transactions(df)  # ML clustering added here
    export_to_csv(df)
