# 📈 Task 2: Predict Future Stock Prices (Short-Term)

This notebook is part of the **DevelopersHub AI/ML Internship** and focuses on using historical stock market data to predict the **next day's closing price** of Apple Inc. (`AAPL`) using machine learning models.

---

## 🧠 Objective

- Load historical stock data using `yfinance`
- Extract meaningful features (`Open`, `High`, `Low`, `Volume`)
- Predict next-day `Close` price using:
  - Linear Regression
  - Random Forest Regressor
- Visualize predicted vs actual results

---

## 📊 Dataset

- **Source**: [Yahoo Finance](https://finance.yahoo.com/)
- **Ticker**: `AAPL`
- **Duration**: Last 3 years (via `yfinance`)
- **Features Used**:
  - `Open`, `High`, `Low`, `Volume`
- **Target**:
  - `Close` price (next day, shifted using `.shift(-1)`)

---

## 🔍 Key Steps

1. Download data using `yfinance`
2. Perform data cleaning and feature-target engineering
3. Train models (Linear Regression + Random Forest)
4. Evaluate using RMSE and R² Score
5. Visualize predictions vs actual prices

---

## 📈 Visualizations (10 Graphs Included)

| Graph No. | Description                                      |
|-----------|--------------------------------------------------|
| 1         | Closing price over time                          |
| 2         | OHLC price comparison                            |
| 3         | Volume traded over time                          |
| 4         | Correlation heatmap of features                  |
| 5         | Histogram of daily returns                       |
| 6         | Year-wise boxplot of closing prices              |
| 7         | 20-day and 50-day moving averages                |
| 8         | Volume vs Closing Price scatter plot             |
| 9         | High vs Low scatter plot with Close hue          |
| 10        | Closing price with highlighted prediction period |

---

## 📏 Evaluation Metrics

| Model              | RMSE (↓) | R² Score (↑) |
|--------------------|----------|--------------|
| Linear Regression  | e.g. ~2.50   | e.g. ~0.93      |
| Random Forest      | e.g. ~1.80   | e.g. ~0.86      |

---

## 🛠️ Libraries Used

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `sklearn` (LinearRegression, RandomForestRegressor)
- `yfinance` for data fetching

---

## 🧠 Author Info

**Zain ul Abdeen**  
🎓 BS in Artificial Intelligence  
🆔 Intern ID: DHC-1204  
🔗 [GitHub](https://github.com/Zain-ul-abdeen-773)  
🔗 [Portfolio](https://zain-ul-abdeen-773.netlify.app/)  
🔗 [LinkedIn](http://www.linkedin.com/in/zain-ul-abdeen-48aa72318)

---

## 📜 License

This project is for educational and internship use under the [MIT License](LICENSE).

---

## ⭐️ Show Support

If you found this useful, feel free to ⭐️ the repo and share your feedback!
