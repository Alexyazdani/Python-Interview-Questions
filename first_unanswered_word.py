r'''
Alex Yazdani
9 July 2025

first_unanswered_word.py
Write a function that takes a string representing a text conversation and returns the first word your ex used that you never replied to.
    The string alternates between messages from "You:" and "Ex:"
    A message is a line starting with "You:" or "Ex:"
    A “reply” is any "You:" message that comes after an "Ex:" message
    Return the first word from the first "Ex:" message that was not followed by a "You:" before the next "Ex:"
'''


def first_unanswered_word(text):
    messages = [line.strip() for line in text.strip().split("\n") if line.strip()]
    for i in range(1, len(messages)):
        if messages[i-1].lower().startswith("ex:") and messages[i].lower().startswith("ex:"):
            return messages[i-1].split()[1]
    if messages and messages[-1].lower().startswith("ex:"):
        return messages[-1].split()[1]
    return None




if __name__ == "__main__":
    test_convos = [
        """
        Ex: hey
        You: hey
        Ex: how are you
        You: fine
        Ex: can we talk
        Ex: hello?
        """,  # "can"
        
        """
        Ex: hi
        Ex: are you there
        You: sorry
        """,  # "hi"
        
        """
        Ex: i still think about you
        You: please don't
        """,  # None
        
        """
        Ex: hey
        """,  # "hey"
    ]

    for convo in test_convos:
        print(first_unanswered_word(convo))
