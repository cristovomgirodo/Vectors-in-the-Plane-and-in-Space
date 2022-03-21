###############################################
#
# The runvectors2dim.py program
# Developed by Cristovom A. Girodo
# Date: 20220123 -- Stable Version: 1.0
#
###############################################

print('\n\n\t\t  **[ WELCOME IN USING THE [RUNVECTORS2DIM.PY] PROGRAM ]**') 
print('\t\t**[ TO [SOLVE] VARIOUS PROBLEMS OF [VECTORS] in the [PLANE] ]**')
print('\t\t\t\t--[Version: 1.0 -- Stable]--')
print('\n\n\t**[INSTRUCTIONS OF USE]**')
print('\t- To find the [Scalar Product: a * b] between [two vectors] key [1]')
print('\t- To calculate the [Perimeter(P)], [Height(h), and [Area(A)] of the TrianglePQR givens the [points: P, Q, and R] key[2]')
print('\t- To get the [Area(S) and Height(h) of the [Parallelogram(PQRS)] given the [points: P, Q, R, and S] key[3]')
print('\t- To find the [angle] between [two vectors] in plane key[4]')
print('\t- To calculate the [value] of the [CossineTheta] between [two vectors] a and b key [5]')
print('\t- To get the [Distance] between [two points] given P and Q key [6]')
print('\t- To find the three [Inner Angles] of the [Triangle] of three points given: P, Q, R key [7]')
print('\t- To calculate the [midPoint M(xM,yM)] between the points: P and Q key [8]')
print('\t- To get the [Addition and Subtraction] of [Two Vectors: a and b] key [9]')
print('\t- To calculate the [Resultant(|R) Vector] key [10]')
print('\t- To find the[VectorA] and [lenght] of givens Points: P, AND Q key [11]')
print('\t- To find the [Addition] and [Subraction] between [Two Vectors] A and B multiplyed by scalars[coeffic1 and coeffic2] key [12]\n')

from VectorModule2Dim import *

print('\t[§] Select an previous [option] that will used--Ok!\n')
numop = vectornumber()

if numop == 1:
    print('\n\t**[TO FIND THE [SCALAR PRODUCT] OF [TWO VECTORS: A and B] IN THE BI-DIMENSIONAL(XY) PLANE]**\n')
    varint = 1
    ScalarProd, VectorAB = scalarProduct(varint)
    print('\t-- The [Vector] of the [terms of the Scalar Product]: vectorAB',VectorAB)
    print('\t-- The [Scalar Product(vectorAB)] of the vectors is:',format(ScalarProd,"<10.2f"),'\n')
    
elif numop == 2:
    print('\n\t**[TO CALCULATE THE [PERIMETER(P), HEIGHTS(H1,H2,H3), AND AREA(A) OF THE TRIANGLE-PQR]**')
    print('\t**[GIVENS THE POINTS: P, Q, AND R IN THE BI-DIMENSIONAL(XY) PLANE]**\n')
    varint = 3
    scalarProduct(varint)
    
elif numop == 3:
    print('\n\t**[TO GET THE [AREA(S) AND HEIGHT(H) OF THE [PARALLELOGRAM(PQRS)] GIVEN ]**')
    print('\t**[THE POINTS: P, Q, R AND S IN THE BI-DIMENSIONAL(XY) PLANE]**\n')
    varint = 4
    scalarProduct(varint)
    
elif numop == 4:
    print('\n\t**[WILL FIND THE [VALUE] OF THE [THETA ANGLE] BETWEEN [TWO VECTORS] GIVEN: A AND B]**\n')
    modVectorA, modVectorB, ScalarProduct,VectorAxB, AngleTheta_degrees = angleVectors()
    print('\t- The [terms] of the [VectorA*B] ís:', VectorAxB)
    print('\t- The [length] of a |vectorA|:', format((modVectorA),'<10.2f'))
    print('\t- The [length] of a |vectorB|:', format((modVectorB),'<10.2f'))
    print('\t- The [Scalar Product] is:',format((ScalarProduct),'<10.2f'))
    print('\n\t- The value of the [THETA ANGLE IN DEGREES] was calculate is:', format((AngleTheta_degrees),'<10.2f'),'\n')

elif numop == 5:
    print('\n\t**[TO CALCULATE THE [VALUE] OF THE [COSSINE THETA] BETWEEN [TWO VECTORS] GIVEN: A AND B]**\n')
    modVectorA, modVectorB, ScalarProduct, VectorAxB, CosineRadians  = cosineTheta()
    print('\t- The [VectorA*B]:', VectorAxB)
    print('\t- The [length] of a |vectorA|:', format((modVectorA),'<10.2f'))
    print('\t- The [length] of a |vectorB|:', format((modVectorB),'<10.2f'))
    print('\t- The [Scalar Product] of the [VectorA*B] is:',format((ScalarProduct),'<10.2f'))
    print('\n\t- The value of the [COSINE THETA IN RADIANS] calculated is:', format((CosineRadians),'<10.2f'),'\n')

elif numop == 6:
    print('\n\t**[TO GET THE [DISTANCE(D)] BETWEEN ANY [TWO POINTS] GIVEN P AND Q]**\n')
    VectorPQ, VectorQUAD, Distance = distanceTwoPoints()
    print('n\t-- The [vectorPQ]: vectorPQ',VectorPQ)
    print('\t-- The [Quadratic Components] of the [vectorPQ]: VectorQUAD',VectorQUAD)
    print('\t-- The [Distance(D)] geted between Two (Points) P and Q] is:',format((Distance),'<10.2f'),'\n')
    
elif numop == 7:
    print('\n\t**[ TO FIND THE THREES [INNER ANGLES] OF THE [TRIANGLE(PQR)] ]**\n')
    innerAngleTriangle()

elif numop == 8:
    print('\n\t**[ WILL DETERMINE THE [MIDPOINT(M)] BETWEEN THE (POINTS): P AND Q GIVEN]**\n')
    VectorMidPoint = midPoint()
    print('\t-- The [(MidPoint)]: M',VectorMidPoint,'\n')

elif numop == 9:
    print('\n\t**[TO FIND THE [ADDITION AND SUBTRACTION] OF [TWO VECTORS: A and B] IN THE BI-DIMENSIONAL(XY) PLANE]**\n')
    Addition, Subtraction = addSubtraction()
    print('\t- The [Addition]: vector[a+b]:',Addition)
    print('\t- The [Subtraction]: vector[a-b]:',Subtraction,'\n')

elif numop == 10:
    print('\n\t**[TO GET THE VALUE OF THE RESULTANT(|R) VECTOR]**\n')
    ResultantVector()
    
elif numop == 11:
    print('\n\t**[TO CALCULATE THE [VECTOR(A)] AND [LENGHT] OF TWO GIVENS POINTS: P, AND Q]**\n')
    findVectorA()

elif numop == 12:
    print('\n\t\t**[ GIVENS [TWO VECTORS: A AND B] MULTIPLYED BY THE [SCALARS]: [COEFFIC1] AND [COEFFIC2] OR ]**')
    print('\t**[ GIVENS [THE POINTS: P, Q, AND R]  FIND [TWO VECTORS]: VECTOR(A)=VECTOR(PQ) AND VECTOR(B)=VECTOR(PR) ]**')
    print('\t**[ AND MULTIPLY BY THE [SCALARS]: [COEFFIC1] AND [COEFFIC2] AND TOO GET THE [ADDITION] AND [SUBTRACTION] ]**\n')
    formaComponent()

else:
    print('\n\t**[NEITHER OF THE PREVIOUS OPTIONS WAS SELECTED -- OK!]**\n')

input('\n\n\t\t. . . Key [ENTER] to exit -- Ok! . . .\n')
    
    
    

