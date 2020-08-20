def half_diamond(N):
  for i in range(2*N):
    if i + 1 <= N:
		print("*" * (i+1))
	else:
		i=2*N-1-i
		print("*" * i)
