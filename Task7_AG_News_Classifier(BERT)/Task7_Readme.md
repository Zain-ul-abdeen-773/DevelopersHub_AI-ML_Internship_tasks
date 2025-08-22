# Task 7 — AG News Topic Classifier (BERT)

**Objective:** Fine-tune BERT (`bert-base-uncased`) to classify news headlines into 4 categories: **World, Sports, Business, Sci/Tech**.  

---

## Dataset
- **AG News** (via Hugging Face Datasets, ~120k news headlines).  
- Train/Validation/Test splits created with 10% of training data used for validation.  
- Balanced dataset across 4 classes.  

---

## Method
- **Preprocessing:** Tokenization with BERT fast tokenizer (truncation, dynamic padding).  
- **Model:** `AutoModelForSequenceClassification` with 4 output labels.  
- **Training:**  
  - Epochs: 3  
  - Learning Rate: 2e-5  
  - Weight Decay: 0.01  
  - Warmup Ratio: 0.06  
  - Batch Sizes: 16 (train), 32 (eval)  
  - Mixed precision (fp16) on GPU  
- **Metrics:** Accuracy and Macro-F1 for balanced evaluation.  

---

## Evaluation
- **Validation Accuracy:** ~94%  
- **Test Macro-F1:** ~0.94  
- Confusion matrix shows strong separation across all classes.  
- Classification report confirms balanced precision/recall.  

---

## Visualizations
- Training set **class distribution bar chart**  
- **Training vs Evaluation loss curves**  
- **Validation Accuracy curve**  
- **Validation Macro-F1 curve**  
- **Confusion Matrix heatmap**  
- **Prediction confidence histogram**  
- **3D t-SNE embedding scatterplot** of CLS vectors (clear topic clusters)  

---

## Deployment
- **Artifacts:** Saved model + tokenizer + label maps in `serve_artifacts/`  
- **Reports:** Metrics JSON in `reports/metrics.json`  
- **Apps:**  
  - **Gradio Interface:** Interactive headline input → topic prediction  
  - **Streamlit App:** `streamlit_app.py` with simple UI  

---

## Reproducibility
- **Seed:** 42  
- **Requirements:** All dependencies listed in `requirements.txt`  
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

---
