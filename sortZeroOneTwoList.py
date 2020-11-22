# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def sortZeroOneTwoList(l):
    x,y,z=0,0,0
    temp=l
    while temp:
        if temp.value==0: x+=1
        if temp.value==1: y+=1
        if temp.value==2: z+=1
        temp=temp.next
    temp=l
    
    while x:
        temp.value=0
        x-=1
        temp=temp.next
    while y:
        temp.value=1
        y-=1
        temp=temp.next
    while z:
        temp.value=2
        z-=1
        temp=temp.next
    return l
            
    

