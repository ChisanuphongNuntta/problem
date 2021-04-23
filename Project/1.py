#Choosing a Fuse
def choose_fuse(fuses, current):
	arr = sorted(fuses + [current], key=lambda x: float(x[:-1]))
	return arr[arr.index(current) + 1]

print(choose_fuse(["3V", "5V", "12V"], "4.5V"))
