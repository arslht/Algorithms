def merge(A,p,q,r):

    #L = []; R = []
    n1 = q-p+1; n2 = r-q
    L = [i for i in range(0,n1)]
    R = [i for i in range(0,n2)]

    for i in range(0,n1):
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+1+j]
    L.append(float("inf"))
    R.append(float("inf"))
    #L[n1] = (float("inf"))
    #R[n2] = (float("inf"))
    i = 0; j =0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
if __name__ == "__main__":
    A = [1,3,7,2,4,6]
    print (A)
    merge(A,0,2,5)
    print (A)
