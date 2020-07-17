import time

start_time = time.time()

class newNode:
    def __init__(self, key):
        self.key = key                      # the value to filter duplicates for
        self.left = self.right = None       # left and right sides of tree set to None

def printDuplicates(tree1, tree2): 
      
    # Create two stacks for two inorder traversals  
    s1 = []                                 # stack 1 initialized to an empty list                  
    s2 = []                                 # stack 2 initialized to an empty list
    count = 0
  
    while True: # do until break (zero nodes left to traverse)
          
        # append the Nodes of first tree to stack s1  
        if tree1:                           # if tree 1 has nodes
            s1.append(tree1)                # append tree 1 to s1
            tree1 = tree1.left              # move everything to tree 1
  
        # append the Nodes of second tree in stack s2  
        elif tree2:                         # if tree 2 has nodes
            s2.append(tree2)                # append tree 2 to s2
            tree2 = tree2.left              # move everything to tree 2
  
        # Both tree1 and tree2 have zero nodes
        elif len(s1) != 0 and len(s2) != 0: # len gives count
            tree1 = s1[-1]                  # last element of tree 1
            tree2 = s2[-1]                  # last element of tree 2
  
            # If current keys in two trees are same  
            if tree1.key == tree2.key:      # if a duplicate found
                print(tree1.key, end = "\n")# print the duplicate list
                count += 1
                s1.pop(-1)                  # delete the duplicate value found in stack 1
                s2.pop(-1)                  # delete the duplicate value found in stack 2
  
                # move to the inorder successor  
                tree1 = tree1.right         # put everything on the right side of tree 1 to tree 1 
                tree2 = tree2.right         # put everything on the right side of tree 2 to tree 2
  
            elif tree1.key < tree2.key:     # if Node of tree 1 is less than Node of tree 2
                s1.pop(-1)                  # remove the last element from stack 1
                tree1 = tree1.right         # tree 1 is set to tree 1 right
                tree2 = None                # tree 2 is set to None 

            elif tree1.key > tree2.key:     # if Node of tree 1 is greater than Node of tree 2
                s2.pop(-1)                  # remove last element from stack 2
                tree2 = tree2.right         # tree 2 is set to tree 2 right
                tree1 = None                # tree 1 is set to None
  
        # Both trees and both stacks are empty (traversing is complete and nothing is left)
        else: 
            print("Total Duplicates Found: " + str(count))
            break                           # get out

def insert(node, key):                      # for every node, insert the name (key)
    if node == None:                        # if no nodes are found
        return newNode(key)                 # return the name

    if key < node.key:                      # check if key to insert is less than the key already there
        node.left = insert(node.left, key)  # if yes, insert the key to the left until key is a leaf in the tree
    elif key > node.key:                    # else the incoming name is greater than what's already there
        node.right = insert(node.right, key)# insert to the right subtree until the new name is a leaf

    return node                             # once done, return the node

if __name__ == '__main__':                  # module to run directly

    # create first tree
    tree1 = None

    #create second tree
    tree2 = None

    # open the first file
    f = open("/Lambda/git/Sprint-Challenge--Data-Structures-Python/names/names_1.txt")
    # read the file and insert into names 1 contents of the file (line by line)
    names_1 = f.read().split("\n")
    # close the file
    f.close()

    # open the second file
    f = open("/Lambda/git/Sprint-Challenge--Data-Structures-Python/names/names_2.txt")
    # read the file and insert into names 2 contents of the file (line by line)
    names_2 = f.read().split("\n")
    # close the file
    f.close()

    for name in names_1:                    # for every name in names_1
        tree1 = insert(tree1, name)         # insert into tree 1 the name found in names and set = to tree 1

    for name in names_2:                    # for every name in names_2
        tree2 = insert(tree2, name)         # insert into tree 2 the name found in names and set = to tree 2

    print("Duplicates: ")                   # label: Duplicates
    printDuplicates(tree1, tree2)           # print duplicates

# duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# print("hello world")

end_time = time.time()                      # end timer
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")