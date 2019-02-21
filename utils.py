#Help Functions
def overrides(interface_class):
	'''Protocol'''
	def overrider(method):
		if method.__name__  not in dir(interface_class):
			raise NotImplementedError("Override error: Protacol {}".format(interface_class.__name__))
		return method
	return overrider


#TODO