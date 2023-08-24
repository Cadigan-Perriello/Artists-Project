'''
Created on Feb 13, 2023

@author: cadiganperriello

This program could be used by an agent or manager of a musical artist. It could be used by then to create albums and view
information on past albums by their artist. It could also be used to store old tours so that the manager could view info
on when the artists past tours and plan and store information on future tours. It also just holds basic information on each
artist which could be used by a manager but could also be searched by fans in order to learn about a new artist.
'''
import csv

"""
The Binary Search Tree nodes have 4 parameters: data, left_node, right_node, and the parent of the node. The only other 
method it has is a represent which returns a string interpretation of the node. Each node in the Binary Search Tree is an
artist object. In this program a BST node is an artist object.
"""
class BST_Node:
    def __init__(self, data, parent = None):
        self.data = data
        self.left_node = None
        self.right_node = None
        #helpful for the remove function
        self.parent = parent
        
    def __repr__(self):
        return (f" {self.data}")
        
"""
The Binary Search Tree class only has two parameters: the root of the tree and the number of nodes in the tree. It has an 
insert and an insert_node class that work together to allow for the inserting of a new node into the tree. The classes work
with recursion and go through the tree to find the correct place to insert the new node or to create a new node. The search
and search_node classes work similarly by traversing through the tree until the given name of the artist equals the node's
data that it is currently on. Similarly, the traverse and traverse_node classes work together in order to loop through 
every node in the class, which is used when we need to print out the tree. We end with a repr which returns a string 
interpretation of the Binary Search tree. In this program the Binary Search Tree is an alphabetically organized tree that
holds all of the artist objects. 

""" 
class BinarySearchTree:
    def __init__(self):
        #we can access the root node exclusively
        self.root = None
        self.num_of_nodes = 0
# the 'add' method     
    def insert(self, data):
        #this is the first node in the BST
        if self.root is None:
            self.root = BST_Node(data)
            self.num_of_nodes +=1
        else:
            self.insert_node(data, self.root)
            self.num_of_nodes +=1
            
    def insert_node(self, data, node):
        if data.name.lower() < node.data.name.lower():
            #print(f"{data.name} is less than {node.data.name}, going left...")
            if node.left_node is not None:
                #when the left node does not exist
                self.insert_node(data, node.left_node)
            else:
                #there is no left child, so we create one
                #print(f"there is no left child, so we will create one")
                node.left_node = BST_Node(data, node)
        else:
           # print(f"{data.name} is greater than or equal to {node.data.name}, going right")
            if node.right_node is not None:
                #when the left node does not exist
                self.insert_node(data, node.right_node)
            else:
                #there is no left child, so we create one
             #   print(f"there is no right child, so we will create one")
                node.right_node = BST_Node(data, node)  

    def search(self, name):
        temp_node = self.root
        if name == self.root.data.name:
   
            return self.root.data
        
        elif name < self.root.data.name and temp_node.left_node is not None:
            temp_node = temp_node.left_node
            return self.search_node(name, temp_node)
        
        elif name > self.root.data.name and temp_node.right_node is not None:
            temp_node = temp_node.right_node
            return self.search_node(name, temp_node) 
# the 'get' method
    def search_node(self, name, node):
        if name == node.data.name:
            return node.data
        elif name < node.data.name and node.left_node is not None:
            return self.search_node(name, node.left_node)
        elif name > node.data.name and node.right_node is not None:
            return self.search_node(name, node.right_node)
        
    
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
           
    def traverse_in_order(self, node):
        if node is not None:
            if node.left_node is not None:
                self.traverse_in_order(node.left_node) 
            print(node.data)
            if node.right_node is not None:
                self.traverse_in_order(node.right_node) 
            
    def __repr__(self):
        #output = ""
        for i in range(len(Artist.all_artists)):
            print(Artist.all_artists.traverse())

 
'''
The parameters of an artist object include its name, facebook, twitter, website, genre, and mtv. Each artist also has a 
Stack of their albums. Each artists also has a Queue of their upcoming tours. Every artist is inserted into the Binary
Search Tree of all_artists when the class is called. The repr method returns a string representation of the artist object.
The instantiate from csv method imports all of the objects in the csv file. It takes a parameter of the file's name and 
then for all of the columns in the spreadsheet, it gets the individual items and makes an artwork object out of them.  
'''
class Artist:
    all_artists = BinarySearchTree()
   
    def __init__(self, name, facebook, twitter, website, genre, mtv):
        self.name = name
        self.facebook = facebook
        self.twitter = twitter
        self.website = website
        self.genre = genre
        self.mtv = mtv
        self.albums = Stack()
        self.upcoming_tours = Queue()
        Artist.all_artists.insert(self)

        
    
    def __repr__(self):
        return (f"Name: '{self.name}' Facebook: {self.facebook}  Twitter:  {self.twitter}  Website: {self.website}  Genre: {self.genre} MTV: {self.mtv}")
    
       
    @classmethod          
    def instantiate_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            all_artists = csv.DictReader(f)
            items = list(all_artists)
        for item in items:
            Artist(
              name = item.get('name')[1:-1],
              facebook = item.get('facebook'), #would by default read as a string
              twitter = item.get('twitter'),
              website = item.get('website'),
              genre = item.get('genre'),
              mtv = item.get('mtv'),
              )
'''
a Queue is a LinkedList that functions in a particular way, like a queue with a first in, first out function. The only
parameters of queue are the front and the rear. In this program a queue is used to hold each albums upcoming tours and the
objects that hold info about them. The enQueue method adds a new node to the end of the queue. first it checks
is the front is none, it adds the new node as the front node. If the rear is none it makes the rear the new node and then
connects the front.next_node as the rear and then makes the rear the new node. If neither of those are true, you make a new
node and make the rear's next node the new node and then makes the new node the rear node. The deQueue method sets a 
temp_node equal to the front node. Then the front node is changed to the front's next node, removing current front node. 
We then return the temp_node's data in order to return the original front node. Then we have a repr function that returns a
string interpretation of a queue by looping through in and adding the repr of each node to an output and returning it.
'''
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
        elif self.rear is None:
            self.front.next_node = new_node
            self.rear = new_node
        else:
            new_node = Node(data)
            temp_node = self.front
            self.rear.next_node = new_node
            self.rear = new_node

    def deQueue(self):
        if self.front is not None:
            temp_node = self.front
            self.front = self.front.next_node
            return temp_node.data

    def __repr__(self):
        output = ""
        temp_node = self.front
        while temp_node is not None:
            output += temp_node.data.__repr__() + "\n"
            temp_node = temp_node.next_node
        return output
'''
In this program the Tours class creates objects of upcoming tours for artists. The class holds a queue with all tours. Each
Tour has a parameter of start_date, end_date, name, artists_name, and upcoming_tours. When the class is called the tour
is added to the all_tours queue. It also has a a parameter of artist which utilizes the search function to return the 
artist object. It also adds the tour to the specific queue for that artists tours. This class has a repr that returns a 
string representation of the tour objects.
'''
class Tours:
    all_tours = Queue()  

    def __init__(self, start_date, end_date, name, artists_name):
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.artists_name = artists_name
        Tours.all_tours.enQueue(self)
        self.upcoming_tours = Queue()
        self.artist = Artist.all_artists.search(self.artists_name)
        print(self.artist)
        self.artist.upcoming_tours.enQueue(self)
    
    def __repr__(self):
        return (f"Name: {self.artists_name} Start Date: {self.start_date}  End Date:{ self.end_date}")

'''
The Node class creates a new node and sets the next node to be null. It has two parameters, the date and the next node. It 
also has a repr that returns a string representation of a a node.
'''
class Node:
    def __init__(self, data):
        self.data = data #actual value in the list
        self.next_node = None #reference for the next node
        
    def __repr__(self):
        return self.data.__repr__()
'''
A stack is a LinkedList but it behaves in a particular way, like a stack and follows a last in, first out rule. The only 
parameters are again the number of nodes and the head_node except here it is called top of a stack object. The push method 
adds a card to the head node of the stack. If the top is none, it adds it to the top, but doesn't connect it
to anything because there is no other node. If it is not none, you connect to the next_node and add it to the top. The pop
method removes and returns the item at the top of the stack. The peek method allows you to see the object at a particular 
"index" by looping through for range of the given index and making the temp node the next node for that amount of times 
and then returning the object at that "index" 
''' 
class Stack:
    def __init__(self):
        self.num_of_nodes = 0
        self.top = None
        
    def __repr__(self):
        output = self.top.data + "\n"
        temp_node = self.top
        while temp_node is not None and temp_node.next_node is not None:
            output += temp_node.next_node.data + "\n"
            temp_node = temp_node.next_node
        return output

    def push(self, data):
        self.num_of_nodes +=1
        new_node = Node(data)
        
        if self.top is None:
            self.top = new_node
        else:
            new_node.next_node = self.top  # links to next node
            self.top = new_node
            
    def pop(self):
        temp_node = self.top
        self.top = self.top.next_node
        return temp_node
    
    def peek(self, index):
        temp_node = self.top
        if temp_node.next_node is not None:
            for i in range(index):
                temp_node = temp_node.next_node
            return temp_node.data
        else:
            return self.top.data
    
Artist.instantiate_from_csv("artists.csv")
def demo():
    print("Would you like to create, remove, or view an album, a tour, or search for an artist? Enter either album, tour, or artist.")
    input1 = input()
    if input1 == "tour":
        print("Would you like to create an album or view all albums? Enter create or view")
        q2 = input()
        if q2 == "create":
            print("What is the start date?")
            start_date_input = input()
            print("What is the end date?")
            end_date_input = input()
            print("What is the name of the tour?")
            tour_name_input = input()
            print("Which artist is going on this tour?")
            artist_name_input = input()
            tour1 = Tours(start_date_input, end_date_input, tour_name_input, artist_name_input)
            print("This is the tour you created:")
            print(tour1)
        if q2 == "view":
            print("Would you like to view a specific artists upcoming tours or all tours? Enter all or artist")
            q3 = input()
            if q3 == "all":
                print(Tours.all_tours)
            if q3 == "artist":
                print("What artist's tours would you like to view?")
                q4 = input()
                artist = Artist.all_artists.search(q4)
                print(artist.upcoming_tours)
                
    if input1 == "album":
        print("Would you like to create, remove the top album, or view an artists album history an album? Enter create or remove or view")
        q1 = input()
        if q1 == "create":
            print("What is the name of the album you would like to create?")
            album_input = input()
            print("Who is the album's artist?")
            artist_album_input = input()
            artist1 = Artist.all_artists.search(artist_album_input)
            artist1.albums.push(album_input)
            print("This is the album you created:")
            print(artist_album_input)
        if q1 == "remove":
            print("Who is the album's artist?")
            artist_album_input2 = input()
            artist2 = Artist.all_artists.search(artist_album_input2)
            artist2.albums.pop()
            print("This is the albums after you removed the top node:")
            print(artist2.albums)
        if q1 == "view":
            print("What artists albums would you like to view?")
            artist_album_input3 = input()
            print("How many of their albums?")
            index = input()
            artist3 = Artist.all_artists.search(artist_album_input3)
            print("Here are the albums:")
            print(artist3.albums.peek(int(index)))
    if input1 == "artist":
        print("Would you like to view all of the artists, or search for a specific one? Enter all or artist")
        q5 = input()
        if q5 == "artist":
            print("What artist would you like to search for?")
            artist_input = input()
            artist = Artist.all_artists.search(artist_input)
            print("Here is the artist:")
            print(artist)
        if q5 == "all":
            print(Artist.all_artists.traverse())
    print("Would you like to add another album or tour? Yes or No")
    question = input()
    if question == "Yes":
        demo()
    if question == "No":
        print("End")

demo()


    
