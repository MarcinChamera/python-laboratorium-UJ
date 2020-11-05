def flatten(sequence):
	def flatten_subfunction(sequence):
		for item in sequence:
			try:
				yield from flatten(item)
			except:
				yield item
	return(list(flatten_subfunction(sequence)))


print(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]))