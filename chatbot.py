import tkinter as tk
from tkinter import scrolledtext

import nltk
from nltk.chat.util import Chat, reflections

class ChatBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot")

        self.chatbot = Chat(self.patterns, reflections)

        self.chat_history = scrolledtext.ScrolledText(master, width=50, height=20)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.user_input = tk.Entry(master, width=40)
        self.user_input.grid(row=1, column=0, padx=10, pady=5)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def send_message(self):
        user_input_text = self.user_input.get()
        self.user_input.delete(0, tk.END)
        self.chat_history.insert(tk.END, "You: " + user_input_text + "\n")
        response = self.chatbot.respond(user_input_text)
        self.chat_history.insert(tk.END, "ChatBot: " + response + "\n")
        self.chat_history.see(tk.END)

    patterns = [
        (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
        (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
        (r"what is your name?", ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]),
        (r"quit|bye|goodbye", ["Goodbye!", "Bye, take care!"]),
        # Add more patterns and responses as needed
    ]

def main():
    root = tk.Tk()
    chatbot_gui = ChatBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
