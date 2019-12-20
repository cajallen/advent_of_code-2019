from json import dumps
#print(dumps(trades, indent = 2))
from math import ceil

def get_trades(file_name):
	trades = { }
	with open(file_name, "r") as input_file:
		input_string = input_file.read().split("\n")
		for line in input_string:
			line = line.split(" => ")
			line[0] = line[0].split(", ")

			for i in range(len(line[0])):
				line[0][i] = line[0][i].split(' ')
			line[1] = line[1].split(' ')
			
			trades[line[1][1]] = {
				"amount": int(line[1][0]),
				"returns": {}
			}
			for trade in line[0]:
				trades[line[1][1]]["returns"][trade[1]] = int(trade[0])
	return trades

class Vendor:
	def __init__(self, file_name):
		self.trades = get_trades(file_name)
		self.inventory = { }
	
	def buy(self, item, amount):
		if item == "ORE":
			return amount
		
		if amount <= self.inventory.get(item, 0):
			self.inventory[item] = self.inventory.get(item, 0) - amount
			return 0
		
		amount -= self.inventory.get(item, 0)
		reactions = ceil(amount / self.trades[item]["amount"])
		self.inventory[item] = (reactions * self.trades[item]["amount"]) - amount
		
		total = 0
		for subcomponent in self.trades[item]["returns"]:
			total += self.buy(subcomponent, reactions * self.trades[item]["returns"][subcomponent])
		return total
		#BUY FUEL 1
		#BUY 7 A, 1 E


vendor = Vendor("day14_input.txt")
print(vendor.buy("FUEL", 1))