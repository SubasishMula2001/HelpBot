# 🧠 Mental Health Support Chatbot for Hostel Students (Rasa Project)

This project is a web-based **mental health support chatbot** built using **Rasa**. It’s specially designed for students staying away from home in **hostels/messes across India**, helping them express their feelings and access support through friendly, human-like conversations.

---

## 🚀 Features

- 🤖 **Conversational AI** powered by Rasa
- 📚 Trained on real conversations with hostel students
- 🧘‍♀️ Focuses on **mental well-being**, stress, loneliness, and peer support
- 🌐 Stylish and responsive **web interface** (HTML + CSS + JS)
- 🔁 Easily customizable and extendable with new intents and responses

---

## 📁 Project Structure

mental-health-chatbot/ │ ├── actions/ # Custom Python actions (if any) ├── data/ # NLU and story training data ├── models/ # Trained models (excluded in .gitignore) ├── frontend/ # HTML/CSS/JS web UI for chatbot ├── config.yml # NLU pipeline and policies ├── domain.yml # Intents, responses, entities, slots ├── credentials.yml # Chat channels config (e.g. REST, Telegram) ├── endpoints.yml # Action and Tracker endpoints ├── requirements.txt # Python dependencies ├── .gitignore # Ignore unnecessary files in Git └── README.md # You're here!

---

## 💬 Example Questions You Can Ask the Bot

- "I feel very lonely at night."
- "I’m homesick and can’t sleep well."
- "What can I do to feel better?"
- "I’m stressed because of studies and hostel rules."
- "How can I manage anxiety being far from my family?"

---

## 🛠️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/SubasishMula2001/mental-health-chatbot.git
cd mental-health-chatbot
