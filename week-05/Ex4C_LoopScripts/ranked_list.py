want_to_go = ["Miami", "Los Angeles", "Cape Cod", "San Francisco", "New York"]

for index, city in enumerate(want_to_go, start=1):

    print(f"{index}. {city}")

    if index == 1:
        print("<- top pick!")
