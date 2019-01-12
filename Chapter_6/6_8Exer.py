# Identify and correct the errors in the following program:
#  def function1(n, m):
#  function2(3.4)
#  def function2(n):
#  if n > 0:
#  return 1
#  elif n == 0:
#  return 0
#  elif n < 0:
#  return –1
#  function1(2, 3)

def function1(n,m):
	print(function2(3.4))
def function2(n):
	if n > 0:
		return 1
	elif n == 0:
		return 0
	elif n < 0:
		return -1

function1(2,3)