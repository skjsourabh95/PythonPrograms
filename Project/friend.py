from colorama import Fore
from Global import spy,friends
from spy_details import Spy


#function to get a new spy friend
def add_friend():
  new_friend=Spy()
  print("\nEnter Friend Details:")
  new_friend.name = raw_input(Fore.GREEN+"Friend's name: ")
  new_friend.salutation = raw_input("Mr. or Ms.?: ")
  new_friend.name = new_friend.salutation + " " + new_friend.name
  new_friend.age = int(raw_input("Age?:"))
  new_friend.rating= float(raw_input("Spy rating?:"))
  if len(new_friend.name) > 0:
            if new_friend.age > 12:
                #comparing new friend rating with existing spy
                 if new_friend.rating>= spy.rating:
                        friends.append(new_friend)
                 else:
                     print Fore.RED+'Sorry! Invalid rating. We can\'t add a spy friend with the details you have provided'
            else:
                print Fore.RED+'Sorry! Invalid age. We can\'t add a spy friend with the details you have provided'
  else:
      print Fore.RED+'Sorry! Invalid name. We can\'t add a spy friend with the details you have provided'
  return len(friends)

#selecting a friend from the list
def select_a_friend():
  item_number = 0
  for friend in friends:
    print "%d." % (item_number + 1)+ friend.getName()

    item_number = item_number + 1
  friend_choice = raw_input(Fore.GREEN+"Choose from your friends:\n")
  friend_choice_position = int(friend_choice) - 1
  return friend_choice_position

#function to display chats between spies
def read_chat():
    friend_choice=select_a_friend()
    for chat in friends[friend_choice].chats:
        if chat.sent_by_me:
            #displaying chats with different colour codes
            print Fore.BLUE+'[%s] %s: \n%s (no of words:%s)' % (Fore.BLUE+" "+chat.time.strftime("%d %B %Y"), Fore.RED+" "+spy.getName(), Fore.BLACK+" "+chat.message, Fore.MAGENTA+" "+str(chat.no_of_words))
        else:
            print Fore.BLUE+'[%s] %s: \n%s (no of words:%s)' % (Fore.BLUE+" "+chat.time.strftime("%d %B %Y"), Fore.RED+" "+friends[friend_choice].name, Fore.BLACK+" "+chat.message,Fore.MAGENTA+" "+str(chat.no_of_words))
