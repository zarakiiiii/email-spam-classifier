# 🚀 Email Spam Classifier + Chrome Extension

### 📧 Detect Spam Emails Using Machine Learning & Deploy with a Chrome Extension

## 🔹 Overview
This project is an **email spam classifier** powered by **Machine Learning (TF-IDF & Classification Model)**. To make it even more user-friendly, I built a **Chrome extension** that allows users to check whether an email is spam or not in real time.

## 🎯 Features
✅ Uses **TF-IDF vectorization** for feature extraction  
✅ Classifies emails as **Spam or Not Spam**  
✅ Flask API for model inference  
✅ Chrome Extension for easy access  
✅ Supports real-time predictions  

## 🛠 Tech Stack
- **Python (Flask, Scikit-Learn, Pickle)** – ML model & API  
- **JavaScript, HTML, CSS** – Chrome Extension  
- **Flask-CORS** – API communication  

## 📂 Project Structure
```
📦 Email-Spam-Classifier-Chrome-Extension
├── 📁 backend  # Flask API & ML Model
│   ├── model2.pkl  # Trained ML model
│   ├── vectorizer3.pkl  # TF-IDF vectorizer
│   ├── app.py  # Flask API for predictions
│   ├── requirements.txt  # Dependencies
├── 📁 extension  # Chrome Extension
│   ├── popup.html  # UI for extension
│   ├── popup.js  # Handles user input & API calls
│   ├── manifest.json  # Chrome extension config
├── README.md  # Project documentation
```

## 🚀 How to Run
### 🔧 Backend (Flask API)
1️⃣ Clone the repo:
```bash
git clone https://github.com/your-username/email-spam-classifier.git
cd email-spam-classifier/backend
```
2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```
3️⃣ Run the Flask API:
```bash
python app.py
```
The API will run at `http://127.0.0.1:5000/predict`.

### 🖥️ Chrome Extension
1️⃣ Open **Chrome** and go to `chrome://extensions/`
2️⃣ Enable **Developer mode** (top right corner)
3️⃣ Click **Load unpacked** and select the `extension` folder
4️⃣ Open the extension and test it!

## 📸 Screenshots
(Add screenshots of your extension & API working here)

## 🔗 Live Demo & GitHub Repo
- **GitHub Repo:** [Your GitHub Link]
- **Demo Video:** [YouTube/Drive Link, if available]

## 📩 Contact
Feel free to reach out for feedback or collaboration! 😃  
✉️ Email: [Your Email]  
💼 LinkedIn: [Your LinkedIn]  

---
### ⭐ If you found this useful, give it a star ⭐ on GitHub!
