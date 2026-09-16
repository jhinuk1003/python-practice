age = int(input("Enter your age: "))
licence = input("Do you have a provisional licence? (y/n): ")

if age >= 17:
    if licence == "y":
        print("You can book the driving test.")
    else:
        print("Get a provisional licence first.")
else:
    print("You must be at least 17.")