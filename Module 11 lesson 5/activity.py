def swap(m,n):
    m = m ^ n
    n = m ^ n
    m = m ^ n

    print("After swapping: m = ", m, "and n = ", n)

swap(12,19)