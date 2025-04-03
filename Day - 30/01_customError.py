fruits = ['Apple', 'Mango', 'Peach']

def make_pie(index):
    try:
        fruit = fruits[index]
        print(f"{fruit} pie")
    except IndexError:
        print(None)

make_pie(2)