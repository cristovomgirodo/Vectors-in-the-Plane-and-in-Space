###################################################################################################
#
# The [runVector3d.py] program will run various Classs inside the [Vector3dClassModule.py] module.
# 
#===================================================
#
# *  The [Vector3dClassModule.py] module
#
#===================================================
#
# -----------------------------------------------
# Begin date: 20250102
# Development - Version: 2.0 (Alpha)
# -----------------------------------------------
#
#***************************************************
#
# -----------------------------------------------
# Begin date: 20250503
# -----------------------------------------------
# Development - Version: 2.0 (Beta)
# -----------------------------------------------
#
#***************************************************
#
#===================================================
#			[ END DEVELOPMENT ]
#===================================================
#
# * [Date]: 20250523
# -----------------------------------------------
# * Release -- Version: 2.0 (Stable)
# -----------------------------------------------
# * Developed by Cristovom A. Girodo
# -----------------------------------------------
#===================================================
#
###################################################################################################

import math

class VectorNumber:
	def __init__(self, coeffic = 0, x = 0):
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
					print('\n\t*[ NO TYPE AN [NEGATIVE INTEGER NUMBER] OR EQUAL [ZERO]--Ok! ]*\n')
					self.coeffic = integerdata()
				return self.coeffic
			
			except ValueError as err:
				print('\n\t _=§=_')
				print('\t  º<º  [Warning!]:',err)
				print('\t  [~]  [ TYPE AN [NEW POSITIVE INTEGER NUMBER ]')
				print('\t       [ IN NEXT INSTRUCTION -- OK! ]\n')
				
vector = VectorNumber()

class Select_an_Option:
	def __init__(self, coefficient = 0, number = 0):
		self.coefficient = coefficient
		self.number = number
		
	def provide_Option(self):
		while True:
			try:
				def integerdata():
					self.coefficient = int(input("\t(º_º) Give the [new] value? "))
					return self.coefficient
				self.number = integerdata()
					
				while self.number < 0 or self.number == 0 or self.number >= 3:
					print('\n\t   *[ NO TYPE: ]*')
					print('\t  **[ ANY [NEGATIVE INTEGER NUMBER] OR EQUAL [ZERO] OR ]**')
					print('\t ***[ ANY [POSITIVE INTEGER NUMBER] BIGGER THAN OR EQUAL [THREE]--Ok! ]***\n')
					self.number = integerdata()
					
				return self.number
				
			except ValueError as err:
				print('\n\t _===_')
				print('\t  º>º  [Warning!]:',err)
				print('\t  [~]  [ TYPE AN [NEW POSITIVE INTEGER NUMBER ]')
				print('\t       [ IN NEXT INSTRUCTION -- OK! ]\n')
				
selectOption = Select_an_Option()

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

class Answer:
	'''View the solution'''
	def view_solution(self):
		print('\n\t *[Answer]*\n')
		
answer = Answer()

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
		print('\t--------------------------------------------------------------------------------------------------------------')
		print('\t  *[ NO EXIST THE TRIANGLE(PQR) WITH THE [COORDINATES] OF THE GIVEN POINTS: P(xP,yP,zP), Q(xQ,yQ,zQ), AND ]*')
		print('\t  *[ R(xR,yR,zR) -- OK! BY [THEOREM OF THE PLANE GEOMETRY] THE BUILDING OF THE TRIANGLE(PQR) USING THE ]*')
		print('\t  *[ COMPASS AND RULER ONLY IS POSSIBLE WHEN: ]*\n')
		print('\t\t\t**[ sideA < sideB + sideC ]** and')
		print('\t\t\t**[ sideB < sideA + sideC ]** and')
		print('\t\t\t**[ sideC < sideA + sideB ]**\n')
		print('\t--------------------------------------------------------------------------------------------------------------\n')
		
textstring2 = TextString2()

class TextString3:
	'''Instructions of the processing after type error option '''
	def error_option(self):
		print('\n\t*[You no type a of the previous options!]*')
		print('\t*[ Run the program again--Ok! ]*\n')
		
textstring3 = TextString3()

class PointCoordinates3d:
	def __init__(self, number1 = 1, pointP = [], pointQ = [], pointR = [], pointS = [], pointK = [], pointL = [],
	pointM = [], PointP = (), PointQ = (), PointR = (), PointS = (),  u = 0, v = 0, w = 0):
		self.number1 = number1
		self.pointP = pointP
		self.pointQ = pointQ
		self.pointR = pointR
		self.pointS = pointS
		
		self.pointK = pointK
		self.pointL = pointL
		self.pointM = pointM
		
		self.PointP = PointP
		self.PointQ = PointQ
		self.PointR = PointR
		self.Points = PointS
		
		self.u = u
		self.v = v
		self.w = w
		
	def getpointcoordinates3d(self):
		'''Will type the given [Coordinates] o the points: P, Q, R, S, K, L and M'''
		if self.number1 == 1:
			print('\n\t-- Enter the [coordinates]: (xP, yP, zP) of the (point P)? ')
			for i in range(1, 4):
				if i == 1:
					print(f"\n\t* Introduce the {i}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointP.append(self.u)
				elif i == 2:
					print(f"\n\t* Enter with the {i}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointP.append(self.v)
				elif i == 3:
					print(f"\n\t* Provide the {i}º[Coordinate(z)].")
					self.w = introduce.enterRealData()
					self.pointP.append(self.w)
					return self.pointP
					
		elif self.number1 == 2:
			print('\n\t-- Introduce the [coordinates]: (xQ, yQ, zQ) of the (point Q)? ')
			for j in range(1, 4):
				if j == 1:
					print(f"\n\t* Introduce the {j}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointQ.append(self.u)
				elif j == 2:
					print(f"\n\t* Enter with the {j}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointQ.append(self.v)
				elif j == 3:
					print(f"\n\t* Provide the {j}º[Coordinate(z)].")
					self.w = introduce.enterRealData()
					self.pointQ.append(self.w)
					return self.pointQ
					
		elif self.number1 == 3:
			print('\n\t-- Provide the [coordinates]: (xR, yR, zR) of the (point R)? ')
			for k in range(1, 4):
				if k == 1:
					print(f"\n\t* Introduce the {k}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointR.append(self.u)
				elif k == 2:
					print(f"\n\t* Enter with the {k}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointR.append(self.v)
				elif k == 3:
					print(f"\n\t* Provide the {k}º[Coordinate(z)].")
					self.w = introduce.enterRealData()
					self.pointR.append(self.w)
					return self.pointR
					
		elif self.number1 == 4:
			print('\n\t-- Give the [coordinates]: (xS, yS, zS) of the (point S)? ')
			for l in range(1, 4):
				if l == 1:
					print(f"\n\t* Introduce the {l}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointS.append(self.u)
				elif l == 2:
					print(f"\n\t* Enter with the {l}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointS.append(self.v)
				elif l == 3:
					print(f"\n\t* Provide the {l}º[Coordinate(z)].")
					self.w = introduce.enterRealData()
					self.pointS.append(self.w)
					return self.pointS
					
		elif self.number1 == 5:
			print('\n\t-- Give the [coordinates]: (xK, yK, zK) of the (Mid_point K)? ')
			for d in range(1, 4):
				if d == 1:
					print(f"\n\t* Introduce the {d}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointK.append(self.u)
				elif d == 2:
					print(f"\n\t* Enter with the {d}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointK.append(self.v)
				elif d == 3:
					print(f"\n\t* Provide the {d}º[Coordinate(z)].")
					self.w = introduce.enterRealData()
					self.pointK.append(self.w)
					return self.pointK
					
		elif self.number1 == 6:
			print('\n\t-- Give the [coordinates]: (xL, yL, zL) of the (Mid_point L)? ')
			for e in range(1, 4):
				if e == 1:
					print(f"\n\t* Introduce the {e}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointL.append(self.u)
				elif e == 2:
					print(f"\n\t* Enter with the {e}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointL.append(self.v)
				elif e == 3:
					print(f"\n\t* Provide the {e}º[Coordinate(z)].")
					self.w = introduce.enterRealData()
					self.pointL.append(self.w)
					return self.pointL
					
		elif self.number1 == 7:
			print('\n\t-- Give the [coordinates]: (xM, yM, zM) of the (Mid_point M)? ')
			for f in range(1, 4):
				if f == 1:
					print(f"\n\t* Introduce the {f}º[Coordinate(x)].")
					self.u = introduce.enterRealData()
					self.pointM.append(self.u)
				elif f == 2:
					print(f"\n\t* Enter with the {f}º[Coordinate(y)].")
					self.v = introduce.enterRealData()
					self.pointM.append(self.v)
				elif f == 3:
					print(f"\n\t* Provide the {f}º[Coordinate(z)].")
					self.w = introduce.enterRealData()
					self.pointM.append(self.w)
					return self.pointM

pointcoordinates3d = PointCoordinates3d()

class CompVector:
	'''Will type the given [Components] of the [Vectors]: vectorA, vectorB, vectorC, and vectorD'''
	def __init__(self, u = 0, v = 0, w = 0, vectorComponents = [], vectorComponentsA = [], vectorComponentsB = [],
	vectorComponentsC = [], vectorComponentsD = [], vectA = 0, vectB = 0, vectC = 0, vectD = 0):
		self.u = u
		self.v = v
		self.w = w
		self.vectorComponents = vectorComponents
		self.vectorComponentsA = vectorComponentsA
		self.vectorComponentsB = vectorComponentsB 
		self.vectorComponentsC = vectorComponentsC
		self.vectorComponentsD = vectorComponentsD
		self.vectA = vectA
		self.vectB = vectB 
		self.vectC = vectC
		self.vectD = vectD 
		
	def getcomponent3dvectorA(self):
		print('\n\t- Attribute the [Components] of the [1º vectorA].')
		for h in range(1,4):
			if h == 1:
				print(f'\n\t- Enter the [coefficient] of the [Component: (i) or (a1)]?')
				self.u = introduce.enterRealData()
				self.vectorComponentsA.append(self.u)
			elif h == 2:
				print(f'\n\t- Introduce the [coefficient] of the [Component: (j) or (a2)]?')
				self.v = introduce.enterRealData()
				self.vectorComponentsA.append(self.v)
			elif h == 3:
				print(f'\n\t- Give the [coefficient] of the [Component: (k) or (a3)]?')
				self.w = introduce.enterRealData()
				self.vectorComponentsA.append(self.w)
				return self.vectorComponentsA
				
	def getcomponent3dvectorB(self):
		print('\n\t- Provide the [Components] of the [2º vectorB].')
		for j in range(1,4):
			if j == 1:
				print(f'\n\t- Enter the [coefficient] of the [Component: (i) or (b1)]?')
				self.u = introduce.enterRealData()
				self.vectorComponentsB.append(self.u)
			elif j == 2:
				print(f'\n\t- Introduce the [coefficient] of the [Component: (j) or (b2)]?')
				self.v = introduce.enterRealData()
				self.vectorComponentsB.append(self.v)
			elif j == 3:
				print(f'\n\t- Give the [coefficient] of the [Component: (k) or (b3)]?')
				self.w = introduce.enterRealData()
				self.vectorComponentsB.append(self.w)
				return self.vectorComponentsB
	
	def getcomponent3dvectorC(self):
		print('\n\t- Give the [Components] of the [3º vectorC].')
		for k in range(1,4):
			if k == 1:
				print(f'\n\t- Enter the [coefficient] of the [Component: (i) or (c1)]?')
				self.u = introduce.enterRealData()
				self.vectorComponentsC.append(self.u)
			elif k == 2:
				print(f'\n\t- Introduce the [coefficient] of the [Component: (j) or (c2)]?')
				self.v = introduce.enterRealData()
				self.vectorComponentsC.append(self.v)
			elif k == 3:
				print(f'\n\t- Give the [coefficient] of the [Component: (k) or (c3)]?')
				self.w = introduce.enterRealData()
				self.vectorComponentsC.append(self.w)
				return self.vectorComponentsC
				
	def getcomponent3dvectorD(self):
		print('\n\t- Give the [Components] of the [4º vectorD].')
		for l in range(1,4):
			if l == 1:
				print(f'\n\t- Enter the [coefficient] of the [Component: (i) or (c1)]?')
				self.u = introduce.enterRealData()
				self.vectorComponentsD.append(self.u)
			elif l == 2:
				print(f'\n\t- Introduce the [coefficient] of the [Component: (j) or (c2)]?')
				self.v = introduce.enterRealData()
				self.vectorComponentsD.append(self.v)
			elif l == 3:
				print(f'\n\t- Give the [coefficient] of the [Component: (k) or (c3)]?')
				self.w = introduce.enterRealData()
				self.vectorComponentsD.append(self.w)
				return self.vectorComponentsD
				
compvector = CompVector()

class Middle3dPoint:
	'''Will determine the midpoints: K, L, M, and N between points: P, Q, R, and S'''
	def __init__(self, coord = 0, number = 0, pointP = [], pointQ = [], pointR = [], pointS = [], PointP = [],
	PointQ = [], PointR = [], PointS = [], vectorMidPointK = [], vectorMidPointL = [], vectorMidPointM = [],
	vectorMidPointN = [], xK = 0, yK = 0, zK = 0, xL = 0, yL = 0, zL = 0, xM = 0, yM = 0, zM = 0, xN = 0, yN = 0,
	zN = 0, xP = 0, yP = 0, zP = 0, xQ = 0, yQ = 0, zQ = 0, xR = 0, yR = 0, zR = 0, xS = 0, yS = 0, zS = 0):
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
		self.zK = zK
		
		self.xL = xL
		self.yL = yL
		self.zL = zL
		
		self.xM = xM
		self.yM = yM
		self.zM = zM
		
		self.xN = xN
		self.yN = yN
		self.zN = zN
		
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
		self.xS = xS
		self.yS = yS
		self.zS = zS
		
	def getmiddle3d_point(self):
		if self.number == 1:
			# pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 1
			self.pointP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 2
			self.pointQ = pointcoordinates3d.getpointcoordinates3d()
			
			for j in range(0,3):
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
				elif j == 2:
					self.zK = self.vectorMidPointK[j]
					self.zP = self.pointP[j]
					self.zQ = self.pointQ[j]
					
			self.PointK = (self.xK,self.yK,self.zK )
			self.PointP = (self.xP,self.yP,self.zP )
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\t- The (Point Q): Q',self.PointQ)
			answer.view_solution()
			print('\t-- The MidPoint_K(xK,yK,zK):', self.PointK)
			
		elif self.number == 2:
			pointcoordinates3d.number1 = 1
			self.pointP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.pointR = pointcoordinates3d.getpointcoordinates3d()
			
			for j in range(0,3):
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
				elif j == 2:
					self.zL = self.vectorMidPointL[j]
					self.zP = self.pointP[j]
					self.zR = self.pointR[j]
					
			self.PointL = (self.xL,self.yL,self.zL)
			self.PointP = (self.xP,self.yP,self.zP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.PointR)
			answer.view_solution()
			print('\t-- The MidPoint_L(xL,yL,zL):', self.PointL)
			
		elif self.number == 3:
			pointcoordinates3d.number1 = 2
			self.pointQ = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.pointR = pointcoordinates3d.getpointcoordinates3d()
			
			for j in range(0,3):
				self.coord = ( self.pointQ[j] + self.pointR[j] ) / 2
				self.vectorMidPointM.append(self.coord)
				if j == 0:
					self.xM = self.vectorMidPointM[j]
					self.xQ = self.pointQ[j]
					self.xR = self.pointR[j]
				elif j == 1:
					self.yM = self.vectorMidPointM[j]
					self.yQ = self.pointQ[j]
					self.yR = self.pointR[j]
				elif j == 2:
					self.zM = self.vectorMidPointM[j]
					self.zQ = self.pointQ[j]
					self.zR = self.pointR[j]
			
			self.PointM = (self.xM,self.yM,self.zM)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\n\t- The (Point Q): Q',self.PointQ)
			self.PointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.PointR)
			answer.view_solution()
			print('\t-- The MidPoint_M(xM,yM,zM):', self.PointM)
			
		elif self.number == 4:
			pointcoordinates3d.number1 = 4
			self.pointS = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 1
			self.pointP = pointcoordinates3d.getpointcoordinates3d()
			for j in range(0,3):
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
				elif j == 2:
					self.zN = self.vectorMidPointN[j]
					self.zS = self.pointS[j]
					self.zP = self.pointP[j]
					
			self.PointN = (self.xN,self.yN,self.zN )
			self.pointS = (self.xS,self.yS,self.zS)
			print('\n\t- The (Point S): S',self.pointS)
			self.pointP = (self.xP,self.yP,self.zP)
			print('\t- The (Point P): P',self.pointP)
			answer.view_solution()
			print('\t-- The MidPoint_N(xN,yN,zN):', self.PointN)
			
		elif self.number == 5:
			pointcoordinates3d.number1 = 2
			self.pointQ = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.pointR = pointcoordinates3d.getpointcoordinates3d()
			for j in range(0,3):
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
				elif j == 2:
					self.zL = self.vectorMidPointL[j]
					self.zQ = self.pointQ[j]
					self.zR = self.pointR[j]
					
			self.PointL = (self.xL,self.yL,self.zL)
			self.pointQ = (self.xQ,self.yQ,self.zQ)
			print('\n\t- The (Point Q): Q',self.pointQ)
			self.pointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.pointR)
			answer.view_solution()
			print('\t-- The MidPoint_L(xL,yL,zL):', self.PointL)
			
		elif self.number == 6:
			pointcoordinates3d.number1 = 3
			self.pointR = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 4
			self.pointS = pointcoordinates3d.getpointcoordinates3d()
			for j in range(0,3):
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
				elif j == 2:
					self.zM = self.vectorMidPointM[j]
					self.zR = self.pointR[j]
					self.zS = self.pointS[j]
					
			self.PointM = (self.xM,self.yM,self.zM)
			self.pointR = (self.xR,self.yR,self.zR)
			print('\n\t- The (Point R): R',self.pointR)
			self.pointS = (self.xS,self.yS,self.zS)
			print('\t- The (Point S): S',self.pointS)
			answer.view_solution()
			print('\t-- The MidPoint_M(xM,yM,zM):', self.PointM)
		# test - ok!
		return
			
middle3dpoint = Middle3dPoint()

class SubQdRoot:
	def __init__(self, cat = 0, height = 0, hip = 0):
		self.cat = cat
		self.height = height
		self.hip = hip
		
	def getheight(self):	
		self.height = math.sqrt( math.pow(self.hip,2) - math.pow(self.cat,2) )
		return self.height

subqdroot = SubQdRoot() 

class MagnitudeBiVector:
	def __init__(self, magnitude = 0, x = 0, y = 0):
		self.magnitude = 0
		self.x = x
		self.y = y
		
	def magbivector(self):
		self.magnitude = math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))
		return self.magnitude
		
magnitudebivector = MagnitudeBiVector()

class MagnitudeTriVector:
	def __init__(self, magnitude = 0, x = 0, y = 0, z = 0):
		self.magnitude = 0
		self.x = x
		self.y = y
		self.z = z
		
	def magtrivector(self):
		self.magnitude = math.sqrt( math.pow(self.x,2) + math.pow(self.y,2) + math.pow(self.z,2) )
		return self.magnitude
		
magnitudeTriVector = MagnitudeTriVector()

class Medians3d:
	def __init__(self, compX = 0, compY = 0, compZ = 0,medianPM = 0, medianQL = 0, medianRK = 0, xK = 0, yK = 0,
	zK = 0, xL = 0, yL = 0, zL = 0, xM = 0, yM = 0, zM = 0, xP = 0, yP = 0, zP = 0, xQ = 0, yQ = 0, zQ = 0, xR = 0,
	yR = 0, zR = 0, PointM = [], pointP = 0, PointL = [], pointQ = 0, PointK = [], pointR = 0, vectorPM = [],
	vectorQL = [], vectorRK = [] ):
		
		self.compX = compX 
		self.compY = compY
		self.compZ = compZ
		  
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
		self.zK = zK
		
		self.xL = xL 
		self.yL = yL
		self.zL = zL
		
		self.xM = xM 
		self.yM = yM
		self.zM = zM
		
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
	def findMedianPM(self):
		middle3dpoint.number = 3
		middle3dpoint.getmiddle3d_point()
		
		# Access the coordinates: xM, yM and zM of the Class MidPoint_M.
		self.xM = middle3dpoint.xM
		self.PointM.append(self.xM)
		self.yM = middle3dpoint.yM
		self.PointM.append(self.yM)
		self.zM = middle3dpoint.zM
		self.PointM.append(self.zM)
		
		pointcoordinates3d.number1 = 1
		self.pointP = pointcoordinates3d.getpointcoordinates3d()
		
		for h in range (0, 3):
			self.compVectorPM = self.PointM[h] - self.pointP[h]
			if h == 0:
				self.compX = self.compVectorPM
			elif h == 1:
				self.compY = self.compVectorPM
			elif h == 2:
				self.compZ = self.compVectorPM		
			self.vectorPM.append(self.compVectorPM)
			
		magnitudeTriVector.x = self.compX
		magnitudeTriVector.y = self.compY
		magnitudeTriVector.z = self.compZ
		self.medianPM = magnitudeTriVector.magtrivector()
		answer.view_solution()
		print('\t-- The terms of the [vectorPM]:', self.vectorPM)
		print(f'\t-- The [median: PM] finded is {self.medianPM:<.2f}','\n')
		return
		
	def findMedianQL(self):
		middle3dpoint.number = 2
		middle3dpoint.getmiddle3d_point()
		
		# Access the coordinates: xL, yL and zL of the Class MidPoint_L.
		self.xL = middle3dpoint.xL
		self.PointL.append(self.xL)
		self.yL = middle3dpoint.yL
		self.PointL.append(self.yL)
		self.zL = middle3dpoint.zL
		self.PointL.append(self.zL)
		
		pointcoordinates3d.number1 = 2
		self.pointQ = pointcoordinates3d.getpointcoordinates3d()
		
		for h in range (0, 3):
			self.compVectorQL = self.PointL[h] - self.pointQ[h]
			if h == 0:
				self.compX = self.compVectorQL
			elif h == 1:
				self.compY = self.compVectorQL
			elif h == 2:
				self.compZ = self.compVectorQL	
			self.vectorQL.append(self.compVectorQL)
			
		# magnitudebivector.magbivector()
		magnitudeTriVector.x = self.compX 
		magnitudeTriVector.y = self.compY
		magnitudeTriVector.z = self.compZ
		self.medianQL = magnitudeTriVector.magtrivector()
		answer.view_solution()
		print('\t-- The terms of the [vectorQL]:', self.vectorQL)
		print(f'\t-- The [median: QL] finded is {self.medianQL:<.2f}','\n')
		return
		
	def findMedianRK(self):
		middle3dpoint.number = 1
		middle3dpoint.getmiddle3d_point()
		# Access the coordinates: xK, yK and zK of the Class MidPoint_K.
		self.xK = middle3dpoint.xK
		self.PointK.append(self.xK)
		self.yK = middle3dpoint.yK
		self.PointK.append(self.yK)
		self.zK = middle3dpoint.zK
		self.PointK.append(self.zK)
		
		pointcoordinates3d.number1 = 3
		self.pointR = pointcoordinates3d.getpointcoordinates3d()
		
		for h in range (0, 3):
			self.compVectorRK = self.PointK[h] - self.pointR[h]
			if h == 0:
				self.compX = self.compVectorRK
			elif h == 1:
				self.compY = self.compVectorRK
			elif h == 2:
				self.compZ = self.compVectorRK		
			self.vectorRK.append(self.compVectorRK)
			
		# magnitudebivector.magbivector()
		magnitudeTriVector.x = self.compX 
		magnitudeTriVector.y = self.compY
		magnitudeTriVector.z = self.compZ
		self.medianRK = magnitudeTriVector.magtrivector()
		answer.view_solution()
		print('\t-- The terms of the [vectorRK]:', self.vectorRK)
		print(f'\t-- The [median: RK] finded is {self.medianRK:<.2f}','\n')
		return
		
medians3d = Medians3d()

class FindTheMedians3d:
	'''Determine the medians of the triangle(PQR)'''
	def __init__(self, number2 = 0):
		self.number2 = number2
		
	def get_the_medians(self):
		print('\t\t- Key [1] to find the new medianPM or')
		print('\t\t- Key [2] to find the new medianQL or')
		print('\t\t- Key [3] to find the new medianRK.')
		print('\t\t- Key [4] to find all the medians: PM, QP, and')
		print('\t\t  RK of a TrianglePQR.\n')
		self.number2 = vector.enterIntegerData()
		
		if self.number2 == 1:
			medians3d.findMedianPM()
		elif self.number2 == 2:
			medians3d.findMedianQL()
		elif self.number2 == 3:
			medians3d.findMedianRK()
		elif self.number2 == 4:
			medians3d.findMedianPM()
			medians3d.findMedianQL()
			medians3d.findMedianRK()

		else:
			textstring3.error_option()
			return

findthemedians3d = FindTheMedians3d()

class CentricG3d:
	def __init__(self, xG = 0, yG = 0, zG = 0, xP = 0, yP = 0, zP = 0, xQ = 0, yQ = 0, zQ = 0, xR = 0, yR = 0, zR = 0, 
	baricG = 0, pointP = [], pointQ = [], pointR = [], PointP = (), PointQ = (), PointR = ()):
		self.baricG =  baricG
		self.xG = xG
		self.yG = yG
		self.zG = zG
		 
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
		self.pointP = pointP
		self.pointQ = pointQ 
		self.pointR = pointR
		
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		
	def find_centricG_3d(self):
		pointcoordinates3d.number1 = 1
		self.pointP = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 2
		self.pointQ = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 3
		self.pointR = pointcoordinates3d.getpointcoordinates3d()
		
		self.xP = self.pointP[0]
		self.xQ = self.pointQ[0]
		self.xR = self.pointR[0]
		
		self.yP = self.pointP[1]
		self.yQ = self.pointQ[1]
		self.yR = self.pointR[1]
		
		self.zP = self.pointP[2]
		self.zQ = self.pointQ[2]
		self.zR = self.pointR[2]
		
		self.xG = ( self.xP + self.xQ + self.xR ) / 3
		self.yG = ( self.yP + self.yQ + self.yR ) / 3
		self.zG = ( self.zP + self.zQ + self.zR ) / 3
		
		self.PointP = (self.xP,self.yP,self.zP)
		print('\n\t- The (Point P): P',self.PointP)
		self.PointQ = (self.xQ,self.yQ,self.zQ)
		print('\t- The (Point Q): Q',self.PointQ)
		self.PointR = (self.xR,self.yR,self.zR)
		print('\t- The (Point R): R',self.PointR)
		answer.view_solution()
		print('\t-- The [Coordenates] of the [CentroidG_3d(xG,yG,zG)] in the Triangle(PQR):')
		print(f'\n\t-- The [Coordinate]: xG is {self.xG:<.2f}')
		print(f'\t-- The [Coordinate]: yG is {self.yG:<.2f}')
		print(f'\t-- The [Coordinate]: zG is {self.zG:<.2f}','\n')
				
centricg3d = CentricG3d()

class CrossProduct:
	"""
	Find the Cross Product
	Given all the [coomponents]: a1, a2, a3, b1, b2, and b3 of two [vectors]: vectorA and vectorB or all the   
	[coordinates]: xP, yP, zP, xQ, yQ, zQ, xR, yR, and zR of the points: P, Q, and R that will represent the 
	[Vectors]: vectorA = vectorPQ, and vectorB = vectorPR.
	    
	                    |  i   j   k |
		vectorAxB = | a1  a2  a3 |  
	                    | b1  b2  b3 |  
	                                           
	Will calculate the value of the [area A of a given parallelogramPQRS] using A = |vectorAxB|
	as also will determine the value of the [area S of a trianglePQR] with S = |vectorAxB| / 2 or
	will get the value of the ThetaSine using [ Thetasine = normAxB / normproduct ].
	"""
	
	def __init__(self, alpha = 0, a1 = 0, a2 = 0, a3 = 0, add = 0, Area = 0, b1 = 0, b2 = 0, b3 = 0,  Area_S = 0,
	 c1 = 0, c2 = 0, c3 = 0, comp0 = 0, comp1 = 0, coordP = [], coordQ = [], coordR = [], coordS = [], height_h = 0,
	 height_Parallelogram = 0, number = 0, number1 = 0, number2 = 0, normA = 0, normB = 0, modAxBproduct = 0,
	 vectorAB = 0, Perimeter = 0, PointP = 0, PointQ = 0,  PointR = 0, vectorA = 0, vectorB = 0, vectorC = 0,
	 vectorQR = [], vectorPQ = [], vectorQP = [], vectorPR = [], radianAngle = 0, radianAlpha = 0, radianTheta = 0,
	 sine = 0, sineAlphaRadians = 0, sideA = 0, sideB = 0, sideC = 0, term = 0, term0 = 0, term1 = 0, term2 = 0,
	 theta = 0, thetaAngle_degree = 0, xP = 0, xQ = 0,xR = 0, yP = 0, yQ = 0, yR = 0,  zP = 0, zQ = 0, zR = 0, Cx = 0,
	 Cy = 0, Cz = 0, vectorAxB = [], normVectorAxB = 0 ):
		
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.add = add
		self.alpha = alpha
		self.theta = theta
		self.Area = Area
		self.Area_S = Area_S
		
		self.b1 = b1
		self.b2 = b2
		self.b3 = b3
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		
		self.comp0 = comp0
		self.comp1 = comp1
		
		self.coordP = coordP
		self.coordQ = coordQ
		self.coordR = coordR
		
		self.height_Parallelogram = height_Parallelogram
		self.height_h = height_h
		
		self.number = number
		self.number1 = number1
		self.number2 = number2 
	
		self.normA = normA
		self.normB = normB
		
		self.modAxBproduct = modAxBproduct
		self.Perimeter = Perimeter
		
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		
		# Attributeused in classes
		self.radianAngle = radianAngle
		self.radianTheta = radianTheta
		
		self.radianAlpha = radianAlpha
		self.sineAlphaRadians = sineAlphaRadians
		self.sine = sine
		
		self.sideA = sideA 
		self.sideB = sideB 
		self.sideC = sideC
		
		self.vectorA = vectorA
		self.vectorB = vectorB
		self.vectorC = vectorC
		
		self.term = term
		self.term0 = term0
		self.term1 = term1
		self.term2 = term2 
		
		self.xP = xP
		self.xQ = xQ
		self.xR = xR
		
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		
		self.zP = zP 
		self.zQ = zQ
		self.zR = zR
		
		# new attribute of class
		self.Cx = Cx
		self.Cy = Cy
		self.Cz = Cx
		
		self.vectorAxB = vectorAxB
		self.normVectorAxB = normVectorAxB
		self.thetaAngle_degree = thetaAngle_degree 
		
		self.vectorPR = vectorPR
		self.vectorQR = vectorQR
		self.vectorQP = vectorQP
		
	def findCrossProduct(self):
		# Given the [coordinates] of the vertice points: P, Q, and R of a trianglePQR or
		# of a ParallelogramPQRS or the given [components] of [two vectors]: vectorA or vectorB.
		self.xP = self.xQ = self.xR = 0
		self.yP = self.yQ = self.yR = 0
		self.zP = self.zQ = self.zR = 0
		
		print('\n\t\t*[NEW INSTRUCTIONS]*\n')
		print('\t* Type [1] to enter new given [Coordinate] points: P, Q, and R or')
		print('\t* Type [2] and provide the given [Components] of [two vectors]: vectorA and vectorB. \n')
		number = selectOption.provide_Option()
		find_crossproduct.number = number
		
		if self.number == 1:
			pointcoordinates3d.number1 = 1
			self.coordP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 2
			self.coordQ = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.coordR = pointcoordinates3d.getpointcoordinates3d()
			
			for t in range(0,3):
				if t == 0:
					self.xP = self.coordP[t]
					self.xQ = self.coordQ[t]
					self.xR = self.coordR[t]
					
				elif t == 1:
					self.yP = self.coordP[t]
					self.yQ = self.coordQ[t]
					self.yR = self.coordR[t]
					
				elif t == 2:
					self.zP = self.coordP[t]
					self.zQ = self.coordQ[t]
					self.zR = self.coordR[t]
					
			self.PointP = (self.xP,self.yP,self.zP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\t- The (Point Q): Q',self.PointQ)
			self.PointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.PointR)
			# answer.view_solution()
			
			self.vectorQR = []
			self.vectorQP = []
			
			for h in range (0,3):
				self.comp0 = self.coordR[h] - self.coordQ[h]
				self.vectorQR.append(self.comp0)
				self.comp1 = self.coordP[h] - self.coordQ[h]
				self.vectorQP.append(self.comp1)
				
			self.vectorA = self.vectorQR
			self.vectorB = self.vectorQP
			
		elif self.number == 2:
			# compvector.getcomponent3dvectorA() 
			self.vectorA = compvector.getcomponent3dvectorA()
			self.vectorB = compvector.getcomponent3dvectorB()
			
		answer.view_solution()
		# self.vectorA = self.vectorQR
		print('\t-- The [vectorA]: vectorA',self.vectorA)
		# self.vectorB = self.vectorQP
		print('\t-- The [vectorB]: vectorB',self.vectorB)
		
		# The area S of the trianglePQR
		# The [components] Vector: A and B
		self.a1 = self.vectorA[0]
		self.a2 = self.vectorA[1]
		self.a3 = self.vectorA[2]
		magnitudeTriVector.x = self.a1
		magnitudeTriVector.y = self.a2
		magnitudeTriVector.z = self.a3
		self.normA = magnitudeTriVector.magtrivector()
		
		self.b1 = self.vectorB[0]
		self.b2 = self.vectorB[1]
		self.b3 = self.vectorB[2]
		
		magnitudeTriVector.x = self.b1
		magnitudeTriVector.y = self.b2
		magnitudeTriVector.z = self.b3
		self.normB = magnitudeTriVector.magtrivector()
		
		# find the Cross Product(AxB)
		self.Cx = ( ( self.vectorA[1] * self.vectorB[2] ) - ( self.vectorA[2] * self.vectorB[1] ) )
		self.vectorAxB.append(self.Cx)
		self.Cy = ( ( self.vectorA[2] * self.vectorB[0] ) - ( self.vectorA[0] * self.vectorB[2] ) )
		self.vectorAxB.append(self.Cy)
		self.Cz = ( ( self.vectorA[0] * self.vectorB[1] ) - ( self.vectorA[1] * self.vectorB[0] ) )
		self.vectorAxB.append(self.Cz)
		self.vectorAxB = find_crossproduct.vectorAxB
		
		magnitudeTriVector.x = self.Cx
		magnitudeTriVector.y = self.Cy
		magnitudeTriVector.z = self.Cz
		# determine the ||normVectorAxB||: area of a Parallelogram PQRS
		self.normVectorAxB = magnitudeTriVector.magtrivector()
		print('\t-- The [Cross Product]: vectorAxB',self.vectorAxB)
		print(f'\t-- The ||normVectorAxB|| is {self.normVectorAxB:<.2f}')
		return
		
	def determine_areaTriangle(self):
		find_crossproduct.findCrossProduct()
		# self.vectorAxB = find_crossproduct.vectorAxB
		self.Area_S = self.normVectorAxB / 2
		print(f'\t-- The [area(S)] of a [TrianglePQR] is {self.Area_S:<.2f}','\n') 
		return
			
	def get_areaParallelogram(self):
		find_crossproduct.findCrossProduct()
		self.height_Parallelogram = abs( self.normVectorAxB / self.normA )
		self.Area = abs(self.normVectorAxB) 
		print(f'\n\t-- The [height(h)] of the [Parallelogram(PQRS)] is {self.height_Parallelogram:<.2f}')
		print(f'\t-- The [Area(P)] of a [Parallelogram(PQRS)] is {self.Area:<.2f}','\n')
		return
		
	def find_Thetasin(self):
		find_crossproduct.findCrossProduct()
		self.sine = self.normVectorAxB / ( self.normA * self.normB )
		print(f'\t-- The [THETA SINE IN RADIAN] is {self.sine:<.2f}','\n')
		return
		
	def get_thetaAngle(self):
		find_crossproduct.findCrossProduct()
		self.vectorAxB = find_crossproduct.vectorAxB
		self.sine = self.normVectorAxB / ( self.normA * self.normB )
		self.radianAngle = math.asin(self.sine)
		self.thetaAngle_degree = math.degrees(self.radianAngle)
		print(f'\t-- The [THETA ANGLE IN DEGREE] is {self.thetaAngle_degree:<.2f}','\n')
		return
		
find_crossproduct = CrossProduct()

class TheoremScalar3dProduct:
	'''
	Find the Scalar Product by [Theorem]: a * b = ||a||*||b||*cos(Theta).
	'''
	def __init__(self, normA = 0, normB = 0, number = 0, AxBscalar_product = 0, theta_degrees = 0, theta_radian = 0, 
	vectorA = 0, vectorB = 0):
		self.number = number
		self.normA = normA
		self.normB = normB
		
		self.AxBscalar_product = AxBscalar_product
		self.theta_degrees = theta_degrees
		self.theta_radian = theta_radian
		
		self.vectorA = vectorA
		self.vectorB = vectorB
		
	def use_theoremScalar3dProduct(self):
		# compvector.getcomponent3dvectorA()
		print('\t* Enter with the [new value] of the [vectorA] module?')
		self.normA = introduce.enterRealData()
		print('\t* Provide the [new value] of the [vectorB] module?')
		self.normB = introduce.enterRealData()

		print('\n\t\t-- The |vectorA|:',self.normA)
		print('\t\t-- The |vectorB|:',self.normB)
		
		# data enter to theta angle in degree
		print('\n\t\t*[NEW INSTRUCTION]*\n')
		print('\t- The [theta angle in degree] between [vectors]: [vectorA] and [vectorB]')
		print('\t- [Type a only integer or real number] without the [Character: º(degree)].')
		print('\t- The [conversion] of [degree] to [radian] will be done automatically by Method.\n')
		self.theta_degrees = introduce.enterRealData()
		self.theta_radian =  math.radians(self.theta_degrees)
		self.AxBscalar_product = self.normA * self.normB * math.cos(self.theta_radian)
		
		answer.view_solution()
		print(f'\t-- The [A*B_Scalar Product] is {self.AxBscalar_product:<.2f}','\n')
		
		return

theorem_scalar3d_product = TheoremScalar3dProduct()

class Scalar3dProduct:
	"""
	Find the scalar product by [Definition].
	The class Scalar3dProduct have 941 lines of code.
	"""
	def __init__(self, alpha = 0, a1 = 0, a2 = 0, a3 = 0, add = 0, Area = 0, Area_S = 0, b1 = 0, b2 = 0, b3 = 0, 
	 c1 = 0, c2 = 0, c3 = 0, comp0 = 0, comp1 = 0, comp3 = 0, coordP = [], coordQ = [], coordR = [], coordS = [],
	 cossineThetaRadians = 0, cossineAlphaRadians = 0, cP = 0, EquatArea = 0, EquatArea1 = 0,EquatArea2 = 0, h1 = 0,
	 h2 = 0, h3 = 0, height_h = 0, height_h1 = 0,  height_h2 = 0, number = 0, number1 = 0, number2 = 0, normA = 0,
	 normB = 0, modAxBproduct = 0, Perimeter = 0, Perimeter1  = 0, PointP = 0, PointQ = 0, PointR = 0, PointS = 0, 
	 vectorA = 0, vectorB = 0, vectorC = 0, vectorAB = 0, vectorQR = [], vectorPQ = [], vectorQP = [], vectorRP = [],
	 vectorPR = [], vectorPS = [], vectorSP = [], vectorSR = [], vectorPQºPR = [], vectorPQºQR = [], vectorQPºQR = [],
	 vectorQRºRP = [], vectorRPºPQ = [], vectorSPºSR = [], radianAngle = 0, radianAlpha = 0, radianTheta = 0,
	 sine = 0, sineAlphaRadians = 0, scalarProduct = 0, vectorRPºRQ = [], ScalarProd0 = 0, ScalarProd1 = 0,  
	 ScalarProd2 = 0, ScalarProd3 = 0, sideA = 0, sideB = 0, sideC = 0, term = 0, term0 = 0, term1 = 0, term2 = 0,
	 theta = 0, xP = 0, xQ = 0, xR = 0, xS = 0, yP = 0, yQ = 0, yR = 0, yS = 0, zP = 0, zQ = 0, zR = 0, zS = 0,
	 Cx = 0, Cy = 0, Cz = 0, vectorAxB = [], normVectorAxB = 0 ):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.add = add
		self.alpha = alpha
		self.theta = theta
		self.Area = Area
		self.Area_S = Area_S
		
		self.b1 = b1
		self.b2 = b2
		self.b3 = b3
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		
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
		self.normVectorAxB = normVectorAxB
		
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
		self.term2 = term2 
		
		self.xP = xP
		self.xQ = xQ
		self.xR = xR
		self.xS = xS
		
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		self.yS = yS
		
		self.zP = zP 
		self.zQ = zQ
		self.zR = zR
		self.zS = zS
		
		# new attribute of class
		self.Cx = Cx
		self.Cy = Cy
		self.Cz = Cx
		self.vectorAxB = vectorAxB
		self.normVectorAxB = normVectorAxB
		
	def getscalar3d_product(self):
		
		if self.number == 1 or self.number == 2:
			# Enter the components of the vectors: a and b
			self.vectorA = compvector.getcomponent3dvectorA()
			self.vectorB = compvector.getcomponent3dvectorB()
			
			answer.view_solution()
			print('\t-- The [vectorA]: vectorA', self.vectorA)
			print('\t-- The [vectorB]: vectorB', self.vectorB, '\n')
			
			self.vectorAB = []
			self.scalarProduct = 0
			
			for i in range(0, 3):
				# Will find the Scalar Product by [Definition].
				self.term = self.vectorA[i] * self.vectorB[i]
				self.scalarProduct = self.scalarProduct + self.term
				self.vectorAB.append(self.term)
			
			# fix self.number1	
			if self.number1 == 1:
				print('\t-- The [Vector] of the [terms of the Scalar Product]: vectorA*B', self.vectorAB)
				print(f'\t-- The [Scalar Product(vectorA*B)] of the vectors is: {self.scalarProduct:<.2f}','\n')
				return 
			
			elif self.number1 == 2:
				magnitudeTriVector.x = self.vectorA[0]
				magnitudeTriVector.y = self.vectorA[1]
				magnitudeTriVector.z = self.vectorA[2]
				self.normA = magnitudeTriVector.magtrivector()
				 
				magnitudeTriVector.x = self.vectorB[0]
				magnitudeTriVector.y = self.vectorB[1]
				magnitudeTriVector.z = self.vectorB[2]
				self.normB = magnitudeTriVector.magtrivector()
				self.modAxBproduct = self.normA * self.normB
				
				self.cossineThetaRadians = self.scalarProduct / self.modAxBproduct
				
				print(f'\t-- The [length] of a ||vectorA||: {self.normA:<.2f}')
				print(f'\t-- The [length] of a ||vectorB||: {self.normB:<.2f}')
				print('\t-- The vectorA*B: vectorA*B', self.vectorAB)
				print(f'\t-- The [value] finded of |vectorA*B| is: {self.modAxBproduct:<.2f}')
				print(f'\t-- The [Scalar Product] of the [vectorA*B] is: {self.scalarProduct:<.2f}')
				print(f'\t-- The [value] determined of the [Theta Cosine in RADIAN] is: {self.cossineThetaRadians:<.2f}')
				return
				
		elif self.number == 3:
			# Give the [coordinates] of the vertices points: P, Q, and R  of trianglePQR
			self.xP = self.xQ = self.xR = 0
			self.yP = self.yQ = self.yR = 0
			self.zP = self.zQ = self.zR = 0
			
			pointcoordinates3d.number1 = 1
			self.coordP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 2
			self.coordQ = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.coordR = pointcoordinates3d.getpointcoordinates3d()
			
			for self.cP in range(0,3):
				if self.cP == 0:
					self.xP = self.coordP[self.cP]
					self.xQ = self.coordQ[self.cP]
					self.xR = self.coordR[self.cP]
					
				elif self.cP == 1:
					self.yP = self.coordP[self.cP]
					self.yQ = self.coordQ[self.cP]
					self.yR = self.coordR[self.cP]
					
				elif self.cP == 2:
					self.zP = self.coordP[self.cP]
					self.zQ = self.coordQ[self.cP]
					self.zR = self.coordR[self.cP]
						
			self.PointP = (self.xP,self.yP,self.zP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\t- The (Point Q): Q',self.PointQ)
			self.PointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.PointR)
			answer.view_solution()
			
			self.vectorQR = []
			self.vectorRP = []
			self.vectorPQ = []
			
			for h in range (0,3):
				self.comp0 = self.coordR[h] - self.coordQ[h]
				self.vectorQR.append(self.comp0)
				self.comp1 = self.coordP[h] - self.coordR[h]
				self.vectorRP.append(self.comp1)
				self.comp3 = self.coordQ[h] - self.coordP[h]
				self.vectorPQ.append(self.comp3)

			self.vectorA = self.vectorQR
			self.vectorB = self.vectorRP
			self.vectorC = self.vectorPQ
			
			# get the three sides of a trianglePQR
			magnitudeTriVector.x = self.vectorQR[0]
			magnitudeTriVector.y = self.vectorQR[1]
			magnitudeTriVector.z = self.vectorQR[2]
			# sideA = |QR|
			self.sideA = magnitudeTriVector.magtrivector()
			
			magnitudeTriVector.x = self.vectorRP[0]
			magnitudeTriVector.y = self.vectorRP[1]
			magnitudeTriVector.z = self.vectorRP[2]
			# sideB = |RP|
			self.sideB = magnitudeTriVector.magtrivector()
			
			magnitudeTriVector.x = self.vectorPQ[0]
			magnitudeTriVector.y = self.vectorPQ[1]
			magnitudeTriVector.z = self.vectorPQ[2]
			# sideC = |PQ|
			self.sideC = magnitudeTriVector.magtrivector()
			
			# The area S of the trianglePQR
			# The [components] Vector: A and B
			
			self.a1 = self.vectorA[0]
			self.a2 = self.vectorA[1]
			self.a3 = self.vectorA[2]
			
			self.b1 = self.vectorB[0]
			self.b2 = self.vectorB[1]
			self.b3 = self.vectorB[2]
			
			# find the Cross Product(AxB)
			self.Cx = ( ( self.vectorA[1] * self.vectorB[2] ) - ( self.vectorA[2] * self.vectorB[1] ) )
			self.vectorAxB.append(self.Cx)
			self.Cy = ( ( self.vectorA[2] * self.vectorB[0] ) - ( self.vectorA[0] * self.vectorB[2] ) )
			self.vectorAxB.append(self.Cy)
			self.Cz = ( ( self.vectorA[0] * self.vectorB[1] ) - ( self.vectorA[1] * self.vectorB[0] ) )
			self.vectorAxB.append(self.Cz)
			
			# Determine the ||normVectorAxB|| and the area of a triangle PQR
			# self.normVectorAxB = magnitudeTriVector.magtrivector()
			magnitudeTriVector.x = self.Cx
			magnitudeTriVector.y = self.Cy
			magnitudeTriVector.z = self.Cz
			self.normVectorAxB = magnitudeTriVector.magtrivector()
			self.Area_S = self.normVectorAxB / 2
			
			if self.sideA < self.sideB + self.sideC and self.sideB < self.sideA + self.sideC and self.sideC < self.sideA + self.sideB:
				textstring1.view_instructions()
				
				self.Perimeter = self.sideA + self.sideB + self.sideC
				
				# vectorAxC = vectorQRºPQ
				# vectorAxB = vectorQRºRP
				# vectorBxC = vectorRPºPQ
				
				self.vectorQRºPQ = []
				self.vectorQRºRP = []
				self.vectorRPºPQ = []
				
				self.ScalarProd0 = 0
				self.ScalarProd1 = 0
				self.ScalarProd2 = 0
				
				# Find the Scalars Procucts between the vectors
				for j in range(0, 3):
					self.term0 = self.vectorQR[j] * self.vectorPQ[j]
					self.ScalarProd0 = self.ScalarProd0 + self.term0
					self.vectorQRºPQ.append(self.term0)
					
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
				self.h3 = subqdroot.getheight()
				
				print('\t-- The [vectorA] = vectorQR', self.vectorQR)
				print('\t-- The [vectorB] = vectorRP', self.vectorRP)
				print('\t-- The [vectorC] = vectorPQ', self.vectorPQ,'\n')
				print(f'\t-- The [sideA] = ||vectorQR|| of the triangle(PQR) is: {self.sideA:<.2f}')
				print(f'\t-- The [sideB] = ||vectorRP|| of the triangle(PQR) is: {self.sideB:<.2f}')
				print(f'\t-- The [sideC] = ||vectorPQ|| of the triangle(PQR) is: {self.sideC:<.2f}','\n')
				print('\t-- The [terms] of the [Scalar Product(QRºPQ)] is:',self.vectorQRºPQ)
				print('\t-- The [terms] of the [Scalar Product(QRºRP)] is:',self.vectorQRºRP)
				print('\t-- The [terms] of the [Scalar Product(RPºPQ)] is:',self.vectorRPºPQ,'\n')
				print(f'\t-- The [Scalar Product(QRºPQ)] is: {self.ScalarProd0:<.2f}')
				print(f'\t-- The [Scalar Product(QRºRP)] is: {self.ScalarProd1:<.2f}')
				print(f'\t-- The [Scalar Product(RPºPQ)] is: {self.ScalarProd2:<.2f}')
				print('\n\t-- The [vectorAxB]: vectorAxB',self.vectorAxB)
				print(f'\t-- The ||normVectorAxB|| is {self.normVectorAxB:<.2f}','\n')
				print(f'\t-- The [Perimeter] of the [triangle(PQR)] is {self.Perimeter:<.2f}','\n')
				print(f'\t-- The [Height(h1) relative as sideQR] is {self.h1:<.2f}')
				print(f'\t-- The [Height(h2) relative as sideRP] is {self.h2:<.2f}')
				print(f'\t-- The [Height(h3) relative as sidePQ] is {self.h3:<.2f}')
				print(f'\t-- The [Area(A)] of the [triangle(PQR)] is {self.Area_S:<.2f}')
				
				return
			else:
				textstring2.error_instructions()
				return
				
		elif self.number == 4:
			self.xP = self.xQ = self.xR = self.xS = 0
			self.yP = self.yQ = self.yR = self.yS = 0
			self.zP = self.zQ = self.zR = self.zS = 0
			print('\t--------------------')
			print('\t*[NEW INSTRUCTIONS]*')
			print('\t--------------------\n')
			print('\t- Key [1] if in problem is given the [coordinates] of the three vertices: P, Q, and R. After')
			print('\t  follow the new [instructions] in [Display] to find the [coordinates: xS, yS, and zS] relative ')
			print('\t  as point: S below - Ok!\n')
			print('\t- Key [2] if in problem is given the [coordinates] of the four vertices: P, Q, R, and S.\n')
			
			self.number1 = vector.enterIntegerData()
			
			if self.number1 == 1:
				print('\n\t\t======================')
				print('\t\t**[NEW INSTRUCTIONS]**')
				print('\t\t======================\n')
				print('\t-- Type [1] to find the [coordinates: xM, yM and zM] of the middle point: M in [diagonal: SP] ')
				print('\t   Use the [coordinates: xQ, yQ, zQ, xR, yR and zR] of the points: Q and R.')
				print('\n\t-- Type [2] to find the [coordinates: xL, yL and zL] of the middle point: L in [diagonal: SQ] ')
				print('\t   Use the [coordinates: xP, yP, zP, xR, yR, and zR] of the points: P and R.')
				print('\n\t-- Type [3] to find the [coordinates: xK, yK, and zK] of the middle point: K in [diagonal: SR] ')
				print('\t   Use the [coordinates: xP, yP, zP, xQ, yQ, and zQ] of the points: P and Q.\n')
				
				self.number2 = vector.enterIntegerData()
				
				if self.number2 == 1:
					# Given the [coordinates] of the points: P, Q, and R of a parallelogramPQRS.
					
					middle3dpoint.number = 3
					middle3dpoint.getmiddle3d_point()
					self.coordQ = []
					self.xQ = middle3dpoint.xQ
					self.coordQ.append(self.xQ)
					self.yQ = middle3dpoint.yQ
					self.coordQ.append(self.yQ)
					self.zQ = middle3dpoint.zQ
					self.coordQ.append(self.zQ)
					
					self.coordR = []
					self.xR = middle3dpoint.xR
					self.coordR.append(self.xR)
					self.yR = middle3dpoint.yR
					self.coordR.append(self.yR)
					self.zR = middle3dpoint.zR
					self.coordR.append(self.zR)
					
					pointcoordinates3d.number1 = 1
					self.coordP = pointcoordinates3d.getpointcoordinates3d()
					
					for h in range(0,3):
						if h == 0:
							self.xP = self.coordP[h]
						elif h == 1:
							self.yP = self.coordP[h]
						elif h == 2:
							self.zP = self.coordP[h]
							
					self.PointP = (self.xP,self.yP,self.zP)
					print('\n\t- The (Point P): P',self.PointP)				
					self.xM = middle3dpoint.xM
					self.yM = middle3dpoint.yM
					self.zM = middle3dpoint.zM
					
					# Find the coordinates: xS, and yS of the point: S
					self.xS = ( 2 * self.xM ) - self.xP 
					self.yS = ( 2 * self.yM ) - self.yP
					self.zS = ( 2 * self.zM ) - self.zP
					answer.view_solution()
					print('\t- The [Coordinates] of the point S:\n')
					print(f'\t  -- The [Coordinate]: xS is {self.xS:<.2f}')
					print(f'\t  -- The [Coordinate]: yS is {self.yS:<.2f}')
					print(f'\t  -- The [Coordinate]: zS is {self.zS:<.2f}','\n')
					self.coordS = [self.xS, self.yS,self.zS]
					
					self.vectorPQ = []
					self.vectorPR = []
					
					for i in range(0,3):
						self.comp0 = self.coordQ[i] - self.coordP[i]
						self.vectorPQ.append(self.comp0)
						self.comp1 = self.coordR[i] - self.coordP[i]
						self.vectorPR.append(self.comp1)
						
					magnitudeTriVector.x = self.vectorPQ[0]
					magnitudeTriVector.y = self.vectorPQ[1]
					magnitudeTriVector.z = self.vectorPQ[2]
					# sideA = |PQ|
					self.sideA = magnitudeTriVector.magtrivector()
					
					magnitudeTriVector.x = self.vectorPR[0]
					magnitudeTriVector.y = self.vectorPR[1]
					magnitudeTriVector.z = self.vectorPR[2]
					# sideB = |PR|
					self.sideB = magnitudeTriVector.magtrivector()
					
					# save copy of the lists: self.vectorPQ and self.vectorPR to 
					# the attributes: self.vectorA and self.vectorB
					self.vectorA = self.vectorPQ
					self.vectorB = self.vectorPR
					
					# The area S of the trianglePQR
					# The [components] Vector: A and B
					
					self.a1 = self.vectorA[0]
					self.a2 = self.vectorA[1]
					self.a3 = self.vectorA[2]
					
					self.b1 = self.vectorB[0]
					self.b2 = self.vectorB[1]
					self.b3 = self.vectorB[2]
					
					# find the Cross Product(AxB)
					self.Cx = ( ( self.vectorA[1] * self.vectorB[2] ) - ( self.vectorA[2] * self.vectorB[1] ) )
					self.vectorAxB.append(self.Cx)
					self.Cy = ( ( self.vectorA[2] * self.vectorB[0] ) - ( self.vectorA[0] * self.vectorB[2] ) )
					self.vectorAxB.append(self.Cy)
					self.Cz = ( ( self.vectorA[0] * self.vectorB[1] ) - ( self.vectorA[1] * self.vectorB[0] ) )
					self.vectorAxB.append(self.Cz)
					
					# Determine the ||normVectorAxB|| and the area of a triangle PQR
					# self.normVectorAxB = magnitudeTriVector.magtrivector()
					magnitudeTriVector.x = self.Cx
					magnitudeTriVector.y = self.Cy
					magnitudeTriVector.z = self.Cz
					self.normVectorAxB = magnitudeTriVector.magtrivector()
					self.Area_S = abs(self.normVectorAxB)
					print('\t-- The [vectorAxB]: vectorAxB',self.vectorAxB)
					print(f'\t-- The ||normVectorAxB|| is {self.normVectorAxB:<.2f}','\n')
					
					self.Perimeter = ( self.sideA + self.sideB ) * 2
						
					self.vectorPQºPR = []
					self.ScalarProd1 = 0
						
					for j in range(0,3):
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
					middle3dpoint.number = 2
					middle3dpoint.getmiddle3d_point()
					
					self.coordP = []
					self.xP = middle3dpoint.xP
					self.coordP.append(self.xP)
					self.yP = middle3dpoint.yP
					self.coordP.append(self.yP)
					self.zP = middle3dpoint.zP
					self.coordP.append(self.zP)
					self.coordR = []
					self.xR = middle3dpoint.xR
					self.coordR.append(self.xR)
					self.yR = middle3dpoint.yR
					self.coordR.append(self.yR)
					self.zR = middle3dpoint.zR
					self.coordR.append(self.zR)
					
					pointcoordinates3d.number1 = 2
					self.coordQ = pointcoordinates3d.getpointcoordinates3d()
					
					for i in range(0,3):
						if i == 0:
							self.xQ = self.coordQ[i]	
						elif i == 1:
							self.yQ = self.coordQ[i]
						elif i == 2:
							self.zQ = self.coordQ[i]
							
					self.PointQ = (self.xQ,self.yQ,self.zQ)
					print('\n\t- The (Point Q): Q',self.PointQ)				
					self.xL = middle3dpoint.xL
					self.yL = middle3dpoint.yL
					self.zL = middle3dpoint.zL
					# Find the coordinates: xS, and yS of the point: S
					self.xS = ( 2 * self.xL ) - self.xQ 
					self.yS = ( 2 * self.yL ) - self.yQ
					self.zS = ( 2 * self.zL ) - self.zQ
					answer.view_solution()
					print('\t- The [Coordinates] of the point S:\n')
					print(f'\t  -- The [Coordinate]: xS is {self.xS:<.2f}')
					print(f'\t  -- The [Coordinate]: yS is {self.yS:<.2f}')
					print(f'\t  -- The [Coordinate]: zS is {self.zS:<.2f}','\n')
					self.coordS = [self.xS, self.yS,self.zS]
					
					self.vectorQP = []
					self.vectorQR = []
					
					for j in range(0,3):
						self.comp0 = self.coordP[j] - self.coordQ[j]
						self.vectorQP.append(self.comp0)
						self.comp1 = self.coordR[j] - self.coordQ[j]
						self.vectorQR.append(self.comp1)
						
					magnitudeTriVector.x = self.vectorQP[0]
					magnitudeTriVector.y = self.vectorQP[1]
					magnitudeTriVector.z = self.vectorQP[2]
					# sideA = |QP|
					self.sideA = magnitudeTriVector.magtrivector()
					
					magnitudeTriVector.x = self.vectorQR[0]
					magnitudeTriVector.y = self.vectorQR[1]
					magnitudeTriVector.z = self.vectorQR[2]
					# sideB = |QR|
					self.sideB = magnitudeTriVector.magtrivector()
					
					# save copy of the lists: self.vectorQP and self.vectorQR to 
					# the attributes: self.vectorA and self.vectorB
					self.vectorA = self.vectorQP
					self.vectorB = self.vectorQR
					
					# The area S of the trianglePQR
					# The [components] Vector: A and B
					
					self.a1 = self.vectorA[0]
					self.a2 = self.vectorA[1]
					self.a3 = self.vectorA[2]
					
					self.b1 = self.vectorB[0]
					self.b2 = self.vectorB[1]
					self.b3 = self.vectorB[2]
					
					# find the Cross Product(AxB)
					self.Cx = ( ( self.vectorA[1] * self.vectorB[2] ) - ( self.vectorA[2] * self.vectorB[1] ) )
					self.vectorAxB.append(self.Cx)
					self.Cy = ( ( self.vectorA[2] * self.vectorB[0] ) - ( self.vectorA[0] * self.vectorB[2] ) )
					self.vectorAxB.append(self.Cy)
					self.Cz = ( ( self.vectorA[0] * self.vectorB[1] ) - ( self.vectorA[1] * self.vectorB[0] ) )
					self.vectorAxB.append(self.Cz)
					
					# Determine the ||normVectorAxB|| and the area of a triangle PQR
					# self.normVectorAxB = magnitudeTriVector.magtrivector()
					magnitudeTriVector.x = self.Cx
					magnitudeTriVector.y = self.Cy
					magnitudeTriVector.z = self.Cz
					self.normVectorAxB = magnitudeTriVector.magtrivector()
					self.Area_S = abs(self.normVectorAxB)
					print('\t-- The [vectorAxB]: vectorAxB',self.vectorAxB)
					print(f'\t-- The ||normVectorAxB|| is {self.normVectorAxB:<.2f}','\n')
						
					self.Perimeter = ( self.sideA + self.sideB ) * 2
						
					self.vectorQPºQR = []
					self.ScalarProd2 = 0
						
					for j in range(0, 3):
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
						
					print('\t-- The [vectorQP]: vectorQP',self.vectorQP)
					print('\t-- The [vectorQR]: vectorQR',self.vectorQR,'\n')
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
					middle3dpoint.number = 1
					middle3dpoint.getmiddle3d_point()
					
					self.coordP = []
					self.xP = middle3dpoint.xP
					self.coordP.append(self.xP)
					self.yP = middle3dpoint.yP
					self.coordP.append(self.yP)
					self.zP = middle3dpoint.zP
					self.coordP.append(self.zP)
					self.coordQ = []
					self.xQ =middle3dpoint.xQ
					self.coordQ.append(self.xQ)
					self.yQ = middle3dpoint.yQ
					self.coordQ.append(self.yQ)
					self.zQ = middle3dpoint.zQ
					self.coordQ.append(self.zQ)
					
					pointcoordinates3d.number1 = 3
					self.coordR = pointcoordinates3d.getpointcoordinates3d()
					
					for j in range(0,3):
						if j == 0:
							self.xR = self.coordR[j]	
						elif j == 1:
							self.yR = self.coordR[j]
						elif j == 2:
							self.zR = self.coordR[j]
							
					self.PointR = (self.xR,self.yR,self.zR)
					print('\n\t- The (Point R): R',self.PointR)				
					self.xK = middle3dpoint.xK
					self.yK = middle3dpoint.yK
					self.zK = middle3dpoint.zK
					# Find the coordinates: xS, and yS of the point: S
					self.xS = ( 2 * self.xK ) - self.xR 
					self.yS = ( 2 * self.yK ) - self.yR
					self.zS = ( 2 * self.zK ) - self.zR
					answer.view_solution()
					print('\t- The [Coordenates] of the point S:\n')
					print(f'\t  -- The [Coordinate]: xS is {self.xS:<.2f}')
					print(f'\t  -- The [Coordinate]: yS is {self.yS:<.2f}')
					print(f'\t  -- The [Coordinate]: zS is {self.zS:<.2f}','\n')
					self.coordS = [self.xS, self.yS,self.zS]
					
					self.vectorRP = []
					self.vectorRQ = []
					
					for j in range(0,3):
						self.comp0 = self.coordP[j] - self.coordR[j]
						self.vectorRP.append(self.comp0)
						self.comp1 = self.coordQ[j] - self.coordR[j]
						self.vectorRQ.append(self.comp1)
						
					magnitudeTriVector.x = self.vectorRP[0]
					magnitudeTriVector.y = self.vectorRP[1]
					magnitudeTriVector.z = self.vectorRP[2]
					# sideA = |RP|
					self.sideA = magnitudeTriVector.magtrivector()
					
					magnitudeTriVector.x = self.vectorRQ[0]
					magnitudeTriVector.y = self.vectorRQ[1]
					magnitudeTriVector.z = self.vectorRQ[2]
					# sideB = |RQ|
					self.sideB = magnitudeTriVector.magtrivector()
					
					# save copy of the lists: self.vectorRP and self.vectorRQ to 
					# the attributes: self.vectorA and self.vectorB
					self.vectorA = self.vectorRP
					self.vectorB = self.vectorRQ
					
					# The area S of the trianglePQR
					# The [components] Vector: A and B
					
					self.a1 = self.vectorA[0]
					self.a2 = self.vectorA[1]
					self.a3 = self.vectorA[2]
					
					self.b1 = self.vectorB[0]
					self.b2 = self.vectorB[1]
					self.b3 = self.vectorB[2]
					
					# find the Cross Product(AxB)
					self.Cx = ( ( self.vectorA[1] * self.vectorB[2] ) - ( self.vectorA[2] * self.vectorB[1] ) )
					self.vectorAxB.append(self.Cx)
					self.Cy = ( ( self.vectorA[2] * self.vectorB[0] ) - ( self.vectorA[0] * self.vectorB[2] ) )
					self.vectorAxB.append(self.Cy)
					self.Cz = ( ( self.vectorA[0] * self.vectorB[1] ) - ( self.vectorA[1] * self.vectorB[0] ) )
					self.vectorAxB.append(self.Cz)
					
					# Determine the ||normVectorAxB|| and the area of a triangle PQR
					# self.normVectorAxB = magnitudeTriVector.magtrivector()
					magnitudeTriVector.x = self.Cx
					magnitudeTriVector.y = self.Cy
					magnitudeTriVector.z = self.Cz
					self.normVectorAxB = magnitudeTriVector.magtrivector()
					self.Area_S = abs(self.normVectorAxB)
					print('\t-- The [vectorAxB]: vectorAxB',self.vectorAxB)
					print(f'\t-- The ||normVectorAxB|| is {self.normVectorAxB:<.2f}','\n')
						
					self.Perimeter = ( self.sideA + self.sideB ) * 2
						
					self.vectorRPºRQ = []
					self.ScalarProd3 = 0
						
					for j in range(0, 3):
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
					textstring3.error_option()
					return
					
			elif self.number1 == 2:
				# Given the coordinates of the points: P, Q, R, and S. The vertices of the parallelogramPQRS
				pointcoordinates3d.number1 = 1
				self.coordP = pointcoordinates3d.getpointcoordinates3d()
				pointcoordinates3d.number1 = 2
				self.coordQ = pointcoordinates3d.getpointcoordinates3d()
				pointcoordinates3d.number1 = 3
				self.coordR = pointcoordinates3d.getpointcoordinates3d()
				pointcoordinates3d.number1 = 4
				self.coordS = pointcoordinates3d.getpointcoordinates3d()
				
				self.xP = self.xQ = self.xR = self.xS = 0
				self.yP = self.yQ = self.yR = self.yS = 0
				self.zP = self.zQ = self.zR = self.zS = 0
				
				# self.cP = i
				
				for i in range(0,3):
					if i == 0:
						self.xP = self.coordP[i]
						self.xQ = self.coordQ[i]
						self.xR = self.coordR[i]
						self.xS = self.coordS[i]
					elif i == 1:
						self.yP = self.coordP[i]
						self.yQ = self.coordQ[i]
						self.yR = self.coordR[i]
						self.yS = self.coordS[i]
					elif i == 2:
						self.zP = self.coordP[i]
						self.zQ = self.coordQ[i]
						self.zR = self.coordR[i]
						self.zS = self.coordS[i]
				
				self.PointP = (self.xP,self.yP,self.zP)
				print('\n\t- The (Point P): P',self.PointP)
				self.PointQ = (self.xQ,self.yQ,self.zQ)
				print('\t- The (Point Q): Q',self.PointQ)
				self.PointR = (self.xR,self.yR,self.zR)
				print('\t- The (Point R): R',self.PointR)
				self.PointS = (self.xS,self.yS,self.zS)
				print('\t- The (Point S): S',self.PointS)
		
				self.vectorPQ = []
				self.vectorPS = []
				
				for k in range (0,3):
					self.comp0 = self.coordQ[k] - self.coordP[k] 
					self.vectorPQ.append(self.comp0)
					
					self.comp1 = self.coordS[k] - self.coordP[k] 
					self.vectorPS.append(self.comp1)
						
				magnitudeTriVector.x = self.vectorPQ[0]
				magnitudeTriVector.y = self.vectorPQ[1]
				magnitudeTriVector.z = self.vectorPQ[2]
				# sideA = |PQ|
				self.sideA = magnitudeTriVector.magtrivector()
				
				magnitudeTriVector.x = self.vectorPS[0]
				magnitudeTriVector.y = self.vectorPS[1]
				magnitudeTriVector.z = self.vectorPS[2]
				
				# sideB = |PS|
				self.sideB = magnitudeTriVector.magtrivector()
				
				# save copy of the lists: self.vectorPQ and self.vectorPR to
				# the attributes: self.vectorA and self.vectorB
				self.vectorA = self.vectorPQ
				self.vectorB = self.vectorPS
				
				# The area S of the trianglePQR
				# The [components] Vector: A and B
				
				self.a1 = self.vectorA[0]
				self.a2 = self.vectorA[1]
				self.a3 = self.vectorA[2]
				
				self.b1 = self.vectorB[0]
				self.b2 = self.vectorB[1]
				self.b3 = self.vectorB[2]
				
				# find the Cross Product(AxB)
				self.Cx = ( ( self.vectorA[1] * self.vectorB[2] ) - ( self.vectorA[2] * self.vectorB[1] ) )
				self.vectorAxB.append(self.Cx)
				self.Cy = ( ( self.vectorA[2] * self.vectorB[0] ) - ( self.vectorA[0] * self.vectorB[2] ) )
				self.vectorAxB.append(self.Cy)
				self.Cz = ( ( self.vectorA[0] * self.vectorB[1] ) - ( self.vectorA[1] * self.vectorB[0] ) )
				self.vectorAxB.append(self.Cz)
				
				# Determine the ||normVectorAxB|| and the area of a triangle PQR
				# self.normVectorAxB = magnitudeTriVector.magtrivector()
				magnitudeTriVector.x = self.Cx
				magnitudeTriVector.y = self.Cy
				magnitudeTriVector.z = self.Cz
				self.normVectorAxB = magnitudeTriVector.magtrivector()
				self.Area_S = abs(self.normVectorAxB)
				answer.view_solution()
				print('\t-- The [vectorAxB]: vectorAxB',self.vectorAxB)
				print(f'\t-- The ||normVectorAxB|| is {self.normVectorAxB:<.2f}','\n')
					
				self.Perimeter = ( self.sideA + self.sideB ) * 2
					
				self.vectorPSºPQ = []
				self.ScalarProd0 = 0
					
				for j in range(0, 3):
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
				textstring3.error_option()
				return
				
		print('\n\t\t----------------------------------------------------')
		print(f'\t\t -_- The [Height(h1)] relative as [sideB] is: {self.height_h1:<.2f}')
		print('\t\t ----------------------- or -----------------------')
		print(f'\t\t º<º The [Height(h2)] relative as [sideA] is: {self.height_h2:<.2f}')
		print('\t\t----------------------------------------------------\n')
		print(f'\t-- The [Area(S)] of the [Parallelogram(PQRS)] is {self.Area_S:<.2f}','\n')
			
		return

scalar3dproduct = Scalar3dProduct()

class InnerAngleTriangle:
	def __init__(self, a1 = 0, a2 = 0, a3 = 0, addInnerAngle = 0, AngleAlpha_degrees = 0, AngleBeta_degrees = 0,
	coord = 0, AngleGama_degrees = 0, b1 = 0, b2 = 0, b3 = 0, c1 = 0, c2 = 0, c3 = 0, comp0 = 0, comp1 = 0, comp3 = 0, 
	coordP = 0, coordQ = 0, coordR = 0, coordS = 0, compAB = 0, compBC = 0, compAC = 0, compBA = 0, compCB = 0,
	compCA = 0, CossineA = 0, CossineB = 0, CossineC = 0, cosineThetaRadians = 0, number1 = 0, normA = 0, normB = 0, 
	normAxBproduct = 0, normBxCproduct = 0, normAxCproduct = 0, pointA = 0, pointB = 0, pointC = 0, PointP = 0,   
	PointQ = 0, PointR = 0, PointS = 0, ScalarProdAB = 0, ScalarProdBC = 0, ScalarProdAC = 0, sideA = 0, sideB = 0, 
	sideC = 0, vectorA = 0, vectorB = 0, vectorC = 0, vectorBC = 0, vectorAC = 0, vectorAB = 0, vectorBA = 0,
	vectorCB = 0, vectorCA = 0, VectorBC = 0, term = 0, term0 = 0, term1 = 0, xP = 0, xQ = 0, xR = 0, yP = 0,
	yQ = 0, yR = 0, zP = 0, zQ = 0, zR = 0 ):  
	
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.addInnerAngle = addInnerAngle 
		self.AngleAlpha_degrees = AngleAlpha_degrees
		self.AngleBeta_degrees = AngleBeta_degrees
		self.AngleGama_degrees = AngleGama_degrees
		self.b1 = b1
		self.b2 = b2
		self.b3 = b3
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		
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
		
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		
		self.zP = zP 
		self.zQ = zQ
		self.zR = zR
		
	def getInner_angle_triangle(self):
		# Given the [coordinates] of the points: P, Q, and R vertics of trianglePQR
		pointcoordinates3d.number1 = 1
		self.coordP = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 2
		self.coordQ = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 3
		self.coordR = pointcoordinates3d.getpointcoordinates3d()
		
		self.PointP, self.PointQ, self.PointR = self.coordP, self.coordQ, self.coordR
		self.pointA, self.pointB, self.pointC = self.PointP, self.PointQ, self.PointR
		self.xP = self.xQ = self.xR = 0
		self.yP = self.yQ = self.yR = 0
		self.zP = self.zQ = self.zR = 0
    
		for self.coord in range(0,3):
			if self.coord == 0:
				self.xP = self.PointP[self.coord]
				self.xQ = self.PointQ[self.coord]
				self.xR = self.PointR[self.coord]
				
			elif self.coord == 1:
				self.yP = self.PointP[self.coord]
				self.yQ = self.PointQ[self.coord]
				self.yR = self.PointR[self.coord]
				
			elif self.coord == 2:
				self.zP = self.PointP[self.coord]
				self.zQ = self.PointQ[self.coord]
				self.zR = self.PointR[self.coord]  
					
		self.PointP = (self.xP,self.yP,self.zP)
		print('\n\t- The (Point P): P',self.PointP)
		self.PointQ = (self.xQ,self.yQ,self.zQ)
		print('\t- The (Point Q): Q',self.PointQ)
		self.PointR = (self.xR,self.yR,self.zR)
		print('\t- The (Point R): R',self.PointR)
		answer.view_solution()
		
		for op in range (0,3):
			# Will find the scalar product: b * c
			if op == 0:
				self.vectorAC = []
				self.vectorAB = []
				
				for p in range (0,3):
					self.compAC = ( self.pointC[p] - self.pointA[p] )
					self.vectorAC.append(self.compAC)
					self.compAB = ( self.pointB[p] - self.pointA[p] )
					self.vectorAB.append(self.compAB)
					
				self.vectorB = self.vectorAC
				self.vectorC = self.vectorAB
				print('\t- The [vectorB]=vectorPR',self.vectorB)
				print('\t- The [vectorC]=vectorPQ',self.vectorC,'\n')

				# In definition of the InnerAngleTriangle class is necessary create the atributes: self.VectorBC = 0,
				# and too self.vectorBC = 0. -- [ self.VectorBC != self.vectorBC ].
				
				self.scalarProductBC = 0
				self.VectorBC = []
				
				for d0 in range (0,3):
					self.term0 = self.vectorAC[d0] * self.vectorAB[d0]
					self.scalarProductBC = self.scalarProductBC + self.term0
					self.VectorBC.append(self.term0)
					
				self.b1 = self.vectorB[0]
				magnitudeTriVector.x = self.b1  
				self.b2 = self.vectorB[1]
				magnitudeTriVector.y = self.b2
				self.b3 = self.vectorB[2]
				magnitudeTriVector.z = self.b3
				self.normB = magnitudeTriVector.magtrivector()
				self.sideB = self.normB
				self.c1 = self.vectorC[0]
				magnitudeTriVector.x = self.c1
				self.c2 = self.vectorC[1]
				magnitudeTriVector.y = self.c2
				self.c3 = self.vectorC[2]
				magnitudeTriVector.z = self.c3
				self.normC = magnitudeTriVector.magtrivector()
				self.sideC = self.normC
				self.normBxCproduct = ( self.normB * self.normC )
				
			elif op == 1:
				# Will find the scalar product: a * c
				self.vectorBC = []
				self.vectorBA = []

				for q in range (0,3):
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

				for d1 in range (0,3):
					self.term1 = self.vectorBC[d1] * self.vectorBA[d1]
					self.scalarProductAC = self.scalarProductAC + self.term1
					self.vectorAC.append(self.term1)
					
				self.a1 = self.vectorA[0]
				magnitudeTriVector.x = self.a1
				self.a2 = self.vectorA[1]
				magnitudeTriVector.y = self.a2
				self.a3 = self.vectorA[2]
				magnitudeTriVector.z = self.a3
				self.normA = magnitudeTriVector.magtrivector()
				self.sideA = self.normA
				self.c1 = self.vectorC[0]
				magnitudeTriVector.x = self.c1
				self.c2 = self.vectorC[1]
				magnitudeTriVector.y = self.c2
				self.c3 = self.vectorC[2]
				magnitudeTriVector.z = self.c3
				self.normC = magnitudeTriVector.magtrivector()
				self.sideC = self.normC
				self.normAxCproduct = ( self.normA * self.normC )
				
			elif op == 2:
				# Will find the scalar product: a * b
				self.vectorCB = []
				self.vectorCA = []

				for r in range (0,3):
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

				for d2 in range (0,3):
					self.term2 = self.vectorCB[d2] * self.vectorCA[d2]
					self.scalarProductAB = self.scalarProductAB + self.term2
					self.vectorAB.append(self.term2)
					
				self.a1 = self.vectorA[0]
				magnitudeTriVector.x = self.a1
				self.a2 = self.vectorA[1]
				magnitudeTriVector.y = self.a2
				self.a3 = self.vectorA[2]
				magnitudeTriVector.z = self.a3
				self.normA = magnitudeTriVector.magtrivector()
				self.sideA = self.normA
				
				self.b1 = self.vectorB[0]
				magnitudeTriVector.x = self.b1
				self.b2 = self.vectorB[1]
				magnitudeTriVector.y = self.b2
				self.b3 = self.vectorB[2]
				magnitudeTriVector.z = self.b3 
				self.normB = magnitudeTriVector.magtrivector()
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

class MixedProduct:
	'''
	------------------------------------------------------------------------------------------------------------------
	This Class MixedProduct after enter all the [coomponents]: self.a1, self.a2, self.a3, self.b1, self.b2, self.b3,  
	self.c1, self.c2, and self.c3 of the self.vectorA, self.vectorB and self.vectorC or the [coordinates] of the given 
	points: P,Q, R, and S will find the [vectors] represented by self.vectorA = self.vectorPQ, self.vectorB = 
	self.vectorPR, and self.vectorC = self.vectorPS and will determine the Mixed Product given to:
	
                                                      | a1  a2  a3 |
    	volume(V) = abs ( vectorA * (B x C) ) = abs ( | b1  b2  b3 | ),    
                                                      | c1  c2  c3 |    
                                                                  						                                                         
    	will calculate the [value] of the [determinant of the ( 3 x 3) matrix] by [Theorem of Sarru's] that is                                                               					
    	the [volume_V(P)] of the [Parallelepiped] and too will find also the [volume_V(T) of the [Tetrahedron]. 
    	------------------------------------------------------------------------------------------------------------------
    	'''
	def __init__(self, add = 0, Area = 0, a1 = 0, a2 = 0, a3 = 0, b1 = 0, b2 = 0, b3 = 0, c1 = 0, c2 = 0, c3 = 0,
	coefficient = 0, comp0 = 0, comp1 = 0, comp2 = 0, coordP = 0, coordQ = 0, coordR = 0, coordS = 0, Cx = 0, Cy = 0,
	Cz = 0, normA = 0, normB = 0, normC = 0, NormAxB = 0, normVectorAxB = 0, heightParallelep = 0, parallelepiped = 0,
	alpha = 0, p1 = 0, p2 = 0, p3 = 0, p4 = 0, p5 = 0, p6 = 0, Perimeter = 0, pointP = 0, PointP = 0, pointQ = 0,
	PointQ = 0, pointR = 0, PointR = 0, pointS = 0, PointS = 0, xP = 0, yP = 0, zP = 0, xQ = 0, yQ = 0, zQ = 0,
	xR = 0, yR = 0, zR = 0, xS = 0, yS = 0, zS = 0, sideA = 0, sideB = 0, sideC = 0, vectorA = 0, vectorB = 0, 
	vectorC = 0, vectorAxB = [], vectorPQ = [], vectorPR = [], vectorPS = [], term = 0, theta = 0, tetrahedron = 0,
	volume = 0, mixedProduct = 0, number = 0, number1 = 0):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.add = add
		self.alpha = alpha
		self.theta = theta
		self.Area = Area
		
		self.b1 = b1
		self.b2 = b2
		self.b3 = b3
		
		self.coefficient = coefficient
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		
		self.sideA = sideA 
		self.sideB = sideB 
		self.sideC = sideC
		
		self.comp0 = comp0
		self.comp1 = comp1
		self.comp2 = comp2
		
		self.coordP = coordP
		self.coordQ = coordQ
		self.coordR = coordR
		self.coordS = coordS
	
		self.Cx = Cx
		self.Cy = Cy
		self.Cz = Cx
	
		self.mixedProduct = mixedProduct
		
		self.number = number
		self.number1 = number1
		
		self.normA = normA
		self.normB = normB
		self.normC = normC
		
		self.vectorA = vectorA
		self.vectorB = vectorB
		self.vectorC = vectorC
		
		self.vectorAxB = vectorAxB
		self.normVectorAxB = normVectorAxB
		
		self.vectorPQ = []
		self.vectorPR = []
		self.vectorPS = []
		
		self.parallelepiped = parallelepiped
		self.heightParallelep = heightParallelep
		self.Perimeter = Perimeter
		
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4
		self.p5 = p5
		self.p6 = p6
		
		self.pointP = pointP
		self.pointQ = pointQ 
		self.pointR = pointR
		self.pointS = pointS
		
		self.PointP = PointP
		self.PointQ = PointQ 
		self.PointR = PointR
		self.PointS = PointS
		
		self.sideA = sideA 
		self.sideB = sideB 
		self.sideC = sideC
		
		self.term = term
		self.volume = volume
	
		self.xP = xP
		self.xQ = xQ
		self.xR = xR
		self.xS = xS
		
		self.yP = yP 
		self.yQ = yQ
		self.yR = yR
		self.yS = yS
		
		self.zP = zP 
		self.zQ = zQ
		self.zR = zR
		self.zS = zS
		
	def findMixedProduct(self):
		# Give the [coordinates] of the vertice points: P, Q, R and S of a Parallelepiped or
		# the [components] of the vectors: vectorA, vectorB, and vectorC
		print('\n\t\t*[NEW INSTRUCTIONS]*\n')
		print('\t* Type [1] to enter all the [Coordinate] points: P, Q, R and S or')
		print('\t* Type [2] and provide all the [Component] vectors: vectorA, vectorB and vectorC.\n')
		
		number = selectOption.provide_Option()		
		mixed_product.number = number
		
		if self.number == 1:
			pointcoordinates3d.number1 = 1
			self.coordP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 2
			self.coordQ = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.coordR = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 4
			self.coordS = pointcoordinates3d.getpointcoordinates3d()
		
			self.xP = self.xQ = self.xR = self.xS = 0
			self.yP = self.yQ = self.yR = self.yS = 0
			self.zP = self.zQ = self.zR = self.zS = 0
			
			for t in range(0,3):
				if t == 0:
					self.xP = self.coordP[t]
					self.xQ = self.coordQ[t]
					self.xR = self.coordR[t]
					self.xS = self.coordS[t]
				elif t == 1:
					self.yP = self.coordP[t]
					self.yQ = self.coordQ[t]
					self.yR = self.coordR[t]
					self.yS = self.coordS[t]
				elif t == 2:
					self.zP = self.coordP[t]
					self.zQ = self.coordQ[t]
					self.zR = self.coordR[t]
					self.zS = self.coordS[t]
					
			self.PointP = (self.xP,self.yP,self.zP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\t- The (Point Q): Q',self.PointQ)
			self.PointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.PointR)
			self.PointS = (self.xS,self.yS,self.zS)
			print('\t- The (Point S): S',self.PointS)
				
			self.vectorPQ = []
			self.vectorPR = []
			self.vectorPS = []
			
			for h in range (0,3):
				self.comp0 = self.coordQ[h] - self.coordP[h]
				self.vectorPQ.append(self.comp0)
				self.comp1 = self.coordR[h] - self.coordP[h]
				self.vectorPR.append(self.comp1)
				self.comp2 = self.coordS[h] - self.coordP[h]
				self.vectorPS.append(self.comp2)
			
			self.vectorA = self.vectorPQ
			self.vectorB = self.vectorPR
			self.vectorC = self.vectorPS
				
		elif self.number == 2:
			self.vectorA = compvector.getcomponent3dvectorA() 
			self.vectorB = compvector.getcomponent3dvectorB()
			self.vectorC = compvector.getcomponent3dvectorC()
		
		answer.view_solution()		
		# self.vectorA = self.vectorPQ
		print('\t-- The [vectorA]: vectorA',self.vectorA)
		# self.vectorB = self.vectorPR
		print('\t-- The [vectorB]: vectorB',self.vectorB)
		# self.vectorC = self.vectorPS
		print('\t-- The [vectorC]: vectorC',self.vectorC)
		
		# The area S of the trianglePQR
		# The [components] Vector: A and B
		self.a1 = self.vectorA[0]
		self.a2 = self.vectorA[1]
		self.a3 = self.vectorA[2]
		magnitudeTriVector.x = self.a1
		magnitudeTriVector.y = self.a2
		magnitudeTriVector.z = self.a3
		self.normA = magnitudeTriVector.magtrivector()
		self.b1 = self.vectorB[0]
		self.b2 = self.vectorB[1]
		self.b3 = self.vectorB[2]
		magnitudeTriVector.x = self.b1
		magnitudeTriVector.y = self.b2
		magnitudeTriVector.z = self.b3
		self.normB = magnitudeTriVector.magtrivector()
		self.c1 = self.vectorC[0]
		self.c2 = self.vectorC[1]
		self.c3 = self.vectorC[2]
		magnitudeTriVector.x = self.c1
		magnitudeTriVector.y = self.c2
		magnitudeTriVector.z = self.c3
		self.normC = magnitudeTriVector.magtrivector()
		
		# Determine the Mixed Product
		self.p1 = self.vectorA[0] * self.vectorB[1] * self.vectorC[2]
		self.p2 = self.vectorA[1] * self.vectorB[2] * self.vectorC[0]
		self.p3 = self.vectorA[2] * self.vectorB[0] * self.vectorC[1]
		self.express1 = self.p1 + self.p2 + self.p3
		
		self.p4 = self.vectorA[2] * self.vectorB[1] * self.vectorC[0]
		self.p5 = self.vectorA[0] * self.vectorB[2] * self.vectorC[1]
		self.p6 = self.vectorA[1] * self.vectorB[0] * self.vectorC[2]
		self.express2 = self.p4 + self.p5 + self.p6
		
		self.mixedProduct = (self.express1 - self.express2)
		print('\n\t-- The value of the [Mixed Product: a * ( b x c )] finded:', self.mixedProduct)
		return
		
	def determine_heigth_Volume(self):
		mixed_product.findMixedProduct()
		# Will determine the volume_V(P) of a Parallelepiped
		self.parallelepiped = abs(self.express1 - self.express2)
		# find the Cross Product(AxB)
		self.Cx = ( ( self.vectorA[1] * self.vectorB[2] ) - ( self.vectorA[2] * self.vectorB[1] ) )
		self.vectorAxB.append(self.Cx)
		self.Cy = ( ( self.vectorA[2] * self.vectorB[0] ) - ( self.vectorA[0] * self.vectorB[2] ) )
		self.vectorAxB.append(self.Cy)
		self.Cz = ( ( self.vectorA[0] * self.vectorB[1] ) - ( self.vectorA[1] * self.vectorB[0] ) )
		self.vectorAxB.append(self.Cz)
		
		magnitudeTriVector.x = self.Cx
		magnitudeTriVector.y = self.Cy
		magnitudeTriVector.z = self.Cz
		self.normVectorAxB = magnitudeTriVector.magtrivector()
		
		# Will determine the Height(h) of a Parallelepiped and too 
		# the Volume_V(T) of a [Tetrahedron]
		self.heightParallelep = ( self.parallelepiped / self.normVectorAxB )
		self.tetrahedron = self.parallelepiped / 6
		
		print('\t-- The [vectorAxB]: vectorAxB',self.vectorAxB)
		print(f'\t-- The ||normVectorAxB|| is {self.normVectorAxB:<.2f}','\n')
		print(f'\t-- The [Height(h)] of a Parallelepiped is {self.heightParallelep:<.2f}')
		print(f'\t-- The [Volume_V(P)] of a Parallelepiped is {self.parallelepiped:<.2f}')
		print(f'\t-- The [Volume_V(T)] of a [Tetrahedron] is {self.tetrahedron:<.2f}')
		return   

mixed_product = MixedProduct()

class EnterCoordPointPQ:
	'''Given any two points: P and Q find the vector A'''
	def __init__(self, coord = 0, pointP = [], pointQ = [], PointP = (), PointQ = (), xP = 0, yP = 0, zP = 0,
	xQ = 0, yQ = 0, zQ = 0):
		self.coord = coord
		self.pointP = pointP
		self.pointQ = pointQ
		
		self.PointP = pointP
		self.PointQ = pointQ
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
	def findcoord_pointPQ(self):
		'''Will find the coordinates of two points: P and Q.'''
		pointcoordinates3d.number1 = 1
		self.pointP = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 2
		self.pointQ = pointcoordinates3d.getpointcoordinates3d()
		
		self.xP = self.yP = self.zP = self.xQ = self.yQ = self.zQ = 0
		
		for self.coord in range(0,3):
			if self.coord == 0:
				self.xP = self.pointP[self.coord]
				self.xQ = self.pointQ[self.coord]
			elif self.coord == 1:
				self.yP = self.pointP[self.coord]
				self.yQ = self.pointQ[self.coord]
			elif self.coord == 2:
				self.zP = self.pointP[self.coord]
				self.zQ = self.pointQ[self.coord]

		self.PointP = (self.xP,self.yP,self.zP)
		print('\n\t- The (Point P): P', self.PointP)
		self.PointQ = (self.xQ,self.yQ,self.zQ)
		print('\t- The (Point Q): Q', self.PointQ,'\n')
		return 

findcoordpq = EnterCoordPointPQ()

class FindVectorA:
	def __init__(self, a1 = 0, a2 = 0, a3 = 0, normA = 0, pointP = [], pointQ = [], vectorA = 0, vectorPQ = [],
	xP = 0, yP = 0, zP = 0, xQ = 0, yQ = 0, zQ = 0):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		
		self.normA = normA
		self.pointP = pointP
		self.pointQ = pointQ
		self.vectorA = vectorA
		self.vectorPQ = vectorPQ
		
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
	def find_vectorA(self):
		self.xP = findcoordpq.xP
		self.pointP.append(self.xP)
		self.yP = findcoordpq.yP
		self.pointP.append(self.yP)
		self.zP = findcoordpq.zP
		self.pointP.append(self.zP)
		
		self.xQ = findcoordpq.xQ
		self.pointQ.append(self.xQ)
		self.yQ = findcoordpq.yQ
		self.pointQ.append(self.yQ)
		self.zQ = findcoordpq.zQ
		self.pointQ.append(self.zQ)
		
		for h in range (0,3):
			self.coord = self.pointQ[h] - self.pointP[h]
			self.vectorPQ.append(self.coord)
			
		self.vectorA = self.vectorPQ
		self.a1 = self.vectorA[0]
		magnitudeTriVector.x = self.a1
		self.a2 = self.vectorA[1]
		magnitudeTriVector.y = self.a2
		self.a3 = self.vectorA[2]
		magnitudeTriVector.z = self.a3
		self.normA = magnitudeTriVector.magtrivector()
		answer.view_solution()
		print('\t-- The [vectorA]: vectorA=vectorPQ', self.vectorA)
		print(f'\t-- The [lenghtPQ = distPQ] is the ||vectorPQ||: {self.normA:<.2f}','\n')
		return self.vectorA

findvectorA = FindVectorA()

class EnterCoordPointPR:
	'''Given any two points: P and R find the vector B'''
	def __init__(self, coord = 0, pointP = [], pointR = [], PointP = (), PointR = (), xP = 0, yP = 0, zP = 0, xR = 0,
	yR = 0, zR = 0):
		self.coord = coord
		self.pointP = pointP
		self.pointR = pointR
		
		self.PointP = PointP
		self.PointR = PointR
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
	def findcoord_pointPR(self):
		'''Will find the coordinates of two points: P and R.'''
		pointcoordinates3d.number1 = 1
		self.pointP = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 3
		self.pointR = pointcoordinates3d.getpointcoordinates3d()
		
		self.xP = self.yP = self.zP = self.xR = self.yR = self.zR = 0
		
		for self.coord in range(0,3):
			if self.coord == 0:
				self.xP = self.pointP[self.coord]
				self.xR = self.pointR[self.coord]
			elif self.coord == 1:
				self.yP = self.pointP[self.coord]
				self.yR = self.pointR[self.coord]
			elif self.coord == 2:
				self.zP = self.pointP[self.coord]
				self.zR = self.pointR[self.coord]

		self.PointP = (self.xP,self.yP,self.zP)
		print('\n\t- The (Point P): P', self.PointP)
		self.PointR = (self.xR,self.yR,self.zR)
		print('\t- The (Point R): R', self.PointR,'\n')
		return 

findcoordpr = EnterCoordPointPR()

class FindVectorB:
	def __init__(self, b1 = 0, b2 = 0, b3 = 0, normB = 0, pointP = [], pointR = [], vectorB = 0, vectorPR = [], 
	xP = 0, yP = 0, zP = 0, xR = 0, yR = 0, zR = 0):
		self.b1 = b1
		self.b2 = b2
		self.b3 = b3
		
		self.normB = normB
		self.pointP = pointP
		self.pointR = pointR
		
		self.vectorB = vectorB
		self.vectorPR = vectorPR
		
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
	def find_vectorB(self):
		self.xP = findcoordpr.xP
		self.pointP.append(self.xP)
		self.yP = findcoordpr.yP
		self.pointP.append(self.yP)
		self.zP = findcoordpr.zP
		self.pointP.append(self.zP)
		
		self.xR = findcoordpr.xR
		self.pointR.append(self.xR)
		self.yR = findcoordpr.yR
		self.pointR.append(self.yR)
		self.zR = findcoordpr.zR
		self.pointR.append(self.zR)
		
		for h in range (0,3):
			self.coord = self.pointR[h] - self.pointP[h]
			self.vectorPR.append(self.coord)
			
		self.vectorB = self.vectorPR
		self.b1 = self.vectorB[0]
		magnitudeTriVector.x = self.b1
		self.b2 = self.vectorB[1]
		magnitudeTriVector.y = self.b2
		self.b3 = self.vectorB[2]
		magnitudeTriVector.z = self.b3
		self.normB = magnitudeTriVector.magtrivector()
		
		answer.view_solution()
		print('\t-- The [vectorB]: vectorB=vectorPR', self.vectorB)
		print(f'\t-- The [lenghtPR = distPR] is the ||vectorPR||: {self.normB:<.2f}','\n')
		return self.vectorB

findvectorB = FindVectorB()

class EnterCoordPointQR:
	'''Given any two points: Q and R find the vector C'''
	def __init__(self, coord = 0, pointQ = [], pointR = [], PointQ = (), PointR = (), xQ = 0, yQ = 0, zQ = 0, xR = 0,
	yR = 0, zR = 0):
		self.coord = coord
		self.pointQ = pointQ
		self.pointR = pointR
		
		self.PointQ = PointQ
		self.PointR = PointR
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
		
	def findcoord_pointQR(self):
		'''Will find the coordinates of two points: Q and R.'''
		pointcoordinates3d.number1 = 2
		self.pointQ = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 3
		self.pointR = pointcoordinates3d.getpointcoordinates3d()
		
		self.xQ = self.yQ = self.zQ = self.xR = self.yR = self.zR = 0
		
		for self.coord in range(0,3):
			if self.coord == 0:
				self.xQ = self.pointQ[self.coord]
				self.xR = self.pointR[self.coord]
			elif self.coord == 1:
				self.yQ = self.pointQ[self.coord]
				self.yR = self.pointR[self.coord]
			elif self.coord == 2:
				self.zQ = self.pointQ[self.coord]
				self.zR = self.pointR[self.coord]

		self.PointQ = (self.xQ,self.yQ,self.zQ)
		print('\n\t- The (Point Q): Q', self.PointQ)
		self.PointR = (self.xR,self.yR,self.zR)
		print('\t- The (Point R): R', self.PointR,'\n')
		return 
		
findcoordqr = EnterCoordPointQR()

class FindVectorC:
	def __init__(self, c1 = 0, c2 = 0, c3 = 0, normC = 0, pointQ = [], pointR = [], vectorC = 0, vectorQR = [],
	xQ = 0, yQ = 0, zQ = 0, xR = 0, yR = 0, zR = 0):
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		self.normC = normC
		self.pointQ = pointQ
		self.pointR = pointR
		
		self.vectorC = vectorC
		self.vectorQR = vectorQR
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
	def find_vectorC(self):
		self.xQ = findcoordqr.xQ
		self.pointQ.append(self.xQ)
		self.yQ = findcoordqr.yQ
		self.pointQ.append(self.yQ)
		self.zQ = findcoordqr.zQ
		self.pointQ.append(self.zQ)
		
		self.xR = findcoordqr.xR
		self.pointR.append(self.xR)
		self.yR = findcoordqr.yR
		self.pointR.append(self.yR)
		self.zR = findcoordqr.zR
		self.pointR.append(self.zR)
		
		for h in range (0,3):
			self.coord = self.pointR[h] - self.pointQ[h]
			self.vectorQR.append(self.coord)
			
		self.vectorC = self.vectorQR
		self.c1 = self.vectorC[0]
		magnitudeTriVector.x = self.c1
		self.c2 = self.vectorC[1]
		magnitudeTriVector.y = self.c2
		self.c3 = self.vectorC[2]
		magnitudeTriVector.z = self.c3
		self.normC = magnitudeTriVector.magtrivector()
		answer.view_solution()
		print('\t-- The [vectorC]: vectorC=vectorQR', self.vectorC)
		print(f'\t-- The [lenghtQR = distQR] is the ||vectorQR||: {self.normC:<.2f}','\n')
		return self.vectorC

findvectorC = FindVectorC()

class EnterCoordPointRS:
	'''Given any two points: Q and R find the vector C'''
	def __init__(self, coord = 0, pointR = [], pointS = [], PointR = (), PointS = (), xR = 0, yR = 0, zR = 0, xS = 0,   
	yS = 0, zS = 0,):
		self.coord = coord
		self.pointR = pointR
		self.pointS = pointS
		
		self.PointR = PointR
		self.PointS = PointS
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
		self.xS = xS
		self.yS = yS
		self.zS = zS
		
	def getcoord_pointRS(self):
		'''Will find the coordinates of two points: Q and R.'''
		pointcoordinates3d.number1 = 3
		self.pointR = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 4
		self.pointS = pointcoordinates3d.getpointcoordinates3d()
		
		self.xR = self.yR = self.zR = 0
		self.xS = self.yS = self.zS = 0 
		
		for self.coord in range(0,3):
			if self.coord == 0:
				self.xR = self.pointR[self.coord]
				self.xS = self.pointS[self.coord]
			elif self.coord == 1:
				self.yR = self.pointR[self.coord]
				self.yS = self.pointS[self.coord]
			elif self.coord == 2:
				self.zR = self.pointR[self.coord]
				self.zS = self.pointS[self.coord]

		self.PointR = (self.xR,self.yR,self.zR)
		print('\n\t- The (Point R): R', self.PointR)
		self.PointS = (self.xS,self.yS,self.zS)
		print('\t- The (Point S): S', self.PointS,'\n')
		return 
		
enterCoordrs = EnterCoordPointRS()

class FindVectorD:
	def __init__(self, d1 = 0, d2 = 0, d3 = 0, normD = 0, pointR = [], pointS = [], vectorD = 0, vectorRS = [],
	xR = 0, yR = 0, zR = 0, xS = 0, yS = 0, zS = 0 ):
		self.d1 = d1
		self.d2 = d2
		self.d3 = d3
		self.normD = normD
		self.pointR = pointR
		self.pointS = pointS
		
		self.vectorD = vectorD
		self.vectorRS = vectorRS
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
		self.xS = xS
		self.yS = yS
		self.zS = zS
		
	def find_vectorD(self):
		self.xR = enterCoordrs.xR
		self.pointR.append(self.xR)
		self.yR = enterCoordrs.yR
		self.pointR.append(self.yR)
		self.zR = enterCoordrs.zR
		self.pointR.append(self.zR)
		
		self.xS = enterCoordrs.xS
		self.pointS.append(self.xS)
		self.yS = enterCoordrs.yS
		self.pointS.append(self.yS)
		self.zS = enterCoordrs.zS
		self.pointS.append(self.zS)
		
		for h in range (0,3):
			self.coord = self.pointS[h] - self.pointR[h]
			self.vectorRS.append(self.coord)
			
		self.vectorD = self.vectorRS
		self.d1 = self.vectorD[0]
		magnitudeTriVector.x = self.d1
		self.d2 = self.vectorD[1]
		magnitudeTriVector.y = self.d2
		self.d3 = self.vectorD[2]
		magnitudeTriVector.z = self.d3
		self.normD = magnitudeTriVector.magtrivector()
		answer.view_solution()
		print('\t-- The [vectorD]: vectorD=vectorRS', self.vectorD)
		print(f'\t-- The [lenghtRS = distRS] is the ||vectorRS||: {self.normD:<.2f}','\n')
		return self.vectorD

getvectorD = FindVectorD()

class VerticesTriangle3d:
	'''
	Given the Midpoints: K(xK,yK,zK), L(xL,yL,zL), and M(xM,yM,zM) of a Triangle(PQR) will find the vertice points: P(xP,yP,zP),
	Q(xQ,yQ,zQ), and R(xR,yR,zR) of the Triangle(PQR).
	'''
	def __init__(self, coord = 0, number4 = 0, midpointK = [], midpointL = [], midpointM = [], PointK = (), 
	PointL = (), PointM = (), PointP = (), PointQ = (), PointR = (), xK = 0, yK = 0, zK = 0, xL = 0, yL = 0, zL = 0,
	xM = 0, yM = 0, zM = 0, xP = 0, yP = 0, zP = 0, xQ = 0, yQ = 0, zQ = 0, xR = 0, yR = 0, zR = 0 ):
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
		self.zK = zK
		
		self.xL = xL 
		self.yL = yL
		self.zL = zL
		
		self.xM = xM 
		self.yM = yM
		self.zM = zM
		
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
	def enter_midpoints3d(self):
		pointcoordinates3d.number1 = 5
		self.midpointK = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 6
		self.midpointL = pointcoordinates3d.getpointcoordinates3d()
		pointcoordinates3d.number1 = 7
		self.midpointM = pointcoordinates3d.getpointcoordinates3d()
		return
		
	def find_verticeP3d(self):
		vertices_triangle3d.enter_midpoints3d()
		
		for i in range(0,3):
			if i == 0:
				self.xK = self.midpointK[i]
				self.xL = self.midpointL[i]
				self.xM = self.midpointM[i]
			elif i == 1:
				self.yK = self.midpointK[i]
				self.yL = self.midpointL[i]
				self.yM = self.midpointM[i]
			elif i == 2:
				self.zK = self.midpointK[i]
				self.zL = self.midpointL[i]
				self.zM = self.midpointM[i]
				
		self.xP = ( self.xK + self.xL ) - self.xM
		self.yP = ( self.yK + self.yL ) - self.yM
		self.zP = ( self.zK + self.zL ) - self.zM
		
		self.PointP = (self.xP,self.yP,self.zP)
		answer.view_solution() 
		print('\t- The (Point P): P',self.PointP)
		return
		
	def find_verticeQ3d(self):
		vertices_triangle3d.enter_midpoints3d()
		
		for j in range(0,3):
			if j == 0:
				self.xK = self.midpointK[j]
				self.xL = self.midpointL[j]
				self.xM = self.midpointM[j]
			elif j == 1:
				self.yK = self.midpointK[j]
				self.yL = self.midpointL[j]
				self.yM = self.midpointM[j]
			elif j == 2:
				self.zK = self.midpointK[j]
				self.zL = self.midpointL[j]
				self.zM = self.midpointM[j]
				
		self.xQ = ( self.xM + self.xK ) - self.xL
		self.yQ = ( self.yM + self.yK ) - self.yL
		self.zQ = ( self.zM + self.zK ) - self.zL
		
		self.PointQ = (self.xQ,self.yQ, self.zQ)
		answer.view_solution() 
		print('\t- The (Point Q): Q',self.PointQ)
		return
		
	def find_verticeR3d(self):
		vertices_triangle3d.enter_midpoints3d()
		
		for k in range(0,3):
			if k == 0:
				self.xK = self.midpointK[k]
				self.xL = self.midpointL[k]
				self.xM = self.midpointM[k]
			elif k == 1:
				self.yK = self.midpointK[k]
				self.yL = self.midpointL[k]
				self.yM = self.midpointM[k]
			elif k == 2:
				self.zK = self.midpointK[k]
				self.zL = self.midpointL[k]
				self.zM = self.midpointM[k]
				
		self.xR = ( self.xL + self.xM ) - self.xK
		self.yR = ( self.yL + self.yM ) - self.yK
		self.zR = ( self.zL + self.zM ) - self.zK
		
		self.PointR = (self.xR,self.yR,self.zR)
		answer.view_solution() 
		print('\t- The (Point R): R',self.PointR)
		return
		
	def determine_verticesPQR3d(self):
		vertices_triangle3d.enter_midpoints3d()
		
		for n in range(0,3):
			if n == 0:
				self.xK = self.midpointK[n]
				self.xL = self.midpointL[n]
				self.xM = self.midpointM[n]
			elif n == 1:
				self.yK = self.midpointK[n]
				self.yL = self.midpointL[n]
				self.yM = self.midpointM[n]
			elif n == 2:
				self.zK = self.midpointK[n]
				self.zL = self.midpointL[n]
				self.zM = self.midpointM[n]
				
		self.xP = ( self.xK + self.xL ) - self.xM
		self.yP = ( self.yK + self.yL ) - self.yM
		self.zP = ( self.zK + self.zL ) - self.zM
		
		self.xR = ( self.xL + self.xM ) - self.xK
		self.yR = ( self.yL + self.yM ) - self.yK
		self.zR = ( self.zL + self.zM ) - self.zK
		
		self.xQ = ( self.xM + self.xK ) - self.xL
		self.yQ = ( self.yM + self.yK ) - self.yL
		self.zQ = ( self.zM + self.zK ) - self.zL
		
		self.PointP = (self.xP,self.yP,self.zP)
		self.PointQ = (self.xQ,self.yQ, self.zQ)
		self.PointR = (self.xR,self.yR,self.zR) 
		
		answer.view_solution() 
		print('\t- The (Point P): P',self.PointP)
		print('\t- The (Point Q): Q',self.PointQ)
		print('\t- The (Point R): R',self.PointR,'\n')
		
		return
		
	def select_findVertice3d(self):
		'''Select what vertice of the Triangle(PQR): P or Q or R will calculate.'''
		print('\n\t\t\t*[NEW INSTRUCTIONS]*\n')
		print('\t\t- Type [1] to find the only vertice: P(xP,yP,zP) of a triangle(PQR).')
		print('\t\t- Type [2] to get the only vertice: Q(xQ,yQ,zQ) of a triangle(PQR).')
		print('\t\t- Type [3] to find the only vertice: R(xR,yR,zR) of a triangle(PQR).')
		print('\t\t- Type [4] to determine the [three vertice points]: P(xP,yP,zP),') 
		print('\t\t  Q(xQ,yQ,zQ), and R(xR,yR,zR) of a triangle(PQR).','\n')
		self.number4 = vector.enterIntegerData()
		
		if self.number4 == 1:
			vertices_triangle3d.find_verticeP3d()
		elif self.number4 == 2:
			vertices_triangle3d.find_verticeQ3d()
		elif self.number4 == 3:
			vertices_triangle3d.find_verticeR3d()
		elif self.number4 == 4:
			vertices_triangle3d.determine_verticesPQR3d()
		else:
			textstring3.error_option()	
		return
								
vertices_triangle3d = VerticesTriangle3d()

class Cosine_Angle_Direction:
	'''Will the [components], lengthA, cosine and angles: Alpha, Beta and Gama directors.'''
	def __init__(self, addCos = 0, angle_radiansA = 0, angle_radiansB = 0, angle_radiansG = 0, a1 = 0, a2 = 0, a3 = 0,
	comp0 = 0, coordP = 0, coordQ = 0, cosineAlpha = 0, cosineBeta = 0, cosineGama = 0, angleAlpha_degreesA = 0,
	angleBeta_degreesB = 0, angleGama_degreesG = 0, lengthA = 0, number1 = 0, PointP = 0, PointQ = 0, 
	vectorComponentsA = 0, vectorPQ = [], xP = 0, yP = 0, zP = 0, xQ = 0, yQ = 0, zQ = 0 ):
		
		self.addCos = addCos
		self.angle_radiansA = angle_radiansA 
		self.angle_radiansB = angle_radiansB
		self.angle_radiansG = angle_radiansG
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		
		self.coordP = coordP 
		self.coordQ = coordQ
		self.cosineAlpha = cosineAlpha
		self.cosineBeta = cosineBeta
		self.cosineGama = cosineGama
		self.comp0 = comp0
		
		self.angleAlpha_degreesA = angleAlpha_degreesA
		self.angleBeta_degreesB = angleBeta_degreesB
		self.angleGama_degreesG = angleGama_degreesG
		self.lengthA = lengthA
		self.number1 = number1
		
		
		self.PointP = PointP
		self.PointQ = PointQ
		self.vectorComponentsA = vectorComponentsA
		self.vectorPQ = vectorPQ 
		
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
	def enter_Components_VectorA(self):
		print('\t*[NEW INSTRUCTIONS]*\n')
		print('\t- Type [1] to enter the [components] of vectorA.')
		print('\t- Type [2] to enter the [coordinats] of two givens points: P and Q.')
		number1 = selectOption.provide_Option()
		cosine_angleDirection.number = number1
		
		if self.number == 1:
			vectorComponentsA = compvector.getcomponent3dvectorA()
			
		elif self.number == 2:
			pointcoordinates3d.number1 = 1
			self.coordP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 2
			self.coordQ = pointcoordinates3d.getpointcoordinates3d()
			
			for u in range(0,3):
				if u == 0:
					self.xP = self.coordP[u]
					self.xQ = self.coordQ[u]
				elif u == 1:
					self.yP = self.coordP[u]
					self.yQ = self.coordQ[u]
				elif u == 2:
					self.zP = self.coordP[u]
					self.zQ = self.coordQ[u]
				
			self.PointP = (self.xP,self.yP,self.zP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\t- The (Point Q): Q',self.PointQ)
			
			self.vectorPQ = []
			
			for h in range (0,3):
				self.comp0 = self.coordQ[h] - self.coordP[h]
				self.vectorPQ.append(self.comp0)
					
			vectorComponentsA = self.vectorPQ
		
		else:
			textstring3.error_option()
			return
			
		answer.view_solution()
		
		self.a1 = vectorComponentsA[0]
		self.a2 = vectorComponentsA[1]
		self.a3 = vectorComponentsA[2]
		
		magnitudeTriVector.x = self.a1
		magnitudeTriVector.y = self.a2
		magnitudeTriVector.z = self.a3
		self.lengthA = magnitudeTriVector.magtrivector()
		
		print('\t- The [vectorA] = vectorA', vectorComponentsA)
		print(f'\t- The [value] of [lengthA] = ||vectorA|| is {self.lengthA:<.2f}','\n')
		
		self.cosineAlpha = self.a1 / self.lengthA
		self.cosineBeta = self.a2 / self.lengthA
		self.cosineGama = self.a3 / self.lengthA
		
		self.addCos = ( pow(self.cosineAlpha,2) + pow(self.cosineBeta,2) + pow(self.cosineGama,2) )

		if self.addCos == 1.0:
			print('\t**[ (COSINEALPHA)² + (COSINEBETA)² + (COSINEGAMA)² = 1 ]**\n')

		print(f'\t-- The [value] of the [CosineAlpha] is {self.cosineAlpha:<.2f}')
		print(f'\t-- The [value] of the [CosineBeta] is {self.cosineBeta:<.2f}')
		print(f'\t-- The [value] of the [CosineGama] is {self.cosineGama:.2f}','\n')
		
		self.angle_radiansA = math.acos(self.cosineAlpha)
		self.angle_radiansB = math.acos(self.cosineBeta)
		self.angle_radiansG = math.acos(self.cosineGama)
		
		self.angleAlpha_degreesA = math.degrees(self.angle_radiansA)
		self.angleBeta_degreesB = math.degrees(self.angle_radiansB)
		self.angleGama_degreesG = math.degrees(self.angle_radiansG)
		
		print(f'\t-- The [value] of the [AlphaAngle] is {self.angleAlpha_degreesA:<.2f}')
		print(f'\t-- The [value] of the [BetaAngle] is {self.angleBeta_degreesB:<.2f}')
		print(f'\t-- The [value] of the [GamaAngle] is {self.angleGama_degreesG:<.2f}','\n')
		
		return 
		
cosine_angleDirection = Cosine_Angle_Direction()

class VectorAddSubMulScalar: 
	'''Will find the vectors: Add, Subtraction, and others - 172 lines'''
	def __init__(self, Addition = [], a1 = 0, a2 = 0, a3 = 0, coeffic1 = 0, coeffic2 = 0, comp0 = 0, comp1 = 0,
	coordP = 0, coordQ = 0, coordR = 0, number = 0, num1prod = 0, num2prod = 0, lengthA = 0, lengthS = 0,
	PointP = 0, PointQ = 0, PointR = 0, s1 = 0, s2 = 0, s3 = 0, Subtraction = [], vectorA = [], coeffic1VectorA = [],
	vectorB = [], coeffic2VectorB = [], vectorPQ = [], vectorPR = [], termA = 0, termS = 0, xP = 0, yP = 0, zP = 0,
	xQ = 0, yQ = 0, zQ = 0, xR = 0, yR = 0, zR = 0):
		self.Addition = Addition
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.coeffic1 = coeffic1 
		self.coeffic2 = coeffic2
		
		self.comp0 = comp0
		self.comp1 = comp1
		self.coordP = coordP
		self.coordQ = coordQ
		self.coordR = coordR
		
		self.number = number 
		self.num1prod = num1prod 
		self.num2prod = num2prod 
		
		self.lengthA = lengthA 
		self.Subtraction = Subtraction
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.lengthS = lengthS
		
		self.vectorA = vectorA
		self.coeffic1VectorA = coeffic1VectorA
		self.vectorB = vectorB  
		self.coeffic2VectorB = coeffic2VectorB
		self.termA = termA
		self.termS = termS
		
		self.vectorPQ = vectorPQ 
		self.vectorPR = vectorPR
		
		self.PointP = PointP
		self.PointQ = PointQ
		self.PointR = PointR
		
		self.xP = xP
		self.yP = yP
		self.zP = zP
		
		self.xQ = xQ
		self.yQ = yQ
		self.zQ = zQ
		
		self.xR = xR
		self.yR = yR
		self.zR = zR
		
	def data_enter(self):
		print('\t*[NEW INSTRUCTIONS]*\n')
		print('\t- To introduce the given [Coordinates] of the [points: P, Q, and R] type [1].')
		print('\t- To enter the given [Components] of [two vectors]: vectorA and vectorB] type [2].')
		number = selectOption.provide_Option()
		vectorAddSubMulscalar.number = number

		if self.number == 1:
			pointcoordinates3d.number1 = 1
			self.coordP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 2
			self.coordQ = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.coordR = pointcoordinates3d.getpointcoordinates3d()
			
			self.xP = self.xQ = self.xR = 0
			self.yP = self.yQ = self.yR = 0
			self.zP = self.zQ = self.zR = 0
			
			for v in range(0,3):
				if v == 0:
					self.xP = self.coordP[v]
					self.xQ = self.coordQ[v]
					self.xR = self.coordR[v]
					
				elif v == 1:
					self.yP = self.coordP[v]
					self.yQ = self.coordQ[v]
					self.yR = self.coordR[v]
					
				elif v == 2:
					self.zP = self.coordP[v]
					self.zQ = self.coordQ[v]
					self.zR = self.coordR[v]
					
			self.PointP = (self.xP,self.yP,self.zP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\t- The (Point Q): Q',self.PointQ)
			self.PointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.PointR)
				
			self.vectorPQ = []
			self.vectorPR = []
			
			for h in range (0,3):
				self.comp0 = self.coordQ[h] - self.coordP[h]
				self.vectorPQ.append(self.comp0)
				self.comp1 = self.coordR[h] - self.coordP[h]
				self.vectorPR.append(self.comp1)
				
			self.vectorA = self.vectorPQ
			self.vectorB = self.vectorPR
				
		elif self.number == 2:
			self.vectorA = compvector.getcomponent3dvectorA() 
			self.vectorB = compvector.getcomponent3dvectorB()
			
		else:
			textstring3.error_option()
			return
			
		answer.view_solution()
		print('\t-- The [vectorA]: vectorA', self.vectorA)
		print('\t-- The [vectorB]: vectorB', self.vectorB, '\n')
		
		print('\t- Enter with new [value] to the (1º)[coefficient]?')
		self.coeffic1 = introduce.enterRealData()
		print('\t- Give the new [value] to the (2º)[coefficient]?')
		self.coeffic2 = introduce.enterRealData()
		
		self.coeffic1VectorA = []
		self.coeffic2VectorB = []
		
		for p in range(0,3):
			self.num1prod = self.vectorA[p] * self.coeffic1
			self.coeffic1VectorA.append(self.num1prod)
			self.num2prod = self.vectorB[p] * self.coeffic2
			self.coeffic2VectorB.append(self.num2prod)

		answer.view_solution()
		print(f'\t+ The ({self.coeffic1}) * vectorA',self.coeffic1VectorA)
		print(f'\t+ The ({self.coeffic2}) * vectorB',self.coeffic2VectorB,'\n')
		
		self.Addition = []
		self.Subtraction = []
    
		for q in range(0,3):
			self.termA = ( self.coeffic1VectorA[q] + self.coeffic2VectorB[q] )
			self.Addition.append(self.termA)
			self.termS = ( self.coeffic1VectorA[q] - self.coeffic2VectorB[q] )
			self.Subtraction.append(self.termS)

		print(f'\t-- The vector( ({self.coeffic1})A + ({self.coeffic2})B )', self.Addition)
		print(f'\t-- The vector( ({self.coeffic1})A - ({self.coeffic2})B )', self.Subtraction,'\n')
		
		self.a1 = self.Addition[0]
		self.a2 = self.Addition[1]
		self.a3 = self.Addition[2]
		
		magnitudeTriVector.x = self.a1
		magnitudeTriVector.y = self.a2
		magnitudeTriVector.z = self.a3
		self.lengthA = magnitudeTriVector.magtrivector()
		
		self.s1 = self.Subtraction[0]
		self.s2 = self.Subtraction[1]
		self.s3 = self.Subtraction[2]
		
		magnitudeTriVector.x = self.s1
		magnitudeTriVector.y = self.s2
		magnitudeTriVector.z = self.s3
		self.lengthS = magnitudeTriVector.magtrivector()
		print(f'\t-- The [length] of the |vector( ({self.coeffic1})A + ({self.coeffic2})B )| is {self.lengthA:<.2f}')
		print(f'\t-- The [length] of the |vector( ({self.coeffic1})A - ({self.coeffic2})B )| is {self.lengthS:<.2f}','\n')
		
		return
		
vectorAddSubMulscalar = VectorAddSubMulScalar()

class Add_SubtractionVectors(VectorAddSubMulScalar):
	def __init__(self, Addition = [], a1 = 0, a2 = 0, a3 = 0, coeffic1 = 0, coeffic2 = 0, comp0 = 0, comp1 = 0,
	coordP = 0, coordQ = 0, coordR = 0, number = 0, num1prod = 0, num2prod = 0, lengthA = 0, lengthS = 0,
	PointP = 0, PointQ = 0, PointR = 0, s1 = 0, s2 = 0, s3 = 0, Subtraction = [], vectorA = [], coeffic1VectorA = [],
	vectorB = [], coeffic2VectorB = [], vectorPQ = [], vectorPR = [], termA = 0, termS = 0, xP = 0, yP = 0, zP = 0,
	xQ = 0, yQ = 0, zQ = 0, xR = 0, yR = 0, zR = 0):
		'''Use the attributes of the father class VectorAddSubMulScalar'''
		super().__init__(Addition = [], a1 = 0, a2 = 0, a3 = 0, coeffic1 = 0, coeffic2 = 0, comp0 = 0, comp1 = 0,
	coordP = 0, coordQ = 0, coordR = 0, number = 0, num1prod = 0, num2prod = 0, lengthA = 0, lengthS = 0,
	PointP = 0, PointQ = 0, PointR = 0, s1 = 0, s2 = 0, s3 = 0, Subtraction = [], vectorA = [], coeffic1VectorA = [],
	vectorB = [], coeffic2VectorB = [], vectorPQ = [], vectorPR = [], termA = 0, termS = 0, xP = 0, yP = 0, zP = 0,
	xQ = 0, yQ = 0, zQ = 0, xR = 0, yR = 0, zR = 0)
	
	def dataEnter(self):
		print('\t*[NEW INSTRUCTIONS]*\n')
		print('\t- To introduce the given [Coordinates] of the [points: P, Q, and R] type [1].')
		print('\t- To enter the given [Components] of [two vectors]: vectorA and vectorB] type [2].')
		number = selectOption.provide_Option()
		add_Subtraction_Vectors.number = number

		if self.number == 1:
			pointcoordinates3d.number1 = 1
			self.coordP = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 2
			self.coordQ = pointcoordinates3d.getpointcoordinates3d()
			pointcoordinates3d.number1 = 3
			self.coordR = pointcoordinates3d.getpointcoordinates3d()
			
			self.xP = self.xQ = self.xR = 0
			self.yP = self.yQ = self.yR = 0
			self.zP = self.zQ = self.zR = 0
			
			for v in range(0,3):
				if v == 0:
					self.xP = self.coordP[v]
					self.xQ = self.coordQ[v]
					self.xR = self.coordR[v]
					
				elif v == 1:
					self.yP = self.coordP[v]
					self.yQ = self.coordQ[v]
					self.yR = self.coordR[v]
					
				elif v == 2:
					self.zP = self.coordP[v]
					self.zQ = self.coordQ[v]
					self.zR = self.coordR[v]
					
			self.PointP = (self.xP,self.yP,self.zP)
			print('\n\t- The (Point P): P',self.PointP)
			self.PointQ = (self.xQ,self.yQ,self.zQ)
			print('\t- The (Point Q): Q',self.PointQ)
			self.PointR = (self.xR,self.yR,self.zR)
			print('\t- The (Point R): R',self.PointR)
				
			self.vectorPQ = []
			self.vectorPR = []
			
			for h in range (0,3):
				self.comp0 = self.coordQ[h] - self.coordP[h]
				self.vectorPQ.append(self.comp0)
				self.comp1 = self.coordR[h] - self.coordP[h]
				self.vectorPR.append(self.comp1)
				
			self.vectorA = self.vectorPQ
			self.vectorB = self.vectorPR
				
		elif self.number == 2:
			self.vectorA = compvector.getcomponent3dvectorA() 
			self.vectorB = compvector.getcomponent3dvectorB()
			
		else:
			textstring3.error_option()
			return
			
		answer.view_solution()
		print('\t-- The [vectorA]: vectorA', self.vectorA)
		print('\t-- The [vectorB]: vectorB', self.vectorB, '\n')
		
		self.Addition = []
		self.Subtraction = []
    
		for q in range(0,3):
			self.termA = ( self.vectorA[q] + self.vectorB[q] )
			self.Addition.append(self.termA)
			
			self.termS = ( self.vectorA[q] - self.vectorB[q] )
			self.Subtraction.append(self.termS)

		print('\t-- The [Addition]: vector(A+B)',  self.Addition)
		print('\t-- The [Subtraction]: vector(A-B)', self.Subtraction,'\n')
		
		return

add_Subtraction_Vectors = Add_SubtractionVectors()
