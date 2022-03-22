#
# The runtoolsvectors.py will run various functions of the VectorModDev.py module
# Developed by Cristovom A. Girodo
# Date: 20220123 -- Stable Version: 1.0
#

import math

print('\n\n\t\t    **[ WELCOME IN USING THE [RUNTOOLSVECTORS.PY] PROGRAM ]**') 
print('\t\t  **[ TO [SOLVE] VARIOUS PROBLEMS OF [VECTORS] in the [SPACE] ]**')
print('\t\t\t\t--[Version: 1.0 -- Stable]--')
print('\n\n\t**[INSTRUCTIONS OF USE]**')
print('\n\t- To find the [value] of the [Dot Product] of two vectors key [1]')
print('\t- To get the [Cross Product] of two [vectors: A and B] and the [Area(A)] of the Triangle(PQR) key [2]')
print('\t- To calculate the [value] of the [SineTheta] between two vectors A and B key [3]')
print('\t- To find the [value] of the [Scalar Triple Product] of three  vectors A, B, and C key [4]')
print('\t- To calculate the [angle] between [two vectors] in space key[5]')
print('\t- To get the [value] of the [CossineTheta] between two vectors A and B key [6]')
print('\t- To find the [Distance] between two points P and Q key [7]')
print('\t- To calculate the [Dimensions] of the [Triangle(PQR)] givens the points: P, Q, R key [8]')
print('\t- To find the [Area] of the [Parallelogram] given [two vectors A and B] key [9]')
print('\t- To get the [Volume(V)], [Height(h)] of the [Parallelepiped and Tetrahedron] given four points: P, Q, R, S key [10]')
print('\t- To calculate the three [Inner Angles] of the [Triangle] given three points: P, Q, R key [11]')
print('\t- To find the [MID-POINT M] OF THE LINE SEGMENT BETWEEN [THE POINTS: P AND Q] key [12]')
print('\t- To get the [Addition] and [Subraction] between [Two Vectors] A and B key [13]')
print('\t- To calculate the[VectorA] and [lenght] of givens Points: P, AND Q key [14]')
print('\t- To determine the [Direction Cosines] and [Direction Angles] givens an Vector A or two points: P and Q key [15]')
print('\t- To find the [Addition] and [Subraction] between [Two Vectors] A and B multiplyed by scalars[coeffic1 and coeffic2] key [16]\n')
      
from VectorModDev import * 	

print('\t[§] Select an previous [option] that will used--Ok!\n')
numb = vectornumber()

if numb == 1:
    print('\n\t**[FIND THE [DOT PRODUCT] OF [TWO VECTORS] IN THE TRI-DIMENSIONAL(XYZ) SPACE]**\n')
    varint = 1
    vectorAB, dotproduct = dotProduct(varint)
    print('\t-- The list of the terms product:', vectorAB)
    print('\n\t- The [Dot product]: [a*b] of two vectors:', format((dotproduct),'<10.2f'),'\n')       
   
elif numb == 2:
    print('\n\t**[DETERMINE THE [CROSS PRODUCT(AxB) OF [TWO VECTORS: A AND B] AND FIND THE [AREA(A) OF THE TRIANGLE(PQR) ] ]**')
    varint = 1
    VectorAxB, AreaTriangle = crossProduct(varint)
    print('\t-- The [Cross Product]: vectorAxB',VectorAxB)
    print('\t-- The [Area(A) of a Triangle(PQR)] is:',format((AreaTriangle),'<10.2f'),'\n')
       
elif numb == 3:
    print('\n\t**[FIND THE VALUE OF THE SINETHETA]**\n')
    varint = 2
    magnitA, magnitB, magnitAxB, SineTheta = crossProduct(varint)
    print('\t-- The [length] of the [vectorA]=|vectorA|:', format((magnitA), '<10.2f'))
    print('\t-- The [length] of the [vectorB]=|vectorB|', format((magnitB), '<10.2f'))
    print('\t-- The [length] of the [vectorAxB]=|vectorAxB|', format((magnitAxB), '<10.2f'))
    print('\t-- The value of the [SINETheta] is:', format((SineTheta), '<10.2f'),'\n')
        
elif numb == 4:
    print('\n\t**[CALCULATE THE [SCALAR TRIPLE PRODUCT] BETWEEN [THREE VECTORS: A, B, AND C] IN TRI-DIMENSIONAL(XYZ) SPACE]**\n')
    varint = 3
    MixedProduct, Parallelepiped, HeightParallelep, Tetrahedron = mixedProduct(varint)
    print('\t--The [SCALAR TRIPLE PRODUCT]: a * ( b x c ) is:', MixedProduct)
    print('\t-- The [VOLUME(V) PARALLELEPIPED]:', format((Parallelepiped),'<10.2f'))
    print('\t-- The [HEIGHT(H) PARALLELEPIPED]:', format((HeightParallelep),'<10.2f'))
    print('\t-- The [Tetrahedron volume]:', format((Tetrahedron),'<10.2f'),'\n')
     
elif numb == 5:
    print('\n\t**[WILL GET THE VALUE OF THE [THETA ANGLE] BETWEEN VECTORS: A AND B]**\n')
    modVectorA, modVectorB, Dotproduct,AngleTheta_degrees = angleVectors()
    print('\n\t- The [length] of the [vectorA]=|vectorA|:', format((modVectorA),'<10.2f'))
    print('\t- The [length] of the [vectorB]=|vectorB|:', format((modVectorB),'<10.2f'))
    print('\t- The [dot product] is:',format((Dotproduct),'<10.2f'))
    print('\n\t\t- The [ANGLE THETA IN DEGREE] was find is:', format((AngleTheta_degrees),'<10.2f'),'\n')
    
elif numb == 6:
    print('\n\t**[FIND THE [VALUE] OF THE [COSSINETHETA] BETWEEN VECTORS: A AND B]**\n')
    varint = 3
    modVectorA, modVectorB, ScalarVectorAB, CossineTheta = dotProduct(varint)
    print('\t-- The length [|vectorA|] is:', format((modVectorA), '<10.2f'))
    print('\t-- The length [|vectorB|] is:', format((modVectorB), '<10.2f'))
    print('\t-- The value [ScalarVectorA*B] is:', format((ScalarVectorAB), '<10.2f'))
    print('\t-- The value of the [CossineTheta] is:', format((CossineTheta), '<10.2f'),'\n')
    
elif numb == 7:
    print('\n\t**[DETERMINE THE DISTANCE(d) BETWEEN TWO GIVENS POINTS P and Q]**\n')
    VectorPQ, VectorQUAD, Distance = distanceTwoPoints()
    print('\t-- The [vectorPQ]: vectorPQ',VectorPQ)
    print('\t-- The [Quadratic Components] of the [vectorCQD]:vectorCQD',VectorQUAD)
    print('\t-- The [Distance(d)] geted between (Two Points) P and Q is:',format((Distance),'<10.2f'),'\n')
        
elif numb == 8:
    print('\n\t **[ GIVENS THE COORDINATES OF THE POINTS P, Q AND R FIND THE DIMENSIONS SIDE(A), SIDE(B), ]**')
    print('\t**[  SIDE(C), PERIMETER(P), HEIGHTS(H1,H2,H3), AND AREA(A) OF THE TRIANGLE(PQR) ]**\n')
    varint = 3
    vectorAxB, AreaTriangle = crossProduct(varint)
    print('\t-- The [Cross Product]: vectorAxB',vectorAxB)
    print('\t-- The [Area(A) of a Triangle(PQR)] is:',format((AreaTriangle),'<10.2f'),'\n')
    
elif numb == 9:
    print('\t\t**[ FIND THE AREA(A) AND HEIGHT(H) PARALLELOGRAM GIVEN THE VECTORS: A AND B ]**\n')
    varint = 4
    Height, AreaParallelogram = crossProduct(varint)
    print('\t-- The [Height(h) Parallelogram] is:', format((Height),'<10.2f'))
    print('\t-- The [Area(A) Parallelogram] is:', format((AreaParallelogram),'<10.2f'),'\n')
    
elif numb == 10:
    print('\n\t**[ GIVENS THE COORDINATES OF THE POINTS P, Q, R AND S FIND THE ]**')
    print('\t**[ VOLUME(V) AND HEIGHT(H) OF THE PARALLELEPIPED AND TETRAHEDRON ]**\n')
    varint = 4
    MixedProduct, Parallelepiped, HeightParallelep, Tetrahedron = mixedProduct(varint)
    print('\n\t-- [THE SCALAR TRIPLE PRODUCT]: a * ( b x c ) is:', MixedProduct)
    print('\t-- The [VOLUME(V) PARALLELEPIPED]:', format((Parallelepiped),'<10.2f'))
    print('\t-- The [HEIGHT(H) PARALLELEPIPED]:', format((HeightParallelep),'<10.2f'))
    print('\t-- The [tetrahedron volume]:', format((Tetrahedron),'<10.2f'),'\n')
    
elif numb == 11:
    print('\n\t**[ GIVENS THE COORDINATES OF THE POINTS P, Q AND R ]**')
    print('\t**[ FIND THE [INNER ANGLES] OF THE TRIANGLE(PQR) ]**\n')
    getThreeAngles()
    
elif numb == 12:
    print('\n\t**[ WILL FIND THE [MIDPOINT(M)] OF THE [LINE SEGMENT] BETWEEN THE POINTS GIVEN: P AND Q ]**\n')
    MidPoint = midPoint()
    print('\t-- The (MidPoint M): M ',MidPoint,'\n')
    
elif numb == 13:
    print('\n\t**[ CALCULATE THE [ADDITION] AND [SUBTRACTION] OF THE [VECTORS]: A AND B ]**\n')
    Addition, Subtraction = addSubtraction()
    print('\n\t-- The [Addition]: vectorA+B',Addition)
    print('\t-- The [Subtraction]: vectorA-B',Subtraction,'\n')
    
elif numb == 14:
    print('\n\t**[ GIVENS TWO POINTS P AND Q] FIND THE [VECTOR(A)] AND [LENGHT] IN THE [TRI-DIMENSIONAL(XYZ) SPACE]**\n')
    varint = 1 
    findVectorA(varint) # Was fix an error finded. 

elif numb == 15:
    print('\n\t**[ GIVENS AN VECTOR(A) OR TWO POINTS: P AND Q DETERMINE THE [DIRECTION ANGLES] AND [DIRECTION COSINES] ]**\n')
    directionAngles()

elif numb == 16:
    print('\n\t\t**[ GIVENS [TWO VECTORS: A AND B] MULTIPLYED BY THE [SCALARS]: [COEFFIC1] AND [COEFFIC2] OR ]**')
    print('\t**[ GIVENS [THE POINTS: P, Q, AND R]  FIND [TWO VECTORS]: VECTOR(A)=VECTOR(PQ) AND VECTOR(B)=VECTOR(PR) ]**')
    print('\t**[ AND MULTIPLY BY THE [SCALARS]: [COEFFIC1] AND [COEFFIC2] AND TOO GET THE [ADDITION] AND [SUBTRACTION] ]**\n')
    formaComponent()

else:
    print('\n\t**[NEITHER OF THE PREVIOUS OPTIONS WAS SELECTED -- OK!]**\n')

input('\n\n\t\t. . . Key [ENTER] to exit -- Ok! . . .\n')


    
