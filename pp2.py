raw_data = "LOC-3914-A27-2025-BATCH"
approved_location = ["LOC", "WHSE", "RACK"]
sliced = raw_data[4:8]
print(sliced)
check1 = sliced in approved_location
year = raw_data[13:17]
print(check1)
print(year)


