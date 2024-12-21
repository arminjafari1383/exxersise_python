def genrate_cartesian_table(n,m):
    result = []
    for i in range(n):
        result.append(' _'*m)
        result.append('| ' * (m + 1))
    result.append(' _' * m)
    return '\n'.join(result)
n,m = map(int,input().split())
output = genrate_cartesian_table(n,m)
print(output)
