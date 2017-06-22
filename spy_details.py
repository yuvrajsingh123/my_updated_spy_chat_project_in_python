# importing datetime.....
from datetime import datetime

# A class of a spy is created
class Spy:
# name, salutation, age etc is assigned to a variable...
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#  class is made of CjatMessage

class ChatMessage:
# sent_by_me, message etc is assigned to a variable
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
#class spy is created...
spy = Spy('yuvraj', 'Mr.', 24, 4.7)

#spy with few friends
friend_one = Spy('Mayank', 'Mr.', 4.9, 27)
friend_two = Spy('Sanjeet', 'Ms.', 4.39, 21)
friend_three = Spy('Akash', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]
