### Curency Calculator
print("Enter BDT any amount currency for calculation")
n = int(input())
print("Amount of Money = {} Taka".format(n))

a = n // 100
n = n - (a * 100)

b = n // 50
n = n - (b * 50)

c = n // 20
n = n - (c * 20)

d = n // 10
n = n - (d * 10)

e = n // 5
n = n - (e * 5)

f = n // 2
n = n - (f * 2)

g = n // 1

print("{} note(s) Taka 100".format(a))
print("{} note(s) Taka 50".format(b))
print("{} note(s) Taka 20".format(c))
print("{} note(s) Taka 10".format(d))
print("{} note(s) Taka 5".format(e))
print("{} note(s) Taka 2".format(f))
print("{} note(s) Taka 1".format(g))

