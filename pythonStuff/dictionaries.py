dic = {}
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

dic["Name"] = name
dic["Age"] = age
dic["City"] = city


for k, v in dic.items():
    print(f"{k}: {v}")
