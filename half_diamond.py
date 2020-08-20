## https://www.geeksforgeeks.org/program-to-print-half-diamond-star-pattern/?ref=leftbar-rightbar
def half_diamond(N):
  for i in range(1,2*N+1):
    if i + 1 <= N:
        print("*" * i)
    else:
        i=2*N-i
        print("*" * i)
