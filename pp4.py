candidates = ["Ava", "Brenda", "Charles", "David", "Elizabeth"]
longest_string = max(candidates, key=len)
check1 = len(longest_string) >= 10
print(f"{longest_string}\n{check1}")
