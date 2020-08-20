import random

class Stack:
    def __init__(self,list,limit):
        self.list = list
        self.limit = limit

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.list.pop()

    def push(self,element):
        if self.is_full():
            print("stack is full")
        else:
            self.list.append(element)

    def peak(self):
        return self.list[len(self.list)-1]

    def is_empty(self):
        return len(self.list) == 0

    def is_full(self):
        return len(self.list) == self.limit


deck = Stack([],20)
colors = ["red","blue","green","yellow"]
for i in range(20):
    rand_color = random.choice(colors)
    rand_num = random.randrange(1,9)
    rand_card = {"color":rand_color, "num":rand_num}
    deck.push(rand_card)
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
    print("%s- %s-%s"%(count,i["color"],i["num"]))
    count += 1

count = 1
print("-------------------------")
print("player 2:")
print("-------------------------")
for i in player_2:
    print("%s- %s-%s"%(count,i["color"],i["num"]))
    count += 1

first_card = deck.peak()
print("\n-------------------------")
print("First card in deck: %s-%s"%(first_card["color"],first_card["num"]))
print("-------------------------")
