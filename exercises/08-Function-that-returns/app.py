def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######

dollars = 137
euros = dollar_to_euro(137)
yens = euro_to_yen(euros)

print(yens)