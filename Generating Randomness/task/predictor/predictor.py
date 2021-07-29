min_len = 100
curr_len = 0
process_in = []

while curr_len < min_len:
    in_ = input("Print a random string containing 0 or 1: \n")
    for i in in_:
        if i in "01":
            process_in.append(i)
    curr_len = len(process_in)
    print(f"Current data length is {curr_len}, {min_len - curr_len} symbols left")

print("Final data string: ")
print("".join(process_in))