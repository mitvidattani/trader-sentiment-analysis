# 📊 Trader Performance vs Market Sentiment Analysis

## 📌 Objective

This project analyzes how market sentiment (Fear vs Greed) impacts trader behavior and performance using real-world trading data.

The goal is to uncover actionable patterns that can help traders make more informed, risk-aware decisions under different market conditions.

---

## 📂 Datasets Used

1. **Bitcoin Market Sentiment Dataset**

   * Features: Date, Sentiment Classification (Fear, Greed, etc.)
   * Represents overall market psychology

2. **Historical Trader Data (Hyperliquid)**

   * Features: Account, Trade Size, Direction, Closed PnL, Timestamp, etc.
   * Captures trader-level behavior and performance

---

## ⚙️ Methodology

### 1. Data Preparation

* Cleaned datasets (handled missing values, removed duplicates)
* Standardized column formats
* Converted timestamps to daily level

### 2. Data Alignment

* Merged trading data with sentiment data using date
* Ensured each trade is mapped to corresponding market sentiment

### 3. Feature Engineering

Created key trader-level daily metrics:

* **Daily PnL (USD)** → profitability
* **Win Rate (0–1)** → consistency
* **Average Trade Size (USD)** → risk appetite
* **Trades per Day (count)** → activity level
* **Long Ratio (0–1)** → directional bias

### 4. Analysis

* Compared performance across sentiment regimes
* Analyzed behavioral shifts (activity, size, direction)
* Evaluated risk using drawdown proxy

### 5. Visualization

* Used bar charts, boxplots, scatter plots, and distributions
* Explored relationships between risk and returns

---

## 🔍 Key Insights

* **Volatility Drives Profitability:**
  Traders achieve highest average PnL during Fear (~5300 USD), indicating that volatile markets offer strong opportunities.

* **Greed Increases Risk Exposure:**
  Despite high win rates (~38.6%), Greed phases show extreme downside risk (losses up to -358K USD), suggesting overconfidence.

* **Panic-Driven Trading Behavior:**
  Trading activity peaks during Extreme Fear (~134 trades/day), indicating emotional and reactive trading patterns.

* **Higher Risk-Taking During Fear:**
  Traders take larger positions during Fear (~8975 USD), contrary to expectations of risk aversion.

* **Profitability is Highly Skewed:**
  Most trades yield minimal returns, while a small number of large trades drive overall profitability.

---

## 💡 Strategy Recommendations

* **Control Risk During Greed:**
  Reduce position sizes and enforce strict stop-loss rules to avoid extreme losses.

* **Limit Overtrading in Fear:**
  Introduce trade limits or cooldown strategies to avoid impulsive decisions.

* **Leverage Volatility Selectively:**
  Experienced traders can capitalize on Fear-driven volatility with disciplined execution.

* **Align with Market Momentum:**
  Favor long positions during Greed phases while remaining cautious during Fear.

---

## 📊 Sample Visualizations

* PnL Distribution Across Sentiment
* Trade Size vs Profitability
* Correlation Heatmap of Trading Metrics
* Time-Series Trend of Trader PnL

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

Open and run:

```id="8dr6qk"
notebooks/01_analysis.ipynb
```

---

## 📈 Future Improvements

* Build predictive model for trader profitability
* Cluster traders into behavioral segments
* Create interactive dashboard (Streamlit)

---

## 📎 Conclusion

Market sentiment significantly influences both trader behavior and performance.

While Fear phases provide higher opportunities due to volatility, Greed phases introduce extreme risk. Effective strategies must adapt dynamically to sentiment conditions, balancing opportunity with disciplined risk management.
