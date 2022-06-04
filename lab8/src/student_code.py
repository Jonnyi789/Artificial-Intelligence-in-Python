import common

def classify(ww, ff):
	dot_p = ww[0]*ff[0]+ww[1]*ff[1]+ww[2]*ff[2]
	return 1 if dot_p>0 else 0 

def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	weight = [0,0,0]
	mistake = True
	while mistake:
		mistake = False
		for data in data_train:
			feature = list(data)
			feature[2]=1		# bias
			cc = classify(weight, feature)
			if cc!=data[2]:
				if cc==1:
					weight = [weight[i] - feature[i] for i in range(3)]
				else:
					weight = [weight[i] + feature[i] for i in range(3)]
				mistake = True
				break
	for data in data_test:
		feature = list(data)
		feature[2]=1
		data[2] = classify(weight, feature)
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	return

def classify_two(ww, ff):
	dot_p = [0]*10
	for ii in range(10):
		dot_p[ii] = ww[ii][0]*ff[0]+ww[ii][1]*ff[1]+ww[ii][2]*ff[2]
	return dot_p.index(max(dot_p))

def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	weight = list(range(10))
	learn_rate = 0.01
	max_error = round(len(data_train)/50)		#2% error allowed
	# Pick 10 weight start values, pay att these 10 values will be trained twice but shouldn't make a diff
	for ii in range(10):
		for data in data_train:
			if data[2]==ii:
				ww=list(data)
				ww[2]=1
				weight[ii]=ww
				break
	mistake = True
	while mistake:
		mis = 0
		for data in data_train:
			feature = list(data)
			feature[2]=1
			cc = classify_two(weight, feature)
			ans = int(data[2])
			if cc!=ans:
				for i in range(3):
					weight[ans][i] += learn_rate*feature[i]
					weight[cc][i] -= learn_rate*feature[i]
				mis+=1
		if mis<=max_error: mistake = False
	for data in data_test:
		feature = list(data)
		feature[2]=1
		data[2] = classify_two(weight, feature)
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	return
