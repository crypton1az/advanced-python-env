items_log = input().split()
frequency_dict = {}
for product in items_log:
    frequency_dict[product] = frequency_dict.get(product, 0) + 1
print("Purchase frequency:")
for product, freq_val in frequency_dict.items():
    print(f"{product}: {freq_val}")
top_item = None
max_freq = 0
for product, freq_val in frequency_dict.items():
    if freq_val > max_freq:
        max_freq = freq_val
        top_item = product
print(f"\nMost popular item: {top_item}")
single_items = []
for product, freq_val in frequency_dict.items():
    if freq_val == 1:
        single_items.append(product)
print(f"\nPurchased once: {' '.join(single_items)}")
sorted_items = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
print("\nSorted by frequency:")
for product, freq_val in sorted_items:
    print(f"{product} {freq_val}")
