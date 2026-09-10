class LinkedList:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
        self.freq=1
class FreqTable:
    def __init__(self):
        self.head=None
        self.tail=None
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.freq={}
        self.curr=0
        self.keyValue={}
    def freqUpdate(self,node,temp):
        if temp.head==node and temp.tail==node:
            temp.head=None
            temp.tail=None
        elif temp.head==node:
            temp.head=temp.head.next
            temp.head.prev=None
        elif temp.tail==node:
            temp.tail=temp.tail.prev
            temp.tail.next=None
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        if temp.head is None and self.curr==node.freq:
            del self.freq[node.freq]
            self.curr+=1
        elif temp.head is None:
            self.freq[node.freq]
        node.freq+=1
        if node.freq not in self.freq:
            self.freq[node.freq]=FreqTable()
        table=self.freq[node.freq]
        if table.head is None:
            table.head=node
            table.tail=node
        else:
            node.next=table.head
            table.head.prev=node
            table.head=node
    def get(self, key: int) -> int:
        if key not in self.keyValue:
            return -1
        node=self.keyValue[key]
        temp=self.freq[node.freq]
        self.freqUpdate(node,temp)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyValue:
            node=self.keyValue[key]
            temp=self.freq[node.freq]
            node.val=value
            self.freqUpdate(node,temp)
            return
        node=LinkedList(key,value) 
        if len(self.keyValue)==self.capacity:
            temp=self.freq[self.curr]
            del self.keyValue[temp.tail.key]
            if temp.head==temp.tail:
                temp.head=None
                temp.tail=None
                del self.freq[self.curr]
            else:
                temp.tail=temp.tail.prev
                temp.tail.next=None

        if  node.freq not in self.freq:
            self.freq[node.freq]=FreqTable()
        table=self.freq[node.freq]
        self.keyValue[node.key]=node
    
        if table.head is None:
            table.head=node
            table.tail=node
        else:
            node.next=table.head
            table.head.prev=node
            table.head=node
        self.curr=1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)