###############################################
#
# The runvectors2dim.py program
# Developed by Cristovom A. Girodo
# Date: 20221025 -- Stable Version: 1.3
#
###############################################

print('\n\n\t  **[ WELCOME IN USING THE [RUNVECTORS2DIM.PY] PROGRAM ]**') 
print('\t**[ TO [SOLVE] VARIOUS PROBLEMS OF [VECTORS] in the [PLANE] ]**')
print('\t\t\t--[Version: 1.3 -- Stable]--')
print('\n\n\t**[INSTRUCTIONS OF USE]**\n')
print('- To find the [Scalar Product: a * b] between [two vectors] key [1]')
print('- To calculate the [Perimeter(P)], [Height(h), and [Area(A)] of the\n  TrianglePQR givens the [points: P, Q, and R] key[2]\n')
print('- To get the [Area(S) and Height(h) of the [Parallelogram(PQRS)] given\n  the [points: P, Q, R, and S] key[3]\n')
print('- To find the [angle] between [two vectors] in plane key[4]')
print('- To calculate the [value] of the [CossineTheta] between\n  [two vectors] a and b key [5]\n')
print('- To get the [Distance] between [two points] given P and Q key [6]')
print('- To find the three [Inner Angles] of the [Triangle] of\n  three points given: P, Q, R key [7]\n')
print('- To calculate the [midPoint M(xM,yM)] between the points: P and Q key [8]')
print('- To get the [Addition and Subtraction] of [Two Vectors: a and b] key [9]')
print('- To calculate the [Resultant(|R) Vector] key [10]')
print('- To find the[VectorA] and [lenght] of givens Points: P, AND Q key [11]')
print('- To find the [Addition] and [Subraction] between [Two Vectors]\n  A and B multiplyed by scalars[coeffic1 and coeffic2] key [12]\n')

from VectorModule2Dim import *

print('\t[§] Select an previous [option] that will used--Ok!\n')
numop = vectornumber()

if numop == 1:
    print('\n\t**[TO FIND THE [SCALAR PRODUCT] OF [TWO VECTORS: A and B] IN THE')
    print('\t  BI-DIMENSIONAL(XY) PLANE]**\n')
    varint = 1
    ScalarProd, VectorAB = scalarProduct(varint)
    print('\t-- The [Vector] of the [terms of the Scalar Product]: vectorAB',VectorAB)
    print('\t-- The [Scalar Product(vectorAB)] of the vectors is:',format(ScalarProd,"<10.2f"),'\n')
    
elif numop == 2:
    print('\n **[TO CALCULATE THE [PERIMETER(P), HEIGHTS(H1,H2,H3),AND AREA(A) OF THE]**')
    print(' **[[TRIANGLE-PQR] GIVENS THE POINTS: P, Q, AND R IN THE BI-DIMENSIONAL(XY)')
    print('   PLANE]**\n')
    varint = 3
    scalarProduct(varint)
    
elif numop == 3:
    print('\n**[TO GET THE [AREA(S) AND HEIGHT(H) OF THE [PARALLELOGRAM(PQRS)] GIVEN ]**')
    print('**[THE POINTS: P, Q, R AND S IN THE BI-DIMENSIONAL(XY) PLANE]**\n')
    varint = 4
    scalarProduct(varint)
    
elif numop == 4:
    print('\n\t**[WILL FIND THE [VALUE] OF THE [THETA ANGLE] BETWEEN ')
    print('\t  [TWO VECTORS] GIVEN: A AND B]**\n')
    modVectorA, modVectorB, ScalarProduct,VectorAxB, AngleTheta_degrees = angleVectors()
    print('\t- The [terms] of the [VectorA*B] ís:', VectorAxB)
    print('\t- The [length] of a |vectorA|:', format((modVectorA),'<10.2f'))
    print('\t- The [length] of a |vectorB|:', format((modVectorB),'<10.2f'))
    print('\t- The [Scalar Product] is:',format((ScalarProduct),'<10.2f'))
    print('\n\t- The value of the [THETA ANGLE IN DEGREES] was calculate is:', format((AngleTheta_degrees),'<10.2f'),'\n')

elif numop == 5:
    print('\n\t**[TO CALCULATE THE [VALUE] OF THE [COSSINE THETA] BETWEEN')
    print('\t[TWO VECTORS] GIVEN: A AND B]**\n')
    modVectorA, modVectorB, ScalarProduct, VectorAxB, CosineRadians  = cosineTheta()
    print('\t- The [VectorA*B]:', VectorAxB)
    print('\t- The [length] of a |vectorA|:', format((modVectorA),'<10.2f'))
    print('\t- The [length] of a |vectorB|:', format((modVectorB),'<10.2f'))
    print('\t- The [Scalar Product] of the [VectorA*B] is:',format((ScalarProduct),'<10.2f'))
    print('\n\t- The value of the [COSINE THETA IN RADIANS] calculated is:', format((CosineRadians),'<10.2f'),'\n')

elif numop == 6:
    print('\n\t**[TO GET THE [DISTANCE(D)] BETWEEN ANY [TWO POINTS] GIVEN P AND Q]**\n')
    VectorPQ, VectorQUAD, Distance = distanceTwoPoints()
    print('\n\t-- The [vectorPQ]: vectorPQ',VectorPQ)
    print('\t-- The [Quadratic Components] of the [vectorPQ]: VectorQUAD',VectorQUAD)
    print('\t-- The [Distance(D)] geted between Two (Points) P and Q] is:',format((Distance),'<10.2f'),'\n')
    
elif numop == 7:
    print('\n**[ TO FIND THE THREES [INNER ANGLES] OF THE [TRIANGLE(PQR)] ]**\n')
    innerAngleTriangle()

elif numop == 8:
    print('\n  **[ WILL DETERMINE THE [MIDPOINT(M)] BETWEEN THE (POINTS): P AND Q GIVEN]**\n')
    VectorMidPoint = midPoint()
    print('\t-- The [(MidPoint)]: M',VectorMidPoint,'\n')

elif numop == 9:
    print('\n\t**[TO FIND THE [ADDITION AND SUBTRACTION] OF [TWO VECTORS: A and B] IN THE')
    print('\tBI-DIMENSIONAL(XY) PLANE]**\n')
    Addition, Subtraction = addSubtraction()
    print('\t- The [Addition]: vector[a+b]:',Addition)
    print('\t- The [Subtraction]: vector[a-b]:',Subtraction,'\n')

elif numop == 10:
    print('\n\t**[TO GET THE VALUE OF THE RESULTANT(|R) VECTOR]**\n')
    ResultantVector()
    
elif numop == 11:
    print('\n **[TO FIND THE [VECTOR(A)] THAT REPRESENT THE TWO GIVENS POINTS: P, AND Q]**')
    print(' **[ AND TOO THE [LENGTH] OF THE VECTOR(A) = VECTOR(PQ) ]**\n')
    findVectorA()

elif numop == 12:
    print('\n\t**[ GIVENS [TWO VECTORS: A AND B] MULTIPLYED BY THE [SCALARS]:')
    print('\t  [COEFFIC1] AND [COEFFIC2] OR ]**\n')
    print('\t**[ GIVENS [THE POINTS: P, Q, AND R]  FIND [TWO VECTORS]: ')
    print('\t  VECTOR(A)=VECTOR(PQ) AND VECTOR(B)=VECTOR(PR) ]**\n')
    print('\t**[ AND MULTIPLY BY THE [SCALARS]: [COEFFIC1] AND [COEFFIC2] AND')
    print('\t  TOO GET THE [ADDITION] AND [SUBTRACTION] ]**\n')
    formaComponent()

else:
    print('\n\t\t**[NEITHER OF THE PREVIOUS OPTIONS WAS SELECTED]**')
    print('\t\t[ RUN THE RUNVECTORS2DIM.PY PROGRAM AGAIN -- OK! ]')

input('\n\n\t\t. . . Key [ENTER] to exit -- Ok! . . .\n')
    
    
    

