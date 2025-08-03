# 🧠 Task 5: Mental Health Support Chatbot (Fine-Tuned using DistilGPT2)

This project is part of the **DevelopersHub AI/ML Internship**.  
It builds a chatbot designed to provide emotionally supportive and empathetic responses using a fine-tuned LLM. The model is trained on a dialogue dataset to help users express their emotions and receive comfort-oriented responses.

---

## 🎯 Objective

- Fine-tune a small LLM (DistilGPT2) using emotional conversation data  
- Build a chatbot that responds gently and empathetically  
- Provide a terminal-based or notebook-based interaction loop  
- Add optional real-time visualization to simulate response generation  

---

## 💡 Key Features

- Trained on `bdotloh/empathetic-dialogues-contexts` from Hugging Face  
- Custom preprocessing: combines `situation` and `emotion` into a response  
- Tokenization using `AutoTokenizer` with padding and truncation  
- Fine-tuned using Hugging Face `Trainer` API with configurable epochs  
- Interactive chatbot loop with optional real-time animated graph  
- Bonus charts for emotion distribution and token length insight  

---

## 📋 Example Prompts to Try

- I feel anxious when I talk in public  
- Nobody seems to understand me  
- I'm mentally exhausted from work  
- I just need someone to listen  

---

## ⚙️ How to Run (Step-by-Step)

### Step 1: Clone the Repo  
Clone the GitHub repository and navigate to the project folder.

### Step 2: Install Dependencies  
Install the required libraries using pip: transformers, datasets, matplotlib, tqdm.

### Step 3: Load Dataset  
Use Hugging Face datasets: bdotloh/empathetic-dialogues-contexts with the training split.

### Step 4: Preprocess  
Combine the situation and emotion columns to simulate a conversational turn. Tokenize inputs using DistilGPT2’s tokenizer.

### Step 5: Train the Model  
Use Hugging Face Trainer with batch size 4 and 1 epoch. The model and tokenizer are saved to the mental_health_model directory.

### Step 6: Chat with the Bot  
Run the interactive chat loop in the notebook or CLI. Includes a real-time animated graph (compatible with Colab) that simulates the bot "thinking."

---

## 📉 Bonus Visualizations

- Emotion Frequency Chart from the training dataset  
- Input Token Length Distribution  
- Multi-prompt Testing Cell to evaluate response variation  
- Real-time progress simulation using a matplotlib animation in Colab  

---

## 🔐 Safety Disclaimer

This chatbot is designed for educational and emotional support only.  
It is not a substitute for mental health counseling, diagnosis, or therapy.  
Please consult a licensed mental health professional for any serious concerns.

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
