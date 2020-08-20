import random


class Node:
    def __init__(self, color, num, next_node=None):
        self.color = color
        self.num = num
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_color(self):
        return self.color

    def get_num(self):
        return self.num

class Stack:
    def __init__(self, limit=20):
        self.top_node = None
        self.size = 0
        self.limit = limit

    def peek(self):
        return self.top_node

    def push(self, color, num):
        if self.is_full():
            print("stack is full")
        else:
            item = Node(color,num)
            item.next_node = self.top_node
            self.top_node = item
            self.size += 1

    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            popped = self.top_node
            self.top_node = popped.get_next_node()
            self.size -= 1
            return popped


    def is_full(self):
        return self.size == self.limit

    def is_empty(self):
        return self.size == 0




deck = Stack()
colors = ["red","blue","green","yellow"]
for i in range(20):
    rand_color = random.choice(colors)
    rand_num = random.randrange(1,9)
    deck.push(rand_color,rand_num)

player_1 = []
for i in range(5):
    player_1.append(deck.pop())
player_2 = []
for i in range(5):
    player_2.append(deck.pop())

count = 1
print("-------------------------")
print("player 1:")
print("-------------------------")
for i in player_1:
    print("%s- %s-%s"%(count,i.get_color(),i.get_num()))
    count += 1

count = 1
print("-------------------------")
print("player 2:")
print("-------------------------")
for i in player_2:
    print("%s- %s-%s"%(count,i.get_color(),i.get_num()))
    count += 1

first_card = deck.peek()
print("\n-------------------------")
print("First card in deck: %s-%s"%(first_card.get_color(),first_card.get_num()))
print("-------------------------")
