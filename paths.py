from random import randint
import time

# this is an A* (A star) path finding algorithm

class Point:
	def __init__(self, point, start=0, finish=0, parent=0):
		self.y = point[0]
		self.x = point[1]
		self.parent = parent		# parent is for getting the shortest path via backtracking
		
		if(self.parent == 0):
			self.Gcost = 0
		else:
			self.Gcost = self.parent.Gcost+1				# distance from start
			self.Hcost = abs(self.y-finish.y) + abs(self.x-finish.x)	# distance from finish
			self.Fcost = self.Gcost + self.Hcost
			

class Pathy:
	def __init__(self, size):
		self.size = size
		self.start = None
		self.finish = None
		self.toBeSearched = []
		self.field = []

		for y in range(size):
			temp = []
			for x in range(size):
				temp.append("-")
			self.field.append(temp)

		self.addBarriers()
		self.placeStartFinish()
		self.drawField()
		self.findPath()


	def addBarriers(self):
		alreadyadded = []

		for a in range(randint(1, self.size-1)):
			index = randint(0, self.size-1)
			while(index in alreadyadded):
				index = randint(0, self.size-1)

			barrierSize = randint(3, self.size-2)
			barrierStart = randint(0, self.size-barrierSize)

			for b in range(barrierSize):
				self.field[index][barrierStart+b] = "0"


	def placeStartFinish(self):
		self.start = Point([randint(0,self.size-1), randint(0,self.size-1)])
		self.finish = Point([randint(0,self.size-1), randint(0,self.size-1)])

		while(self.field[self.start.y][self.start.x]!="-"):
			self.start = Point([randint(0,self.size-1), randint(0,self.size-1)])
		self.field[self.start.y][self.start.x] = "A"

		while(self.field[self.finish.y][self.finish.x]!="-"):
			self.finish = Point([randint(0,self.size-1), randint(0,self.size-1)])
		self.field[self.finish.y][self.finish.x] = "B"


	def drawField(self):			
		for i in self.field:
			string = ""
			for x in i:
				string += x + " "
			print(string)
		print("")


	def getPoint(self, y, x):
		for i in self.toBeSearched:
			if(i.y == y and i.x == x):
				return i


	def availablePoints(self, position):
		directions = ["up", "right", "down", "left"]
		size = self.size

		point = [position.y, position.x]

		if(point[0]==0):
			directions.remove("up")
		
		if(point[0]==size-1):
			directions.remove("down")

		if(point[1]==0):
			directions.remove("left")

		if(point[1]==size-1):
			directions.remove("right")

		for i in directions:
			tpoint = point.copy()
			if(i=="up"):
				tpoint[0] = tpoint[0]-1
			elif(i=="right"):
				tpoint[1] = tpoint[1]+1
			elif(i=="down"):
				tpoint[0] = tpoint[0]+1
			elif(i=="left"):
				tpoint[1] = tpoint[1]-1

			tempp = Point(tpoint, self.start, self.finish, position)
			if(self.field[tempp.y][tempp.x]=="-"):
				self.field[tempp.y][tempp.x] = "="
				self.toBeSearched.append(tempp)

			elif(self.field[tempp.y][tempp.x]=="="):
				toUpdate = self.getPoint(tempp.y, tempp.x)
				if(toUpdate.Fcost>tempp.Fcost or (toUpdate.Fcost==tempp.Fcost and toUpdate.Hcost>tempp.Hcost)):
					self.toBeSearched.remove(toUpdate)
					self.toBeSearched.append(tempp)					

			elif(self.field[tempp.y][tempp.x]=="B"):
				self.toBeSearched.append(tempp)


	def lowestCost(self):
		toBeSearched = self.toBeSearched
		lowest = []

		lowestCosts = []
		for a in toBeSearched:
			lessFound = 0

			for b in toBeSearched:
				if(b.Fcost<a.Fcost):
					lessFound = 1
					break

			if(lessFound==0):
				lowestCosts.append(a)
		
		if(len(lowestCosts)>0):
			for a in lowestCosts:
				lessFound = 0

				for b in lowestCosts:
					if(b.Hcost<a.Hcost):
						lessFound = 1
						break

				if(lessFound==0):
					lowest = a
					break

			for i in toBeSearched:
				if(i.y == lowest.y and i.x == lowest.x):
					toBeSearched.remove(i)
					break
		else:
			lowest = -1

		return lowest


	def findPath(self):
		position = self.start
		self.availablePoints(position)
		input("press any key to start...")

		while(True):
			position = self.lowestCost()

			if(position==-1):
				print("There is no path from A to B")
				return

			if(self.field[position.y][position.x] == "B"):
				break
			else:
				self.field[position.y][position.x] = "*"
				self.availablePoints(position)
				self.drawField()
				time.sleep(0.05)

		# clears unnecessary "*"s and "-"s
		for y in range(self.size):
			for x in range(self.size):
				if(self.field[y][x] == "*" or self.field[y][x] == "="):
					self.field[y][x] = "-"

		position = position.parent
		while(position.parent!=0):
			self.field[position.y][position.x] = "x"
			position = position.parent

		self.drawField()
						
			

# "-" not searched, "=" to be searched, "*" searched, "x" path
			
if __name__ == "__main__":
	sixer = Pathy(30)




