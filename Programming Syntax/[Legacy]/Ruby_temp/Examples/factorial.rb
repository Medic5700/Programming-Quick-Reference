def factorial(i)
	if i <= 0
		return 1
	else
		return i*(factorial(i-1))
	end
end

for i in 0...11
	puts String(i) + "!\t= " + String(factorial(i))
end
