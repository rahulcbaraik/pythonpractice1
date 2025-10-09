base_bonus = 4000
perfomance_score = 3.8
new_bonus = base_bonus + (3.8 * 100)
remainder = new_bonus % 3
check1 = new_bonus > 4500 and remainder == 0
print(new_bonus, check1)

