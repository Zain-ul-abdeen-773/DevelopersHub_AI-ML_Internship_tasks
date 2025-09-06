# 🏠 Task 3: Multimodal Housing Price Prediction (Images + Tabular Data)

This project is part of the **DevelopersHub AI/ML Internship**.  
It builds a multimodal machine learning pipeline to predict housing prices using both **tabular structured data** (square footage, bedrooms, bathrooms, age, neighborhood) and **house images**. The project demonstrates feature fusion and regression modeling with professional evaluation and visualizations.

---

## 🎯 Objective

- Combine **tabular + image data** for housing price prediction  
- Extract visual features from house images and fuse them with tabular features  
- Train a regression model to predict house prices  
- Evaluate the model using **MAE** and **RMSE**  
- Provide professional notebook with visualizations and animations  

---

## 💡 Key Features

- Synthetic dataset with **1600 samples** (tabular + generated house images)  
- Custom image generation with brightness/windows related to house price  
- Feature extraction: **Color histograms + edge-based features**  
- Feature scaling and fusion with tabular data  
- Regression using **RandomForestRegressor**  
- Evaluation metrics: **Mean Absolute Error (MAE)**, **Root Mean Squared Error (RMSE)**  
- Interactive notebook with professional graphs and an **animated learning curve**  

---

## 📋 Example Use Cases

- Estimate housing prices from property features and images  
- Demonstrate multimodal machine learning workflows  
- Educational project for combining **vision + tabular** data in ML pipelines  

---

## ⚙️ How to Run (Step-by-Step)

### Step 1: Clone the Repo  
Clone the GitHub repository and navigate to the project folder.

### Step 2: Install Dependencies  
Install the required Python libraries:  
\`\`\`bash
pip install numpy pandas scikit-learn matplotlib pillow joblib imageio
\`\`\`

### Step 3: Run the Notebook  
Open `Multimodal_Housing_Price_Notebook.ipynb` and run all cells.  

### Step 4: Train the Model  
The notebook will:  
- Generate synthetic dataset (tabular + images)  
- Extract image features and tabular features  
- Fuse them into a single dataset  
- Train a Random Forest regression model  

### Step 5: Evaluate the Model  
Check outputs for:  
- **MAE (Mean Absolute Error)**  
- **RMSE (Root Mean Squared Error)**  
- True vs Predicted scatter plot  
- Residuals histogram  
- Feature importances  

---

## 📉 Bonus Visualizations

- House Price Distribution Histogram  
- Price vs Square Footage Scatter Plot  
- True vs Predicted Scatter Plot  
- Residuals Histogram  
- Feature Importances (Top 10)  
- **Animated Learning Curve GIF** (RMSE vs training fraction)  

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

If this notebook helped you or inspired you, please ⭐️ the repository and share your feedback.  
Your support helps the open-source and AI learning community grow!
