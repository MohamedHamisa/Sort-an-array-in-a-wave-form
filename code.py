def rearrange(A):
    for i in range(len(A)):
        # for even positioned items
        if i%2 == 0 and A[i] > A[i+1] :
            A[i], A[i+1] = A[i+1], A[i]

        # for odd positioned items
        if i%2 == 1 and A[i] < A[i+1] :
            A[i], A[i+1] = A[i+1], A[i]
    return A
