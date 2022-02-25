import random


destination_list = ['the mountains','the sea','the city','stay at home']
restaurant_list = ['mexican food','indian food','thai food','junk food','chinese food']
transportation_list = ['motorcycle','car','plane','train','your best walking shoes']
entertainment_list = ['go swimming','play video games','go clubbing','play a sport','take a hike']


# function for destination
def random_dest ():
    destination = (random.choice(destination_list))
    print(f'We have chosen {destination}, for your destination.')
    user_dest_choice = input('Do you like this destination? y/n: ')
    find_place = True
    while find_place is True:
        if user_dest_choice == ('y'):
            find_place = False
            print(f'Great! You have chosen {destination}. Lets move on.')
        elif user_dest_choice == ('n'):
            print(f'Oh no! Lets choose a different one')
            destination = (random.choice(destination_list))
            print(f'We have chosen {destination}, for your destination.')
            user_dest_choice = input('Do you like this destination? y/n: ')
        else:
            print('Something went wrong.')
            print(f'We have chosen {destination}, for your destination.')
            user_dest_choice = input('Do you like this destination? y/n: ')
    return destination    


#function for restraunt list
def random_food ():
    restaurant = (random.choice(restaurant_list))
    print(f'We have chosen {restaurant} as the type of food you will eat! ')
    users_food_choice = input(f'Do you like {restaurant}? y/n: ')
    find_food = True
    while find_food is True:
        if users_food_choice == ('y'):
            find_food = False
            print(f'Yummy! What a good choice! I love {restaurant} too! Lets move on.') 
        elif users_food_choice == ('n'):
            print('Sorry! Lets choose a different type!')
            restaurant = (random.choice(restaurant_list))
            print(f'We have chosen {restaurant} as the type of food you will eat! ')
            users_food_choice = input(f'Do you like {restaurant}? y/n: ')
        else:
            print('Silly goose, thats not an answer')
            print(f'We have chosen {restaurant} as the type of food you will eat! ')
            users_food_choice = input(f'Do you like {restaurant}? y/n: ')
    return restaurant



#function for transportation
def random_travel ():
    transportation = (random.choice(transportation_list))
    print(f'We have chosen {transportation}, as your mode of travel!')
    users_transpo_choice = input(f'Would you like to use {transportation}, as your mode of travel? y/n: ')
    find_transpo = True
    while find_transpo is True:
        if users_transpo_choice == ('y'):
            find_transpo = False
            print(f'Amazing! We are happy to see you traveling by {transportation}. Lets continue!')
        elif users_transpo_choice == ('n'):
            print('Oops! Lets pick a different mode of travel.')
            transportation = (random.choice(transportation_list))
            print(f'We have chosen {transportation}, as your mode of travel!')
            users_transpo_choice = input(f'Would you like to use {transportation}, as your mode of travel? y/n: ')
        else:
            print('Thats not the response we were looking for.')
            print(f'We have chosen {transportation}, as your mode of travel!')
            users_transpo_choice = input(f'Would you like to use {transportation}, as your mode of travel? y/n: ')
    return transportation



#function for entertainment 
def random_ent ():
    entertainment = (random.choice(entertainment_list))
    print(f'We have chosen {entertainment} as the activity.')
    users_ent_choice = input(f'Do you like {entertainment} as your activity? y/n: ')
    find_ent = True
    while find_ent is True:
        if users_ent_choice == ('y'):
            find_ent = False
            print(f'Woohoo! {entertainment} is going to be so fun!')
        elif users_ent_choice == ('n'):
            print('Dang! Well lets choose another one!')
            entertainment = (random.choice(entertainment_list))
            print(f'We have chosen {entertainment} as the activity.')
            users_ent_choice = input(f'Do you like {entertainment} as your activity? y/n: ')
        else:
            print('Oops we didnt expect that answer. Lets try again')
            print(f'We have chosen {entertainment} as the activity.')
            users_ent_choice = input(f'Do you like {entertainment} as your activity? y/n: ')
    return entertainment


def reselect ():
    redo_stuff1 = True
    redo_stuff2 = True
    redo_stuff3 = True
    redo_stuff4 = True
    while redo_stuff1 is True:
        redo_dest = input('Would you like to reselect the destination? y/n: ')
        if redo_dest == ('y'):
            random_dest()
        elif redo_dest == ('n'):
            redo_stuff1 = False
            print(f'Ok, we will keep the destinatin of {users_fin_dest_choice}.')
    while redo_stuff2 is True:
        redo_food = input('Would you like to reselect the type of food? y/n: ')
        if redo_food == ('y'):
            random_food()
        elif redo_food == ('n'):
            redo_stuff2 = False
            print(f'Ok we will keep your food choice of {users_fin_food_choice}.')
    while redo_stuff3 is True:
        redo_travel = input('Would you like to reselect the mode of travel? y/n: ')
        if redo_travel == ('y'):
            random_travel 
        elif redo_travel == ('n'):
            redo_stuff3 = False
            print(f'Ok, we will keep your mode of travel choice of {users_fin_transpo_choice}')
    while redo_stuff4 is True:
        redo_ent = input('Would you like to reselect the entertainment? y/n: ')
        if redo_ent == ('y'):
            random_ent
        elif redo_ent == ('n'):
            redo_stuff4 = False
            print(f'Ok we will keep your entertainment choice of {users_fin_ent_choice}.')
        else:
            final_choices_confirm()

#finalizing choices
def final_choices_confirm ():
    print(f' For your destination you are going to {users_fin_dest_choice}.')
    print(f' For your food selection. You have chosen {users_fin_food_choice}.')
    print(f' You will be travelling by {users_fin_transpo_choice}.')
    print(f' Your choice of entertainment will be to {users_fin_ent_choice}.')
    confirm = True
    while confirm is True:
        users_confirm = input('Do these selections look correct to you? y/n: ')
        if users_confirm == ('y'):
            confirm = False
            print('Congrats! We know you will have an amazing time! Enjoy!')
        elif users_confirm ==('n'):
            print('Oh no! Which would you like to redo?')
            reselect ()
        else:
            print('Something went wrong , lets try again.')
            print(f'For your destination you are going to {users_fin_dest_choice}.')
            print(f'For your food selection. You have chosen {users_fin_food_choice}.')
            print(f' You will be travelling by {users_fin_transpo_choice}.')
            print(f'Your choice of entertainment will be {users_fin_ent_choice}.')
            users_confirm = input('Do these selections look correct to you? y/n: ')
    



users_fin_dest_choice = random_dest()
users_fin_food_choice = random_food()
users_fin_transpo_choice = random_travel()    
users_fin_ent_choice = random_ent()
final_choices_confirm()


