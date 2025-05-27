###################################################################################################
#
# The [runVector3d.py] program will run various Classs inside the [Vector3dClassModule.py] module.
# 
#===================================================
#
# *  The [runVector3d.py] program
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

print('\n\n\t         **[ WELCOME IN USING THE [RUNVECTOR3D.PY] PROGRAM ]**') 
print('\t   **[ TO [SOLVE] VARIOUS PROBLEMS OF [VECTORS] IN THE [SPACE] ]**')
print('\t\t\t--[Version: 2.0 -- Stable]--')
print('\n\n\t**[INSTRUCTIONS OF USE]**\n')

print('- To find the [value] of the [Dot Product] of [two vectors]: vectorA and vectorB using the')
print('  [Definition]: a * b = a1*b1 + a2*b2 + a3*b3 key [1]')
print('- To Determine the [value] of the [Dot Product] of [two vectors]: vectorA and vectorB using the')
print('  [Theorem]: a * b = ||a||*||b||*cos(theta) key [2]')
print('- To get the [Cross Product] with the given [Components] of [two vectors]: vectorA and vectorB or using')
print('  the given [Coordinates] of the [points]: P, Q, and R key [3] ')
print('- To calculate the [value] of the [Theta Sine] between [two vectors]: vectorA and vectorB key [4]')
print('- To find the [value] of the [Scalar Triple Product] of [three vectors]: vectorA, vectorB, and vectorC key [5]')
print('- To determine the [value] of the [Theta angle in degrees] between the [two vectors]: vectorA and vectorB key [6]')
print('- To get the [value] of the [Theta Cosine] between [two vectors]: vectorA and vectorB key [7]')
print('- To find the [Vectors: vectorA, vectorB, vectorC, and vectorD] and [Modules] using the [Theorem] of the')
print('  [Distance] between any [two points]: P and Q or P and R or Q and R or R and S key [8]')
print('- To calculate the [Area(S)] of the [Triangle(PQR)] with the given [Coordinates] of the [points]: P, Q, and R')
print('  or the given [Components] of [two vectors]: vector_A and vector_B key [9]')
print('- To find the [height(h)], and [Area(P)] of the [Parallelogram(PQRS)] determined to [two adjacent vectors]:')
print('  vectorA and vectorB or with given [Coordinates] of the [vertice points: P, Q, and R key [10]')
print('- To get the [Volume_V(P)], and [Height(h)] of a [Parallelepiped] and too the [Volume_V(T)] of a [Tetrahedron] with')
print('  the given [Coordinates] of the [four points]: P, Q, R, S or with the given [Components] of the [three vectors]:')
print('  vector_A, vector_B, and vector_C key [11]')
print('- To calculate the three [Inner Angles: Alpha, Beta, and Gama] of the [TrianglePQR] with the given [Coordinates]')
print('  of the given [points]: P, Q, and R key [12]')
print('- To Determine the following [Middle Points]: K(xK,yK,zK), L(xL,yL,zL), M(xM,yM,zM)] and N(xN,yN,zN)] ') 
print('  between [points]: P(xP,yP,zP), Q(xQ,yQ,zQ), R(xR,yR,zR), and S(xS,yS,zS) or in [sides]: PQ, PR, and QR')
print('  of a Triangle(PQR).key [13]')
print('- To find the [Centroid: G(xG, yG, zG)] of the triangle(PQR) key [14]')
print('- To determine the [Medians: PM, QL, and RK] of a triangle(PQR) key [15]')
print('- To get the [Addition] and [Subraction] between [Two Vectors]: vectorA and vectorB key [16]')
print('- Provide the given [Components] of a [vectorA] or find a [new vectorA] that represent a [oriented segmentPQ] with the')
print('  given [Coordinates] of [two points]: P and Q and calculate the [Direction Cosines] and [Direction Angles] key [17]')
print('- To find the [Addition] and [Subraction] between [two vectors]: vectorA and vectorB multiplyed by')
print('  [two scalars]: [coeffic1 and coeffic2] key [18]')
print('- To calculate the [dimensions]: [Perimeter(P)], [Heights(h1,h2,h3)], and [Area(A)] of a [TrianglePQR]')
print('  with the given [Coordinates] of the [three points]: P, Q, and R key [19]')
print('- To get the [dimensions]: [Perimeter(P)], [height(h1,h2)], and [Area(S)] of a [Parallelogram(PQRS) key [20]')
print('- Given the [Coordinates] of the [Middle Points]: K(xK,yK,zK), L(xL,yL,zL), and M(xM,yM,zM) will calculate')
print('  the [Coordinates] of the [vertice points]: P, Q, and R of a Triangle(PQR). key [21]\n')

from Vector3dClassModule import * 
	
print('\n\t[§] Select an previous [option] that will used--Ok!\n')
numb = vector.enterIntegerData()

match numb:
	case 1:
		print('\n\t**[ FIND THE [DOT PRODUCT] OF [TWO VECTORS: A AND B USING THE [DEFINITION]: ]**')
		print('\t**[ A * B = A1*B1 + A2*B2 + A3*B3 IN THE TRI-DIMENSIONAL(XYZ) SPACE]**\n')
		# New -- Ok!
		scalar3dproduct.number = 1
		scalar3dproduct.number1 = 1
		scalar3dproduct.getscalar3d_product()
		
	case 2:
		print('\n\t**[ FIND THE [DOT PRODUCT] OF [TWO VECTORS: A AND B USING THE [THEOREM]: ]**')
		print('\t**[ A * B = ||A||*||B||*COS(THETA) IN |R³ ]**\n')
		# New -- Ok!
		theorem_scalar3d_product.use_theoremScalar3dProduct()
		
	case 3:
		print('\n\t**[DETERMINE THE [CROSS PRODUCT(AxB)] WITH THE GIVEN [COMPONENTS] OF [TWO VECTORS: A AND B] in |R³]**')
		# New -- Ok!
		find_crossproduct.findCrossProduct()
		
	case 4:
		print('\n\t**[FIND THE VALUE OF THE [THETA SINE IN RADIAN] IN RADIAN]**\n')
		# New -- Ok!
		find_crossproduct.find_Thetasin()
		
	case 5:
		print('\n\t**[WILL CALCULATE THE [SCALAR TRIPLE PRODUCT] BETWEEN THE THREE ')
		print('\t**[VECTORS: A, B, AND C] IN TRI-DIMENSIONAL(XYZ) SPACE]**\n')
		# New -- Ok!
		mixed_product.findMixedProduct()
		
	case 6:
		print('\n\t**[WILL GET THE [VALUE] OF THE [THETA ANGLE IN DEGREE ] BETWEEN VECTORS: A AND B]**\n')
		# New -- Ok!
		find_crossproduct.get_thetaAngle()
		
	case 7:
		print('\n\t**[FIND THE [VALUE] OF THE [THETA COSINE IN RADIAN] BETWEEN VECTORS: vectorA AND vectorB]**\n')
		# New -- Ok!
		scalar3dproduct.number = 2
		scalar3dproduct.number1 = 2
		scalar3dproduct.getscalar3d_product()
		
	case 8:
		print('\n\t  **[ WILL DETERMINE THE [VECTOR] AND [MODULE] BETWEEN ANY TWO GIVEN POINTS:]**')
		print('\t  **[ P AND Q OR P AND R OR Q AND R OR R AND S]**\n')
		print('\n\t   **[TO FIND THE [VECTOR(A)] THAT REPRESENT THE TWO GIVEN POINTS: P, AND Q]**')
		print('\t   **[ AND TOO THE [MODULE] OF THE VECTOR(A) = |VECTOR(PQ)| ]**\n')
		print('\t   **[ TO GET THE [VECTOR(B)] THAT REPRESENT THE TWO GIVEN POINTS: P, AND R]**')
		print('\t   **[ AND TOO THE [MODULE] OF THE VECTOR(B) = |VECTOR(PR)| ]**\n')
		print('\t   **[ TO FIND THE [VECTOR(C)] THAT REPRESENT THE TWO GIVEN POINTS: Q, AND R]**')
		print('\t   **[ AND TOO THE [MODULE] OF THE VECTOR(C) = |VECTOR(QR)| ]**\n')
		print('\t   **[ TO GET THE [VECTOR(D)] THAT REPRESENT THE TWO GIVEN POINTS: R, AND S]**')
		print('\t   **[ AND TOO THE [MODULE] OF THE VECTOR(D) = |VECTOR(RS)| ]**\n')
		# New -- Ok!
		print('\t\t\t*[NEW INSTRUCTIONS]*\n')
		print('\t- Type [1] to find the [vectorA] and [module] usind the [distance]: d(P,Q)')
		print('\t- Type [2] to determine the [vectorB] and [module] usind the [distance]: d(P,R)')
		print('\t- Type [3] to get the [vectorC] and [module] usind the [distance]: d(Q,R)')
		print('\t- Type [4] to find the [vectorD] and [module] usind the [distance]: d(R,S)')
		print('\t- Type [5] to determine the [Vectors: vectorA, vectorB, vectorC, and vectorD] and')
		print('\t  [modules] usind the [distances]: d(P,Q), d(P,R), d(Q,R), d(R,S).\n')
		number = vector.enterIntegerData()
		
		match number:
			case 1:
				print('\n\t- Will find only the distance: d(P,Q)')
				findcoordpq.findcoord_pointPQ()
				findvectorA.find_vectorA()
				
			case 2:
				print('\n\t- Will get only the distance: d(P,R)')
				findcoordpr.findcoord_pointPR()
				findvectorB.find_vectorB()
				
			case 3:
				print('\n\t- Will determine only the distance: d(Q,R)')
				findcoordqr.findcoord_pointQR()
				findvectorC.find_vectorC()
			
			case 4:
				print('\n\t- Will find only the distance: d(R,S)')
				enterCoordrs.getcoord_pointRS()
				getvectorD.find_vectorD()
				
			case 5:
				print('\n\t- Will get all the [Vectors] and [Modules]: d(P,Q), d(P,R), d(Q,R), and d(R,S).\n')
				findcoordpq.findcoord_pointPQ()
				findvectorA.find_vectorA()
				findcoordpr.findcoord_pointPR()
				findvectorB.find_vectorB()
				findcoordqr.findcoord_pointQR()
				findvectorC.find_vectorC()
				enterCoordrs.getcoord_pointRS()
				getvectorD.find_vectorD()
				
			case _:
				print('\n\t\t*[ NEITHER OF THE  PREVIOUS OPTIONS -- Ok! ]*\n')
	
	case 9:
		print('\n\t**[ FIND THE [AREA(S)] OF THE TRIANGLE(PQR) WITH THE GIVEN [COORDINATES] OF THE [POINTS]: ]**')
		print('\t**[ P, Q AND R] OR USE THE GIVEN [COMPONENTS] OF TWO [VECTORS: VECTOR_A AND VECTOR_B]]**\n')
		# New -- Ok!
		find_crossproduct.determine_areaTriangle()
		
	case 10:
		print('\n\t**[ FIND THE [HEIGHT(H), AND AREA(P) OF THE PARALLELOGRAM(PQRS) DETERMINED BY]**')
		print('\t**[ [TWO ADJACENT VECTORS]: VECTOR_A AND VECTOR_B OR WITH THE GIVEN [COORDINATES] ]**') 
		print('\t**[ OF THE [VERTICES]: P, Q, AND R ]**\n')
		# New -- Ok!
		find_crossproduct.get_areaParallelogram()
		
	case 11:
		print('\n\t**[ GIVE THE [COMPONENTS] OF [THREE VECTORS]: VECTOR_A, VECTOR_B AND VECTOR_C OR ]**')
		print('\t**[ PROVIDE THE [COORDINATES] OF THE POINTS: P, Q, R AND S IN [SPACE |R³] AND FIND ]**')
		print('\t**[ THE [THREE VECTORS]: VECTOR_A, VECTOR_B AND VECTOR_C. AFTER FOLLOW TO DETERMINE ]**')
		print('\t**[ THE [DIMENSIONS]: [HEIGTH(H)] AND [VOLUME_V(P)] OF A PARALLELEPIPED AND TOO ]**')
		print('\t**[ THE [VOLUME_V(T)] OF A TETRAHEDRON ]**\n')
		# New -- Ok!
		mixed_product.determine_heigth_Volume()
	
	case 12:
		print('\n\t**[ GIVEN THE COORDINATES OF THE POINTS P, Q AND R ]**')
		print('\t**[ FIND THE [INNER ANGLES] OF THE TRIANGLE(PQR) ]**\n')
		# New -- Ok!
		inner_angle_triangle.getInner_angle_triangle()
		
	case 13:
		# New -- Ok!
		print('\n\t=======================================')
		print('\t**[ WILL DETERMINE THE [MIDPOINTS]: ]**')
		print('\t=======================================\n')
		print('\t\t*[NEW INSTRUCTIONS]*\n')
		print('\t- Type [1] to find the [Middle points] of the sides: PQ, PR, and QR of a Triangle(PQR).')
		print('\t- Type [2] to determine the [Middle Point: K(xK,yK,zK)] relative as points: P(xP,yP,zP) and Q(xQ,yQ,zQ).')
		print('\t- Type [3] to get the [Middle Point: L(xL,yL,zL)] relative as points: Q(xQ,yQ,zQ) and R(xR,yR,zR).')
		print('\t- Type [4] to find the [Middle Point: M(xM,yM,zM)] relative as points: R(xR,yR,zR) and S(xS,yS).')
		print('\t- Type [5] to calculate the [Middle Point: N(xN,yN,zN)] relative as points: S(xS,yS,zS) and P(xP,yP,zP).\n')
		number = vector.enterIntegerData()
		
		match number:
			case 1:
				print('\n\t\t-- [Middle point]: K(xK,yK,zK) relative as sidePQ.')
				print('\t\t-- [Middle point]: L(xL,yL,zL) relative as sidePR.')
				print('\t\t-- [Middle point]: M(xM,yM,zM) relative as sideQR.\n')
				middle3dpoint.number = 1
				middle3dpoint.getmiddle3d_point()
				middle3dpoint.number = 2
				middle3dpoint.getmiddle3d_point()
				middle3dpoint.number = 3
				middle3dpoint.getmiddle3d_point()
			
			case 2:
				middle3dpoint.number = 1
				middle3dpoint.getmiddle3d_point()
				
			case 3:
				middle3dpoint.number = 5
				middle3dpoint.getmiddle3d_point()
				
			case 4:
				middle3dpoint.number = 6
				middle3dpoint.getmiddle3d_point()
				
			case 5: 
				middle3dpoint.number = 4
				middle3dpoint.getmiddle3d_point()
			
			case _:
				textstring3.error_option()
			
	case 14:
		# New -- Ok!
		print('\n\t**[ TO DETERMINE THE [CENTROID: G(xG,yG,zG)] OF A TRIANGLE(PQR) WITH THE ]**') 
		print('\t**[ GIVEN [COORDINATES] OF THE [POINTS]: P(xP,yP,zP), Q(xQ,yQ,zQ), AND R(xR,yR,zR)]**\n')
		centricg3d.find_centricG_3d()
		
	case 15:
		# New -- Ok!
		print('\n\t =====================================================')
		print('  \t **[ TO DETERMINE THE MEDIANS OF THE TRIANGLE(PQR) ]**')
		print('  \t =====================================================\n')
		findthemedians3d.get_the_medians()
	
	case 16:
		print('\n   **[ GIVE THE [COMPONENTS] OF [TWO VECTORS]: VECTOR_A AND VECTOR_B OR ]**')
		print('   **[ PROVIDE THE [COORDINATES] OF [THREE POINTS]: P, Q, AND R IN [SPACE |R³] ]**')
		print('   **[ AFTER FIND THE [TWO VECTORS]: VECTOR_A AND VECTOR_B AND FOLLOW ]**')
		print('   **[ TO CALCULATE THE [ADDITION] AND [SUBTRACTION] OF THIS [VECTORS]]**\n')
		# New -- Ok!
		add_Subtraction_Vectors.dataEnter()
		
	case 17:
		print('\n\t**[ PROVIDE THE GIVEN [COMPONENTS] OF A [VECTOR_A] OR FIND A [NEW VECTOR_A] THAT REPRESENT A [ORIENTED SEGMENT_PQ] ]**')
		print('\t**[ WITH THE GIVEN [COORDINATES] OF [TWO POINTS]: P AND Q AND CALCULATE THE [DIRECTION COSINES] AND [DIRECTION ANGLES] ]**\n')
		# New -- Ok!
		cosine_angleDirection.enter_Components_VectorA()
		
	case 18:
		print('\n **[ GIVEN [TWO VECTORS]: VECTOR_A AND VECTOR_B MULTIPLYED BY [TWO SCALARS]:')
		print('   [COEFFIC1 AND COEFFIC2] OR ]**\n')
		print(' **[ GIVEN [THE POINTS: P, Q, AND R] FIND [TWO VECTORS]: VECTOR_A=VECTOR(PQ)')
		print('   AND VECTOR_B=VECTOR(PR) ]**\n')
		print(' **[ AND MULTIPLY BY [TWO SCALARS]: [COEFFIC1] AND [COEFFIC2] AND TOO GET THE')
		print('   [ADDITION] AND [SUBTRACTION] ]**\n')
		# New -- Ok!
		vectorAddSubMulscalar.data_enter()
		
	case 19:
		print('\n\t **[ DETERMINE THE DIMENSIONS:[PERIMETER(P), [HEIGHTS(H1,H2,H3)], AND [AREA(A)] OF A]**')
		print('\t **[ TRIANGLE(PQR) WITH THE GIVEN [COORDINATES] OF THE [POINTS]: P, Q, AND, R USING THE ]**')
		print('\t **[ SCALAR PRODUCT OF VECTORS.]**\n')
		scalar3dproduct.number = 3
		scalar3dproduct.getscalar3d_product()
		
	case 20:
		print('\n   **[ FIND THE [DIMENSIONS]: [PERIMETER(P), [HEIGTHS(H1,H2)], AND [AREA(S)] OF A ]**')
		print('   **[ [PARALLELOGRAM(PQRS)] WITH THE GIVEN [COORDINATES] OF THE [POINTS]: P, Q, AND R ]**')
		print('   **[ OR WITH ALL GIVEN [COORDINATES] OF THE [POINTS]: P, Q, R, AND S ]**\n')
		# New -- Ok!
		scalar3dproduct.number = 4
		scalar3dproduct.getscalar3d_product()
		
	case 21:
		print('\n\t **[ GIVEN THE [COORDINATES] OF THE [MIDDLE POINTS]: K(xK,yK,zK), L(xL,yL,zL), AND M(xM,yM,zM) ]**')
		print('\t **[ WILL FIND ALL THE [COORDENATES] OF THE [VERTICE POINTS: P, Q, AND R] OF A TRIANGLE(PQR) ]**\n')
		# New -- Ok!
		vertices_triangle3d.select_findVertice3d()
		
	case _:
		print('\n\t**[NEITHER OF THE PREVIOUS OPTIONS WAS SELECTED]**')
		print('\t  [ RUN THE [RUNVECTOR3D.PY PROGRAM] AGAIN--OK! ]')
		
input('\n\n\t\t. . . Key [ENTER] to exit -- Ok! . . .\n')
		
			
			
