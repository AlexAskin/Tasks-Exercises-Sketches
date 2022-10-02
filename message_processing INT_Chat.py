# Testing Part of INT-Chat app  #  August 2022

# Name validation

# Slicing and processing of User's message

# Exception cases



def input_nickname():
    nickname = input('Enter your NickName/Login/alias:\n(use only letters!)>>> ')
    
    #  "Exceptions List" method:
    '''except_symbols = ['0','1','2','3','4','5','6','7','8','9',
                      '!','?','"',"'",'#','$','%','&','(',')',
                      '*','+','-','/','{','}','<','>','_','~',
                      '№',';',':']
    for i in nickname:
        if i in except_symbols:
            print('Invalid LOGIN!')
            nickname = input_nickname()
    '''

    # str.isalpha() method:
    if nickname == '':
        print('User Input is missing')
        print('You\'ve get NickName: "AnonUser"')
        nickname = 'AnonUser'
    else:
        if nickname.isalpha() == False:
            print('Invalid LOGIN!')
            nickname = input_nickname()
        elif len(nickname) > 10:
            print('Lenght of NickName must be < 10!')
            nickname = input_nickname()    

    return nickname


#    len_nick:   |
def length_nickname():
    if len(nickname) < 10:
        len_nick = '0' + str(len(nickname))
    elif len(nickname) == 10:
        len_nick = str(len(nickname))
    else:
        len_nick= 'XX'
    
    return len_nick


nickname = input_nickname()
len_nick = length_nickname()

room_index = 'L0' # "L0" - index of LOBBY-chat
# in first opening of the client , the User enters the lobby



def input_user_message():
    
    #user_message_to_server = (nickname + ':')

    nick_user_message = (nickname + ':')

    
    user_message = input(f'{nickname}: ')

    if len(user_message) > 90: # Max Length of User's messsage
        print('Length LIMIT! \n(Lenght of message must be < 90!)')
        user_message,nick_user_message,len_msg,len_nick = input_user_message()
        #client_send()
        return user_message,nick_user_message,len_msg
    
    elif len(user_message) == 0:
        print('You cannot send an Empty message!')
        user_message,nick_user_message,len_msg,len_nick = input_user_message()
        #client_send()
        return user_message,nick_user_message,len_msg

    
    nick_user_message += user_message
    
    #print(nick_user_message)


    #    len_msg:   |
    if len(user_message) < 10:
        len_msg = '00' + str(len(user_message))
    elif len(user_message) < 100:
        len_msg = '0' + str(len(user_message))
    else:
        msg_len = 'xxx'
        
    
    return user_message,nick_user_message,len_msg




def types_message():
    global room_index
    '''
    Indexes of types message:
    
    "S1" - Usual message for Lobby or Private chat

    Requests to Server:
    "S2" - command 'openroom' for request to Server for Enterence to Private chat-room
    (this changes the "Room-index" from "L0" to "P#")
    
    "S3" - command 'exitroom' for request to Server
    for Exiting from a Private chat-room to the Lobby-chat
    (this changes the "Room-index" from "P#" to "L0")
    
    "S4" - command 'newroom' for request to Server to create a new Private chat-room
    from list of  available (free) Private rooms

    "S5" - command 'delroom' for request to Server for delete (remove) the current Private chat-room
    delete (remove)  the  the current Private chat-room may only user that created this  Private chat-room
    (or Admin in futures too)

    "S7" - command 'users' for request to Server to showing the list of Users in the current Private chat-room
    or in the Lobby-chat
    
    "S8" - command 'freerooms' for request to Server to showing the list of available (free) Private rooms
    
    Additional requests to Server:
    "S6" - command 'nacknick' for request to Server for changing the User's Nickname (in futures)

    "S0" -  command 'time'/'время'/'זמן' for request to Server for showing the current date and time
    '''
     

    if user_message == 'openroom':
            type_msg = 'S2'
            room_index = list_rooms()  
            
    elif user_message == 'exitroom':
            type_msg = 'S3'
            room_index = 'L0'
            
    elif user_message == 'newroom':
            type_msg = 'S4'
            room_index = 'P#'
            
    elif user_message == 'delroom':
            type_msg = 'S5'
            
    elif user_message == 'nacknick': # (in futures)
            type_msg = 'S6'
            
    elif user_message == 'users':
            type_msg = 'S7'
            
    elif user_message == 'freerooms':
            type_msg = 'S8'

#           additional requests to Server:

    elif user_message == 'time':  
            type_msg = 'S0'
    elif user_message == 'время':
            type_msg = 'S0'
    #elif user_message == 'זמן':
            #type_msg = 'S0'
            
    else:
            type_msg = 'S1'

    print(type_msg)

    return type_msg


def list_rooms():
    print('Выберите комнату для Входа:')
    print('#0 - LOBBY-chat: 12')
    print('#1 - 2')
    print('#2 - 45') # len(users_room_P2)
    print('#3 - 5')
    print('#4 - 0')
    print('#5 - X')
    print('#6 - X')
    print('#7 - X')
    print('#8 - X')
    print('#9 - X')
    get_room = input()
    try :
        get_room_check = int(get_room)
        if get_room_check > 9:
            print('Invalid!')
            
            print('You are stayed into LOBBY-chat')
            get_room = list_rooms()
        elif get_room_check == 0:
            print('You are come backed into LOBBY-chat')
            get_room = 'L0'
        else:    
            get_room = 'P' + get_room
    except:
        print('Invalid!')
        print('Enter Nums(0-9), NOT LETTERS!')
        print('You are stayed in LOBBY-chat')
        get_room = list_rooms()
        #get_room = 'L0'

         
    return get_room


def concatenate_user_message():
    '''
    User message to server =
    Index of types message +
    Index of Chat-Rooms +
    Lenght of Message + 
    Lenght of User's Nickname + 
    Nickname of User +
    Message of User
    '''
    user_message_to_server = type_msg + room_index + len_msg + len_nick + nick_user_message

    all_msg =  type_msg +'|'+ room_index +'|'+ len_msg +'|'+ len_nick +'|'+ nick_user_message    
    
    print(user_message_to_server)
    print(all_msg)
    pass
    


while True:
    print('_____________')
 
    user_message,nick_user_message,len_msg = input_user_message()
    
    type_msg = types_message()

    concatenate_user_message()





