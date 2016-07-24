A = [5,2,4,6,1,3]
print (A)
length = len(A)
print (length)
#----insert sort----
#for j in range(1,length):
#    key = A[j]
#    i = j-1
#    while i>=0 and A[i]>key:
#        A[i+1] = A[i]
#        i = i-1
#    A[i+1] = key

#----select sort----
#for j in range(0,length-1):
#    key = A[j]
#    key_id = j
#    for i in range(j+1,length):
#        if A[i]<key:
#            key = A[i]
#            key_id = i
#        i = i+1
#    A[key_id] = A[j]
#    A[j] = key

print (A)