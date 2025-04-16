A = []
ST = []

def build(node, L, R):
    global A, ST

    # Leaf node where L == R
    if (L == R):
        ST[node] = A[L]
    else:
        mid = (L+R)//2

    # Recursively travel the left half
    build(2*node, L, mid)

    #Recurcively travel the right half
    build(2*node +1, mid+1, R)

    #Storing the sum of both children into parent
    ST[node] = ST[2*node] + ST[2*node + 1]


if __name__ == "__main__":
    n = 6
    A = [0, 1, 3, 5, -2, 3]

    # Create a segment tree of size 4*n
    ST = [0 for i in range(4*n)]

    # Build a segement tree
    build(1, 0, n-1)
    