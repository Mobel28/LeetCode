class LinkedList:
    def __init__(self,val,key):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.curr=0
        self.cache={}
        self.head=None
        self.tail=None
    def updateHead(self,node):
        node.prev.next=node.next
        if node.next:
            node.next.prev=node.prev
        else:
            self.tail=node.prev
        node.next=self.head
        self.head.prev=node
        node.prev=None
        self.head=node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            if node!=self.head:
                self.updateHead(node)
            # self.curr-=1
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val=value
            if self.cache[key]!=self.head:
                self.updateHead(self.cache[key])
            return
        node=LinkedList(value,key)
        # self.cache[key]=node
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            if self.curr==self.cap:
                old_tail=self.tail.prev
                del self.cache[self.tail.key]
                if old_tail:
                    self.tail=old_tail
                    self.tail.next=None
                else:
                    self.head=node
                    self.tail=node
                    self.cache[key]=node
                    return
                self.curr-=1
            self.head.prev=node
            node.next=self.head
            self.head=node
        self.cache[key]=node

        self.curr+=1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)