X = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
    for J in range(len(X[0])):
        result[J][i] = X[i][J]        
        
for r in result:
    print(r)