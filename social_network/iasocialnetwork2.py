#TO DO:
#- Integrate the csv file with the Dictionaries and the usernames and id lists
#- Prevent the user from repeating a username name
#- Allow the user to delete users from the list and dictionaries
#- Create a list for each user to have personalized connections 



#Beginning of class User

class User :
    def __init__(self, user_name, user_id): #Constructor (requieres username and user id)
        self.user_name = user_name
        self.user_id= user_id
        self.connections = []

    #Getter Methods

    def getUserName(self):
        return self.user_name

    def getUserId(self):
        return self.user_id

    def getConnections(self):
        return self.connections

    #Setter Methods

    def addConnection (self, other_user_name):
        self.connections.append(other_user_name)


    #to delete a connection, get the index number of it and use del self.connections [index]

#End of User class

#Beginning of class Network
class Network :
    def __init__(self): #Network constuctor
        self.users = []
        self.usernames= []


    #Getter methods
    def numUsers(self):
        return len(self.users)

    def getUserId(self, user_name):
        #length = Network.numUsers()
        for index in range(len(self.users)):
            possible_user = self.users[index]
            if (possible_user.getUserName() == user_name):
                return possible_user.getUserId() #Match found
        return -1 #Match not found

    def getUsernameList(self):
        doc_usernames = open("Network_Usernames.txt","r")
        self.usernames = doc_usernames.readlines()
        return (self.usernames)
    #Setter Methods
    def addUser(self,csv):
        new_user_name= raw_input ("Create a new user name: ")
        new_user_id= (len(self.users)+1)
        new_user= User(new_user_name, new_user_id) #Creates a new user
        self.users.append(new_user)
        self.usernames.append(new_user_name)

        #Creating the dictionary and putting the data in the csv file
        dic ={"Username":[], "User ID":[]}
        dic["Username"].append(new_user_name)
        dic["User ID"].append(new_user_id)

        new_user_id=str(new_user_id)

        #Writing it out
        csv.write(new_user_name+","+new_user_id+"\n")




        #Keeping track of data
        #doc_usernames= open("Network_Usernames.csv","a")
        #doc_usernames.write(new_user_name)
        #doc_user_id= open ("Network_User_ID.csv","a")
        #snew_user_id= str(new_user_id)
        #doc_user_id.write(snew_user_id)
        #doc_usernames.close()
        #doc_user_id.close()




    def addConnection(self, user_name1, user_name2):
        user_id_1= self.getUserId(user_name1)
        user_id_2= self.getUserId(user_name2)

        if (user_id_1==-1 or user_id_2==-1):
            print("Users are not in the network.")
        else:
            user1= self.users[user_id_1]
            user2= self.users[user_id_2]

            user1.addConnection(user_name2)
            user2.addConnection(user_name1)
            print("These are the current connections")
            connections = User.getConnections()
            print(connections)
#End of Network Class

#This defines the program flow for the user interface / Main method
def main():
    net=intro()
    csv=open("Network_Users.csv","a")
    action (net,csv)

def intro():
    print("Welcome to the Network!")
    print("\t~~~~~~~")
    print("What would you like to do?")
    return (Network())

def action(net,csv):
    print ("A) Create a user \t B) Connect to a user \t C) Delete a user \t D) View current users \t E) Exit")
    decision = raw_input()
    #Create a user
    if decision == "A":
        net.addUser(csv)
        action(net,csv)
    #Connect users
    elif decision == "B":
        username1= raw_input("User Name 1:")
        username2= raw_input("User Name 2:")
        net.addConnection(username1,username2)
        action(net,csv)
    #Delete a user
    elif decision == "C":
        print ("Work in progress ... restart")
        main()
    #View current users
    elif decision =="D":
        user_list= net.getUsernameList()
        print ("These are the current users of the Network")
        print (user_list)
        action(net, csv)

    elif decision =="E":
        print ("Closing the Network")
        csv.close()
        quit()

#This runs your program

if __name__== '__main__':
    main()
