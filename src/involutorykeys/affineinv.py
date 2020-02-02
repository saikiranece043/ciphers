import prettytable as p


t = p.PrettyTable([ 'a', 'b', 'a * a  mod m', ' b (a+1) mod m', 'inv keys'])
m = 39
b = 1
count =0
for a in range(m):
    for b in range(m):
        x = a * a % m
        y = (b * (a + 1)) % m
        if x == 1 and y == 0:
            t.add_row([a, b, x ,y, (a,b)])
            count = count +1



print(t)
print(count)