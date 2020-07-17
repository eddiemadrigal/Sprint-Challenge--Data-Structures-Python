class Node:
    def __init__(self, value=None, next_node=None): # constructor given
        self.value = value                          # assignment
        self.next_node = next_node                  # assignment

    def get_value(self):                            # method given
        return self.value                           # given

    def get_next(self):                             # method given
        return self.next_node                       # given

    def set_next(self, new_next):                   # method given
        self.next_node = new_next                   # given

class LinkedList:
    def __init__(self):                             # default constructor
        self.head = None                            # initialize head of the list to None (empty list)
        
    def add_to_head(self, value):                   # given 
        node = Node(value)                          # given

        if self.head is not None:                   # check if head is None
            node.set_next(self.head)                # given

        self.head = node                            # assign head the node, node is now the new head

    def contains(self, value):                      # given
        if not self.head:                           # if there is no head
            return False                            # end

        current = self.head                         # set head as current position

        while current:                              # while current is True
            if current.get_value() == value:        # if the value is in the right position
                return True                         # return True   

            current = current.get_next()            # set the next position to current

        return False                                # return False

    def reverse_list(self, node, prev):             # node and prev will be used
        prev = None                                 # keep track of prev (now set to None)
        current = self.head                         # set current to the head of the list
        while current:                              # while not at the end of the list (hence True)
            next_node = current.next_node           # set current's next node to next_node
            current.next_node = prev                # change direction: current.next_node is reversed to prev
            prev = current                          # remember to move right, to the next item on the list 
            current = next_node                     # current becomes the next_node to evaluate
        self.head = prev                            # when while is False, set head as prev (opposite direction)
