# for n in [2,3,4,5,6,7,8,9]:
#     print("--{0}단--".format(n))
#     for i in [2,3,4,5,6,7,8,9]:
#         print("{0} * {1} = {2}".format(n, i, n * i))

# l = [1,2,3,4,5]
# rst = {i**2 for i in l}
# print(rst)

# l = [10,25,30]
# IterL = filter(None, l)
# #[print(i) for i in IterL]

# def GetBiggerThan20(i):
#     return i > 20

# IterL = filter(GetBiggerThan20, l)
#[print(i) for i in IterL]

x = [1,2,3,4,5]
y = ['a','b','c','d']

for item in zip(x,y):
    print(item)

L = [1,2,3]
def add(i):
    return i + 10

for i in map(add, L):
    print(i)


