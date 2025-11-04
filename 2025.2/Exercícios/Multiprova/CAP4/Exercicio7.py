n = int(input())
borda = input()
interior = input()

linha_borda = borda * n
linha_meio = borda + (interior * (n - 2)) + borda

print(linha_borda)

for _ in range(n-2):
  print(linha_meio)
  
print(linha_borda)