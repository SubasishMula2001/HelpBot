HelpBot: A Chatbot for Mental Health Support
Overview
HelpBot is a chatbot project that helps students who are feeling lonely, stressed, or homesick, especially those staying away from home in hostels. It provides instant responses based on user inputs related to mental health issues and general queries.

Project 1: General Purpose Chatbot
This version of the bot responds to general queries like greetings, farewells, food issues, sleep problems, loneliness, homesickness, and stress.

Project 2: Mental Health Chatbot
This customized version of the bot is designed to assist students dealing with mental health challenges while staying in hostels or messes. It includes a set of conversational patterns designed to help users who are feeling lonely, homesick, stressed, or facing other emotional challenges.

Features
Handles general queries and basic chit-chat.

Provides emotional support based on common mental health issues such as loneliness, homesickness, stress, etc.

Custom responses tailored to the needs of students staying away from home.

Trained on conversational data collected from peers to ensure real-life applicability.

How to Interact with the Chatbot
Here are some example questions you can ask the chatbot. You can type these directly to get a response:

General Queries (Project 1)
Greeting the Bot:

"Hi"

"Hello"

"Hey"

"Good morning"

Farewell:

"Goodbye"

"Bye"

"See you"

Food Issues:

"The food is not good"

"I'm having food problems"

"The food tastes bad"

Sleep Problems:

"I can't sleep"

"I'm having trouble sleeping"

"I haven't had a good night's sleep"

Loneliness:

"I'm feeling lonely"

"I'm alone"

"I miss home"

Homesickness:

"I feel homesick"

"I miss my family"

"I miss home a lot"

Stress/Exam Stress:

"I'm stressed about exams"

"I have too much stress"

"I'm feeling anxious about my exams"

Mental Health Queries (Project 2)
Loneliness:

"I feel really lonely here"

"I'm feeling very alone"

"No one is talking to me"

Homesickness:

"I miss my home"

"I wish I could go home"

"I'm feeling homesick"

Sleep Issues:

"I can't sleep at night"

"I'm struggling to fall asleep"

"I feel restless when I try to sleep"

Exam Anxiety:

"I'm so anxious about my exams"

"I'm worried about my upcoming exams"

"I can't concentrate because of exam stress"

Feeling Down:

"I feel sad all the time"

"I feel low"

"I'm not feeling myself lately"

Food Issues:

"The food here isn't great"

"I don't like the food at my hostel"

"The mess food is terrible"

Socializing Problems:

"I'm finding it hard to make friends"

"I don't know anyone here"

"It's difficult to socialize in my hostel"

How to Run the Bot Locally
Step 1: Install Dependencies
Make sure you have Python installed. Then, install the necessary dependencies by running:

bash
Copy
Edit
pip install rasa
pip install rasa_sdk
Step 2: Train the Model
To train the Rasa model, use the following command:

bash
Copy
Edit
rasa train
Step 3: Run the Bot
To start the action server:

bash
Copy
Edit
rasa run actions
Then, to run the Rasa chatbot server:

bash
Copy
Edit
rasa shell
Step 4: Test Your Bot
Once the server is running, you can interact with your bot directly in the command line.

Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

