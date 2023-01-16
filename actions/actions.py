# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCarousel(Action):

    def name(self) -> Text:
        return "actions_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Belgrade-Budapest",
                        "subtitle": "Price per person: 110 €  Economy class",
                        "image_url": "http://localhost:4200/assets/images/1.jpg",
                        "buttons": [
                            {
                                "title": "Details", #details -> kao dugme
                                "url": "http://localhost:4200/products/1",
                                "type": "web_url"
                            },
                            {
                                "title": "Book now", #Dugme -> Buy now
                                "url": "postback",
                                "payload": "/buynowarticle", #nlu.yml
                                "url": "http://localhost:4200/product",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Belgrade-Abu Dhabi",
                        "subtitle": "Price per person: 400 €  Business class",
                        "image_url": "http://localhost:4200/assets/images/9.jpg",
                        "buttons": [
                            {
                                "title": "Details", #details -> kao dugme
                                "url": "http://localhost:4200/products/9",
                                "type": "web_url"
                            },
                            {
                                "title": "Book now", #Dugme -> Buy now
                                "url": "postback",
                                "payload": "/buynowarticle", #nlu.yml
                                "url": "http://localhost:4200/product",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Belgrade-Doha",
                        "subtitle": "Price per person: 450 €  Business class",
                        "image_url": "http://localhost:4200/assets/images/12.png",
                        "buttons": [
                            {
                                "title": "Details", #details -> kao dugme
                                "url": "http://localhost:4200/products/12",
                                "type": "web_url"
                            },
                            {
                                "title": "Book now", #Dugme -> Buy now
                                "url": "postback",
                                "payload": "/buynowarticle", #nlu.yml
                                "url": "http://localhost:4200/product",
                                "type": "web_url"
                            }
                        ]
                    }
                ]

            }

        }

        dispatcher.utter_message(text="We provide good flights at affordable prices! You can take a look at our best offers here:", attachment=new_carousel)

        return []
                
class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def user_choice(self):
        generatednum = random.randint(1,4)
        if generatednum == 1:
            userchoice = "Shangai"
        elif generatednum == 2:
            userchoice = "Beijing"
        elif generatednum == 3:
            userchoice = "New York"
        elif generatednum == 4:
            userchoice = "Tokyo"
        
        return(userchoice)
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"Hmm, you said {user_choice}")
       
        if user_choice == "Tokyo":
            dispatcher.utter_message(text="Congrats, you won your promo code is 789 ツ.")
        elif user_choice == "Beijing":
            dispatcher.utter_message(text="Unfortunately you didn't earn discount.")
        elif user_choice == "New York":
            dispatcher.utter_message(text="Unfortunately you didn't earn discount.")
        elif user_choice == "Shangai":
            dispatcher.utter_message(text="Unfortunately you didn't earn discount.")
        
        return []