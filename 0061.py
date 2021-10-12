A, B = input().split()
C, D = input().split()
E, F = input().split()
G, H = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
E = int(E)
F = int(F)
G = int(G)
H = int(H)

if A + C + E + G > B + D + F + H:
    print(1)
elif A + C + E + G < B + D + F + H:
    print(2)
else: print("DRAW")
