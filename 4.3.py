def pie(t, sides, radius):
	import math
	for i in range(sides):
		t.fd(radius)
		t.bk(radius)
		t.lt(360 / sides)
	t.fd(radius)
	t.lt(180 - (180 - (360 / sides)) / 2)
	for i in range(sides):
		t.fd(math.sin(360 / sides / 2 / 180 * math.pi) * radius * 2)
		t.lt(360 / sides)
		#good work me
		