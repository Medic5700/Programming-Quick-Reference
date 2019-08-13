def fib(i)
	if i == 0
		return 0
	elsif i == 1
		return 1
	else
		return fib(i-1) + fib(i-2)
	end
end

for i in 0...11
	puts String(i) + "!\t= " + String(fib(i))
end
