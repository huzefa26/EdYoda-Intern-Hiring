from random import randint

class Person:
	def __init__(self, name, rating, review):
		self.name = name
		self.rating = rating
		self.review = review
	def get_name(self):
		return self.name
	def get_rating(self):
		return self.rating



class Elder(Person):

	def __init__(self, name, rating, review, funds, required_rating=3):
		super().__init__(name, rating, review)
		self.funds = funds
		self.aid_name = None
		self.required_rating = required_rating

	def needs_aid(self, youngsters):
		youngsters.sort(key=lambda y:y.rating)

		for youngster in youngsters:
			if youngster.rating >= self.required_rating:
				if youngster.allocate_elder(self):
					self.aid_name = youngster.name
					youngster.salary += self.funds
				print(self.name + ' is taken care by ' + youngster.name)
				return True
		print('No caretaker found for ' + self.name)
		return False


class Youngster(Person):
	
	LIMIT = 4
	def __init__(self, name, rating, review=''):
		super().__init__(name, rating, review)
		self.salary = 0
		self.asoc_elders = []

	def allocate_elder(self, elder):
		if len(self.asoc_elders) < Youngster.LIMIT:
			self.asoc_elders.append(elder)
			return True
		return False

	def takes_care_of(self):
		return [oldie.name for oldie in self.asoc_elders]


if __name__=='__main__':
	alice, bob, charlie = Youngster('Alice', 3.7, ''), Youngster('Bob', 2.9, ''), Youngster('Charlie', 5, '')
	youngsters = [alice, bob, charlie]
	elders = ['dexter', 'eve', 'france', 'gordon', 'hilbert', 'ian', 'jamfal', 'kaju']
	e_ratings = [3,2,2,4,2,4,3,2]
	dexter, eve, france, gordon, hilbert, ian, jamfal, kaju = \
		[Elder(name, randint(1,5), '', 100*randint(1,9), req) for name,req in zip(elders,e_ratings)]
	elders = [dexter, eve, france, gordon, hilbert, ian, jamfal, kaju]
	for elder in elders:
		elder.needs_aid(youngsters)
	for y in youngsters:
		print();print()
		print('Name: ', y.name)
		print('Rating: ', y.rating)
		print('Salary: ', y.salary)
		print('Elders: ', y.takes_care_of())