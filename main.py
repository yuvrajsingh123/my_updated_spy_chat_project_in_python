# importing spy_details from another file into this file
from spy_details import spy, Spy, ChatMessage, friends

#importing steganography
from steganography.steganography import Steganography

#importing datetime
from datetime import datetime

#importing termcolor
from termcolor import colored
p=-1
special_message=['SAVE ME','SOS']

#you can select built-in status messages from here
STATUS_MESSAGES = ['Hey There!!!I am using SpyChat', 'I am Busy', 'I am available']


print "Hello.....We should start our SpyChat application....Start chatting now"

#asking from the user again and again to check whther the existing user is logging in or not
question = "Do you want to preceed further with  " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

#function is used to add status
def add_status():

    updated_status_message = None

#if you entered any text then status will be printed else it will print-you don't have any status messages
    if spy.current_status_message != None:
        print 'status selected!!!!'
        print ' Hello, Your current status is %s \n' % (spy.current_status_message)
    else:
        print 'Status message is not set yet..You have no status message \n'

   #helps to select older messages
    default = raw_input("Do you want to select from the older or existing status (y/n)? ")

    if default.upper() == "N":
        #asking for status messages which you want to execute
        new_status_message = raw_input("Tell me what status message do you want to set? ")

#if message is greater than 0, then it will update the status message
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1
       #printing default messages
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above given messages quickly "))

#user's status message is updated
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'You have entered wrong input. Choose and type either y or n.'
#printing updated status messgae
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'Right now, you don\'t have any update of status'

    return updated_status_message

#function is used to add a friend
def add_friend():
#spy is a class for adding a friend
    new_friend = Spy('','',0,0.0)

#input your friends name please!!!!
    new_friend.name = raw_input("Please enter your friend's name you would like to add in a spyChat: ")
    new_friend.salutation = raw_input("Are your friend Mr. or Ms.?: ")

    #printing friends name with salutation
    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Please enter your Age?")

    #converting string to integer as age is an integer, not a string
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Please enter your Spy rating?")

#converting string to float as rating is an float, not a string
    new_friend.rating = float(new_friend.rating)

    #based on the below conditions if it meets, then friends will be added else not added
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Congratulations!!!!! Friend Added successfully!'
    else:
        print 'Sorry for that! we can\'t add your friend due to invalid entry.'

#returning number of friends added
    return len(friends)

#function is used to sealect your friend
def select_a_friend():
    item_number = 0

#printing your all friends you have
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

#from the friends list, select the friend you want to talk to
    friend_choice = raw_input("Please Choose from your friends which you have added")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#function to send a message to a friend
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("Now tell me the name of the image")

    output_path = "output.jpg"

#message you want to say to your friend
    text = raw_input("What message would you like to send??????? ")



    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)
# your message is appended
    friends[friend_choice].chats.append(new_chat)

    #calculate average words spoken by a spy in order the record
    words = text.split()
    average = sum(len(word) for word in words) / len(words)
    average=float(average)
    print "Average number of words spoken by a spy is" ,average


    if len(text)>0:
     print "Your secret message image is ready! Now the unauthorized users can't read your message"

    else:
     print "Please enter secret message....You can't go further!!!!!"


#function to read a message sent by you
def read_message():

#please select a friend
    sender = select_a_friend()

    output_path = raw_input("Now, tell me the name of the file")
    try:
    #message is decoded here
      secret_text = Steganography.decode(output_path)
    except:
        print 'Your message is not valid'
        return
    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)
    if secret_text.upper() in special_message:
        print "We are on our way!\n"
#function to read a chat history

def read_chat_history():

#select a friend
    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:

            # printing your message in colour and also time when the message has sent and received
            print '[%s] %s said: %s' % (colored(chat.time.strftime("%d %B %Y"),"blue"), colored('You',"red"), chat.message)
        else:
            print '[%s] %s said: %s' % (colored(chat.time.strftime("%d %B %Y"),"blue"), colored(friends[read_for].name,"red"), chat.message)

def delete_friends():
    sender = select_a_friend()
    for friend in friends:

        print 'Your current friend is:=', friends

        textt = raw_input("Enter the text")

        if len(textt)>5:

            del friends[sender]
        else:
            print 'none of your friends are deleted'



#function to start a chat
def start_chat(spy):

    #spy name and salutation
    spy.name = spy.salutation + " " + spy.name

#condition
    if spy.age > 12 and spy.age < 50:

#checking its authentication..if yes, then the user is logged in else not
        print "Congratulations!!!! Authentication is completed. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Welcome to SpyChat application"

        show_menu = True
#providing  list of choices which you can select to perform operation
        while show_menu:
            menu_choices = "Tell me,What do you want to do now as a spy? \n 1. Would you like to add a status update?Press 1 \n 2. Would you like to add a friend? Press 2 \n 3. Would you like to send a secret message? Press 3 \n 4. Would you like to read a secret message? Press 4 \n 5. Would you like to read Chats from a user? Press 5 \n 6. Would you like to delete your friend? Press 6 \n 7. Would you like to close an Application? Press 7 \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                #converting string to integer
                menu_choice = int(menu_choice)
#according to the input 1,2,3,4,5 particular condition will run
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                elif menu_choice == 6:
                    delete_friends()
                else:
                    show_menu = False
    else:
        print 'Sorry!!!! You don not belong to the correct age of the spy.....Enter your age between the valid spy\'s age'
#if existing user then directly he/she will be logged in
if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)
#if new user, then please enter your complete information

    spy.name = raw_input("Welcome to spy chat, Please tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Are you Mr. or Ms.?: ")

        spy.age = raw_input("Tell me yout age")
        spy.age = int(spy.age)

        spy.rating = raw_input("Tell me your your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
