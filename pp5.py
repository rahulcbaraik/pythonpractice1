delivery_manifest = ("ITEM-X12", 240, 0.45)
product_id, quantity, unit_weight = delivery_manifest
total_weight = unit_weight * quantity
average_weight = divmod(quantity, 10)
print(f"{product_id},{total_weight:.3f}")