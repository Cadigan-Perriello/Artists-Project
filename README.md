# Artists Project
Program Usage:
This program could be used by an agent or manager of a musical artist. It could be used by then to create albums and view
information on past albums by their artist. It could also be used to store old tours so that the manager could view info
on when the artists past tours and plan and store information on future tours. It also just holds basic information on each
artist which could be used by a manager but could also be searched by fans in order to learn about a new artist.

BST Node:
The Binary Search Tree nodes have 4 parameters: data, left_node, right_node, and the parent of the node. The only other 
method it has is a represent which returns a string interpretation of the node. Each node in the Binary Search Tree is an
artist object. In this program a BST node is an artist object.

BST Class:
The Binary Search Tree class only has two parameters: the root of the tree and the number of nodes in the tree. It has an 
insert and an insert_node class that work together to allow for the inserting of a new node into the tree. The classes work
with recursion and go through the tree to find the correct place to insert the new node or to create a new node. The search
and search_node classes work similarly by traversing through the tree until the given name of the artist equals the node's
data that it is currently on. Similarly, the traverse and traverse_node classes work together in order to loop through 
every node in the class, which is used when we need to print out the tree. We end with a repr which returns a string 
interpretation of the Binary Search tree. In this program the Binary Search Tree is an alphabetically organized tree that
holds all of the artist objects.

Artist Object:
The parameters of an artist object include its name, facebook, twitter, website, genre, and mtv. Each artist also has a 
Stack of their albums. Each artists also has a Queue of their upcoming tours. Every artist is inserted into the Binary
Search Tree of all_artists when the class is called. The repr method returns a string representation of the artist object.
The instantiate from csv method imports all of the objects in the csv file. It takes a parameter of the file's name and 
then for all of the columns in the spreadsheet, it gets the individual items and makes an artwork object out of them.

Queue:
a Queue is a LinkedList that functions in a particular way, like a queue with a first in, first out function. The only
parameters of queue are the front and the rear. In this program a queue is used to hold each albums upcoming tours and the
objects that hold info about them. The enQueue method adds a new node to the end of the queue. first it checks
is the front is none, it adds the new node as the front node. If the rear is none it makes the rear the new node and then
connects the front.next_node as the rear and then makes the rear the new node. If neither of those are true, you make a new
node and make the rear's next node the new node and then makes the new node the rear node. The deQueue method sets a 
temp_node equal to the front node. Then the front node is changed to the front's next node, removing current front node. 
We then return the temp_node's data in order to return the original front node. Then we have a repr function that returns a
string interpretation of a queue by looping through in and adding the repr of each node to an output and returning it.

Tours class:
In this program the Tours class creates objects of upcoming tours for artists. The class holds a queue with all tours. Each
Tour has a parameter of start_date, end_date, name, artists_name, and upcoming_tours. When the class is called the tour
is added to the all_tours queue. It also has a a parameter of artist which utilizes the search function to return the 
artist object. It also adds the tour to the specific queue for that artists tours. This class has a repr that returns a 
string representation of the tour objects.

Node Class:
The Node class creates a new node and sets the next node to be null. It has two parameters, the date and the next node. It 
also has a repr that returns a string representation of a a node.

Stack Class:
A stack is a LinkedList but it behaves in a particular way, like a stack and follows a last in, first out rule. The only 
parameters are again the number of nodes and the head_node except here it is called top of a stack object. The push method 
adds a card to the head node of the stack. If the top is none, it adds it to the top, but doesn't connect it
to anything because there is no other node. If it is not none, you connect to the next_node and add it to the top. The pop
method removes and returns the item at the top of the stack. The peek method allows you to see the object at a particular 
"index" by looping through for range of the given index and making the temp node the next node for that amount of times 
and then returning the object at that "index"
