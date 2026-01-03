"""
Rule-Based Chatbot (Stateful Version)
Author: Isomiddin

Description:
A stateful rule-based chatbot that keeps simple context
and responds using intent rules and fallback logic.
"""

import random


# Intent rules
INTENTS = {
    "greeting": {
        "keywords": ["hi", "hello", "hey"],
        "responses": [
            "Hello! 😊",
            "Hi there!",
            "Hey! How can I help you?"
        ],
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": [
            "Goodbye! 👋",
            "See you later!",
            "Take care!"
        ],
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I'm a rule-based chatbot 🤖",
            "You can call me RuleBot."
        ],
    },
    "mood": {
        "keywords": ["how are you", "how do you feel"],
        "responses": [
            "I'm doing great! Thanks for asking 😊",
            "All systems running smoothly!"
        ],
    },
}

FALLBACK_RESPONSES = [
    "I'm not sure I understand.",
    "Could you rephrase that?",
    "Let's talk about something else 🙂"
]


class Chatbot:
    """Stateful rule-based chatbot."""

    def __init__(self) -> None:
        self.last_intent = None

    def normalize(self, text: str) -> str:
        return text.lower().strip()

    def detect_intent(self, text: str) -> str | None:
        """Detect intent based on keyword matching."""
        for intent, data in INTENTS.items():
            for keyword in data["keywords"]:
                if keyword in text:
                    return intent
        return None

    def generate_response(self, intent: str | None) -> str:
        """Generate a response based on intent and state."""
        if intent:
            self.last_intent = intent
            return random.choice(INTENTS[intent]["responses"])

        if self.last_intent:
            return "Can you tell me more about that?"

        return random.choice(FALLBACK_RESPONSES)

    def chat(self) -> None:
        """Start chat loop."""
        print("=" * 50)
        print("🤖 RULE-BASED CHATBOT v2")
        print("Type 'exit' to quit")
        print("=" * 50)

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Bot: Goodbye! 👋")
                break

            text = self.normalize(user_input)
            intent = self.detect_intent(text)
            response = self.generate_response(intent)
            print(f"Bot: {response}")


def main() -> None:
    bot = Chatbot()
    bot.chat()


if __name__ == "__main__":
    main()
