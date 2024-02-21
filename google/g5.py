from googlesearch import search

query = "數據治理"

for j in search(query, stop=10, pause=2.0): 
	print(j)

