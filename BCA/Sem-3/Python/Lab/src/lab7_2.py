def clean_and_sort(items):
	count_ = len(items)
	sorted_ = sorted(set(items))
	removed = count_ - len(sorted_)
	return (sorted_,removed)

print("Input:[1,23,43,23,4,43,34,56]")
set_ = clean_and_sort([1,23,43,23,4,43,34,56])
print(f"Cleaned: {set_[0]}\nRemoved: {set_[1]}") 
