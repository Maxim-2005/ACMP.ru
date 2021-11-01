K = int(input())
G, C, V = "G", "C", "V"
for i in range(K % 3):
    G, C, V = V, G, C
print(G+C+V)
