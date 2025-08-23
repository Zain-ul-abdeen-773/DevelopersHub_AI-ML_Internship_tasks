# Task 8 — End-to-End ML Pipeline with Scikit-learn

**Objective:** Build a complete **end-to-end machine learning pipeline** on the **Breast Cancer dataset** using Scikit-learn, covering preprocessing, training, hyperparameter tuning, evaluation, and deployment.  

---

## Dataset
- **Source:** Scikit-learn’s built-in Breast Cancer dataset (569 samples, 30 features).  
- **Target Classes:**  
  - 0 = Malignant  
  - 1 = Benign  
- **Features:** Numerical tumor characteristics (e.g., mean radius, mean texture, mean concavity).  
- Balanced dataset suitable for binary classification.  

---

## Method
- **Data Preprocessing:**  
  - Scaling features with `StandardScaler`  
  - Train-test split (80/20)  

- **Pipeline Construction:**  
  - Logistic Regression as baseline  
  - Random Forest as advanced model  
  - Integrated preprocessing + modeling using `Pipeline`  

- **Hyperparameter Tuning:**  
  - `GridSearchCV` applied on Logistic Regression and Random Forest  
  - Scored with `f1` for balanced evaluation  

- **Evaluation Metrics:**  
  - Accuracy, Precision, Recall, F1-score  
  - Confusion Matrix, ROC-AUC  

---

## Exploratory Data Analysis (EDA)
Pre-model insights were explored with **8 professional graphs**:
1. Class Distribution (Benign vs Malignant)  
2. Feature Correlation Heatmap  
3. Scatterplot: Mean Radius vs Mean Texture  
4. Histogram of Mean Radius by Class  
5. KDE Distribution of Mean Texture  
6. Boxplot of Worst Radius by Class  
7. PCA 2D Projection (cluster visualization)  
8. Pairplot of Top Features (compact, global title)  

---

## Evaluation
- **Best Model:** Random Forest with tuned hyperparameters  
- **Validation Accuracy:** ~97%  
- **F1-score:** ~0.97  
- **ROC-AUC:** ~0.99  
- Confusion Matrix shows very strong class separation.  

---

## Deployment
- **Artifacts:** Best pipeline saved with `joblib`  
- **Apps:**  
  - **Gradio Interface:** Real-time cancer diagnosis predictions  
  - **Streamlit App:** User-friendly web app for input + prediction  

---

## Reproducibility
- **Seed:** 42  
- **Requirements:** Listed in `requirements.txt`  
- Notebook organized into ≥30 professional code/markdown cells.  

---

## 👨‍💻 Author

**Zain ul Abdeen**  
Intern ID: DHC-1204  
BS in Artificial Intelligence  
GitHub: [Zain-ul-abdeen-773](https://github.com/Zain-ul-abdeen-773)  
Portfolio: [zain-ul-abdeen-773.netlify.app](https://zain-ul-abdeen-773.netlify.app/)  
LinkedIn: [linkedin.com/in/zain-ul-abdeen-48aa72318](http://www.linkedin.com/in/zain-ul-abdeen-48aa72318)

---

## 📜 License

This project is open for educational use under the MIT License.

---

## ⭐️ Feedback

If you found this project helpful, please ⭐ the repo and share your thoughts.  
Your support helps grow the open-source learning community!
