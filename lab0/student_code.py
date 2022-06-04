def order(data):
	end = len(data)-1
	quicksort(data, 0, end)
	return 0

def quicksort(data, start, end):
	if start < end:
		pp = part(data, start, end)
		quicksort(data, start, pp-1)
		quicksort(data, pp+1, end)

def part(data, start, end):
	pivot = data[end]
	ii = start-1
	for jj in range(start, end):
		if data[jj] < pivot:
			ii+=1
			data[ii], data[jj] = data[jj], data[ii]
	data[ii+1], data[end] = data[end], data[ii+1]
	return ii+1