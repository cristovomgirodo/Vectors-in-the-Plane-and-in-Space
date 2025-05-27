#######################################################################
#
#	The Vetor2DModuleClass.py module
# 	Developed by Cristovom A. Girodo
# 	Date: 20240902 -- new Version: 2.0
#
#######################################################################

import math

class VectorNumber:
	def __init__(self, coeffic = 0,  x = 0):
		self.coeffic = coeffic
		self.x = x
		
	def enterIntegerData(self):
		while True:
			try:
				def integerdata():
					self.x = int(input('\t[º>º] Provide the [new] value? '))
					return self.x
				self.coeffic = integerdata()
				
				while self.coeffic <= 0:
					print('\n\t*[ NO TYPE AN [NEGATIVE INTEGER NUMBER] or equal [ZERO]--Ok! ]*\n')
					self.coeffic = integerdata()
				return self.coeffic
				
			except ValueError as err:
				print('\n\t ////') 
				print('\t º<º  [Warning!]:',err)
				print('\t [~]  [ TYPE AN [NEW POSITIVE INTEGER NUMBER ]')
				print('\t      [ IN NEXT INSTRUCTION -- OK! ]\n')

vector = VectorNumber()

class Introduce:
	def __init__(self, coeffic1 = 0, y = 0):
		self.coeffic1 = coeffic1
		self.y = y 
		
	def enterRealData(self):
		while True:
			try:
				def realdata():
					self.y = float(input('\t(ª<ª) Enter the [new] value? '))
					return self.y
				self.coeffic1 = realdata()
				return self.coeffic1
				
			except ValueError as err:
				print('\n\t _=§=_') 
				print('\t  º>º  [Warning!]:',err)
				print('\t  [=]  [ TYPE AN NEW [POSITIVE OR NEGATIVE OR ZERO] FLOAT NUMBER ]')
				print('\t       [ IN NEXT INSTRUCTION -- OK! ]\n')

introduce = Introduce()

class PositiveReal_Radius:
	def __init__(self, coeffic2 = 0, r = 0):
		self.coeffic2 = coeffic2
		self.r = r
	def enterRealRadius(self):
		while True:
			try:
				def newRadius():
					self.r = float(input('\t[º<º] Type a [new] value? '))
					return self.r
				self.coeffic2 = newRadius()
				
				while self.coeffic2 <= 0:
					print('\n\t   _===_')
					print('\t    º>º  [Warning!]:')
					print('\t    [~]  **[ No exist none [vector] when the [component]: radius is: ]')
					print('\t         **[ A Negative float number: radius < 0 ] or [ Zero: radius = 0 ] -- Ok! ]**\n')
					self.coeffic2 = newRadius()
				return self.coeffic2
				
			except ValueError as err:
				print('\n\t    _===_')
				print('\t     @<@  [Warning!]:',err)
				print('\t     [-]  **[ NO KEY ANY OTHER CHARACTER OR [ENTER] IN THE KEYBOARD ]**')
				print('\t          -------------------------------------------------------------')
				print('\t          [ TYPE ALWAYS A NEW [POSITIVE FLOAT NUMBER] TO THE [RADIUS] ]')
				print('\t          [ IN NEXT INSTRUCTION -- OK! ]\n')
				
realradius = PositiveReal_Radius()

class MagnitudeBiVector:
	def __init__(self, magnitude = 0, x = 0, y = 0):
		self.magnitude = 0
		self.x = x
		self.y = y
		
	def magbivector(self):
		self.magnitude = math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))
		return self.magnitude
		
magnitudebivector = MagnitudeBiVector()

class Answer:
	'''View the solution'''	
	def view_solution(self):
		print('\n\t *[Answer]*\n')
		
answer = Answer()
		          	
class ResultantVector:
	def __init__(self, angle_degrees = 0, angle_radians = 0, arg = 0, i = 1, numb = 0, radius = 0,  rdvect = 0,
	Rx = 0, Ry = 0, resultant_vector = 0, value_angle_degrees = 0, value_angle_radians = 0, Vx = 0, Vy = 0, 
	theta_degrees = 0):
		self.arg = arg
		self.angle_degrees = angle_degrees
		self.angle_radians = angle_radians
		self.i = i
		self.numb = numb
		self.radius = radius
		self.resultant_vector = resultant_vector
		self.rdvect = rdvect
		self.Rx = Rx
		self.Ry = Ry
		self.theta_degrees = theta_degrees
		self.value_angle_degrees = value_angle_degrees
		self.value_angle_radians = value_angle_radians
		self.Vx = Vx
		self.Vy = Vy
		
	def instruction1(self):
		print("\n\t- Enter with the [new value] of the [angle] in degree? ")
		
	def instruction2(self):
		print("\t- Provide the [new value] of the [radius] of vector? ")
		
	def getresultant_vector(self):
		print('\n\t+ How much [Vectors] will necessary to get the [Resultant(R) Vector]?')
		self.numb = vector.enterIntegerData()
		
		while self.i <= self.numb:
			if self.i == 1:
				print('\n\t**[Warning]**')
				print('\t- All the [Vectorials Components] will can be:')
				print('\t  [positive] or [negative] or Zero!\n')
				
			def subRotine():
				self.instruction1()
				self.value_angle_degrees = introduce.enterRealData()
				self.value_angle_radians = math.radians(self.value_angle_degrees)
				self.instruction2()
				self.rdvect = realradius.enterRealRadius()
				return self.value_angle_degrees, self.value_angle_radians, self.rdvect 
				
			print(f"\n\t+ What are the arguments: [angle] and [radius] of the ({self.i}º) [vector]?")
			self.angle_degrees, self.angle_radians, self.radius = subRotine()
			
			self.Vx = self.radius * math.cos(self.angle_radians)
			self.Vy = self.radius * math.sin(self.angle_radians)
			
			print("\n\t\t\t_-_ . . .[Running]. . . _-_\n")
			answer.view_solution() 
			print(f"\t- The component of the ({self.i})º [vector]: Vx({self.i})= {self.Vx:<10.2f}")
			print(f"\t- The component of the ({self.i})º [vector]: Vy({self.i})= {self.Vy:<10.2f}","\n")
			
			if self.i == 1:
				print("\n\t**[Warning]**:")
				print(f"\t**[ THE [PREVIOUS COMPONENTS]: Vx({self.i}) AND Vy({self.i}) BEEN CALCULED; BUT ]**")
				print("\t**[ [NO EXIST RESULTANT(R) VECTOR] TO A ONLY VECTOR!]**\n")
				
			self.Rx = self.Vx + self.Rx
			self.Ry = self.Vy + self.Ry
			
			if self.i == self.numb and self.i != 1:
				magnitudebivector.x = self.Rx
				magnitudebivector.y = self.Ry
				self.resultant_vector = magnitudebivector.magbivector()
				self.arg = ( self.Ry / self.Rx )
				self.angle_radians = math.atan(self.arg)
				self.theta_degrees = math.degrees(self.angle_radians)
				print(f"\n\t+ The sum of all the components of x_axis: Rx = {self.Rx:<10.2f}")
				print(f"\t+ The sum of all the components of y_axis: Ry = {self.Ry:<10.2f}")
				print(f"\n\n\t+ The resultant vector: [Resultant(R)_Vector] = {self.resultant_vector:<10.2f}")
				print(f"\t+ The [theta angle] in [degrees] = {self.theta_degrees:<10.2f}")
				
			self.i = self.i + 1
		print("\n\n\t**[End Processing of the [ RESULTANTVECTOR CLASS ]--Ok! ]**\n")
		return

resultant = ResultantVector()

class CompVector:
	def __init__(self, u = 0, v = 0, vectorComponents = [], vectorComponentsA = [], vectorComponentsB = [],
	vectorComponentsC = [], vectA = 0, vectB = 0, vectC = 0):
		self.u = u
		self.v = v
		self.vectorComponents = vectorComponents
		self.vectorComponentsA = vectorComponentsA
		self.vectorComponentsB = vectorComponentsB 
		self.vectorComponentsC = vectorComponentsC
		self.vectA = vectA
		self.vectB = vectB 
		self.vectC = vectC 
		
	def getcomponentvectorA(self):
		print('\n\t- Attribute the [Components] of the [1º vectorA]!')
		for h in range(1,3):
			if h == 1:
				print(f'\n\t- Enter the [coefficient] of the [Component: (i) or (a1)]?')
				self.u = introduce.enterRealData()
				self.vectorComponentsA.append(self.u)
			elif h == 2:
				print(f'\n\t- Introduce the [coefficient] of the [Component: (j) or (a2)]?')
				self.v = introduce.enterRealData()
				self.vectorComponentsA.append(self.v)
				return self.vectorComponentsA
		
	def getcomponentvectorB(self):
		print('\n\t- Provide the [Components] of the [2º vectorB]?')
		for j in range(1,3):
			if j == 1:
				print(f'\n\t- Enter the [coefficient] of the [Component: (i) or (b1)]?')
				self.u = introduce.enterRealData()
				self.vectorComponentsB.append(self.u)
			elif j == 2:
				print(f'\n\t- Introduce the [coefficient] of the [Component: (j) or (b2)]?')
				self.v = introduce.enterRealData()
				self.vectorComponentsB.append(self.v)
				return self.vectorComponentsB
				
	def getcomponentvectorC(self):
		print('\n\t- Give the [Components] of the [3º vectorC]?')
		for k in range(1,3):
			if k == 1:
				print(f'\n\t- Enter the [coefficient] of the [Component: (i) or (b1)]?')
				self.u = introduce.enterRealData()
				self.vectorComponentsC.append(self.u)
			elif k == 2:
				print(f'\n\t- Introduce the [coefficient] of the [Component: (j) or (b2)]?')
				self.v = introduce.enterRealData()
				self.vectorComponentsC.append(self.v)
				return self.vectorComponentsC
				
compvector = CompVector()
  
class SubQdRoot:
	def __init__(self, cat = 0, height = 0, hip = 0):
		self.cat = cat
		self.height = height
		self.hip = hip
		
	def getheight(self):	
		self.height = math.sqrt( math.pow(self.hip,2) - math.pow(self.cat,2) )
		return self.height

subqdroot = SubQdRoot()
	
class CoordinatesPoint:
	def __init__(self, number1 = 1, pointP = [], pointQ = [], pointR = [], pointS = [], pointK = [], pointL = [],
	pointM = [], u = 0, v = 0):
		self.number1 = number1
		self.pointP = pointP
		self.pointQ = pointQ
		self.pointR = pointR
		self.pointS = pointS
		
		self.pointK = pointK
		self.pointL = pointL 
		self.pointM = pointM
		
	def getcoordinatepoint(self):
		
		if self.number1 == 1: 
			print('\n\t-- Enter the [coordinates]: (xP, yP) of the (point P)? ')
			for i in range(1, 3):
				if i == 1:
					print(f"\n\t* Introduce the {i}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointP.append(self.u)
				elif i == 2:
					print(f"\n\t* Enter with the {i}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointP.append(self.v)
					return self.pointP
					
		elif self.number1 == 2:
			print('\n\t-- Introduce the [coordinates]: (xQ, yQ) of the (point Q)? ')
			for j in range(1, 3):
				if j == 1:
					print(f"\n\t* Introduce the {j}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointQ.append(self.u)
				elif j == 2:
					print(f"\n\t* Enter with the {j}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointQ.append(self.v)
					return self.pointQ
			
		elif self.number1 == 3:
			print('\n\t-- Provide the [coordinates]: (xR, yR) of the (point R)? ')
			for k in range(1, 3):
				if k == 1:
					print(f"\n\t* Introduce the {k}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointR.append(self.u)
				elif k == 2:
					print(f"\n\t* Enter with the {k}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointR.append(self.v)
					return self.pointR
					
		elif self.number1 == 4:
			print('\n\t-- Give the [coordinates]: (xS, yS) of the (point S)? ')
			for l in range(1, 3):
				if l == 1:
					print(f"\n\t* Introduce the {l}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointS.append(self.u)
				elif l == 2:
					print(f"\n\t* Enter with the {l}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointS.append(self.v)
					return self.pointS
					
		elif self.number1 == 5:
			print('\n\t-- Give the [coordinates]: (xK, yK) of the (Mid_point K)? ')
			for d in range(1, 3):
				if d == 1:
					print(f"\n\t* Introduce the {d}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointK.append(self.u)
				elif d == 2:
					print(f"\n\t* Enter with the {d}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointK.append(self.v)
					return self.pointK
					
		elif self.number1 == 6:
			print('\n\t-- Give the [coordinates]: (xL, yL) of the (Mid_point L)? ')
			for e in range(1, 3):
				if e == 1:
					print(f"\n\t* Introduce the {e}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointL.append(self.u)
				elif e == 2:
					print(f"\n\t* Enter with the {e}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointL.append(self.v)
					return self.pointL
					
		elif self.number1 == 7:
			print('\n\t-- Give the [coordinates]: (xM, yM) of the (Mid_point M)? ')
			for f in range(1, 3):
				if f == 1:
					print(f"\n\t* Introduce the {f}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointM.append(self.u)
				elif f == 2:
					print(f"\n\t* Enter with the {f}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointM.append(self.v)
					return self.pointM
			 			
coordinatespoint = CoordinatesPoint()

class TextString1:
	'''Instructions of the processing after test of enter data.'''
	def view_instructions(self):
		print('\t=========================================================================')
		print('\t**[ EXIST THE TRIANGLE(PQR) WITH THE GIVEN POINTS: P, Q, AND R -- OK! ]**')
		print('\t=========================================================================\n')
		
textstring1 = TextString1()

class TextString2:
	'''Instructions of the processing after test of enter error data.'''
	def error_instructions(self):
		print('\t--------------------------------------------------------------------------------------------------------')
		print('\t  *[ NO EXIST THE TRIANGLE(PQR) WITH THE [COORDINATES] OF THE GIVEN POINTS: P(xP,yP), Q(xQ,yQ), AND ]*')
		print('\t  *[ R(xR,yR) -- OK! BY [THEOREM OF THE PLANE GEOMETRY] THE BUILDING OF THE TRIANGLE(PQR) USING THE ]*')
		print('\t  *[ COMPASS AND RULER ONLY IS POSSIBLE WHEN: ]*\n')
		print('\t\t**[ sideA < sideB + sideC ]** and')
		print('\t\t**[ sideB < sideA + sideC ]** and')
		print('\t\t**[ sideC < sideA + sideB ]**\n')
		print('\t--------------------------------------------------------------------------------------------------------\n')

textstring2 = TextString2()

class TextString3:
	'''Instructions of the processing after type error option '''
	def no_OptionKey(self):
		print('\n\t*[You no type a of the previous options!]*')
		print('\t*[ Run the program again--Ok! ]*\n')

textstring3 = TextString3()

class MidPoint:
	'''Will determine the midpoints: K, L, M, and N between points: P, Q, R, and S'''
	def __init__(self, coord = 0, number = 0, pointP = [], pointQ = [], pointR = [], pointS = [], PointP = [], 
	PointQ = [], PointR = [], PointS = [], vectorMidPointK = [], vectorMidPointL = [], vectorMidPointM = [],
	vectorMidPointN = [], xK = 0, yK = 0, xL = 0, yL = 0,  xM = 0, yM = 0, xN = 0, yN = 0, xP = 0, xQ = 0, xR = 0,  
	xS = 0, yP = 0, yQ = 0, yR = 0, yS = 0 ):
		self.coord = coord
		self.number = number
		self.pointP = pointP 
		self.pointQ = pointQ 
		self.pointR = pointR 
		self.pointS = pointS
		
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		self.PointS = PointS
		
		self.vectorMidPointK = vectorMidPointK
		self.vectorMidPointL = vectorMidPointL 
		self.vectorMidPointM = vectorMidPointM 
		self.vectorMidPointN = vectorMidPointN
		
		self.xK = xK 
		self.yK = yK
		self.xL = xL 
		self.yL = yL 
		self.xM = xM 
		self.yM = yM 
		self.xN = xN 
		self.yN = yN 
		self.xP = xP
		self.yP = yP 
		self.xQ = xQ
		self.yQ = yQ
		self.xR = xR
		self.yR = yR
		self.xS = xS
		self.yS = yS 
		
	def getmid_point(self):
		
		if self.number == 1:
			coordinatespoint.number1 = 1
			self.pointP = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 2
			self.pointQ = coordinatespoint.getcoordinatepoint()
			
			for j in range(0,2):
				self.coord = ( ( self.pointP[j] + self.pointQ[j] ) / 2 )
				self.vectorMidPointK.append(self.coord)
				if j == 0:
					self.xK = self.vectorMidPointK[j]
					self.xP = self.pointP[j]
					self.xQ = self.pointQ[j]
				elif j == 1:
					self.yK = self.vectorMidPointK[j]
					self.yP = self.pointP[j]
					self.yQ = self.pointQ[j]
				
			self.PointK = (self.xK,self.yK)
			self.pointP = (self.xP,self.yP)
			print('\n\t- The (Point P): P',self.pointP)
			self.pointQ = (self.xQ,self.yQ)
			print('\t- The (Point Q): Q',self.pointQ)
			answer.view_solution()
			print('\t-- The MidPoint_K(xK,yK):', self.PointK)
			
		elif self.number == 2:
			coordinatespoint.number1 = 1
			self.pointP = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 3
			self.pointR = coordinatespoint.getcoordinatepoint()
			
			for j in range(0,2):
				self.coord = ( ( self.pointP[j] + self.pointR[j] ) / 2 )
				self.vectorMidPointL.append(self.coord)
				if j == 0:
					self.xL = self.vectorMidPointL[j]
					self.xP = self.pointP[j]
					self.xR = self.pointR[j]
				elif j == 1:
					self.yL = self.vectorMidPointL[j]
					self.yP = self.pointP[j]
					self.yR = self.pointR[j]
				
			self.PointL = (self.xL,self.yL)
			self.pointP = (self.xP,self.yP)
			print('\n\t- The (Point P): P',self.pointP)
			self.pointR = (self.xR,self.yR)
			print('\t- The (Point R): R',self.pointR)
			answer.view_solution()
			print('\t-- The MidPoint_L(xL,yL):', self.PointL)
			
		elif self.number == 3:
			coordinatespoint.number1 = 2
			self.pointQ = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 3
			self.pointR = coordinatespoint.getcoordinatepoint()
			
			for j in range(0,2):
				self.coord = ( ( self.pointQ[j] + self.pointR[j] ) / 2 )
				self.vectorMidPointM.append(self.coord)
				if j == 0:
					self.xM = self.vectorMidPointM[j]
					self.xQ = self.pointQ[j]
					self.xR = self.pointR[j]
				elif j == 1:
					self.yM = self.vectorMidPointM[j]
					self.yQ = self.pointQ[j]
					self.yR = self.pointR[j]
				
			self.PointM = (self.xM,self.yM)
			self.pointQ = (self.xQ,self.yQ)
			print('\n\t- The (Point Q): Q',self.pointQ)
			self.pointR = (self.xR,self.yR)
			print('\t- The (Point R): R',self.pointR)
			answer.view_solution()
			print('\t-- The MidPoint_M(xM,yM):', self.PointM)
			
		elif self.number == 4:
			coordinatespoint.number1 = 4
			self.pointS = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 1
			self.pointP = coordinatespoint.getcoordinatepoint()
			
			for j in range(0,2):
				self.coord = ( ( self.pointS[j] + self.pointP[j] ) / 2 )
				self.vectorMidPointN.append(self.coord)
				if j == 0:
					self.xN = self.vectorMidPointN[j]
					self.xS = self.pointS[j]
					self.xP = self.pointP[j]
				elif j == 1:
					self.yN = self.vectorMidPointN[j]
					self.yS = self.pointS[j]
					self.yP = self.pointP[j]
				
			self.PointN = (self.xN,self.yN)
			self.pointS = (self.xS,self.yS)
			print('\n\t- The (Point S): S',self.pointS)
			self.pointP = (self.xP,self.yP)
			print('\t- The (Point P): P',self.pointP)
			answer.view_solution()
			print('\t-- The MidPoint_N(xN,yN):', self.PointN)
			
		elif self.number == 5:
			coordinatespoint.number1 = 2
			self.pointQ = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 3
			self.pointR = coordinatespoint.getcoordinatepoint()
			
			for j in range(0,2):
				self.coord = ( ( self.pointQ[j] + self.pointR[j] ) / 2 )
				self.vectorMidPointL.append(self.coord)
				if j == 0:
					self.xL = self.vectorMidPointL[j]
					self.xQ = self.pointQ[j]
					self.xR = self.pointR[j]
				elif j == 1:
					self.yL = self.vectorMidPointL[j]
					self.yQ = self.pointQ[j]
					self.yR = self.pointR[j]
				
			self.PointL = (self.xL,self.yL)
			self.pointQ = (self.xQ,self.yQ)
			print('\n\t- The (Point Q): Q',self.pointQ)
			self.pointR = (self.xR,self.yR)
			print('\t- The (Point R): R',self.pointR)
			answer.view_solution()
			print('\t-- The MidPoint_L(xL,yL):', self.PointL)
			
		elif self.number == 6:
			coordinatespoint.number1 = 3
			self.pointR = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 4
			self.pointS = coordinatespoint.getcoordinatepoint()
			
			for j in range(0,2):
				self.coord = ( ( self.pointS[j] + self.pointR[j] ) / 2 )
				self.vectorMidPointM.append(self.coord)
				if j == 0:
					self.xM = self.vectorMidPointM[j]
					self.xR = self.pointR[j]
					self.xS = self.pointS[j]
				elif j == 1:
					self.yM = self.vectorMidPointM[j]
					self.yR = self.pointR[j]
					self.yS = self.pointS[j]
				
			self.PointM = (self.xM,self.yM)
			self.pointR = (self.xR,self.yR)
			print('\n\t- The (Point R): R',self.pointR)
			self.pointS = (self.xS,self.yS)
			print('\t- The (Point S): S',self.pointS)
			answer.view_solution()
			print('\t-- The MidPoint_M(xM,yM):', self.PointM)
			
		return
		
midpoint = MidPoint()

class ScalarProduct:
	"""Find the scalar product """
	def __init__(self, alpha = 0, a1 = 0, a2 = 0, add = 0, Area = 0, b1 = 0, b2 = 0, c1 = 0, c2 = 0, comp0 = 0, comp1 = 0, 
	 comp3 = 0, coordP = [], coordQ = [], coordR = [], coordS = [], cossineThetaRadians = 0, cossineAlphaRadians = 0,
	 cP = 0, EquatArea = 0, EquatArea1 = 0,EquatArea2 = 0, h1 = 0, h2 = 0, h3 = 0, height_h = 0, height_h1 = 0,
	 height_h2 = 0, number = 0, number1 = 0, number2 = 0, normA = 0, normB = 0, modAxBproduct = 0, Perimeter = 0, 
	 Perimeter1  = 0, PointP = 0, PointQ = 0, PointR = 0, PointS = 0, vectorA = 0, vectorB = 0, vectorC = 0,
	 vectorAB = 0, vectorQR = [], vectorPQ = [], vectorQP = [], vectorRP = [], vectorPR = [], vectorPS = [],
	 vectorSP = [], vectorSR = [], vectorPQºPR = [], vectorPQºQR = [], vectorQPºQR = [], vectorQRºRP = [],
	 vectorRPºPQ = [], vectorSPºSR = [], radianAngle = 0, radianAlpha = 0, radianTheta = 0, sine = 0,
	 sineAlphaRadians = 0, scalarProduct = 0, vectorRPºRQ = [], ScalarProd0 = 0, ScalarProd1 = 0, ScalarProd2 = 0,
	 ScalarProd3 = 0, sideA = 0, sideB = 0, sideC = 0, term = 0, term0 = 0, term1 = 0, theta = 0, xP = 0, xQ = 0,
	 xR = 0, xS = 0, yP = 0, yQ = 0, yR = 0, yS = 0):
		self.a1 = a1
		self.a2 = a2
		self.add = add
		self.alpha = alpha
		self.theta = theta
		self.Area = Area
		
		self.b1 = b1
		self.b2 = b2
		self.c1 = c1
		self.c2 = c2
		
		self.comp0 = comp0
		self.comp1 = comp1
		self.comp3 = comp3
		
		self.coordP = coordP
		self.coordQ = coordQ
		self.coordR = coordR
		self.coordS = coordS
		self.cossineAlphaRadians = cossineAlphaRadians
		self.cossineThetaRadians = cossineThetaRadians
		self.cP = cP
		
		self.EquatArea = EquatArea
		self.EquatArea1 = EquatArea1
		self.EquatArea2 = EquatArea2
		self.h1 = h1
		self.h2 = h2
		self.h3 = h3
		self.height_h = height_h
		self.height_h1 = height_h1
		self.height_h2 = height_h2
		
		self.number = number
		self.number1 = number1
		self.number2 = number2 
	
		self.normA = normA
		self.normB = normB
		
		self.modAxBproduct = modAxBproduct
		self.Perimeter = Perimeter
		self.Perimeter1 = Perimeter1 
		
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		self.PointS = PointS
		
		self.radianAngle = radianAngle
		self.radianTheta = radianTheta 
		self.radianAlpha = radianAlpha
		self.sineAlphaRadians = sineAlphaRadians
		self.sine = sine
		
		self.scalarProduct = scalarProduct
		self.ScalarProd0 = ScalarProd0
		self.ScalarProd1 = ScalarProd1
		self.ScalarProd2 = ScalarProd2
		self.ScalarProd3 = ScalarProd3 
		
		self.sideA = sideA 
		self.sideB = sideB 
		self.sideC = sideC
		
		self.vectorA = vectorA
		self.vectorB = vectorB
		self.vectorC = vectorC
		
		self.vectorAB = vectorAB
		self.vectorQP = vectorQP
		self.vectorQR = vectorQR
		 
		self.vectorPR = vectorPR
		self.vectorRP = vectorRP
		
		self.vectorPQ = vectorPQ
		self.vectorPS = vectorPS
		self.vectorSP = vectorSP
		self.vectorSR = vectorSR
		
		self.vectorPQºQR = vectorPQºQR
		self.vectorPQºPR = vectorPQºPR
		
		self.vectorQPºQR = vectorQPºQR 
		
		self.vectorQRºRP = vectorQRºRP
		self.vectorRPºPQ = vectorRPºPQ
		self.vectorSPºSR = vectorSPºSR
		
		self.vectorRPºRQ = vectorRPºRQ 
		
		self.term = term
		self.term0 = term0
		self.term1 = term1
		
		self.xP = xP
		self.xQ = xQ
		self.xR = xR
		self.xS = xS
		
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		self.yS = yS
		
	def getscalar_product(self):
		
		if self.number == 1 or self.number == 2:
			# Enter the components of the vectors: a and b
			self.vectorA = compvector.getcomponentvectorA()
			self.vectorB = compvector.getcomponentvectorB()
			
			answer.view_solution()
			print('\t-- The [vectorA]: vectorA', self.vectorA)
			print('\t-- The [vectorB]: vectorB', self.vectorB, '\n')
			
			self.vectorAB = []
			self.scalarProduct = 0
			
			for i in range(0, 2):
				self.term = self.vectorA[i] * self.vectorB[i]
				self.scalarProduct = self.scalarProduct + self.term
				self.vectorAB.append(self.term)
				
			if self.number == 1:
				print('\t-- The [Vector] of the [terms of the Scalar Product]: vectorA*B = ', self.vectorAB)
				print(f'\t-- The [Scalar Product(vectorAB)] of the vectors is: {self.scalarProduct:<.2f}','\n')
				return 
			
			elif self.number == 2:
				magnitudebivector.x = self.vectorA[0]
				magnitudebivector.y = self.vectorA[1]
				self.normA = magnitudebivector.magbivector() 
				magnitudebivector.x = self.vectorB[0]
				magnitudebivector.y = self.vectorB[1]
				self.normB = magnitudebivector.magbivector()
				self.modAxBproduct = self.normA * self.normB
				self.cossineThetaRadians = self.scalarProduct / self.modAxBproduct
				
				print('\t-- The VectorA*B:', self.vectorAB)
				print(f'\t-- The [length] of a ||vectorA||: {self.normA:<.2f}')
				print(f'\t-- The [length] of a ||vectorB||: {self.normB:<.2f}')
				print(f'\t-- The [value] finded of |A*B| is: {self.modAxBproduct:<.2f}')
				print(f'\t-- The [Scalar Product] of the [VectorA*B] is: {self.scalarProduct:<.2f}')
				return self.cossineThetaRadians
				
		elif self.number == 3:
			# Give the [coordinates] of the points: P, Q, and R a of trianglePQR
			coordinatespoint.number1 = 1
			self.coordP = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 2
			self.coordQ = coordinatespoint.getcoordinatepoint()
			coordinatespoint.number1 = 3
			self.coordR = coordinatespoint.getcoordinatepoint()
			
			self.xP = self.xQ = self.xR = self.yP = self.yQ = self.yR = 0
			
			for self.cP in range(0,2):
				if self.cP == 0:
					self.xP = self.coordP[self.cP]
					self.xQ = self.coordQ[self.cP]
					self.xR = self.coordR[self.cP]
					
				elif self.cP == 1:
					self.yP = self.coordP[self.cP]
					self.yQ = self.coordQ[self.cP]
					self.yR = self.coordR[self.cP]
						
			self.PointP = (self.xP,self.yP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ)
			print('\t- The (Point Q): Q',self.PointQ)
			self.PointR = (self.xR,self.yR)
			print('\t- The (Point R): R',self.PointR)
			answer.view_solution()
			
			self.vectorQR = []
			self.vectorRP = []
			self.vectorPQ = []
			
			for h in range (0,2):
				self.comp0 = self.coordR[h] - self.coordQ[h]
				self.vectorQR.append(self.comp0)
				self.comp1 = self.coordP[h] - self.coordR[h]
				self.vectorRP.append(self.comp1)
				self.comp3 = self.coordQ[h] - self.coordP[h]
				self.vectorPQ.append(self.comp3)

			self.vectorA = self.vectorQR
			self.vectorB = self.vectorRP
			self.vectorC = self.vectorPQ
			
			# The Area = ( |b1*c2 -b2*c1| ) / 2
			self.b1 = self.vectorB[0]
			self.b2 = self.vectorB[1]
			self.c1 = self.vectorC[0]
			self.c2 = self.vectorC[1]
			self.term0 = self.vectorB[0] * self.vectorC[1]
			self.term1 = self.vectorB[1] * self.vectorC[0]
			self.add = self.term0 - self.term1
			self.Area = ( abs(self.add) ) / 2 
			
			magnitudebivector.x = self.vectorQR[0]
			magnitudebivector.y = self.vectorQR[1]
			# sideA = |QR|
			self.sideA = magnitudebivector.magbivector()
			magnitudebivector.x = self.vectorRP[0]
			magnitudebivector.y = self.vectorRP[1]
			# sideB = |RP|
			self.sideB = magnitudebivector.magbivector()
			magnitudebivector.x = self.vectorPQ[0]
			magnitudebivector.y = self.vectorPQ[1]
			# sideC = |PQ|
			self.sideC = magnitudebivector.magbivector()
			
			if self.sideA < self.sideB + self.sideC and self.sideB < self.sideA + self.sideC and self.sideC < self.sideA + self.sideB:
				textstring1.view_instructions()

				self.Perimeter = self.sideA + self.sideB + self.sideC
				
				# vectorCxA = vectorPQºQR
				# vectorAxB = vectorQRºRP
				# vectorBxC = vectorRPºPQ
				
				self.vectorPQºQR = []
				self.vectorQRºRP = []
				self.vectorRPºPQ = []

				self.ScalarProd0 = 0
				self.ScalarProd1 = 0
				self.ScalarProd2 = 0
				
			   # Find the Scalars Procucts
				for j in range(0, 2):
					self.term0 = self.vectorPQ[j] * self.vectorQR[j]
					self.ScalarProd0 = self.ScalarProd0 + self.term0
					self.vectorPQºQR.append(self.term0)
					self.term1 = self.vectorQR[j] * self.vectorRP[j]
					self.ScalarProd1 = self.ScalarProd1 + self.term1
					self.vectorQRºRP.append(self.term1)
					self.term2 = self.vectorRP[j] * self.vectorPQ[j]
					self.ScalarProd2 = self.ScalarProd2 + self.term2
					self.vectorRPºPQ.append(self.term2)
				  
				# Find the component of c along a
				subqdroot.cat = ( self.ScalarProd0 / self.sideA )
				subqdroot.hip = self.sideC
				self.h1 = subqdroot.getheight()
				# Find the component of a along b
				subqdroot.cat = ( self.ScalarProd1 / self.sideB )
				subqdroot.hip = self.sideA
				self.h2 = subqdroot.getheight()
				# Find the component of b along c
				subqdroot.cat = ( self.ScalarProd2 / self.sideC )
				subqdroot.hip = self.sideB
				self.h3 =subqdroot.getheight()

				print('\t-- The [vectorA] = vectorQR', self.vectorQR)
				print('\t-- The [vectorB] = vectorRP', self.vectorRP)
				print('\t-- The [vectorC] = vectorPQ', self.vectorPQ,'\n')
				print(f'\t-- The [sideA] = ||vectorQR|| of the triangle(PQR) is: {self.sideA:<.2f}')
				print(f'\t-- The [sideB] = ||vectorRP|| of the triangle(PQR) is: {self.sideB:<.2f}')
				print(f'\t-- The [sideC] = ||vectorPQ|| of the triangle(PQR) is: {self.sideC:<.2f}','\n')
				print('\t-- The [terms] of the [Scalar Product(PQºQR)] is:',self.vectorPQºQR)
				print('\t-- The [terms] of the [Scalar Product(QRºRP)] is:',self.vectorQRºRP)
				print('\t-- The [terms] of the [Scalar Product(RPºPQ)] is:',self.vectorRPºPQ,'\n')
				print(f'\t-- The [Scalar Product(PQºQR)] is: {self.ScalarProd0:<.2f}')
				print(f'\t-- The [Scalar Product(QRºRP)] is: {self.ScalarProd1:<.2f}')
				print(f'\t-- The [Scalar Product(RPºPQ)] is: {self.ScalarProd2:<.2f}','\n')
				print(f'\t-- The [Perimeter] of the [triangle(PQR)] is {self.Perimeter:<.2f}')
				print(f'\t-- The [Height(h1) relative as sideQR] is {self.h1:<.2f}')
				print(f'\t-- The [Height(h2) relative as sideRP] is {self.h2:<.2f}')
				print(f'\t-- The [Height(h3) relative as sidePQ] is {self.h3:<.2f}')
				print(f'\t-- The [Area(A)] of the [triangle(PQR)] is {self.Area:<.2f}')
				return
			
			else:
				textstring2.error_instructions()
				return
					
		elif self.number == 4:
			print('\t- Key [1] if in problem is given the [coordinates] of the three vertices: P, Q, and R. After')
			print('\t  follow the new [instructions] in [Display] to find the [coordinates: xS, and yS] relative as ')
			print('\t  point: S below - Ok!\n')
			print('\t- Key [2] if in problem is given the [coordinates] of the four vertices: P, Q, R, and S.\n')
			
			self.number1 = vector.enterIntegerData()
			
			if self.number1 == 1:
				print('\n\t-- Type [1] to find the [coordinates: xM and yM] of the middle point: M in [diagonal: SP] ')
				print('\t   Use the [coordinates: xQ, yQ, xR, and yR] of the points: Q and R.')
				print('\n\t-- Type [2] to find the [coordinates: xL and yL] of the middle point: L in [diagonal: SQ] ')
				print('\t   Use the [coordinates: xP, yP, xR, and yR] of the points: P and R.')
				print('\n\t-- Type [3] to find the [coordinates: xK and yK] of the middle point: K in [diagonal: SR] ')
				print('\t   Use the [coordinates: xP, yP, xQ, and yQ] of the points: P and Q.\n')
				
				self.number2 = vector.enterIntegerData()
				
				if self.number2 == 1:
					# Given the [coordinates] of the points: P, Q, and R. The vertices of the parallelogramPQRS
					midpoint.number = 3
					midpoint.getmid_point()
					self.coordQ = []
					self.xQ = midpoint.xQ
					self.coordQ.append(self.xQ)
					self.yQ = midpoint.yQ
					self.coordQ.append(self.yQ)
					self.coordR = []
					self.xR = midpoint.xR
					self.coordR.append(self.xR)
					self.yR = midpoint.yR
					self.coordR.append(self.yR)
					
					coordinatespoint.number1 = 1
					self.coordP = coordinatespoint.getcoordinatepoint()
					
					for h in range(0,2):
						if h == 0:
							self.xP = self.coordP[h]
						elif h == 1:
							self.yP = self.coordP[h]
							
					self.PointP = (self.xP,self.yP)
					print('\n\t- The (Point P): P',self.PointP)				
					self.xM = midpoint.xM
					self.yM = midpoint.yM		
					# Find the coordinates: xS, and yS of the point: S
					self.xS = ( 2 * self.xM ) - self.xP 
					self.yS = ( 2 * self.yM ) - self.yP
					answer.view_solution()
					print('\t-- The [Coordenates] of the point S:')
					print(f'\n\t-- The [Coordinate]: xS is {self.xS:<.2f}')
					print(f'\t-- The [Coordinate]: yS is {self.yS:<.2f}','\n')
					self.coordS = [self.xS, self.yS]
					
					self.vectorPQ = []
					self.vectorPR = []
					
					for i in range(0,2):
						self.comp0 = self.coordQ[i] - self.coordP[i]
						self.vectorPQ.append(self.comp0)
						self.comp1 = self.coordR[i] - self.coordP[i]
						self.vectorPR.append(self.comp1)
						
					magnitudebivector.x = self.vectorPQ[0]
					magnitudebivector.y = self.vectorPQ[1]
					# sideA = |PQ|
					self.sideA = magnitudebivector.magbivector()
					
					magnitudebivector.x = self.vectorPR[0]
					magnitudebivector.y = self.vectorPR[1]
					# sideB = |PR|
					self.sideB = magnitudebivector.magbivector()
						
					self.Perimeter = ( self.sideA + self.sideB ) * 2
						
					self.vectorPQºPR = []
					self.ScalarProd1 = 0
						
					for j in range(0, 2):
						self.term0 =  self.vectorPQ[j] * self.vectorPR[j]
						self.ScalarProd1 = self.ScalarProd1 + self.term0
						self.vectorPQºPR.append(self.term0)
					
					# Find the component of a along b
					self.cossineThetaRadians = self.ScalarProd1 / ( self.sideA * self.sideB  )
					self.radianAngle = math.acos(self.cossineThetaRadians)	
					self.theta = math.degrees(self.radianAngle)
					self.radianTheta = math.radians(self.theta)
					self.alpha = 180 - self.theta
					self.radianAlpha = math.radians(self.alpha)
					self.sineAlphaRadians = math.sin(self.radianAlpha)				
					self.sine = self.sineAlphaRadians
					self.height_h1 = self.sideA * self.sine
					self.height_h2 = self.sideB * self.sine
					self.EquatArea1 = ( ( self.vectorPQ[0] * self.vectorPR[1] ) - ( self.vectorPQ[1] * self.vectorPR[0]) )
						
					print('\t-- The [vectorPQ]: vectorPQ',self.vectorPQ)
					print('\t-- The [vectorPR]: vectorPR',self.vectorPR,'\n')
					print(f'\t-- The [sideA] relative as |vectorPQ|: {self.sideA:<.2f}')
					print(f'\t-- The [sideB] relative as |vectorPR|: {self.sideB:<.2f}')
					print(f'\t-- The [Perimeter(P)] is: {self.Perimeter:<.2f}','\n')
					print('\t-- The [terms] of the Scalar Product(vectorPQºPR) is:',self.vectorPQºPR)
					print('\t-- The [Scalar Product(PQºPR)] is:',self.ScalarProd1)
					print(f'\t-- The Cossine of theta: {self.cossineThetaRadians:<.2f}') 
					print(f'\t-- The [Theta angle] between vectors: vectorPQ and vectorPR is: {self.theta:<.2f}')
					print(f'\t-- The Sine of alpha: {self.sineAlphaRadians:<.2f}') 
					print(f'\t-- The [Alpha angle] between vectors: vectorPQ and vectorQS is: {self.alpha:<.2f}')
					
				elif self.number2 == 2:
					midpoint.number = 2
					midpoint.getmid_point()
					self.coordP = []
					self.xP = midpoint.xP
					self.coordP.append(self.xP)
					self.yP = midpoint.yP
					self.coordP.append(self.yP)
					self.coordR = []
					self.xR = midpoint.xR
					self.coordR.append(self.xR)
					self.yR = midpoint.yR
					self.coordR.append(self.yR)
					
					coordinatespoint.number1 = 2
					self.coordQ = coordinatespoint.getcoordinatepoint()
					
					for i in range(0,2):
						if i == 0:
							self.xQ = self.coordQ[i]	
						elif i == 1:
							self.yQ = self.coordQ[i]
							
					self.PointQ = (self.xQ,self.yQ)
					print('\n\t- The (Point Q): Q',self.PointQ)				
					self.xL = midpoint.xL
					self.yL = midpoint.yL		
					# Find the coordinates: xS, and yS of the point: S
					self.xS = ( 2 * self.xL ) - self.xQ 
					self.yS = ( 2 * self.yL ) - self.yQ
					answer.view_solution()
					print('\t-- The [Coordenates] of the point S:')
					print(f'\n\t-- The [Coordinate]: xS is {self.xS:<.2f}')
					print(f'\t-- The [Coordinate]: yS is {self.yS:<.2f}','\n')
					self.coordS = [self.xS, self.yS]
					
					self.vectorQP = []
					self.vectorQR = []
					
					for j in range(0,2):
						self.comp0 = self.coordP[j] - self.coordQ[j]
						self.vectorQP.append(self.comp0)
						self.comp1 = self.coordR[j] - self.coordQ[j]
						self.vectorQR.append(self.comp1)
						
					magnitudebivector.x = self.vectorQP[0]
					magnitudebivector.y = self.vectorQP[1]
					# sideA = |QP|
					self.sideA = magnitudebivector.magbivector()
					
					magnitudebivector.x = self.vectorQR[0]
					magnitudebivector.y = self.vectorQR[1]
					# sideB = |QR|
					self.sideB = magnitudebivector.magbivector()
						
					self.Perimeter = ( self.sideA + self.sideB ) * 2
						
					self.vectorQPºQR = []
					self.ScalarProd2 = 0
						
					for j in range(0, 2):
						self.term0 =  self.vectorQP[j] * self.vectorQR[j]
						self.ScalarProd2 = self.ScalarProd2 + self.term0
						self.vectorQPºQR.append(self.term0)
						
					# Find the component of b along a
					self.cossineThetaRadians = self.ScalarProd2 / ( self.sideA * self.sideB  )
					self.radianAngle = math.acos(self.cossineThetaRadians)
					self.theta = math.degrees(self.radianAngle)
					self.radianTheta = math.radians(self.theta)
					self.alpha = 180 - self.theta
					self.radianAlpha = math.radians(self.alpha)
					self.sineAlphaRadians = math.sin(self.radianAlpha)				
					self.sine = self.sineAlphaRadians
					self.sine = math.sin(self.radianTheta)
					self.height_h1 = self.sideA * self.sine
					self.height_h2 = self.sideB * self.sine
					self.EquatArea1 = ( ( self.vectorQP[0] * self.vectorQR[1] ) - ( self.vectorQP[1] * self.vectorQR[0]) )
						
					print('\t-- The [vectorPQ]: vectorQP',self.vectorQP)
					print('\t-- The [vectorPR]: vectorQR',self.vectorQR,'\n')
					print(f'\t-- The [sideA] relative as |vectorQP|: {self.sideA:<.2f}')
					print(f'\t-- The [sideB] relative as |vectorQR|: {self.sideB:<.2f}')
					print(f'\t-- The [Perimeter(P)] is: {self.Perimeter:<.2f}','\n')
					print('\t-- The [terms] of the Scalar Product(vectorQPºQR) is:',self.vectorQPºQR)
					print('\t-- The [Scalar Product(QPºQR)] is:',self.ScalarProd2)
					print(f'\t-- The Cossine of theta: {self.cossineThetaRadians:<.2f}') 
					print(f'\t-- The [Theta angle] between vectors: vectorQP and vectorQR is: {self.theta:<.2f}')
					print(f'\t-- The Sine of alpha: {self.sineAlphaRadians:<.2f}') 
					print(f'\t-- The [Alpha angle] between vectors: vectorQP and vectorPS is: {self.alpha:<.2f}')
					
				elif self.number2 == 3:
					midpoint.number = 1
					midpoint.getmid_point()
					self.coordP = []
					self.xP = midpoint.xP
					self.coordP.append(self.xP)
					self.yP = midpoint.yP
					self.coordP.append(self.yP)
					self.coordQ = []
					self.xQ = midpoint.xQ
					self.coordQ.append(self.xQ)
					self.yQ = midpoint.yQ
					self.coordQ.append(self.yQ)
					
					coordinatespoint.number1 = 3
					self.coordR = coordinatespoint.getcoordinatepoint()
					
					for j in range(0,2):
						if j == 0:
							self.xR = self.coordR[j]	
						elif j == 1:
							self.yR = self.coordR[j]
							
					self.PointR = (self.xR,self.yR)
					print('\n\t- The (Point R): R',self.PointR)				
					self.xK = midpoint.xK
					self.yK = midpoint.yK		
					# Find the coordinates: xS, and yS of the point: S
					self.xS = ( 2 * self.xK ) - self.xR 
					self.yS = ( 2 * self.yK ) - self.yR
					answer.view_solution()
					print('\t-- The [Coordenates] of the point S:')
					print(f'\n\t-- The [Coordinate]: xS is {self.xS:<.2f}')
					print(f'\t-- The [Coordinate]: yS is {self.yS:<.2f}','\n')
					self.coordS = [self.xS, self.yS]
					
					self.vectorRP = []
					self.vectorRQ = []
					
					for j in range(0,2):
						self.comp0 = self.coordP[j] - self.coordR[j]
						self.vectorRP.append(self.comp0)
						self.comp1 = self.coordQ[j] - self.coordR[j]
						self.vectorRQ.append(self.comp1)
						
					magnitudebivector.x = self.vectorRP[0]
					magnitudebivector.y = self.vectorRP[1]
					# sideA = |RP|
					self.sideA = magnitudebivector.magbivector()
					
					magnitudebivector.x = self.vectorRQ[0]
					magnitudebivector.y = self.vectorRQ[1]
					# sideB = |RQ|
					self.sideB = magnitudebivector.magbivector()
						
					self.Perimeter = ( self.sideA + self.sideB ) * 2
						
					self.vectorRPºRQ = []
					self.ScalarProd3 = 0
						
					for j in range(0, 2):
						self.term0 =  self.vectorRP[j] * self.vectorRQ[j]
						self.ScalarProd3 = self.ScalarProd3 + self.term0
						self.vectorRPºRQ.append(self.term0)
						
					# Find the component of a along b
					self.cossineThetaRadians = self.ScalarProd3 / ( self.sideA * self.sideB )
					self.radianAngle = math.acos(self.cossineThetaRadians)	
					self.theta = math.degrees(self.radianAngle)
					self.radianTheta = math.radians(self.theta)
					self.alpha = 180 - self.theta
					self.radianAlpha = math.radians(self.alpha)
					self.sineAlphaRadians = math.sin(self.radianAlpha)				
					self.sine = self.sineAlphaRadians
					self.height_h1 = self.sideA * self.sine
					self.height_h2 = self.sideB * self.sine
					self.EquatArea1 = ( ( self.vectorRP[0] * self.vectorRQ[1] ) - ( self.vectorRP[1] * self.vectorRQ[0]) )
						
					print('\t-- The [vectorRP]: vectorRP',self.vectorRP)
					print('\t-- The [vectorRQ]: vectorRQ',self.vectorRQ,'\n')
					print(f'\t-- The [sideA] relative as |vectorRP|: {self.sideA:<.2f}')
					print(f'\t-- The [sideB] relative as |vectorRQ|: {self.sideB:<.2f}')
					print(f'\t-- The [Perimeter(P)] is: {self.Perimeter:<.2f}','\n')
					print('\t-- The [terms] of the Scalar Product(vectorRPºRQ) is:',self.vectorRPºRQ)
					print('\t-- The [Scalar Product(QPºQR)] is:',self.ScalarProd3)
					print(f'\t-- The Cossine of theta: {self.cossineThetaRadians:<.2f}') 
					print(f'\t-- The [Theta angle] between vectors: vectorRP and vectorRQ is: {self.theta:<.2f}')
					print(f'\t-- The Sine of alpha: {self.sineAlphaRadians:<.2f}') 
					print(f'\t-- The [Alpha angle] between vectors: vectorRP and vectorPS is: {self.alpha:<.2f}')
					
				else:
					textstring3.no_OptionKey()
					return
				
			elif self.number1 == 2:
				# Given the coordinates of the points: P, Q, R, and S. The vertices of the parallelogramPQRS
				coordinatespoint.number1 = 1
				self.coordP = coordinatespoint.getcoordinatepoint()
				coordinatespoint.number1 = 2
				self.coordQ = coordinatespoint.getcoordinatepoint()
				coordinatespoint.number1 = 3
				self.coordR = coordinatespoint.getcoordinatepoint()
				coordinatespoint.number1 = 4
				self.coordS = coordinatespoint.getcoordinatepoint()
				
				self.xP = self.xQ = self.xR = self.xS = self.yP = self.yQ = self.yR = self.yS = 0
				
				for self.cP in range(0,2):
					if self.cP == 0:
						self.xP = self.coordP[self.cP]
						self.xQ = self.coordQ[self.cP]
						self.xR = self.coordR[self.cP]
						self.xS = self.coordS[self.cP]
					elif self.cP == 1:
						self.yP = self.coordP[self.cP]
						self.yQ = self.coordQ[self.cP]
						self.yR = self.coordR[self.cP]
						self.yS = self.coordS[self.cP]
				
				self.PointP = (self.xP,self.yP)
				print('\n\t- The (Point P): P',self.PointP)
				self.PointQ = (self.xQ,self.yQ)
				print('\t- The (Point Q): Q',self.PointQ)
				self.PointR = (self.xR,self.yR)
				print('\t- The (Point R): R',self.PointR)
				self.PointS = (self.xS,self.yS)
				print('\t- The (Point S): S',self.PointS)
		
				self.vectorPQ = []
				self.vectorPS = []
				
				for k in range (0,2):
					self.comp0 = self.coordQ[k] - self.coordP[k] 
					self.vectorPQ.append(self.comp0)
					
					self.comp1 = self.coordS[k] - self.coordP[k] 
					self.vectorPS.append(self.comp1)
						
				magnitudebivector.x = self.vectorPQ[0]
				magnitudebivector.y = self.vectorPQ[1]
				# sideA = |PQ|
				self.sideA = magnitudebivector.magbivector()
				
				magnitudebivector.x = self.vectorPS[0]
				magnitudebivector.y = self.vectorPS[1]
				# sideB = |PS|
				self.sideB = magnitudebivector.magbivector()
					
				self.Perimeter = ( self.sideA + self.sideB ) * 2
					
				self.vectorPSºPQ = []
				self.ScalarProd0 = 0
					
				for j in range(0, 2):
					self.term0 =  self.vectorPS[j] * self.vectorPQ[j]
					self.ScalarProd0 = self.ScalarProd0 + self.term0
					self.vectorPSºPQ.append(self.term0)
				
				# Find the component of a along b
				self.cossineThetaRadians = self.ScalarProd0 / ( self.sideA * self.sideB  )
				self.radianAngle = math.acos(self.cossineThetaRadians)
				self.theta = math.degrees(self.radianAngle)
				self.alpha = 180 - self.theta	
				self.radianAlpha = math.radians(self.alpha)
				self.sine = math.sin(self.radianTheta)
				self.alpha = 180 - self.theta
				self.radianAlpha = math.radians(self.alpha)
				self.sineAlphaRadians = math.sin(self.radianAlpha)
				self.sine = self.sineAlphaRadians
				
				self.height_h1 = self.sideA * self.sine
				self.height_h2 = self.sideB * self.sine
				self.EquatArea1 = ( ( self.vectorPQ[0] * self.vectorPS[1] ) - ( self.vectorPQ[1] * self.vectorPS[0]) )
				answer.view_solution()
				print('\t-- The [vectorPQ]: vectorPQ',self.vectorPQ)
				print('\t-- The [vectorPS]: vectorPS',self.vectorPS,'\n')
				print(f'\t-- The [sideA] relative as |vectorPQ|: {self.sideA:<.2f}')
				print(f'\t-- The [sideB] relative as |vectorPS|: {self.sideB:<.2f}')
				print(f'\t-- The [Perimeter(P)] is: {self.Perimeter:<.2f}','\n')
				print('\t-- The [terms] of the Scalar Product(vectorPSºPQ) is:',self.vectorPSºPQ)
				print('\t-- The [Scalar Product(PQºPS)] is:',self.ScalarProd0)
				print(f'\t-- The Cossine of theta: {self.cossineThetaRadians:<.2f}') 
				print(f'\t-- The [Theta angle] between vectors: vectorPQ and vectorPS is: {self.theta:<.2f}')
				print(f'\t-- The Sine of alpha: {self.sineAlphaRadians:<.2f}') 
				print(f'\t-- The [Alpha angle] between vectors: vectorPQ and vectorQR is: {self.alpha:<.2f}')
			
			else:
				textstring3.no_OptionKey()
				
				return
		
		print('\n\t\t----------------------------------------------------')
		print(f'\t\t -_- The [Height(h1)] relative as [sideB] is: {self.height_h1:<.2f}')
		print('\t\t ----------------------- or -----------------------')
		print(f'\t\t º<º The [Height(h2)] relative as [sideA] is: {self.height_h2:<.2f}')
		print('\t\t----------------------------------------------------\n')
		print('\t-- The [Area(S)] of the [Parallelogram(PQRS)]:',format(abs(self.EquatArea1),"<10.2f"),'\n')
			 
		return

scalar_product = ScalarProduct()

class AngleVectors:
	def __init__(self, angleTheta = 0, angleThetaDegrees = 0, cossineThetaRadians = 0):
		self.angleTheta = angleTheta 
		self.cossineThetaRadians = cossineThetaRadians
		self.angleThetaDegrees = angleThetaDegrees
		
	def getangleTheta(self):
		scalar_product.number = 2
		self.cossineThetaRadians = scalar_product.getscalar_product()
		self.angleTheta = math.acos(self.cossineThetaRadians)
		self.angleThetaDegrees = math.degrees(self.angleTheta)
		print(f'\t-- The value of the [THETA ANGLE IN DEGREES] calculated is: {self.angleThetaDegrees:<.2f}','\n')
		return
				
anglevectors = AngleVectors() 
        
class CossineTheta:
	def __init__(self, cossineThetaRadians = 0):
		self.cossineThetaRadians = cossineThetaRadians 
		
	def getcossineTheta(self):
		scalar_product.number = 2
		self.cossineThetaRadians = scalar_product.getscalar_product()
		print(f'\t-- The value of the [COSSINE THETA IN RADIANS] calculated is: {self.cossineThetaRadians:<.2f}','\n')
		return
		
cossinetheta = CossineTheta()

class InnerAngleTriangle:
	def __init__(self, a1 = 0, a2 = 0, addInnerAngle = 0, AngleAlpha_degrees = 0, AngleBeta_degrees = 0, coord = 0, 
	AngleGama_degrees = 0, b1 = 0, b2 = 0, c1 = 0, c2 = 0, comp0 = 0, comp1 = 0, comp3 = 0, coordP = 0, coordQ = 0,
	coordR = 0, coordS = 0, compAB = 0, compBC = 0, compAC = 0, compBA = 0, compCB = 0, compCA = 0, CossineA = 0, 
	CossineB = 0, CossineC = 0, cosineThetaRadians = 0, number1 = 0, normA = 0, normB = 0, normAxBproduct = 0, 
	normBxCproduct = 0, normAxCproduct = 0, pointA = 0, pointB = 0, pointC = 0, PointP = 0,  PointQ = 0, PointR = 0,
	PointS = 0, ScalarProdAB = 0, ScalarProdBC = 0, ScalarProdAC = 0, sideA = 0, sideB = 0, sideC = 0, vectorA = 0,  
	vectorB = 0, vectorC = 0, vectorBC = 0, vectorAC = 0, vectorAB = 0, vectorBA = 0, vectorCB = 0, vectorCA = 0,   
	VectorBC = 0, term = 0, term0 = 0, term1 = 0, xP = 0, xQ = 0, xR = 0, xS = 0, yP = 0, yQ = 0,yR = 0, yS = 0 ):  
	
		self.a1 = a1
		self.a2 = a2
		self.addInnerAngle = addInnerAngle 
		self.AngleAlpha_degrees = AngleAlpha_degrees
		self.AngleBeta_degrees = AngleBeta_degrees
		self.AngleGama_degrees = AngleGama_degrees
		self.b1 = b1
		self.b2 = b2
		self.c1 = c1
		self.c2 = c2
		
		self.comp0 = comp0
		self.comp1 = comp1
		self.comp3 = comp3 
		self.compAB = compAB
		self.compBC = compBC
		self.compAC = compAC
		self.compBA = compBA
		self.compCB = compCB
		self.compCA = compCA 
	 
		self.coord = coord 
		self.coordP = coordP
		self.coordQ = coordQ
		self.coordR = coordR
		self.coordS = coordS
		self.CossineA = CossineA
		self.CossineB = CossineB
		self.CossineC = CossineC
		self.cosineThetaRadians = cosineThetaRadians
		
		self.number1 = number1
		self.normA = normA
		self.normB = normB
		self.normAxBproduct = normAxBproduct
		self.normBxCproduct = normBxCproduct
		self.normAxCproduct = normAxCproduct
		
		self.pointA = pointA
		self.pointB = pointB
		self.pointC = pointC
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		self.PointS = PointS
		
		self.ScalarProdAB = ScalarProdAB
		self.ScalarProdBC = ScalarProdBC
		self.ScalarProdAC = ScalarProdAC
		
		self.sideA = sideA 
		self.sideB = sideB 
		self.sideC = sideC
		
		self.vectorA = vectorA
		self.vectorB = vectorB
		self.vectorC = vectorC
		self.vectorAB = vectorAB
		self.vectorAC = vectorAC 
		self.vectorBC = vectorBC
		self.VectorBC = VectorBC
		self.vectorBA = vectorBA
		self.vectorCB = vectorCB
		self.vectorCA = vectorCA 
		
		self.term = term
		self.term0 = term0
		self.term1 = term1
		self.xP = xP
		self.xQ = xQ
		self.xR = xR
		self.xS = xS
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		self.yS = yS
		
	def getInner_angle_triangle(self):
		# Given the [coordinates] of the points: P, Q, and R of a trianglePQR
		coordinatespoint.number1 = 1
		self.coordP = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 2
		self.coordQ = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 3
		self.coordR = coordinatespoint.getcoordinatepoint()
		
		self.PointP, self.PointQ, self.PointR = self.coordP, self.coordQ, self.coordR
		self.pointA, self.pointB, self.pointC = self.PointP, self.PointQ, self.PointR
		self.xP = self.xQ = self.xR = self.yP = self.yQ = self.yR = 0
    
		for self.coord in range(0,2):
			if self.coord == 0:
				self.xP = self.PointP[self.coord]
				self.xQ = self.PointQ[self.coord]
				self.xR = self.PointR[self.coord]
				
			elif self.coord == 1:
				self.yP = self.PointP[self.coord]
				self.yQ = self.PointQ[self.coord]
				self.yR = self.PointR[self.coord]  
					
		self.PointP = (self.xP,self.yP)
		print('\n\t- The (Point P): P',self.PointP)
		self.PointQ = (self.xQ,self.yQ)
		print('\t- The (Point Q): Q',self.PointQ)
		self.PointR = (self.xR,self.yR)
		print('\t- The (Point R): R',self.PointR)
		answer.view_solution()
		
		for op in range (0,3):
			# Will find the scalar product: b * c
			if op == 0:
				self.vectorAC = []
				self.vectorAB = []
				
				for p in range (0,2):
					self.compAC = ( self.pointC[p] - self.pointA[p] )
					self.vectorAC.append(self.compAC)
					self.compAB = ( self.pointB[p] - self.pointA[p] )
					self.vectorAB.append(self.compAB)
					
				self.vectorB = self.vectorAC
				self.vectorC = self.vectorAB
				print('\t- The [vectorB]=vectorPR',self.vectorB)
				print('\t- The [vectorC]=vectorPQ',self.vectorC,'\n')

				self.scalarProductBC = 0
				
				# In definition of the InnerAngleTriangle class is necessary create the atributes: self.VectorBC = 0,
				# and too self.vectorBC = 0. -- [ self.VectorBC != self.vectorBC ].
				self.VectorBC = []
				
				for d0 in range (0,2):
					self.term0 = self.vectorAC[d0] * self.vectorAB[d0]
					self.scalarProductBC = self.scalarProductBC + self.term0
					self.VectorBC.append(self.term0)
					
				self.b1 = self.vectorB[0]
				magnitudebivector.x = self.b1  
				self.b2 = self.vectorB[1]
				magnitudebivector.y = self.b2
				self.normB = magnitudebivector.magbivector()
				self.sideB = self.normB
				self.c1 = self.vectorC[0]
				magnitudebivector.x = self.c1
				self.c2 = self.vectorC[1]
				magnitudebivector.y = self.c2
				self.normC = magnitudebivector.magbivector()
				self.sideC = self.normC
				self.normBxCproduct = ( self.normB * self.normC )
				
			elif op == 1:
				# Will find the scalar product: a * c
				self.vectorBC = []
				self.vectorBA = []

				for q in range (0,2):
					self.compBC = ( self.pointC[q] - self.pointB[q] )
					self.vectorBC.append(self.compBC)
					self.compBA = ( self.pointA[q] - self.pointB[q] )
					self.vectorBA.append(self.compBA)

				self.vectorA = self.vectorBC
				self.vectorC = self.vectorBA
				print('\t- The [vectorA]=vectorQR',self.vectorA)
				print('\t- The [vectorC]=vectorQP',self.vectorC,'\n')

				self.scalarProductAC = 0
				self.vectorAC = []

				for d1 in range (0,2):
					self.term1 = self.vectorBC[d1] * self.vectorBA[d1]
					self.scalarProductAC = self.scalarProductAC + self.term1
					self.vectorAC.append(self.term1)
					
				self.a1 = self.vectorA[0]
				magnitudebivector.x = self.a1
				self.a2 = self.vectorA[1]
				magnitudebivector.y = self.a2
				self.normA = magnitudebivector.magbivector()
				self.sideA = self.normA
				self.c1 = self.vectorC[0]
				magnitudebivector.x = self.c1
				self.c2 = self.vectorC[1]
				magnitudebivector.y = self.c2
				self.normC = magnitudebivector.magbivector()
				self.sideC = self.normC
				self.normAxCproduct = ( self.normA * self.normC )
				
			elif op == 2:
				# Will find the scalar product: a * b
				self.vectorCB = []
				self.vectorCA = []

				for r in range (0,2):
					self.compCB = ( self.pointB[r] - self.pointC[r] )
					self.vectorCB.append(self.compCB)
					self.compCA = ( self.pointA[r] - self.pointC[r] )
					self.vectorCA.append(self.compCA)

				self.vectorA = self.vectorCB
				self.vectorB = self.vectorCA
				print('\t- The [vectorA]=vectorRQ',self.vectorA)
				print('\t- The [vectorB]=vectorRP',self.vectorB,'\n')

				self.scalarProductAB = 0
				self.vectorAB = []

				for d2 in range (0,2):
					self.term2 = self.vectorCB[d2] * self.vectorCA[d2]
					self.scalarProductAB = self.scalarProductAB + self.term2
					self.vectorAB.append(self.term2)
					
				self.a1 = self.vectorA[0]
				magnitudebivector.x = self.a1
				self.a2 = self.vectorA[1]
				magnitudebivector.y = self.a2
				self.normA = magnitudebivector.magbivector()
				self.sideA = self.normA
				self.b1 = self.vectorB[0]
				magnitudebivector.x = self.b1
				self.b2 = self.vectorB[1]
				magnitudebivector.y = self.b2 
				self.normB = magnitudebivector.magbivector()
				self.sideB = self.normB
				self.normAxBproduct = ( self.normA * self.normB )
				
				if self.sideA < self.sideB + self.sideC and self.sideB < self.sideA + self.sideC and self.sideC < self.sideA + self.sideB:
					textstring1.view_instructions()
					
					self.CossineA = ( self.scalarProductBC / self.normBxCproduct )
					self.angle_radians = math.acos(self.CossineA)
					self.AngleAlpha_degrees = math.degrees(self.angle_radians)
					
					self.CossineB = ( self.scalarProductAC / self.normAxCproduct )
					self.angle_radians = math.acos(self.CossineB)
					self.AngleBeta_degrees = math.degrees(self.angle_radians)
					
					self.CossineC = ( self.scalarProductAB / self.normAxBproduct )
					self.angle_radians = math.acos(self.CossineC)
					self.AngleGama_degrees = math.degrees(self.angle_radians)
					
					print(f'\n\t\t-- The [sideA]=|vectorA| of the triangle(PQR)] is: {self.sideA:<.2f}','\n')
					print('\t-- The [terms] of the [Scalar Profuct(ACºAB)] is the vector[ACºAB]:', self.VectorBC )
					print(f'\t-- The [value] of the [Scalar Profuct(ACºAB)] is: {self.scalarProductBC:<.2f}')
					print(f'\t\t- The value of the [ALPHA ANGLE] was calculate is: {self.AngleAlpha_degrees:<.2f}','\n')
					print(f'\t\t-- The [sideB]=|vectorB| of the triangle(PQR)] is: {self.sideB:<.2f}','\n')
					print('\t-- The [terms] of the [Scalar Profuct(BCºBA)] is the vector[BCºBA]:', self.vectorAC )
					print(f'\t-- The [value] of the [Scalar Profuct(BCºBA)] is: {self.scalarProductAC:<.2f}')
					print(f'\t\t- The value of the [BETA ANGLE] was calculate is: {self.AngleBeta_degrees:<.2f}','\n')
					print(f'\t\t-- The [sideC]=|vectorC| of the triangle(PQR)] is: {self.sideC:<.2f}','\n')
					print('\t-- The [terms] of the [Scalar Profuct(CBºCA)] is the vector[CBºCA]:', self.vectorAB )
					print(f'\t-- The [value] of the [Scalar Profuct(CBºCA)] is: {self.scalarProductAB:<.2f}' )
					print(f'\t\t- The value of the [GAMA ANGLE] was calculate is: {self.AngleGama_degrees:<.2f}','\n')
					
					if self.AngleAlpha_degrees == self.AngleBeta_degrees and self.AngleAlpha_degrees == self.AngleGama_degrees and self.AngleBeta_degrees == self.AngleGama_degrees:
						print('\n\t\t\t-- The triangle(PQR) is [Equilateral]!','\n')
					elif self.AngleAlpha_degrees == self.AngleBeta_degrees or self.AngleAlpha_degrees == self.AngleGama_degrees or self.AngleBeta_degrees == self.AngleGama_degrees:
						print('\n\t\t\t-- The triangle(PQR) is [Isosceles]!','\n')
					elif self.AngleAlpha_degrees != self.AngleBeta_degrees and self.AngleAlpha_degrees != self.AngleGama_degrees and self.AngleBeta_degrees != self.AngleGama_degrees:
						print('\n\t\t\t-- The triangle(PQR) is [Scalene]!','\n')

					self.addInnerAngle = self.AngleAlpha_degrees + self.AngleBeta_degrees + self.AngleGama_degrees
					
					print(f'\n\t-- The [Add] of the [Inner Angles: ALPHA, BETA, GAMA] is {self.addInnerAngle}','\n')
					
					if math.floor(self.addInnerAngle) == 180:
						print(f'\t- THE [ADD] OF THE [INNER ANGLES] OF THE [TRIANGLE-PQR] is {self.addInnerAngle:<.2f}','\n')
					else:
						print(f'\t-- *[The Integer part] = {math.floor(self.addInnerAngle)} of the Real Number is not equal the [Add] of the')
						print('\t-- *[ [Inner Angles]: [ALPHA + BETA + GAMA = 180º] by theorem! ]*')
					print('\n\t\t\t  --[END CALCULUS-OK!]--\n')
				else:
					textstring2.error_instructions()	
		return
    
inner_angle_triangle = InnerAngleTriangle()

class Medians:
	def __init__(self, compX = 0, compY = 0, medianPM = 0, medianQL = 0, medianRK = 0, xK = 0, yK = 0, xL = 0, yL = 0,
	xM = 0, yM = 0, xP = 0, yP = 0, xQ = 0, yQ = 0, xR = 0, yR = 0, PointM = [], pointP = 0, PointL = [], pointQ = 0,
	PointK = [], pointR = 0, vectorPM = [], vectorQL = [], vectorRK = [] ):
		
		self.compX = compX 
		self.compY = compY 
		self.medianPM = medianPM
		self.medianQL = medianQL 
		self.medianRK = medianRK 
		
		self.PointM = PointM 
		self.pointP = pointP
		self.PointL = PointL 
		self.pointQ = pointQ 
		self.PointK = PointK
		self.pointR = pointR 
		
		self.vectorPM = vectorPM 
		self.vectorQL = vectorQL
		self.vectorRK = vectorRK
		
		self.xK = xK 
		self.yK = yK
		self.xL = xL 
		self.yL = yL 
		self.xM = xM 
		self.yM = yM
		self.xP = xP
		self.yP = yP
		self.xQ = xQ
		self.yQ = yQ
		self.xR = xR
		self.yR = yR
		
	def findMedianPM(self):
		midpoint.number = 3
		midpoint.getmid_point()
		# Access the coordinates: xM and yM of the Class MidPoint.
		self.xM = midpoint.xM
		self.PointM.append(self.xM)
		self.yM = midpoint.yM
		self.PointM.append(self.yM)
		coordinatespoint.number1 = 1
		self.pointP = coordinatespoint.getcoordinatepoint()
		
		for h in range (0, 2):
			self.compVectorPM = self.PointM[h] - self.pointP[h]
			if h == 0:
				self.compX = self.compVectorPM
			elif h == 1:
				self.compY = self.compVectorPM	
			self.vectorPM.append(self.compVectorPM)
			
		# magnitudebivector.magbivector()
		magnitudebivector.x = self.compX 
		magnitudebivector.y = self.compY
		self.medianPM = magnitudebivector.magbivector()
		answer.view_solution()
		print('\t-- The terms of the [vectorPM]:', self.vectorPM)
		print(f'\t-- The [mediana: PM] finded is {self.medianPM:<.2f}','\n')
		return
		
	def findMedianQL(self):
		midpoint.number = 2
		midpoint.getmid_point()
		# Access the coordinates: xL and yL of the Class MidPoint.
		self.xL = midpoint.xL
		self.PointL.append(self.xL)
		self.yL = midpoint.yL
		self.PointL.append(self.yL)
		coordinatespoint.number1 = 2
		self.pointQ = coordinatespoint.getcoordinatepoint()
		
		for h in range (0, 2):
			self.compVectorQL = self.PointL[h] - self.pointQ[h]
			if h == 0:
				self.compX = self.compVectorQL
			elif h == 1:
				self.compY = self.compVectorQL	
			self.vectorQL.append(self.compVectorQL)
			
		# magnitudebivector.magbivector()
		magnitudebivector.x = self.compX 
		magnitudebivector.y = self.compY
		self.medianQL = magnitudebivector.magbivector()
		answer.view_solution()
		print('\t-- The terms of the [vectorQL]:', self.vectorQL)
		print(f'\t-- The [mediana: QL] finded is {self.medianQL:<.2f}','\n')
		return
		
	def findMedianRK(self):
		midpoint.number = 1
		midpoint.getmid_point()
		# Access the coordinates: xK and yK of the Class MidPoint.
		self.xK = midpoint.xK
		self.PointK.append(self.xK)
		self.yK = midpoint.yK
		self.PointK.append(self.yK)
		coordinatespoint.number1 = 3
		self.pointR = coordinatespoint.getcoordinatepoint()
		
		for h in range (0, 2):
			self.compVectorRK = self.PointK[h] - self.pointR[h]
			if h == 0:
				self.compX = self.compVectorRK
			elif h == 1:
				self.compY = self.compVectorRK	
			self.vectorRK.append(self.compVectorRK)
			
		# magnitudebivector.magbivector()
		magnitudebivector.x = self.compX 
		magnitudebivector.y = self.compY
		self.medianRK = magnitudebivector.magbivector()
		answer.view_solution()
		print('\t-- The terms of the [vectorRK]:', self.vectorRK)
		print(f'\t-- The [mediana: RK] finded is {self.medianRK:<.2f}','\n')
		return
		
medians = Medians()

class FindTheMedians:
	'''Determine the medianas of the triangle(PQR)'''
	def __init__(self, number2 = 0):
		self.number2 = number2
		
	def getmedians(self):
		print('\t\t- Key [1] to find the new medianaPM or')
		print('\t\t- Key [2] to find the new medianaQL or')
		print('\t\t- Key [3] to find the new medianaRK.\n')
		self.number2 = vector.enterIntegerData()
		if self.number2 == 1:
			medians.findMedianPM()
		elif self.number2 == 2:
			medians.findMedianQL()
		elif self.number2 == 3:
			medians.findMedianRK()
		else:
			textstring3.no_OptionKey()
		return

findthemedians = FindTheMedians()

class CentricG:
	def __init__(self, xG = 0, yG = 0, xP = 0, yP = 0, xQ = 0, yQ = 0, xR = 0, yR = 0, baricG = 0, pointP = [],
	pointQ = [], pointR = [], PointP = (), PointQ = (), PointR = ()):
		self.baricG =  baricG
		self.xG = xG
		self.yG = yG 
		self.xP = xP
		self.yP = yP
		self.xQ = xQ
		self.yQ = yQ
		self.xR = xR
		self.yR = yR
		self.pointP = pointP
		self.pointQ = pointQ 
		self.pointR = pointR
		
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		
	def find_centricG(self):
		coordinatespoint.number1 = 1
		self.pointP = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 2
		self.pointQ = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 3
		self.pointR = coordinatespoint.getcoordinatepoint()
		
		self.xP = self.pointP[0]
		self.xQ = self.pointQ[0]
		self.xR = self.pointR[0]
		self.yP = self.pointP[1]
		self.yQ = self.pointQ[1]
		self.yR = self.pointR[1]
		
		self.xG = ( self.xP + self.xQ + self.xR ) / 3
		self.yG = ( self.yP + self.yQ + self.yR ) / 3
		
		self.PointP = (self.xP,self.yP)
		print('\n\t- The (Point P): P',self.PointP)
		self.PointQ = (self.xQ,self.yQ)
		print('\t- The (Point Q): Q',self.PointQ)
		self.PointR = (self.xR,self.yR)
		print('\t- The (Point R): R',self.PointR)
		answer.view_solution()
		print('\t-- The [Coordenates] of the [Centroid_ G(xG,yG)] in the Triangle(PQR):')
		print(f'\n\t-- The [Coordinate]: xG is {self.xG:<.2f}')
		print(f'\t-- The [Coordinate]: yG is {self.yG:<.2f}','\n')
				
centricg = CentricG()

class EnterCoordPointPQ:
	'''Given any two points: P and Q find the vector A'''
	def __init__(self, coord = 0, pointP = [], pointQ = [], PointP = (), PointQ = (), xP = 0, yP = 0, xQ = 0, yQ = 0):
		self.coord = coord
		self.pointP = pointP
		self.pointQ = pointQ
		
		self.PointP = pointP
		self.PointQ = pointQ
		self.xP = xP
		self.yP = yP
		self.xQ = xQ
		self.yQ = yQ
		
	def findcoord_pointPQ(self):
		'''Will find the coordinates of two points: P and Q.'''
		coordinatespoint.number1 = 1
		self.pointP = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 2
		self.pointQ = coordinatespoint.getcoordinatepoint()
		
		self.xP = self.yP = self.xQ = self.yQ = 0
		
		for self.coord in range(0,2):
			if self.coord == 0:
				self.xP = self.pointP[self.coord]
				self.xQ = self.pointQ[self.coord]
			elif self.coord == 1:
				self.yP = self.pointP[self.coord]
				self.yQ = self.pointQ[self.coord]

		self.PointP = (self.xP,self.yP)
		print('\n\t- The (Point P): P', self.PointP)
		self.PointQ = (self.xQ,self.yQ)
		print('\t- The (Point Q): Q', self.PointQ,'\n')
		return 

findcoordpq = EnterCoordPointPQ()

class FindVectorA:
	def __init__(self, a1 = 0, a2 = 0, normA = 0, pointP = [], pointQ = [], vectorA = 0, vectorPQ = [], xP = 0, yP = 0,
	xQ = 0, yQ = 0):
		self.a1 = a1
		self.a2 = a2
		self.normA = normA
		self.pointP = pointP
		self.pointQ = pointQ
		self.vectorA = vectorA
		self.vectorPQ = vectorPQ
		self.xP = xP
		self.yP = yP
		self.xQ = xQ
		self.yQ = yQ
		
	def find_vectorA(self):
		self.xP = findcoordpq.xP
		self.pointP.append(self.xP)
		self.yP = findcoordpq.yP
		self.pointP.append(self.yP)
		self.xQ = findcoordpq.xQ
		self.pointQ.append(self.xQ)
		self.yQ = findcoordpq.yQ
		self.pointQ.append(self.yQ)
		
		for h in range (0,2):
			self.coord = self.pointQ[h] - self.pointP[h]
			self.vectorPQ.append(self.coord)
			
		self.vectorA = self.vectorPQ
		self.a1 = self.vectorA[0]
		magnitudebivector.x = self.a1
		self.a2 = self.vectorA[1]
		magnitudebivector.y = self.a2
		self.normA = magnitudebivector.magbivector()
		
		answer.view_solution()
		print('\t-- The [vectorA]: vectorA=vectorPQ', self.vectorA)
		print(f'\t-- The [lenghtPQ = distPQ] is the ||vectorPQ||: {self.normA:<.2f}','\n')
		return self.vectorA

findvectorA = FindVectorA()

class EnterCoordPointPR:
	'''Given any two points: P and R find the vector B'''
	def __init__(self, coord = 0, pointP = [], pointR = [], PointP = (), PointR = (), xP = 0, yP = 0, xR = 0, yR = 0):
		self.coord = coord
		self.pointP = pointP
		self.pointR = pointR
		
		self.PointP = PointP
		self.PointR = PointR
		self.xP = xP
		self.yP = yP
		self.xR = xR
		self.yR = yR
		
	def findcoord_pointPR(self):
		'''Will find the coordinates of two points: P and R.'''
		coordinatespoint.number1 = 1
		self.pointP = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 3
		self.pointR = coordinatespoint.getcoordinatepoint()
		
		self.xP = self.yP = self.xR = self.yR = 0
		
		for self.coord in range(0,2):
			if self.coord == 0:
				self.xP = self.pointP[self.coord]
				self.xR = self.pointR[self.coord]
			elif self.coord == 1:
				self.yP = self.pointP[self.coord]
				self.yR = self.pointR[self.coord]

		self.PointP = (self.xP,self.yP)
		print('\n\t- The (Point P): P', self.PointP)
		self.PointR = (self.xR,self.yR)
		print('\t- The (Point R): R', self.PointR,'\n')
		return 

findcoordpr = EnterCoordPointPR()

class FindVectorB:
	def __init__(self, b1 = 0, b2 = 0, normB = 0, pointP = [], pointR = [], vectorB = 0, vectorPR = [], xP = 0, yP = 0,
	xR = 0, yR = 0):
		self.b1 = b1
		self.b2 = b2
		self.normB = normB
		self.pointP = pointP
		self.pointR = pointR
		
		self.vectorB = vectorB
		self.vectorPR = vectorPR
		
		self.xP = xP
		self.yP = yP
		self.xR = xR
		self.yR = yR
		
	def find_vectorB(self):
		self.xP = findcoordpr.xP
		self.pointP.append(self.xP)
		self.yP = findcoordpr.yP
		self.pointP.append(self.yP)
		self.xR = findcoordpr.xR
		self.pointR.append(self.xR)
		self.yR = findcoordpr.yR
		self.pointR.append(self.yR)
		
		for h in range (0,2):
			self.coord = self.pointR[h] - self.pointP[h]
			self.vectorPR.append(self.coord)
			
		self.vectorB = self.vectorPR
		self.b1 = self.vectorB[0]
		magnitudebivector.x = self.b1
		self.b2 = self.vectorB[1]
		magnitudebivector.y = self.b2
		self.normB = magnitudebivector.magbivector()
		
		answer.view_solution()
		print('\t-- The [vectorB]: vectorB=vectorPR', self.vectorB)
		print(f'\t-- The [lenghtPR = distPR] is the ||vectorPR||: {self.normB:<.2f}','\n')
		return self.vectorB

findvectorB = FindVectorB()

class EnterCoordPointQR:
	'''Given any two points: Q and R find the vector C'''
	def __init__(self, coord = 0, pointQ = [], pointR = [], PointQ = (), PointR = (), xQ = 0, yQ = 0, xR = 0, yR = 0):
		self.coord = coord
		self.pointQ = pointQ
		self.pointR = pointR
		
		self.PointQ = PointQ
		self.PointR = PointR
		self.xQ = xQ
		self.yQ = yQ
		self.xR = xR
		self.yR = yR
		
	def findcoord_pointQR(self):
		'''Will find the coordinates of two points: Q and R.'''
		coordinatespoint.number1 = 2
		self.pointQ = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 3
		self.pointR = coordinatespoint.getcoordinatepoint()
		
		self.xQ = self.yQ = self.xR = self.yR = 0
		
		for self.coord in range(0,2):
			if self.coord == 0:
				self.xQ = self.pointQ[self.coord]
				self.xR = self.pointR[self.coord]
			elif self.coord == 1:
				self.yQ = self.pointQ[self.coord]
				self.yR = self.pointR[self.coord]

		self.PointQ = (self.xQ,self.yQ)
		print('\n\t- The (Point Q): Q', self.PointQ)
		self.PointR = (self.xR,self.yR)
		print('\t- The (Point R): R', self.PointR,'\n')
		return 
		
findcoordqr = EnterCoordPointQR()

class FindVectorC:
	def __init__(self, c1 = 0, c2 = 0, normC = 0, pointQ = [], pointR = [], vectorC = 0, vectorQR = [], xQ = 0, yQ = 0,
	xR = 0, yR = 0):
		self.c1 = c1
		self.c2 = c2
		self.normC = normC
		self.pointQ = pointQ
		self.pointR = pointR
		
		self.vectorC = vectorC
		self.vectorQR = vectorQR
		
		self.xQ = xQ
		self.yQ = yQ
		self.xR = xR
		self.yR = yR
		
	def find_vectorC(self):
		self.xQ = findcoordqr.xQ
		self.pointQ.append(self.xQ)
		self.yQ = findcoordqr.yQ
		self.pointQ.append(self.yQ)
		self.xR = findcoordqr.xR
		self.pointR.append(self.xR)
		self.yR = findcoordqr.yR
		self.pointR.append(self.yR)
		
		for h in range (0,2):
			self.coord = self.pointR[h] - self.pointQ[h]
			self.vectorQR.append(self.coord)
			
		self.vectorC = self.vectorQR
		self.c1 = self.vectorC[0]
		magnitudebivector.x = self.c1
		self.c2 = self.vectorC[1]
		magnitudebivector.y = self.c2
		self.normC = magnitudebivector.magbivector()
		
		answer.view_solution()
		print('\t-- The [vectorC]: vectorC=vectorQR', self.vectorC)
		print(f'\t-- The [lenghtQR = distQR] is the ||vectorQR||: {self.normC:<.2f}','\n')
		return self.vectorC

findvectorC = FindVectorC()

class BisectrixPoints:
	'''Will find the [coordinates] of three points: D(xD,yD), E(xE,yE). and F(xF,yF)'''
	def __init__(self, compX = 0, compY = 0, number1 = 0, pointD = [], pointE = [], pointF = [], pointP = [],
	pointQ = [], pointR = [], sideA = 0, sideB = 0,  sideC = 0, xD = 0, xE = 0, xF = 0, yD = 0, yE = 0, yF = 0,  
	xP = 0, xQ = 0, xR = 0, yP = 0, yQ = 0, yR = 0 ):
		self.compX = compX 
		self.compY = compY
		self.number1 = number1 
		
		self.pointD = pointD
		self.pointE = pointE
		self.pointF = pointF
		
		self.pointP = pointP
		self.pointQ = pointQ
		self.pointR = pointR
		
		self.sideA = sideA
		self.sideB = sideB 
		self.sideC = sideC 
		
		self.xD = xD
		self.xE = xE
		self.xF = xF
		self.yD = yD 
		self.yE = yE
		self.yF = yF
		
		self.xP = xP
		self.xQ = xQ
		self.xR = xR
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		
	def enterCoordinates(self):
		# Enter the coordinates
		coordinatespoint.number1 = 1
		self.pointP = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 2
		self.pointQ = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 3
		self.pointR = coordinatespoint.getcoordinatepoint()
		return
		
	def determine_pointD(self):
		self.enterCoordinates()
		for d in range(0,2):
			if d == 0:
				self.xP = self.pointP[d]
				self.xQ = self.pointQ[d]
				self.xR = self.pointR[d]
				self.compX = self.xQ - self.xP
			elif d == 1:
				self.yP = self.pointP[d]
				self.yQ = self.pointQ[d]
				self.yR = self.pointR[d]
				self.compY = self.yQ - self.yP
				
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY 
		self.sideA = magnitudebivector.magbivector()
		self.compX = self.xR - self.xP
		self.compY = self.yR - self.yP
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY 
		self.sideB = magnitudebivector.magbivector()
		self.xD = ( self.sideB * self.xQ + self.sideA * self.xR ) / ( self.sideB + self.sideA ) 
		self.yD = ( self.sideB * self.yQ + self.sideA * self.yR ) / ( self.sideB + self.sideA )
		answer.view_solution()
		print(f'\t-- The [coordinate: xD] is {self.xD:<.2f}' )
		print(f'\t-- The [coordinate: yD] is {self.yD:<.2f}','\n')
		return
		
	def determine_pointE(self):
		self.enterCoordinates()
		for e in range(0,2):
			if e == 0:
				self.xP = self.pointP[e]
				self.xQ = self.pointQ[e]
				self.xR = self.pointR[e]
				self.compX = self.xQ - self.xP
			elif e == 1:
				self.yP = self.pointP[e]
				self.yQ = self.pointQ[e]
				self.yR = self.pointR[e]
				self.compY = self.yQ - self.yP
				
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY 
		self.sideA = magnitudebivector.magbivector()
		self.compX = self.xR - self.xQ
		self.compY = self.yR - self.yQ
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY 
		self.sideC = magnitudebivector.magbivector()
		self.xE = ( self.sideA * self.xR + self.sideC * self.xP ) / ( self.sideA + self.sideC )
		self.yE = ( self.sideA * self.yR + self.sideC * self.yP ) / ( self.sideA + self.sideC )
		answer.view_solution()
		print(f'\t-- The [coordinate: xE] is {self.xE:<.2f}' )
		print(f'\t-- The [coordinate: yE] is {self.yE:<.2f}','\n')
		return
		
	def determine_pointF(self):
		self.enterCoordinates()
		for f in range(0,2):
			if f == 0:
				self.xP = self.pointP[f]
				self.xQ = self.pointQ[f]
				self.xR = self.pointR[f]
				self.compX = self.xR - self.xP
			elif f == 1:
				self.yP = self.pointP[f]
				self.yQ = self.pointQ[f]
				self.yR = self.pointR[f]
				self.compY = self.yR - self.yP
				
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY 
		self.sideB = magnitudebivector.magbivector()
		self.compX = self.xR - self.xQ
		self.compY = self.yR - self.yQ
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY 
		self.sideC = magnitudebivector.magbivector()
		self.xF = ( self.sideC * self.xP + self.sideB * self.xQ ) / ( self.sideC + self.sideB )
		self.yF = ( self.sideC * self.yP + self.sideB * self.yQ ) / ( self.sideC + self.sideB )
		answer.view_solution()
		print(f'\t-- The [coordinate: xF] is {self.xF:<.2f}' )
		print(f'\t-- The [coordinate: yF] is {self.yF:<.2f}','\n')
		return
		
	def select_point(self):
		print("\t- What's the point: D, or E, or F will get?\n")
		print('\t\t-- Type [1] to find the [coordinate] of the point: D(xD,yD).')
		print('\t\t-- Type [2] to find the [coordinate] of the point: E(xE,yE).')
		print('\t\t-- Type [3] to find the [coordinate] of the point: F(xF,yF).\n')
		self.number1 = vector.enterIntegerData()
		if  self.number1 == 1:
			bisectrixpoints.determine_pointD()
		elif self.number1 == 2:
			bisectrixpoints.determine_pointE()
		elif self.number1 == 3:
			bisectrixpoints.determine_pointF()
		else:
			textstring3.no_OptionKey()
		return
		
bisectrixpoints = BisectrixPoints()

class BisectrixTriangle:
	'''Will calculate the three bisectrix: distPD, distQE, and distRF of a Triangle(PQR).'''
	def __init__(self, compX = 0, compY = 0, distPD = 0, distQE = 0, distRF = 0, number3 = 0, pointD = [], pointE = [], 
	pointF = [], pointP = [], pointQ = [], pointR = [], xD = 0, xE = 0, xF = 0, yD = 0, yE = 0, yF = 0, xP = 0, xQ = 0,
	xR = 0, yP = 0, yQ = 0, yR = 0 ):
		self.compX = compX 
		self.compY = compY
		self.distPD = distPD 
		self.distQE = distQE 
		self.distRF = distRF
		
		self.pointD = pointD
		self.pointE = pointE
		self.pointF = pointF
		
		self.pointP = pointP
		self.pointQ = pointQ
		self.pointR = pointR
		
		self.xD = xD
		self.xE = xE
		self.xF = xF
		self.yD = yD 
		self.yE = yE
		self.yF = yF
		
		self.xP = xP
		self.xQ = xQ
		self.xR = xR
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		
	def find_bisectrixPD(self):
		coordinatespoint.number1 = 1
		self.pointP = coordinatespoint.getcoordinatepoint()
		self.xD = bisectrixpoints.xD
		self.yD = bisectrixpoints.yD
		self.xP = self.pointP[0]
		self.yP = self.pointP[1]
		self.compX = self.xD - self.xP
		self.compY = self.yD - self.yP
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY
		self.distPD = magnitudebivector.magbivector()
		answer.view_solution()
		print(f'\t-- The value finded of the [bisectrixPD] of the Triangle(PQR) is {self.distPD:<.2f}','\n')
		return
		
	def find_bisectrixQE(self):
		coordinatespoint.number1 = 2
		self.pointQ = coordinatespoint.getcoordinatepoint()
		self.xE = bisectrixpoints.xE
		self.yE = bisectrixpoints.yE
		self.xQ = self.pointQ[0]
		self.yQ = self.pointQ[1]
		self.compX = self.xE - self.xQ
		self.compY = self.yE - self.yQ
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY
		self.distQE = magnitudebivector.magbivector()
		answer.view_solution()
		print(f'\t-- The value finded of the [bisectrixQE] of the Triangle(PQR) is {self.distQE:<.2f}','\n')
		return
		
	def find_bisectrixRF(self):
		coordinatespoint.number1 = 3
		self.pointR = coordinatespoint.getcoordinatepoint()
		self.xF = bisectrixpoints.xF
		self.yF = bisectrixpoints.yF
		self.xR = self.pointR[0]
		self.yR = self.pointR[1]
		self.compX = self.xF - self.xR
		self.compY = self.yF - self.yR
		magnitudebivector.x = self.compX
		magnitudebivector.y = self.compY
		self.distRF = magnitudebivector.magbivector()
		answer.view_solution()
		print(f'\t-- The value finded of the [bisectrixRF] of the Triangle(PQR) is {self.distRF:<.2f}','\n')
		return
		
	def select_bisectrix(self):
		print("\t- What's the bisectrix: PD, or QE, or RF of a Triangle(PQR) will determine?\n")
		print('\t\t-- Key [1] to calculate the [bisectrixPD]')
		print('\t\t-- Key [2] to calculate the [bisectrixQE]')
		print('\t\t-- Key [3] to calculate the [bisectrixRF]\n')
		self.number3 = vector.enterIntegerData()
		if  self.number3 == 1:
			bisectrixpoints.determine_pointD()
			bisectrixtriangle.find_bisectrixPD()
		elif self.number3 == 2:
			bisectrixpoints.determine_pointE()
			bisectrixtriangle.find_bisectrixQE()
		elif self.number3 == 3:
			bisectrixpoints.determine_pointF()
			bisectrixtriangle.find_bisectrixRF()
		else:
			textstring3.no_OptionKey()
		return
				
bisectrixtriangle = BisectrixTriangle()

class VerticesTriangle:
	'''
	Given the Midpoints: K(xK,yK), L(xL,yL), and M(xM,yM) of a Triangle(PQR) will find the vertice points: P(xP,yP),
	Q(xQ,yQ), and R(xR,yR) of the Triangle(PQR).
	'''
	def __init__(self, coord = 0, number4 = 0, midpointK = [], midpointL = [], midpointM = [], PointK = (), 
	PointL = (), PointM = (), PointP = (), PointQ = (), PointR = (),xK = 0, yK = 0, xL = 0, yL = 0,  xM = 0, yM = 0, 
	xP = 0, xQ = 0, xR = 0, yP = 0, yQ = 0, yR = 0 ):
		self.coord = coord
		self.number4 = number4
		
		self.midpointK = midpointK 
		self.midpointL = midpointL 
		self.midpointM = midpointM
		self.PointK = PointK
		self.PointL = PointL 
		self.PointM = PointM
		
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		
		self.xK = xK 
		self.yK = yK
		self.xL = xL 
		self.yL = yL
		self.xM = xM 
		self.yM = yM
		
		self.xP = xP
		self.yP = yP
		self.xQ = xQ
		self.yQ = yQ
		self.xR = xR
		self.yR = yR
		
	def enter_midpoints(self):
		coordinatespoint.number1 = 5
		self.midpointK = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 6
		self.midpointL = coordinatespoint.getcoordinatepoint()
		coordinatespoint.number1 = 7
		self.midpointM = coordinatespoint.getcoordinatepoint()
		return
		
	def find_verticeP(self):
		verticestriangle.enter_midpoints()
		
		for i in range(0,2):
			if i == 0:
				self.xK = self.midpointK[i]
				self.xL = self.midpointL[i]
				self.xM = self.midpointM[i]
			elif i == 1:
				self.yK = self.midpointK[i]
				self.yL = self.midpointL[i]
				self.yM = self.midpointM[i]
				
		self.xP = ( self.xK + self.xL ) - self.xM
		self.yP = (	self.yK + self.yL ) - self.yM
		
		self.PointP = (self.xP,self.yP)
		answer.view_solution() 
		print('\t- The (Point P): P',self.PointP)
		return
		
	def find_verticeQ(self):
		verticestriangle.enter_midpoints()
		
		for j in range(0,2):
			if j == 0:
				self.xK = self.midpointK[j]
				self.xL = self.midpointL[j]
				self.xM = self.midpointM[j]
			elif j == 1:
				self.yK = self.midpointK[j]
				self.yL = self.midpointL[j]
				self.yM = self.midpointM[j]
				
		self.xQ = ( self.xM + self.xK ) - self.xL
		self.yQ = (	self.yM + self.yK ) - self.yL
		
		self.PointQ = (self.xQ,self.yQ)
		answer.view_solution() 
		print('\t- The (Point Q): Q',self.PointQ)
		return
		
	def find_verticeR(self):
		verticestriangle.enter_midpoints()
		
		for k in range(0,2):
			if k == 0:
				self.xK = self.midpointK[k]
				self.xL = self.midpointL[k]
				self.xM = self.midpointM[k]
			elif k == 1:
				self.yK = self.midpointK[k]
				self.yL = self.midpointL[k]
				self.yM = self.midpointM[k]
				
		self.xR = ( self.xL + self.xM ) - self.xK
		self.yR = (	self.yL + self.yM ) - self.yK
		
		self.PointR = (self.xR,self.yR)
		answer.view_solution() 
		print('\t- The (Point R): R',self.PointR)
		return
		
	def select_findVertice(self):
		'''Select what vertice of the Triangle(PQR): P or Q or R will calculate.'''
		print('\t\t- Type [1] to find the vertice: P(xP,yP) triangle(PQR).')
		print('\t\t- Type [2] to get the vertice: Q(xQ,yQ) triangle(PQR).')
		print('\t\t- Type [3] to find the vertice: R(xR,yR) triangle(PQR).\n')
		
		self.number4 = vector.enterIntegerData()
		
		if self.number4 == 1:
			verticestriangle.find_verticeP()
		elif self.number4 == 2:
			verticestriangle.find_verticeQ()
		elif self.number4 == 3:
			verticestriangle.find_verticeR()
		else:
			textstring3.no_OptionKey()
		return
								
verticestriangle = VerticesTriangle()

class AddSubtraction:
	def __init__(self, addition = [], subtraction = [], vectorA = 0, vectorB = 0, ):
		self.vectorA = vectorA
		self.vectorB = vectorB
		self.addition = addition
		self.subtraction = subtraction 
		
	def getadd_subtraction(self):
		self.vectorA = compvector.getcomponentvectorA()
		self.vectorB = compvector.getcomponentvectorB()
		print('\n\t-- The [vectorA]: vectorA', self.vectorA)
		print('\t-- The [vectorB]: vectorB', self.vectorB, '\n')
		for j in range(0,2):
			self.add = ( self.vectorA[j] + self.vectorB[j] )
			self.addition.append(self.add)
			self.subt = ( self.vectorA[j] - self.vectorB[j] )
			self.subtraction.append(self.subt)
			
		answer.view_solution()
		print('\t- The [Addition]: vector[a+b]:',self.addition)
		print('\t- The [Subtraction]: vector[a-b]:',self.subtraction,'\n')
		return 
		
addsubtraction = AddSubtraction()

class FormaComponent:
	def __init__(self, A0 = 0, A1 = 0, Addition = 0, coeffic1 = 0, coeffic2 = 0, lengthA = 0, lengthS = 0, number3 = 0,
	num1prod = 0, num2prod = 0, Subtraction = 0, S0 = 0, S1 = 0, vectorA = 0, vectorB = 0, vectorAcoeffic1 = 0, 
	vectorBcoeffic2 = 0, termA = 0, termS = 0 ):
		self.Addition = Addition 
		self.A0 = A0
		self.A1 = A1
		self.lengthA = lengthA
		self.coeffic1 = coeffic1
		self.coeffic2 = coeffic2
		
		self.number3 = number3
		self.num1prod = num1prod
		self.num2prod = num2prod
		self.Subtraction = Subtraction 
		self.S0 = S0
		self.S1 = S1
		self.lengthS = lengthS
		
		self.termA = termA
		self.termS = termS  
		self.vectorA = vectorA 
		self.vectorB = vectorB
		
		self.vectorAcoeffic1 = vectorAcoeffic1
		self.vectorBcoeffic2 = vectorBcoeffic2 
		
	def getforma_component(self):
		print('\n\t- To enter the [Components] of the [vectors] type [1].')
		print('\t- To introduce the [Coordinates] of the [points] type [2].')
		self.number3 = vector.enterIntegerData()
		
		if self.number3 == 1:
			print('\n\t- Provide the [Components] of the [vectors]: vectorA and vectorB.')
			self.vectorA = compvector.getcomponentvectorA()
			self.vectorB = compvector.getcomponentvectorB()
			
		elif self.number3 == 2:
			print('\n\t- Give the [Coordinates] of the [givens points: P and Q].')
			findcoordpq.findcoord_pointPQ()
			self.vectorA = findvectorA.find_vectorA()
			
			print('\t- Enter the [Coordinates] of the [givens points: P and R].')
			findcoordpr.findcoord_pointPR()
			self.vectorB = findvectorB.find_vectorB()
			
		print('\n\t-- The [vectorA]: vectorA', self.vectorA)
		print('\t-- The [vectorB]: vectorB', self.vectorB, '\n')
			
		print('\t- Enter with new [value] to the (1º)[coefficient]?')
		self.coeffic1 = introduce.enterRealData()
		print('\t- Give the new [value] to the (2º)[coefficient]?')
		self.coeffic2 = introduce.enterRealData()
			
		self.vectorAcoeffic1 = []
		self.vectorBcoeffic2 = []
			
		for p in range(0,2):
			self.num1prod = self.vectorA[p] * self.coeffic1
			self.vectorAcoeffic1.append(self.num1prod)
			self.num2prod = self.vectorB[p] * self.coeffic2
			self.vectorBcoeffic2.append(self.num2prod)
			
		answer.view_solution()
		print(' + The [product]: (coeffic1)*[vectorA] = coeffic1*vectorA',self.vectorAcoeffic1)
		print(' + The [product]: (coeffic2)*[vectorB] = coeffic2*vectorB',self.vectorBcoeffic2,'\n')
		
		self.Addition = []
		self.Subtraction = []
		
		for q in range(0,2):
			self.termA = ( self.vectorAcoeffic1[q] + self.vectorBcoeffic2[q] )
			self.Addition.append(self.termA)
			self.termS = ( self.vectorAcoeffic1[q] - self.vectorBcoeffic2[q] )
			self.Subtraction.append(self.termS)
			
		print(' -- The [Addition] = (coeffic1)vectorA+(coeffic2)vectorB', self.Addition)
		print(' -- The [Subtraction] = (coeffic1)vectorA-(coeffic2)vectorB', self.Subtraction,'\n')
		
		self.A0 = self.Addition[0]
		magnitudebivector.x = self.A0
		self.A1 = self.Addition[1]
		magnitudebivector.y = self.A1
		self.lengthA = magnitudebivector.magbivector()
		self.S0 = self.Subtraction[0]
		magnitudebivector.x = self.S0
		self.S1 = self.Subtraction[1]
		magnitudebivector.y = self.S1
		self.lengthS = magnitudebivector.magbivector()
		print(f' -- The [length] of the |vectorAddition| is: {self.lengthA:<.2f}')
		print(f' -- The [length] of the |vectorSubtraction| is: {self.lengthS:<.2f}','\n')
			
		return

formacomponent = FormaComponent()





                        
                        
                        

                        
                                
      
        
