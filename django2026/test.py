print("hello")


def foo(a, b):
    return a + b


a = 1
b = 2
foo(a, b)


args = [1, 2]
foo(args[0], args[1])

args = [10, 2]
foo(*args)


def kek(a=1, b=1):
    return a + b * 10


kwargs = {"a": 2, "b": 1}
kek(**kwargs)


def lol(*args, **kwargs):
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")


lol(1, 2, 3, a=1, b=2, c=3)


ls = [
    {"id": 1, "name": "иван"},
    {"id": 2, "name": "Петр"},
    {"id": 2, "name": "Грирорий"},
]
ls_name = []
for x in ls:
    ls_name.append(x["name"])
print(ls_name)

list(map(lambda x: x["name"], ls))
