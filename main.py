from funcs.utils import sorted_operations, censored_sender, cencored_addressee, new_time_format

count = 0
while count < 5:
    print(new_time_format(count),end=" ")
    print(sorted_operations()[count]["description"])
    print(censored_sender(count),end=" ")
    print(cencored_addressee(count))
    print(sorted_operations()[count]["operationAmount"]["amount"],end=" ")
    print(sorted_operations()[count]["operationAmount"]["currency"]["name"],end="\n\n")
    count += 1
