class RingBuffer:                                               # create RingBuffer class with arg capacity
    def __init__(self, capacity):                               # constructor, add capacity
        self.capacity = capacity                                # make capacity useful
        self.data = []

    class __Full:                                               # create Full class to be used when needed
        def append(self, item):                                 # append method allows items to be added
            self.data[self.cur] = item                          # item is set as the current element in the list
            self.cur = (self.cur + 1) % self.capacity           # set current count equal to what remains (modulus)

        def get(self):                                          # get method defined
            return self.data[self.cur:]+self.data[:self.cur]    # return list (recursively)

    def append(self, item):                                     # append method defined
        self.data.append(item)                                  # append an item to the data
        if len(self.data) == self.capacity:                     # if full
            self.cur = 0                                        # reset current count to zero
            self.__class__=self.__Full                          # launch the Full class and make it active

    def get(self):                                              # get data method defined
        return self.data                                        # return the data

"""
my test follows:

"""

x = RingBuffer(5)

x.append("a")
x.append("b")
x.append("c")
x.append("d")
x.append("e")
print(x.data), x.get()

x = RingBuffer(5)
x.append("a")
x.append("b")
x.append("c")
x.append("d")
x.append("e")
x.append("f")
print(x.data), x.get()

x = RingBuffer(5)
x.append("a")
x.append("b")
x.append("c")
x.append("d")
x.append("e")
x.append("f")
x.append("g")
x.append("h")
x.append("i")
print(x.data), x.get()