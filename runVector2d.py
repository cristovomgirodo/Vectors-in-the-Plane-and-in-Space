#######################################################################
#
#	The runVector2d.py program
# 	Developed by Cristovom A. Girodo
# 	Date: 20241223 -- new Version: 2.0(Stable)
#
#######################################################################

print('\n\n\t         **[ WELCOME IN USING THE [RUNVECTORS2D.PY] PROGRAM ]**') 
print('\t    **[ TO [SOLVE] VARIOUS PROBLEMS OF [VECTORS] IN THE [PLANE] ]**')
print('\t\t\t    --[Version: 2.0 -- Stable]--')
print('\n\n\t**[INSTRUCTIONS OF USE]**\n')
print('\t- To find the [Scalar Product: a * b] between [two vectors] key [1]')
print('\t- To calculate the [Perimeter(P)], [Heights(h), and [Area(A)] of the TrianglePQR:')
print('\t  Givens the [coordinates] of the [points: P(xP,yP), Q(xQ,yQ), and R(xR,yR)] key [2]')
print('\t- To get the [Area(S)] and [Heights: h1 and h2] of the [Parallelogram(PQRS)] with the [coordinates] of the')
print('\t  [points: P(xP,yP), Q(xQ,yQ), R(xR,yR), and S(xS,yS)] key [3]')
print('\t- To find the [angle] between [two vectors] in plane key [4]')
print('\t- To calculate the [value] of the [CossineTheta] between the [two vectors]:')
print('\t  A and B key [5]')
print('\t- To find the three sides and [Inner Angles: ALPHA, BETA, and GAMA] of the [Triangle(PQR)] with ')
print('\t  the [coordinates] of the [points: P(xP,yP), Q(xQ,yQ), and R(xR,yR)] key [6]')
print('\t- To Determine the following [Middle Points]: K(xK,yK), L(xL,yL), M(xM,yM)] and N(xN,yN)] ') 
print('\t  between [ points: P(xP,yP), Q(xQ,yQ), R(xR,yR), and S(xS,yS) ] or in the sides: PQ, PR, and QR')
print('\t  of a Triangle(PQR).key [7]') 
print('\t- To get the [Addition and Subtraction] of [Two Vectors: A and B] key [8]')
print('\t- To calculate the [Resultant(|R) Vector] key [9]')
print('\t- To find the [VectorA and lenght|A|] with the [coordinates] of the [points: P(xP,yP), and Q(xQ,yQ)]')
print('\t  To get the [VectorB and lenght|B|] with the [coordinates] of the [points: P(xP,yP), and R(xR,yR)]')
print('\t  To find the [VectorC and lenght|C|] with the [coordinates] of the [points: Q(xQ,yQ), and R(xR,yR)]')
print('\t  key [10]')
print('\t- To get the [Addition] and [Subraction] between [Two Vectors: A and B]')
print('\t  Multiplyed by scalars: [coeffic1 and coeffic2] key [11]')
print('\t- To determine the [Medianas: PM, QL, and RK] of the triangle(PQR) key [12]')
print('\t- To find the [Centroid: G(xG, yG)] of the triangle(PQR) key [13]')
print('\t- To calculate the [ Vertices: P(xP.yP), Q(xQ,yQ), and R(xR,yR) ] of the triangle(PQR) with')
print('\t  the [Coordinates] given of the [ Middle points: K(xK,yK), L(xL,yL), and M(xM,yM) ] key [14]')
print('\t- To get the [Coordinates] of any a of the [ Points: D(xD,yD) or E(xE,yE), or F(xF,yF) ] that are')
print('\t  meeted with the [bisectrixs: PD or QE or RF] in the sides: QR or PR or PQ of a Triangle(PQR)')
print('\t  key [15]')
print('\t- To determine any a of the [bisectrixs: PD or QE or RF] of a Triangle(PQR) key [16]\n')

from Vector2DClassModule import *

print('\t[§] Select an previous [option] that will used--Ok!\n')
numop = vector.enterIntegerData()

if numop == 1:
	print('\n\t**[TO FIND THE [SCALAR PRODUCT] OF [TWO VECTORS: A and B] IN THE')
	print('\t   PLANE]**\n')
	scalar_product.number = 1
	scalar_product.getscalar_product()
	
elif numop == 2:
	print('\n\t\t**[ TO CALCULATE THE SIDES: SIDE_A, SIDE_B, AND SIDE_C, THE PERIMETER(P), THE HEIGHTS: H1,H2, AND H3, AND THE ]**')
	print('\t\t**[ AREA(A) OF THE  [TRIANGLE(PQR)] GIVEN THE [COORDINATES] OF THE [ VERTICE POINTS: P, Q, AND R [ IN THE PLANE] ]**\n')
	scalar_product.number = 3
	scalar_product.getscalar_product()
		
elif numop == 3:
	print('\n\t\t**[ TO GET THE SIDES: SIDE_A AND SIDE_B, PERIMETER(P), [HEIGHTS: H1 AND H2], AND THE [AREA(S)] OF THE  ]**')
	print('\t\t**[ [PARALLELOGRAM(PQRS)] GIVEN THE [COORDINATES] OF THE [ VERTICES POINTS: P, Q, R AND S] IN THE PLANE ]**\n')
	scalar_product.number = 4
	scalar_product.getscalar_product()

elif numop == 4:
	print('\n\t**[WILL FIND THE [VALUE] OF THE [THETA ANGLE] BETWEEN ')
	print('\t  [TWO VECTORS] GIVEN: A AND B]**\n')
	anglevectors.getangleTheta()

elif numop == 5:
	print('\n\t**[ TO CALCULATE THE [VALUE] OF THE [COSSINE THETA] BETWEEN')
	print('\t     THE [TWO VECTORS]: A AND B]**\n')
	cossinetheta.getcossineTheta()
	
elif numop == 6:
    print('\n\t**[ TO FIND THE THREES SIDES: SIDEA, SIDEB, AND SIDEC, THE [INNER ANGLES: ALPHA, BETA, AND GAMA]]**')
    print('\t**[ OF THE [TRIANGLE(PQR)] GIVENS THE [COORDINATES] OF THE POINTS: P, Q, AND R IN THE PLANE ]**\n')
    scalar_product.number = 3
    inner_angle_triangle.getInner_angle_triangle()
    
elif numop == 7:
	print('\n\t=======================================')
	print('\t**[ WILL DETERMINE THE [MIDPOINTS]: ]**')
	print('\t=======================================\n')
	print('\t- Type [1] to find the [Middle points] of the sides: PQ, PR, and QR of a Triangle(PQR).')
	print('\t- Type [2] to determine the [Middle Point: K(xK,yK)] relative as points: P(xP,yP) and Q(xQ,yQ).')
	print('\t- Type [3] to get the [Middle Point: L(xL,yL)] relative as points: Q(xQ,yQ) and R(xR,yR).')
	print('\t- Type [4] to find the [Middle Point: M(xM,yM)] relative as points: R(xR,yR) and S(xS,yS).')
	print('\t- Type [5] to calculate the [Middle Point: N(xN,yN)] relative as points: S(xS,yS) and P(xP,yP).\n')	
	number = vector.enterIntegerData()
	
	if number == 1:
		print('\n\t-- [Middle point: K(xK,yK) relative as sidePQ.')
		print('\t-- [Middle point: L(xL,yL) relative as sidePR.')
		print('\t-- [Middle point: M(xM,yM) relative as sideQR.\n')
		midpoint.number = 1
		midpoint.getmid_point()
		midpoint.number = 2
		midpoint.getmid_point()
		midpoint.number = 3
		midpoint.getmid_point()
		
	elif number == 2:
		midpoint.number = 1
		midpoint.getmid_point()
		
	elif number == 3:
		midpoint.number = 5
		midpoint.getmid_point()
		
	elif number == 4:
		midpoint.number = 6
		midpoint.getmid_point()
		
	elif number == 5:
		midpoint.number = 4
		midpoint.getmid_point()
	else:
		print('\n\t\t*[ NEITHER OF THE  PREVIOUS OPTIONS -- Ok! ]*\n')
   
elif numop == 8:
    print('\n\t\t**[TO FIND THE [ADDITION AND SUBTRACTION] OF [TWO VECTORS: A and B] IN THE PLANE]**\n')
    addsubtraction.getadd_subtraction()
    
elif numop == 9:
    print('\n\t**[TO GET THE VALUE OF THE RESULTANT(|R) VECTOR]**\n')
    resultant.getresultant_vector()
    
elif numop == 10:
    print('\n\t\t**[TO FIND THE [VECTOR(A)] THAT REPRESENT THE TWO GIVENS POINTS: P, AND Q]**')
    print('\t\t**[ AND TOO THE [LENGTH] OF THE VECTOR(A) = |VECTOR(PQ)| ]**\n')
    print('\t\t**[TO GET THE [VECTOR(B)] THAT REPRESENT THE TWO GIVENS POINTS: P, AND R]**')
    print('\t\t**[ AND TOO THE [LENGTH] OF THE VECTOR(B) = |VECTOR(PR)| ]**\n')
    print('\t\t**[TO FIND THE [VECTOR(C)] THAT REPRESENT THE TWO GIVENS POINTS: Q, AND R]**')
    print('\t\t**[ AND TOO THE [LENGTH] OF THE VECTOR(C) = |VECTOR(QR)| ]**\n')
    findcoordpq.findcoord_pointPQ()
    findvectorA.find_vectorA()
    findcoordpr.findcoord_pointPR()
    findvectorB.find_vectorB()
    findcoordqr.findcoord_pointQR()
    findvectorC.find_vectorC()
   
elif numop == 11:
    print('\n\t**[ GIVENS [TWO VECTORS: A AND B] MULTIPLYED BY THE [SCALARS]:')
    print('\t  [COEFFIC1] AND [COEFFIC2] OR ]**\n')
    print('\t**[ GIVENS [THE POINTS: P, Q, AND R]  FIND [TWO VECTORS]: ')
    print('\t  VECTOR(A)=VECTOR(PQ) AND VECTOR(B)=VECTOR(PR) ]**\n')
    print('\t**[ AND MULTIPLY BY THE [SCALARS]: [COEFFIC1] AND [COEFFIC2] AND')
    print('\t  TOO GET THE [ADDITION] AND [SUBTRACTION] ]**\n')
    formacomponent.getforma_component()
    
elif numop == 12:
	print('\n\t ======================================================')
	print('  \t **[ TO DETERMINE THE MEDIANAS OF THE TRIANGLE(PQR) ]**')
	print('  \t ======================================================\n')
	findthemedianas.find_the_medianas()
	
elif numop == 13:
	 print('\n\t**[TO DETERMINE THE [CENTROID: G(xG,yG)] OF A TRIANGLE(PQR) GIVEN: ]**') 
	 print('\t**[THE [COORDINATES] OF THE [POINTS]: P(xP,yP), Q(xQ,yQ), AND R(xR,yR)]**\n')
	 centricg.find_centricG()
	 
elif numop == 14:
	 print('\n\t**[ TO FIND THE VERTICES: P(xP.yP), Q(xQ,yQ), AND R(xR,yR) OF A TRIANGLE(PQR) ]**\n')
	 verticestriangle.select_findVertice()

elif numop == 15:
	 print('\n\t**[ TO GET ANY A OF THE [POINTS: D(xD,yD) or E(xE,yE), or F(xF,yF)] IN THE SIDES: ]**')
	 print('\t**[ QR, PR, AND PQ OF A TRIANGLE(PQR) ]**\n')
	 bisectrixpoints.select_point()
	 
elif numop == 16:
	 print('\n\t**[ TO FIND ANY A OF THE [BISECTRIXS: PD, QE, and RF] OF INNER ANGLES OF A TRIANGLE(PQR)]**\n')
	 bisectrixtriangle.select_bisectrix()
	 
else:
    print('\n\t\t**[NEITHER OF THE PREVIOUS OPTIONS WAS SELECTED]**')
    print('\t\t[ RUN THE RUNVECTOR2D.PY PROGRAM AGAIN -- OK! ]')

input('\n\n\t\t. . . Key [ENTER] to exit -- Ok! . . .\n')
	
	
	
