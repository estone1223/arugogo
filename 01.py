#%%
l = [int(i) for i in range(1, 6)]

for i, e in enumerate(l):
    print(i, e)

#%%
i = 0
while i < 4:
    print(i)
    i += 1


# %%
data = [int(i) for i in range(10)]
data

# %%
data = [int(i) for i in range(10) if i % 2 == 0]
data
# %%
def add (a, b):
    return a + b

add(1, 3)
add(2, 50)
# %%
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def login(self, password):
        if self.__password == password:
            print('ログインに成功しました')
            return True
        else:
            print('ログインに失敗しました')
            return False

    def logout(self):
        print('logout')


a = User('estone', 'haroharo')

if a.login('haroharo'):
    a.logout()

# %%
class GuestUser(User):
    def __init__(self):
        super().__init__('guest', 'guest')

b = GuestUser()
if b.login('guest'):
    b.logout()
    
# %%
x = 3

def calc(x):
    x += 4
    return x

print(x)
print(calc(x))
print(x)

# %%
a = [3]

def calc(a):
    a[0] += 4
    return a

print(a)
print(calc(a))
print(a)

# %%

a = [3]

def calc(a):
    a = [4]
    return a

print(a)
print(calc(a))
print(a)

# %%
