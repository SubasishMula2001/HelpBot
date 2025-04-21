# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet

# class ActionGreetUser(Action):
#     def name(self):
#         return "action_greet_user"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="Hello, how can I help you?")
#         return []

# # Action for loneliness support
# class ActionLonelinessSupport(Action):
#     def name(self):
#         return "action_loneliness_support"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="I'm really sorry you're feeling lonely. Would you like to talk about it?")
#         return []

# # Action for stress relief
# class ActionStressRelief(Action):
#     def name(self):
#         return "action_stress_relief"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="Stress can be tough. Have you tried deep breathing exercises or taking a break?")
#         return []

# # Action for homesickness
# class ActionHomesickness(Action):
#     def name(self):
#         return "action_homesickness"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="I understand that being away from home can be hard. How can I help you today?")
#         return []
