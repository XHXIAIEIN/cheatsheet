import csv

headers = ['id','name','price']

items = [
    {'id': 1, 'name': "Apple", 'price': 12.0},
    {'id': 2, 'name': "Banana", 'price': 13.0},
    {'id': 3, 'name': "Cherry", 'price': 17.0},
    {'id': 4, 'name': "Mango", 'price': 49.0}
]

try:
    with open(r"test.csv", mode='a+', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for data in items:
            writer.writerow(data)
except IOError:
    print("I/O error")
