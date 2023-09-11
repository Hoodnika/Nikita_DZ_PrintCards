from funcs.utils import sorted_operations, censored_sender, cencored_addressee, new_time_format

count = 0
while count < 5:
    print(new_time_format("operations.json", count),end=" ")
    print(sorted_operations("operations.json")[count]["description"])
    print(censored_sender("operations.json", count),end=" ")
    print(cencored_addressee("operations.json", count))
    print(sorted_operations("operations.json")[count]["operationAmount"]["amount"],end=" ")
    print(sorted_operations("operations.json")[count]["operationAmount"]["currency"]["name"],end="\n\n")
    count += 1
