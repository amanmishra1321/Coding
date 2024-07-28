# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    temp = head
    temp1 = ListNode(0,head)
    temp2 = temp1
    while(temp):
        if(temp.val < x):
            temp1.next = temp
            temp1 = temp1.next
        temp = temp.next
    temp = head
    # print("Infinite :Loop")
    while(temp):
        if(temp.val >= x):
            temp1.next = temp
            temp1 = temp1.next
        temp = temp.next
    # print("Infinite :Loop2")
    return temp2.next

arr = [1,4,3,2,5,2]
x = 3

# arr = [2,3]
# x = 2

head = ListNode(arr[0])
temp = head
temp1 = head
for i in range(1,len(arr)):
    temp.next = ListNode(arr[i])
    temp = temp.next
# while(temp1):
#     print(ans.val,end=" ")
ans = partition(head,x)
while(ans):
    print(ans.val,end=" ")
    ans=ans.next
