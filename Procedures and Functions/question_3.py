def isValid(string, minLen, maxLen):
	if len(string)>= minLen and len(string)<= maxLen:
		return True
	else:
		return False


print isValid( "Hello all", 4, 7)
