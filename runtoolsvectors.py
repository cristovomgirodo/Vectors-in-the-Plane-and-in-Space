######################################################################################
#
# The runtoolsvectors.py will run various functions of the VectorModDev.py module
# Developed by Cristovom A. Girodo
# Date: 20230427 -- Stable Version: 1.3
#
######################################################################################

import math

print('\n\n\t    **[ WELCOME IN USING THE [RUNTOOLSVECTORS.PY] PROGRAM ]**') 
print('\t  **[ TO [SOLVE] VARIOUS PROBLEMS OF [VECTORS] in the [SPACE] ]**')
print('\t\t\t--[Version: 1.3 -- Stable]--')
print('\n\n\t**[INSTRUCTIONS OF USE]**')
print('\n- To find the [value] of the [Dot Product] of two vectors key [1]')
print('- To get the [Cross Product] of two [vectors: A and B] and the [Area(A)] of the')
print('  Triangle(PQR) key [2]\n')
print('- To calculate the [value] of the [SineTheta] between [two vectors] A and B')
print('  key [3]\n')
print('- To find the [value] of the [Scalar Triple Product] of three  vectors A, B,')
print('  and C key [4]\n')
print('- To calculate the [angle] between [two vectors] in space key[5]')
print('- To get the [value] of the [CossineTheta] between two vectors A and B key [6]')
print('- To find the [Distance] between two points P and Q key [7]')
print('- To calculate the [Dimensions] of the [Triangle(PQR)] givens the points: P, Q,')
print('  and R key [8]\n')
print('- To find the [Height(h)], [Area(A)] and angle[Theta] of the [Parallelogram(PQRS)] ')
print('  determined to [two adjacent vectors]: A and B or to [Coordinates] of the vertices: ')
print('  P, Q, R, and S key [9]\n')
print('- To get the [Volume(V)],[Height(h)] of the [Parallelepiped and Tetrahedron]')
print('  given four points: P, Q, R, S key [10]\n')
print('- To calculate the three [Inner Angles] of the [Triangle] given three points:')
print('  P,Q,and R key [11]\n')
print('- To find the [MID-POINT M] OF THE LINE SEGMENT BETWEEN [THE POINTS: P AND Q]')
print('  key [12]\n')
print('- To get the [Addition] and [Subraction] between [Two Vectors] A and B key [13]')
print('- To calculate the[VectorA] and [lenght] between the given Points: P, AND Q key [14]')
print('- To determine the [Direction Cosines] and [Direction Angles] givens an')
print('  Vector A or [two points]: P and Q key [15]\n')
print('- To find the [Addition] and [Subraction] between [Two Vectors]: A and B')
print('  multiplyed by scalars: [coeffic1 and coeffic2] key [16]\n')
      
from VectorModDev import * 
	
print('\n\t[§] Select an previous [option] that will used--Ok!\n')
numb = vectornumber()

if numb == 1:
    print('\n\t**[FIND THE [DOT PRODUCT] OF [TWO VECTORS] IN THE TRI-DIMENSIONAL(XYZ)')
    print(' SPACE]**\n')
    varint = 1
    vectorAB, dotproduct = dotProduct(varint)
    print('\t-- The list of the terms product:', vectorAB)
    print('\n\t- The [Dot product]: [a*b] of two vectors:', format((dotproduct),'<10.2f'),'\n')       
   
elif numb == 2:
    print('\n\t**[DETERMINE THE [CROSS PRODUCT(AxB) OF [TWO VECTORS: A AND B] AND FIND ')
    print('\t  THE [AREA(A) OF THE TRIANGLE(PQR) ] ]**')
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
    print('\n\t**[CALCULATE THE [SCALAR TRIPLE PRODUCT] BETWEEN [THREE VECTORS: A, B, ')
    print('\t  AND C] IN TRI-DIMENSIONAL(XYZ) SPACE]**\n')
    varint = 3
    MixedProduct, Parallelepiped, HeightParallelep, Tetrahedron = mixedProduct(varint)
    print('\t-- The [SCALAR TRIPLE PRODUCT]: a * ( b x c ) is:', MixedProduct)
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
    print('\n\t**[ GIVENS THE COORDINATES OF THE POINTS P, Q AND R FIND THE DIMENSIONS:')
    print('\t    SIDE(A), SIDE(B),SIDE(C), PERIMETER(P), HEIGHTS(H1,H2,H3), AND THE ]**')
    print('\t**[ AREA(A) OF THE TRIANGLE(PQR) ]**\n')
    varint = 3
    vectorAxB, AreaTriangle = crossProduct(varint)
    print('\t-- The [Cross Product]: vectorAxB',vectorAxB)
    print('\t-- The [Area(A) of a Triangle(PQR)] is:',format((AreaTriangle),'<10.2f'),'\n')
    
elif numb == 9:
    print('\t**[ FIND THE HEIGHT(H), AREA(A), AND THE ANGLE(THETA) OF THE PARALLELOGRAm(PQRS) ')
    print('\t   DETERMINED BY TWO ADJACENT VECTORS: A AND B OR TO [COORDINATES] VERTICES: P, Q,')
    print('\t   R, AND S  ]**\n')
    height, area, theta = coordOrcomp()
    print('\t-- The [height]:', format(height,"<10.2f"))
    print('\t-- The [Area]:', format(area,"<10.2f"))
    print('\t-- The angle [Theta in degree(º)] between the [adjacent vectors]: [vectorA] and ')
    print('\t-- [vectorB] is:', format(theta,"<10.2f"),'\n') 
    
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
    print('\n\t**[ WILL FIND THE [MIDPOINT(M)] OF THE [LINE SEGMENT] BETWEEN THE GIVEN')
    print('\t   POINTS : P AND Q ]**\n')
    MidPoint = midPoint()
    print('\t-- The (MidPoint M): M ',MidPoint,'\n')
    
elif numb == 13:
    print('\n\t**[ CALCULATE THE [ADDITION] AND [SUBTRACTION] OF THE [VECTORS]: A AND B ]**\n')
    Addition, Subtraction = addSubtraction()
    print('\n\t-- The [Addition]: vectorA+B',Addition)
    print('\t-- The [Subtraction]: vectorA-B',Subtraction,'\n')
    
elif numb == 14:
    print('\n**[ GIVENS [TWO POINTS P AND Q] FIND THE [VECTOR(A)] AND [LENGTH] IN THE')
    print('   [TRI-DIMENSIONAL(XYZ) SPACE]**\n')
    varint = 1 
    findVectorA(varint) # Was fix an error finded. 

elif numb == 15:
    print('\n\t**[ GIVENS AN VECTOR(A) OR TWO POINTS: P AND Q DETERMINE THE [DIRECTION')
    print('\t  ANGLES] AND [DIRECTION COSINES] ]**\n')
    directionAngles()

elif numb == 16:
    print('\n **[ GIVENS [TWO VECTORS: A AND B] MULTIPLYED BY THE [SCALARS]: [COEFFIC1] AND')
    print('   [COEFFIC2] OR ]**\n')
    print(' **[ GIVENS [THE POINTS: P, Q, AND R]  FIND [TWO VECTORS]: VECTOR(A)=VECTOR(PQ)')
    print('   AND VECTOR(B)=VECTOR(PR) ]**\n')
    print(' **[ AND MULTIPLY BY THE [SCALARS]: [COEFFIC1] AND [COEFFIC2] AND TOO GET THE')
    print('   [ADDITION] AND [SUBTRACTION] ]**\n')  
    formaComponent()

else:
    print('\n\t\t**[NEITHER OF THE PREVIOUS OPTIONS WAS SELECTED]**')
    print('\t\t[ RUN THE RUNTOOLSVECTORS.PY PROGRAM AGAIN -- OK! ]')

input('\n\n\t\t. . . Key [ENTER] to exit -- Ok! . . .\n')


    
