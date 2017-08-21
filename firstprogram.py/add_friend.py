friends = []
def add_friend():
  new_friend = {
    'name': '',
    'salutation': '',
    'age': 0,
    'rating': 0.0
  }

  new_friend['name'] = raw_input("Please add your friend's name: ")
  new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
  new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

  new_friend['age'] = int(raw_input("Age?"))
  new_friend['rating'] = float(raw_input("Spy rating?"))
  if len(new_friend['name']) > 0 and new_friend['age'] > 12 :
      friends.append(new_friend)
  else:
      print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
  return len(friends)


def select_friend():
  item_number = 0
  for friend in friends:
    print '%d. %s' % (item_number + 1), friend['name']
    item_number = item_number + 1
  friend_choice = raw_input("Choose from your friends")
  friend_choice_position = int(friend_choice) - 1
  return friend_choice_position