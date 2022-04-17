# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from collections import deque


def graph():
    # Adjacency List
    # example is singly linked
    # 1->2,3,4
    # 2->3,4
    # 3->5,6
    # ->7

    # Create a dictionary of Lists which contain the current index and the index of list it is connected to

    sl_list = {1: [2, 3, 4],
               2: [3, 4],
               3: [5, 6],
               5: [7],
               6: [None]
               }

    # Accessing

    print(" accessing vertex 5 through other verteces: ", sl_list[sl_list[sl_list[sl_list[1][0]][0]][0]])
    print(" accessing vertex 5 through other verteces: ", sl_list[5])


def deque_queue():
    # initializing A Deque linked list
    queue = deque()
    queue.append("bob")
    queue.append("James")
    queue.append("Rohan")
    queue.append("Okame")

    print("queue", queue)
    # popleft- FIRST IN FIRST OUT
    queue.popleft()
    print("queue.popleft()", queue)

    # items are accessed from index 0 to end

    for items in queue:
        print(items)


def stack():

    # LIFO Approach- Append-left

    stacking = deque()
    # eat food (0)
    stacking.appendleft("eat food")
    # prepare food (0), eat food(1)
    stacking.appendleft("prepare food ")
    # source food (0), prepare food (1), eat food(2)
    stacking.appendleft("source food ")
    # earn money(0), source food (1), prepare food (2), eat food(3)
    stacking.appendleft("earn money")

    # items are accessed from index 0 to end

    for items in stacking:
        print(items)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LList:

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        # insert at the head
        node = Node(data, next=self.head)
        self.head = node

    def insert_back(self, data):
        # insert at the tail where next = None
        if self.head is None:
            self.head = Node(data, next=None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, next=None)

    def insert_values(self, data_list, location: str = "back"):

        for item in data_list:
            match location:
                case "back":
                    self.insert_back(item)
                case "front":
                    self.insert_front(item)
                case _:
                    raise Exception("invalid value for 'location' parameter")

    def remove_item(self, index: int):
        if index < 0 or index >= self.length():
            raise Exception("invalid index")
        if index == 0:
            # only 1 node in the linked list and that by default is the head
            self.head = self.head.next
            return

        counter = 0
        itr = self.head

        while itr:
            if counter < index - 1:
                itr = itr.next
                counter += 1

            else:
                itr.next = itr.next.next
                break

    def insert_at(self, index: int, data):

        if index < 0 or index >= self.length():
            raise Exception("invalid index")

        if index == 0:
            # only 1 node in the linked list and that by default is the head
            self.insert_front(data)
            return

        counter = 0
        itr = self.head
        while itr:
            if counter < index - 1:  # while counter value is less than the index before the desired index
                itr = itr.next
                counter += 1

            # create node with with points to the next node. (current next node currently is at desired index)
            # e.g index = 3, therefore the while loop breaks at counter = 2
            # created node will point to the node which is currently at index 3

            node = Node(data, itr.next)
            # set the current node the newly created node
            # ... e.g current node is at index 2. so the new next index ( index 3) is set to the node just created
            # 0-> 1 -> 2 -> node -> previous 3 -> 4
            itr.next = node
            break  # used otherwise while loop will continue until itr.next = None

    def insert_after_value(self, value, data_to_insert):

        if self.head is None:
            self.insert_back(data_to_insert)
            return

        itr = self.head

        while itr:
            if itr.data != value:
                itr = itr.next

            else:
                # create node with with points to the next node. (current next node currently is at desired index)
                node = Node(data_to_insert, itr.next)
                # set the current node the newly created node
                itr.next = node
                break

            if itr is None:
                print(f"linked list doesnt not contain the value: {value}")

    def remove_by_value(self, value):

        itr = self.head
        counter = 0

        while itr:
            if itr.data != value:
                itr = itr.next
                counter += 1

            else:
                self.remove_item(counter)
                break
        if itr is None:
            print(f"Linked list does not contain value: {value}")

    def print(self):

        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstring = ''

        while itr:
            llstring += str(itr.data) + '-->'
            itr = itr.next
        print(llstring)

    def length(self):
        length = 0
        itr = self.head

        while itr:
            length += 1
            itr = itr.next
        return length

    def pop(self):
        pass


class NodeTest:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LlistTest:
    # innit
    def __init__(self):
        self.head = None

    # add item to front
    def add_to_front_test(self, data):
        node = NodeTest(data, next=self.head)
        self.head = node

    # add item back
    def add_to_back_test(self, data):
        if self.head is None:
            self.head = Node(data, next=None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, next=None)

    def length_test(self):

        counter: int = 0
        itr = self.head

        while itr:
            itr = itr.next
            counter += 1

        return counter

    # remove item

    def remove_item_test(self, index: int):
        if index < 0 or index >= self.length_test():
            raise Exception("Invalid Index")
        itr = self.head
        counter = 0
        while itr:
            if counter < index-1:
                itr = itr.next
                counter += 1

            else:
                itr.next = itr.next.next
                break
    # print

    def print_test(self):

        itr = self.head
        llstring = ""
        while itr:
            llstring = str(itr) + "-->"
            itr = itr.next
        print(llstring)

    # add item item at index

    def add_item_at_test(self, index, data):

        if index < 0 or index >= self.length_test():
            raise Exception("Invalid Index")
        itr = self.head
        counter = 0
        while itr:
            if counter < index - 1:
                itr = itr.next
                counter += 1

            else:
                node = NodeTest(data, next=itr.next)
                itr.next = node
                break

    # add item after value

    def add_after_value_test(self, value, data):

        itr = self.head

        while itr:
            if itr.data != value:
                itr = itr.next

            else:
                node = NodeTest(data, next=itr.next)
                itr.next = node
                break

        if itr is None:
            print("Linked List doesn't contain item")

    # remove item at value

    def remove_item_at_value_test(self, value):

        counter = 0
        itr = self.head

        while itr:
            if itr.data != value:
                itr = itr.next
                counter += 1

            else:
                self.remove_item_test(counter)
                break

        if itr is None:
            print("Linked List doesn't contain item")

    def insert_values(self, data_values, location: str = "back"):

        for item in data_values:
            match location:
                case "back":
                    self.add_to_back_test(item)
                case "front":
                    self.add_to_front_test(item)
                case _:
                    raise Exception("invalid value for 'location' parameter")

def linked_list():

    llist1 = LList()

    llist1.insert_front(40)
    llist1.insert_front(89)
    llist1.insert_front(43)
    llist1.insert_back(55)
    llist1.print()

    llist2 = LList()
    list_values = ["Houcine", 30, "programming", "python"]
    llist2.insert_values(list_values)
    llist2.print()
    print(llist2.length())
    llist2.remove_item(3)
    llist2.print()
    llist2.insert_at(2, "loves")
    llist2.print()
    llist2.insert_after_value("python", "stuff")
    llist2.insert_after_value("programming", "stuff")
    llist2.print()
    llist2.remove_by_value(30)
    llist2.print()
    llist2.remove_by_value(10)


#=======================================================================================================================

class HashTable:
    def __init__(self, size: int = 100, mode: str = "probe"):
        self.size = size

        self.mode = mode

        if mode == "probe":
            self.table = [None for i in range(self.size)]

        elif mode == "chain":
            self.table = [LList() for i in range(self.size)]

        else:
            raise Exception("Invalid mode. Mode should be 'chain' or 'probe'")

    def hash(self, key: str):
        h = 0
        for ch in key:
            h += ord(ch) # ord() returns the asci value of a character
        return h % self.size

    def __getitem__(self, key):
        h = self.hash(key)

        if self.mode == "chain":
            itr = self.table[h].head

            while itr:
                if itr.data[0] == key:
                    break
                else:
                    itr = itr.next
            if itr is None:
                print("item key not in list")
            else:
                return itr.data[1]

        else:
            return self.table[h]

    def __setitem__(self, key, value):

        h = self.hash(key)

        if self.mode == "chain":

            itr = self.table[h].head
            while itr:
                if itr.data[0] == key:
                    itr.data = (key, value)
                    break
                itr = itr.next

            if itr is None:
                self.table[h].insert_back((key, value))

        if self.mode == "probe":
            if self.table[h] is not None:
                i = 0
                while i < len(self.table) and self.table[h] is not None:
                    self.table[i] = value
            else:
                self.table[h] = value

    def __delitem__(self, key):
        h = self.hash(key)

        if self.mode == "probe":
            self.table[h] = None

        else:
            self.table[h].remove_by_value(key)

class BSTNode:

    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data: int):
        if data == self.data:
            print("value already in tree")
            return
        elif data < self.data:
            # add a child to the left sub_tree
            if self.left:
                # recursion is used to traverse the subtrees until the left child is None
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)


    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):

        elements =[]


        pass

    def post_order_traversal(self):

        pass


class BST:
    def __init__(self, value_list: list = ""):

        self.root = None
        self.value_list = value_list
        if value_list:
            self.root = BSTNode(value_list[0])
        for i in range(1, len(value_list)):
            self.root.add_child(value_list[i])


    def search(self, value,  mode="breadth", order: str = "in"):

        if mode == "breadth":

            match order:
                case "in":
                # check if tree has a root
                    if self.root:
                        print("tree is empty")
                        return

                # check if root.data == value
                    if self.root.data == value:
                        return True

                    if self.root.data < value:
                        if self.root.left:
                            return self.root.left.search(value)

                        else:
                            return False

                    if self.root.data > value:
                        if self.root.right:
                            self.root.right.search(value)
                        else:
                            return False



                case "pre":
                    pass

                case "post":
                    pass

                case _:
                    raise Exception("invalid paramater value for 'order'.")

        elif mode == "depth":
            if not self.root:
                print("tree is empty")
                return

            match order:
                case "in":

                    pass

                case "pre":
                    pass

                case "post":
                    pass

                case _:
                    raise Exception("Invalid paramater value for 'order'.")

        else:
            raise Exception("Invalid paramater value for 'mode'.")

    def insert(self, values: list):

        if not self.root:
            self.root = BSTNode(values[0])

        for i in range(1, len(values)):
            self.root.add_child(values[i])


    def remove(self, value):
        pass







def binary_search_tree():

    pass


def hash_map():

    ht = HashTable()

    ht["hello"] = "world"

    print("ht[hello] = ", ht["hello"])

    del ht["hello"]

    print("ht[hello] = ", ht["hello"])

    ht2 = HashTable(mode="chain")

    ht2["chaining"] = "almost!"

    print("ht2['chaining']: ", ht2["chaining"])

    i = 0

    strng = "chaining"

    for ch in strng:
        i += ord(ch)

    print("ascii total of 'chaining': ", i)

    strng2 = "dddddddd!"
    j = 0
    for ch in strng2:
        j += ord(ch)
    print("ascii total of 'dddddddd!': ", j)

    ht2["dddddddd!"] = "done!"

    print("ht2['dddddddd!']: ", ht2["dddddddd!"])









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph()
    deque_queue()
    stack()
    linked_list()
    hash_map()


