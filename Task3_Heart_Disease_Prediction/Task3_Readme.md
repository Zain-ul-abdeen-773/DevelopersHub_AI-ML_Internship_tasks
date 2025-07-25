# ❤️ Task 3: Heart Disease Prediction

This notebook is part of the **DevelopersHub AI/ML Internship** and focuses on predicting the presence of heart disease based on clinical data using classification models.

---

## 🧠 Objective

- Analyze and clean the UCI Heart Disease dataset
- Perform exploratory data analysis (EDA)
- Train classification models (Logistic Regression & Decision Tree)
- Evaluate using accuracy, ROC AUC, and confusion matrix
- Identify and visualize the most important features

---

## 📊 Dataset

- **Source**: [UCI Heart Disease Dataset on Kaggle](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)
- **Features**:
  - Age, Chest Pain Type, Cholesterol, Max Heart Rate, etc.
- **Target**:
  - `1` → Heart Disease Present  
  - `0` → No Heart Disease

---

## 🔍 Key Steps

1. Load and inspect dataset
2. Handle missing values (if any)
3. Visualize trends and feature relationships
4. Train models:
   - Logistic Regression
   - Decision Tree Classifier
5. Evaluate using:
   - Accuracy
   - ROC Curve & AUC
   - Confusion Matrix
6. Visualize feature importance

---

## 📈 Visualizations Included

| Graph No. | Description                                      |
|-----------|--------------------------------------------------|
| 1         | Target class distribution                        |
| 2         | Age vs Max Heart Rate (scatter)                  |
| 3         | Chest pain type vs heart disease (bar plot)      |
| 4         | Correlation heatmap                              |
| 5         | 3D: Age, Cholesterol, Max Heart Rate             |
| 6         | Boxplot of Cholesterol by Target                 |
| 7         | 3D: BP, HR, Age                                  |
| 8         | Pairplot of selected features                    |
| 9         | ROC Curve – Logistic Regression                  |
| 10        | ROC Curve – Decision Tree                        |

---

## 📦 Model Saving

Both models are saved using `joblib`:
- `logistic_model.pkl`
- `decision_tree_model.pkl`

---

## 📏 Evaluation Summary

| Model              | Accuracy | ROC AUC |
|--------------------|----------|---------|
| Logistic Regression| ~0.85    | ~0.90   |
| Decision Tree      | ~0.82    | ~0.87   |

> *Actual scores may vary depending on test split and hyperparameters.*

---

## 🛠️ Libraries Used

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`
- `joblib`

---

## 👨‍💻 Author

**Zain ul Abdeen**  
🆔 Intern ID: DHC-1204  
🎓 BS in Artificial Intelligence  
🔗 [GitHub](https://github.com/Zain-ul-abdeen-773)  
🔗 [Portfolio](https://zain-ul-abdeen-773.netlify.app/)  
🔗 [LinkedIn](http://www.linkedin.com/in/zain-ul-abdeen-48aa72318)

---

## 📜 License

This notebook is provided for educational and internship project use under the [MIT License](LICENSE).

---

## ⭐️ Show Support

If this project helped you learn or build your portfolio, consider giving it a ⭐️ and sharing your feedback!
