#######################################################
#
# The VectorModDev.py module
# Developed by Cristovom A. Girodo
# Date: 20220102 -- Stable Version: 1.0
#
#######################################################

import math

def vectornumber():
    while True:
        try:
            coeffic1 = int(input("\t[º>º] What is the new value? "))
            print('\t   **[The typed number]:',coeffic1,'is a [valid integer number!]\n]')
            return coeffic1
        except ValueError as err:
            print('\t    /////')
            print('\t   @<@  [Warning!]:',err)
            print('\t    \~/  [TYPE AN [NEW INTEGER NUMBER] IN NEXT INSTRUCTION -- OK!]\n')
       
def introduce():
    while True:
        try:
            coeffic = float(input("\t-_- What is the new value? "))
            print('\t    **[The typed number]:',coeffic,'is a [valid float number!]\n]')
            return coeffic
        except ValueError as err:
            print('\t    /////')
            print('\t    º<º [Warning!]:',err)
            print('\t    \~/ [TYPE AN NEW INTEGER OR FLOAT NUMBER IN NEXT INSTRUCTION -- OK!]\n')

def pointCoord():
    # This function pointCoord() only will enter all the coordinates: x, y, z of any point.
    
    point = []
    
    for j in range(1, 4):
       
        if j == 1:
            print("\n\t* Introduce the %dº" %j,"[Coordinate(x)].")
            u = introduce()
            point.append(u)      
        elif j == 2:
            print("\n\t* Enter with the %dº" %j,"[Coordinate(y)].")
            v = introduce()
            point.append(v)  
        elif j == 3:
            print("\n\t* Give the %dº" %j,"[Coordinate(z)].")
            w = introduce()
            point.append(w)
            return point

def coordinatesPoint(number):
    print('\n\t-- Enter the (coordinates: xP, yP, zP) of the (Point P)? ')
    pointP = pointCoord()
    print('\t-- Introduce the (coordinates: xQ, yQ, zQ) of the (Point Q)? ')
    pointQ = pointCoord()

    if number == 2:
        return pointP, pointQ
    elif number == 3:
        print('\t-- Provide the (coordinates: xR, yR, zR) of the (Point R)? ')
        pointR = pointCoord()
        return pointP, pointQ, pointR
    
def compVector():

    vectorComponents = []

    for h in range(1,4):
        
        if h == 1:
            print('\n\t- Enter the %dº' %h,'[Component(x)]!')
            u = introduce()
            vectorComponents.append(u)     
        elif h == 2:
            print('\n\t- Introduce the %dº' %h,'[Component(y)]!')
            v = introduce()
            vectorComponents.append(v)
        elif h == 3:
            print('\n\t- Give the %dº' %h,'[Component(z)]!')
            w = introduce()
            vectorComponents.append(w)
            return vectorComponents
            
def componentsVector(number):
    print('\n\t- Attribute the [Components] of the [1º vectorA]!')
    vectA = compVector()
    print('\n\t- Provide the [Components] of the [2º vectorB]!')
    vectB = compVector()
    
    if number == 2:
        return vectA, vectB
    elif number == 3:
        print('\n\t- Provide the [Components] of the [3º vectorC]!')
        vectC = compVector()
        return vectA, vectB, vectC

def magnitudeBiVector(x,y):
    magbivector = math.sqrt(math.pow(x,2) + math.pow(y,2))
    return magbivector

def magnitudeTriVector(x,y,z):
    magtrivector = math.sqrt(math.pow(x,2) + math.pow(y,2) + math.pow(z,2) )
    return magtrivector

def subQdRoot(hip,cat):
    height = math.sqrt( math.pow(hip,2) - math.pow(cat,2) )
    return height

def answer():
    print('\n\t*[ANSWER]*\n')
    return

def addSubtraction():
    varint = 2
    vectorA, vectorB = componentsVector(varint)
    print('\n\t-- The [vectorA]: vectorA', vectorA)
    print('\t-- The [vectorB]: vectorB', vectorB, '\n')
    addition = []
    subtraction = []
    answer()

    for j in range(0,3):
        add = ( vectorA[j] + vectorB[j] )
        addition.append(add)
        subt = ( vectorA[j] - vectorB[j] )
        subtraction.append(subt)
        
    return addition, subtraction

def findTwoOrThreeVectors(number):
    
    if number == 3:
        # Enter the coordinates of the vertices points: P, Q, and R of Triangle
        pointP, pointQ, pointR = coordinatesPoint(number)
        
        xP=xQ=xR=yP=yQ=yR=zP=zQ=zR = 0
        for coord in range(0,3):
            if coord == 0:
                xP = pointP[coord]
                xQ = pointQ[coord]
                xR = pointR[coord]
            elif coord == 1:
                yP = pointP[coord]
                yQ = pointQ[coord]
                yR = pointR[coord]
            elif coord == 2:
                zP = pointP[coord]
                zQ = pointQ[coord]
                zR = pointR[coord]
                
        PointP = (xP,yP,zP)
        print('\n\t- The (Point P): P',PointP)
        PointQ = (xQ,yQ,zQ)
        print('\t- The (Point Q): Q',PointQ)
        PointR = (xR,yR,zR)
        print('\t- The (Point R): R',PointR)
        
        vectorPQ = []
        vectorPR = []
        vectorQR = []
        
        for p in range (0,3):
            coordPQ = ( pointQ[p] - pointP[p] )
            vectorPQ.append(coordPQ)
            coordPR = ( pointR[p] - pointP[p] )
            vectorPR.append(coordPR)
            coordQR = ( pointR[p] - pointQ[p] )
            vectorQR.append(coordQR)
  
        vectA = vectorPQ
        vectB = vectorPR
        vectC = vectorQR

        a1 = vectorPQ[0]
        a2 = vectorPQ[1]
        a3 = vectorPQ[2]
        sideA = magnitudeTriVector(a1,a2,a3)
        b1 = vectorPR[0]
        b2 = vectorPR[1]
        b3 = vectorPR[2]
        sideB = magnitudeTriVector(b1,b2,b3)
        c1 = vectorQR[0]
        c2 = vectorQR[1]
        c3 = vectorQR[2]
        sideC = magnitudeTriVector(c1,c2,c3)

        Perimeter = sideA + sideB + sideC

        # find the heights
        # vectorAxC = vectorPQºQR
        # vectorCxB = vectorQRºPR
        # vectorBxA = vectorPRºPQ
        
        vectorPQºQR = []
        vectorQRºPR = []
        vectorPRºPQ = []

        ScalarProd0 = 0
        ScalarProd1 = 0
        ScalarProd2 = 0
        
       # Find the Scalars Procucts
        for j in range(0, 3):
            term0 = vectorPQ[j] * vectorQR[j]
            ScalarProd0 = ScalarProd0 + term0
            vectorPQºQR.append(term0)
            term1 = vectorQR[j] * vectorPR[j]
            ScalarProd1 = ScalarProd1 + term1
            vectorQRºPR.append(term1)
            term2 = vectorPR[j] * vectorPQ[j]
            ScalarProd2 = ScalarProd2 + term2
            vectorPRºPQ.append(term2)
          
        # Find the component of a along c
        cat1 = ( ScalarProd0 /sideC )
        hip1 = sideA
        height1 = subQdRoot(hip1, cat1)
        # Find the component of c along b
        cat2 = (  ScalarProd1 / sideB )
        hip2 = sideC
        height2 = subQdRoot(hip2, cat2)
        # Find the component of b along a
        cat3 = ( ScalarProd2 / sideA )
        hip3 = sideB
        height3 = subQdRoot(hip3, cat3)
        answer()
        print('\t- The [vectorA]=vectorPQ',vectorPQ)
        print('\t- The [vectorB]=vectorPR',vectorPR)
        print('\t- The [vectorC]=vectorQR',vectorQR,'\n')
        print('\t-- The [sideA] of the triangle(PQR)] is:',format(sideA,"<10.2f"))
        print('\t-- The [sideB] of the triangle(PQR)] is:',format(sideB,"<10.2f"))
        print('\t-- The [sideC] of the triangle(PQR)] is:',format(sideC,"<10.2f"))
        print('\t-- The [Perimeter] of the [triangle(PQR)] is',format(Perimeter,"<10.2f"),'\n')
        print('\t-- The [terms] of the [Scalar Product(PQºQR)] is:',vectorPQºQR)
        print('\t-- The [terms] of the [Scalar Product(QRºPR)] is:',vectorQRºPR)
        print('\t-- The [terms] of the [Scalar Product(PRºPQ)] is:',vectorPRºPQ,'\n')
        print('\t-- The [Scalar Product(PQºQR)] is:',format(ScalarProd0,"<10.2f"))
        print('\t-- The [Scalar Product(QRºPR)] is:',format(ScalarProd1,"<10.2f"))
        print('\t-- The [Scalar Product(PRºPQ)] is:',format(ScalarProd2,"<10.2f"),'\n')
        print('\t-- The [Height(h1) relative as sideQR] is',format(height1,"<10.2f"))
        print('\t-- The [Height(h2) relative as sidePR] is',format(height2,"<10.2f"))
        print('\t-- The [Height(h3) relative as sidePQ] is',format(height3,"<10.2f"),'\n')
        
        return vectA, vectB
    
    elif number == 4:
        # Enter the coordinates of the vertices points: P, Q, R, and S
        varint = 3 
        pointP, pointQ, pointR = coordinatesPoint(varint)
        print('\t-- Give the [Coordinates: xS, yS, zS] of the [point S]? ')
        pointS = pointCoord()

        xP=xQ=xR=xS=yP=yQ=yR=yS=zP=zQ=zR=zS = 0
        for coord in range(0,3):
            if coord == 0:
                xP = pointP[coord]
                xQ = pointQ[coord]
                xR = pointR[coord]
                xS = pointS[coord]
            elif coord == 1:
                yP = pointP[coord]
                yQ = pointQ[coord]
                yR = pointR[coord]
                yS = pointS[coord]
            elif coord == 2:
                zP = pointP[coord]
                zQ = pointQ[coord]
                zR = pointR[coord]
                zS = pointS[coord]
                
        PointP = (xP,yP,zP)
        print('\n\t- The (Point P): P',PointP)
        PointQ = (xQ,yQ,zQ)
        print('\t- The (Point Q): Q',PointQ)
        PointR = (xR,yR,zR)
        print('\t- The (Point R): R',PointR)
        PointS = (xS,yS,zS)
        print('\t- The (Point S): S',PointS)
       
        vectorPQ = []
        vectorPR = []
        vectorPS = []
        
        for q in range (0,3):
            coordPQ = pointQ[q] - pointP[q]
            vectorPQ.append(coordPQ)
            coordPR = pointR[q] - pointP[q]
            vectorPR.append(coordPR)
            coordPS = pointS[q] - pointP[q]
            vectorPS.append(coordPS)
            
        vectA = vectorPQ
        vectB = vectorPR
        vectC = vectorPS
        answer()
        
        print('\t- The [vectorA]=vectorPQ',vectorPQ)
        print('\t- The [vectorB]=vectorPR',vectorPR)
        print('\t- The [vectorC]=vectorPS',vectorPS ,'\n')
        return vectA, vectB, vectC

def getThreeAngles():
    varint = 3
    pointP, pointQ, pointR = coordinatesPoint(varint)
    
    xP=xQ=xR=yP=yQ=yR=zP=zQ=zR = 0
    for coord in range(0,3):
        if coord == 0:
            xP = pointP[coord]
            xQ = pointQ[coord]
            xR = pointR[coord] 
        elif coord == 1:
            yP = pointP[coord]
            yQ = pointQ[coord]
            yR = pointR[coord]  
        elif coord == 2:
            zP = pointP[coord]
            zQ = pointQ[coord]
            zR = pointR[coord] 
                
    PointP = (xP,yP,zP)
    print('\n\t- The (Point P): P',PointP)
    PointQ = (xQ,yQ,zQ)
    print('\t- The (Point Q): Q',PointQ)
    PointR = (xR,yR,zR)
    print('\t- The (Point R): R',PointR)
    answer()
    for sp in range (0,3):
        # Will find the scalar product: PR * PQ = b * c
        if sp == 0:
            vectorPR = []
            vectorPQ = []
            for p in range (0,3):
                compPR = ( pointR[p] - pointP[p] )
                vectorPR.append(compPR)
                compPQ = ( pointQ[p] - pointP[p] )
                vectorPQ.append(compPQ)
                
            print('\t- The [vectorB]=vectorPR',vectorPR)
            print('\t- The [vectorC]=vectorPQ',vectorPQ,'\n')

            vectorB = vectorPR
            vectorC = vectorPQ 
            
            scalarProductBC = 0
            vectBC = []
            
            for v0 in range (0,3):
                term0 = vectorPR[v0] * vectorPQ[v0]
                scalarProductBC = scalarProductBC + term0
                vectBC.append(term0)
                
            b1 = vectorB[0]
            b2 = vectorB[1]
            b3 = vectorB[2]
            normB = ( magnitudeTriVector(b1, b2, b3) )
            c1 = vectorC[0]
            c2 = vectorC[1]
            c3 = vectorC[2]
            normC = ( magnitudeTriVector(c1, c2, c3) )
            normBxCproduct = ( normB * normC )
            CossineT = ( scalarProductBC / normBxCproduct )
            angle_radians = math.acos(CossineT)
            AngleTheta_degrees = math.degrees(angle_radians)
            print('\t- The Dot Product: [b * c] is:',format((scalarProductBC),'<10.2f'))
            print('\t- The value of the [ANGLE THETA] was calculate is:', format((AngleTheta_degrees),'<10.2f'),'\n')
     
        elif sp == 1:
            # Will find the scalar product: QR * QP = a * c
            vectorQR = []
            vectorQP = []
            
            for q in range (0,3):
                compQR = ( pointR[q] - pointQ[q] )
                vectorQR.append(compQR)
                compQP = ( pointP[q] - pointQ[q] )
                vectorQP.append(compQP)
                
            print('\n\t- The [vectorA]=vectorQR',vectorQR)
            print('\t- The [vectorC]=vectorQP',vectorQP,'\n')

            vectorA = vectorQR
            vectorC = vectorQP 
            
            scalarProductAC = 0
            vectBC = []
            
            for v1 in range (0,3):
                term1 = vectorQR[v1] * vectorQP[v1]
                scalarProductAC = scalarProductAC + term1
                vectBC.append(term1)
                
            a1 = vectorA[0]
            a2 = vectorA[1]
            a3 = vectorA[2]
            normA = ( magnitudeTriVector(a1, a2, a3) )
            c1 = vectorC[0]
            c2 = vectorC[1]
            c3 = vectorC[2]
            normC = ( magnitudeTriVector(c1, c2, c3) )
            normAxCproduct = ( normA * normC )
            CossineB = ( scalarProductAC / normAxCproduct )
            angle_radians = math.acos(CossineB)
            AngleBeta_degrees = math.degrees(angle_radians)
            print('\t- The Dot Product: [a * c] is:',format((scalarProductAC),'<10.2f'))
            print('\t- The value of the [ANGLE BETA] was calculate is:', format((AngleBeta_degrees),'<10.2f'),'\n')
            
        elif sp == 2:
            # Will find the scalar product: RQ * RP = a * b
            vectorRQ = []
            vectorRP = []
            
            for r in range (0,3):
                compRQ = ( pointQ[r] - pointR[r] )
                vectorRQ.append(compRQ)
                compRP = ( pointP[r] - pointR[r] )
                vectorRP.append(compRP)
                
            print('\n\t- The [vectorA]=vectorRQ',vectorRQ)
            print('\t- The [vectorB]=vectorRP',vectorRP,'\n')

            vectorA = vectorRQ
            vectorB = vectorRP
            
            scalarProductAB = 0
            vectAB = []
            
            for v2 in range (0,3):
                term2 = vectorRQ[v2] * vectorRP[v2]
                scalarProductAB = scalarProductAB + term2
                vectAB.append(term2)
                
            a1 = vectorA[0]
            a2 = vectorA[1]
            a3 = vectorA[2]
            normA = ( magnitudeTriVector(a1, a2, a3) )
            b1 = vectorB[0]
            b2 = vectorB[1]
            b3 = vectorB[2]
            normB = ( magnitudeTriVector(b1, b2, b3) )
            normAxBproduct = ( normA * normB )
            CossineGama = ( scalarProductAB / normAxBproduct )
            angle_radians = math.acos(CossineGama)
            AngleGama_degrees = math.degrees(angle_radians)
            print('\t- The Dot Product: [a * b] is:',format((scalarProductAB),'<10.2f'))
            print('\t- The value of the [ANGLE GAMA] was calculate is:', format((AngleGama_degrees),'<10.2f'),'\n')
            
            if AngleTheta_degrees == AngleBeta_degrees and AngleTheta_degrees == AngleGama_degrees and AngleBeta_degrees == AngleGama_degrees:
                print('\n\t\t-- The triangle is [Equilateral]!','\n')
            elif AngleTheta_degrees == AngleBeta_degrees or AngleTheta_degrees == AngleGama_degrees or AngleBeta_degrees == AngleGama_degrees:
                print('\n\t\t-- The triangle is [Isosceles]!','\n')
            elif AngleTheta_degrees != AngleBeta_degrees and AngleTheta_degrees != AngleGama_degrees and AngleBeta_degrees != AngleGama_degrees:
                print('\n\t\t-- The triangle is [Scalene]!','\n')

            addInnerAngle = AngleTheta_degrees + AngleBeta_degrees + AngleGama_degrees
                
            print('\t- THE [ADD] OF THE INNER ANGLE OF THE TRIANGLE] is:',format((addInnerAngle),'<10.2f'),'\n')
            print('\n\t\t--[END CALCULUS-OK!]--\n')
    return

def dotProduct(number):
    #
    # This function dotProduct(number) after enter all the coordinates: x, y, z of the 
    # vectorA and vectorB, will find [the Dot Product]: A*B = a1*b1 + a2*b2 + a3*b3 
    # or get the CossineTheta given to Cossine(Theta) = dot_product / normAxBproduct
    #

    varint = 2
    vectorA, vectorB = componentsVector(varint)
    
    print('\n\t-- The [vectorA]: vectorA',vectorA)
    print('\t-- The [vectorB]: vectorB',vectorB, '\n')
    
    dot_product = 0
    vectAB = []
    
    for p in range(0,3):
        term = vectorA[p] * vectorB[p]
        dot_product = dot_product + term
        vectAB.append(term)
    
    if number == 1:
        answer()
        return vectAB, dot_product

    elif number == 2:
        answer()
        return vectorA, vectorB, vectAB, dot_product
    
    elif number == 3:
        answer()
        a1 = vectorA[0]
        a2 = vectorA[1]
        a3 = vectorA[2]
        normA = ( magnitudeTriVector(a1, a2, a3) )
        b1 = vectorB[0]
        b2 = vectorB[1]
        b3 = vectorB[2]
        normB = ( magnitudeTriVector(b1, b2, b3) )
        normAxBproduct = normA * normB
        cossineTheta = dot_product / normAxBproduct
        return normA, normB, dot_product, cossineTheta
        
def crossProduct(number):
    # This function crossProduct(number) after enter all the [coomponents]: a1, a2, a3, b1, b2, b3   
    # of the vectorA and vectorB or the (coordinates) of the given points: P, Q, and R, 
    # will find the Cross Product given to:
    #
    #             |  i   j   k |
    # vectorAxB = | a1  a2  a3 |  
    #             | b1  b2  b3 |  
    #                                       
    #  will calculate the value of the [area A of the parallelogram] given to [ A = |vectorAxB| ]
    #  as also will determine the value of the [area A of the triangle]: A = |vectorAxB| / 2 or
    #  will get the value of the SineTheta given to [ sineTheta = normAxB / normproduct ].
    # 
    
    if number == 1 or number == 2 or number == 4:
        # Enter the [components] of the vectors: A an B
        varint = 2
        vectorA, vectorB = componentsVector(varint)
        print('\n\t-- The [vectorA]: vectorA',vectorA)
        print('\t-- The [vectorB]: vectorB',vectorB, '\n')
        
    elif number == 3:
        # Enter the [coordinates] of the givens points: P, Q, and R
        varint = 3
        vectorA, vectorB = findTwoOrThreeVectors(varint)

    vectAxB = []
    Cx = ( ( vectorA[1] * vectorB[2] ) - ( vectorA[2] * vectorB[1] ) )
    vectAxB.append(Cx)
    Cy = ( ( vectorA[2] * vectorB[0] ) - ( vectorA[0] * vectorB[2] ) )
    vectAxB.append(Cy)
    Cz = ( ( vectorA[0] * vectorB[1] ) - ( vectorA[1] * vectorB[0] ) )
    vectAxB.append(Cz)
    
    if number == 1:
        # find the area(A) trianglePQR
        answer()
        areaTriangle = abs( magnitudeTriVector(Cx, Cy, Cz) ) / 2 
        return vectAxB, areaTriangle
    
    elif number == 2:
        answer()
        a1 = vectorA[0]
        a2 = vectorA[1]
        a3 = vectorA[2]
        normA = ( magnitudeTriVector(a1, a2, a3) )
        b1 = vectorB[0]
        b2 = vectorB[1]
        b3 = vectorB[2]
        normB = ( magnitudeTriVector(b1, b2, b3) )
        normAxB = ( magnitudeTriVector(Cx, Cy, Cz) )
        normproduct = normA * normB
        sineTheta = normAxB / normproduct
        return normA, normB, normAxB, sineTheta
    
    elif number == 3:
        # find the area(A) trianglePQR
        areaTriangle = abs( magnitudeTriVector(Cx, Cy, Cz) ) / 2  
        return vectAxB, areaTriangle

    elif number == 4 :
        # find the area(A) parallelogramPQRS
        answer()
        normAxB = abs( magnitudeTriVector(Cx, Cy, Cz) )
        a1 = vectorA[0]
        a2 = vectorA[1]
        a3 = vectorA[2]
        normA = ( magnitudeTriVector(a1, a2, a3) )
        heightParallelog = abs(  normAxB / normA )
        return heightParallelog, normAxB
    
def mixedProduct(number):
    #
    # This function mixedProduct(number) after enter all tthe [coomponents]: a1, a2, a3, b1, b2, b3, c1, c2, and c3  
    # of the vectorA,  vectorB and vectorC or the (coordinates) of the given points: P, Q, R, and S , will find  the
    # Mixed Product given to:
    #                                               | a1  a2  a3 |
    # volume(V) = abs ( vectorA * (B x C) ) = abs ( | b1  b2  b3 | )   
    #                                               | c1  c2  c3 |    
    #                                                                 						                                                         
    #   will calculate the [value] of the [determinant of the ( 3 x 3) matrix] by [Theorem of Sarru's] that is                                                               					
    #   the [volume(V)] of the [Parallelepiped] and will find also the [volume(V)  of the Tetrahedron]. 
    #   

    if number == 3:
        # Enter the [components] of the vectors
        vectorA, vectorB, vectorC = componentsVector(number)
        answer()
        print('\n\t-- The [vectorA]: vectorA',vectorA)
        print('\t-- The [vectorB]: vectorB',vectorB)
        print('\t-- The [vectorC]: vectorC', vectorC, '\n')
     
    elif number == 4:
        # Enter the [coordinates] of the points
        vectorA, vectorB, vectorC = findTwoOrThreeVectors(number)
    
    a1 = vectorA[0]
    a2 = vectorA[1]
    a3 = vectorA[2]

    b1 = vectorB[0]
    b2 = vectorB[1]
    b3 = vectorB[2]

    c1 = vectorC[0]
    c2 = vectorC[1]
    c3 = vectorC[2]
    
    p1 = vectorA[0] * vectorB[1] * vectorC[2]
    p2 = vectorA[1] * vectorB[2] * vectorC[0]
    p3 = vectorA[2] * vectorB[0] * vectorC[1]
    express1 = p1 + p2 + p3
    
    p4 = vectorA[2] * vectorB[1] * vectorC[0]
    p5 = vectorA[0] * vectorB[2] * vectorC[1]
    p6 = vectorA[1] * vectorB[0] * vectorC[2]
    express2 = p4 + p5 + p6
    
    mixedProduct = (express1 - express2)
    parallelepiped = abs(express1 - express2)

    Cx = ( ( vectorA[1] * vectorB[2] ) - ( vectorA[2] * vectorB[1] ) )
    Cy = ( ( vectorA[2] * vectorB[0] ) - ( vectorA[0] * vectorB[2] ) )
    Cz = ( ( vectorA[0] * vectorB[1] ) - ( vectorA[1] * vectorB[0] ) )
    
    NormAxB = magnitudeTriVector(Cx, Cy, Cz) 
    heightParallelep = ( parallelepiped / NormAxB )
    tetrahedron = parallelepiped / 6

    return mixedProduct, parallelepiped, heightParallelep, tetrahedron  

def angleVectors():
    varint = 2
    vectorA, vectorB, vectorAB, dotproduct = dotProduct(varint)    
    a0 = vectorA[0]
    a1 = vectorA[1]
    a2 = vectorA[2]
    valuemagVectorA = magnitudeTriVector(a0,a1,a2)
    b0 = vectorB[0]
    b1 = vectorB[1]
    b2 = vectorB[2]
    valuemagVectorB = magnitudeTriVector(b0,b1,b2)
    product = dotproduct / (valuemagVectorA * valuemagVectorB)
    angle_radians = math.acos(product)
    angleTheta_degrees = math.degrees(angle_radians)
    return valuemagVectorA, valuemagVectorB, dotproduct, angleTheta_degrees

def enterCoordPointPQ():
    # Given any two points: P and Q find the vector A
    varint = 2
    pointP, pointQ = coordinatesPoint(varint)
    
    xP=yP=zP=xQ=yQ=zQ=0
    for coord in range(0,3):
        if coord == 0:
            xP = pointP[coord]
            xQ = pointQ[coord]
        elif coord == 1:
            yP = pointP[coord]
            yQ = pointQ[coord]
        elif coord == 2:
            zP = pointP[coord]
            zQ = pointQ[coord]

    PointP = (xP,yP,zP)
    print('\n\t- The (Point P): P',PointP)
    PointQ = (xQ,yQ,zQ)
    print('\t- The (Point Q): Q',PointQ,'\n')
    return pointP, pointQ, xP, yP, zP, xQ, yQ, zQ

def findVectorA(num):
    pointP, pointQ, xP, yP, zP, xQ, yQ, zQ = enterCoordPointPQ()
    vectorPQ = []

    for f in range (0,3):
        coord = pointQ[f] - pointP[f]
        vectorPQ.append(coord)
        
    vectorA =  vectorPQ
    a1 = vectorA[0]
    a2 = vectorA[1]
    a3 = vectorA[2]
    normA = ( magnitudeTriVector(a1, a2, a3) )
    answer()
    print('\t-- The [vectorA]: vectorA=vectorPQ',vectorA)
    print('\t-- The [lenght] of the vectorA=|vectorA|: ', format((normA),'<10.2f'),'\n')
    # update
    if num == 1:
        return vectorA, normA # fix an error
    elif num == 2:
        return vectorA  

def enterCoordPointPR():
    # Given any two points: P and R find the vector B
    print('\n\t-- Enter the [coordinates]: (xP, yP) of the (point P)? ')
    pointP = pointCoord()
    print('\n\t-- Provide the [coordinates]: (xR, yR) of the (point R)? ')
    pointR = pointCoord()
    
    xP=yP=zP=xR=yR=zR=0
    for coord in range(0,2):
        if coord == 0:
            xP = pointP[coord]
            xR = pointR[coord]
        elif coord == 1:
            yP = pointP[coord]
            yR = pointR[coord]
        elif coord == 2:
            zP = pointP[coord]
            zR = pointR[coord]

    PointP = (xP,yP,zP)
    print('\n\t- The (Point P): P',PointP)
    PointR = (xR,yR,zR)
    print('\t- The (Point R): R',PointR,'\n')
    return pointP, pointR, xP, yP, zP, xR, yR, zR 

def findVectorB():
    pointP, pointR, xP, yP, zP, xR, yR, zR   = enterCoordPointPR()
    vectorPR = []

    for f in range (0,3):
        coord = pointR[f] - pointP[f]
        vectorPR.append(coord)
        
    vectorB =  vectorPR
    b1 = vectorB[0]
    b2 = vectorB[1]
    b3 = vectorB[2]
    normB = ( magnitudeTriVector(b1, b2, b3) )
    answer()
    print('\t-- The [vectorB]: vectorB=vectorPR',vectorB)
    print('\t-- The [lenght] of the vectorB=|vectorB|: ', format((normB),'<10.2f'),'\n')
    return vectorB

def formaComponent():
    print('\n\t- To enter the [Components] of the [vectors: A and B] type [1].')
    print('\t- To introduce the [Coordinates] of the [points: P, Q, and R] type [2].')
    number = vectornumber()
    
    if number == 1:
        print('\n\t- Provide the [Components] of the [vectors]: vectorA and vectorB.')
        # update
        varint = 2
        vectorA, vectorB = componentsVector(varint)
    elif number == 2:
        print('\n\t- Give the [Coordinates] of the [givens points: P and Q].')
        varint = 2 #
        vectorA = findVectorA(varint) # update
        print('\t- Enter the [Coordinates] of the [givens points: P and R].')
        vectorB = findVectorB()
          
    print('\n\t-- The [vectorA]: vectorA', vectorA)
    print('\t-- The [vectorB]: vectorB', vectorB, '\n')

    # update
    print('\t- Enter with new [value] to the (1º)[coefficient]?')
    coeffic1 = introduce()
    print('\t- Give the new [value] to the (2º)[coefficient]?')
    coeffic2 = introduce()

    vectorAcoeffic1 = []
    vectorBcoeffic2 = []

    for p in range(0,3):
        num1prod = vectorA[p] * coeffic1
        vectorAcoeffic1.append(num1prod)
        num2prod = vectorB[p] * coeffic2
        vectorBcoeffic2.append(num2prod)

    answer()
    print('\t+ The [vectorProduct]: [vectorA]*[scalar(coeffic1)]=vectorAcoeffic1',vectorAcoeffic1)
    print('\t+ The [vectorproduct]: [vectorB]*[scalar(coeffic2)]=vectorBcoeffic2',vectorBcoeffic2,'\n')
    Addition = []
    Subtraction = []
    
    for q in range(0,3):
        termA = ( vectorAcoeffic1[q] + vectorBcoeffic2[q] )
        Addition.append(termA)
        termS = ( vectorAcoeffic1[q] - vectorBcoeffic2[q] )
        Subtraction.append(termS)

    print('\t-- The [vectorAddition]=[vectorA(coeffic1)+vectorB(coeffic2)]', Addition)
    print('\t-- The [vectorSubtraction]=[vectorA(coeffic1)-vectorB(coeffic2)]', Subtraction,'\n')

    A0 = Addition[0]
    A1 = Addition[1]
    A2 = Addition[2]
    lengthA = magnitudeTriVector(A0,A1,A2)
    S0 = Subtraction[0]
    S1 = Subtraction[1]
    S2 = Subtraction[2]
    lengthS = magnitudeTriVector(S0,S1,S2)
    print('\t-- The [length] of the |vectorAddition| is:',format((lengthA),'<10.2f'))
    print('\t-- The [length] of the |vectorSubtraction| is:',format(( lengthS),'<10.2f'),'\n')
    return

def distanceTwoPoints():
    pointP, pointQ, xP, yP, zP, xQ, yQ, zQ = enterCoordPointPQ()
    vectPQ = []
    vectCQD = []
    addQD = 0

    for f in range (0,3):
        coord = pointQ[f] - pointP[f]
        vectPQ.append(coord)
        coordQD = pow(coord,2)
        vectCQD.append(coordQD)
        addQD = addQD + coordQD
        
    length = math.sqrt(addQD)
    answer()
    
    return vectPQ, vectCQD, length

def midPoint():
    pointP, pointQ, xP, yP, zP, xQ, yQ, zQ = enterCoordPointPQ()
       
    vectorMidPoint = []
    xM=yM=zM=0

    for j in range(0,3):
        coord = ( ( pointP[j] + pointQ[j] ) / 2 )
        vectorMidPoint.append(coord)
        if j == 0:
            xM = vectorMidPoint[j]
        elif j == 1:
            yM = vectorMidPoint[j]
        elif j == 2:
            zM = vectorMidPoint[j]
    PointM = (xM,yM,zM)
    answer()
    return PointM

def directionAngleSub(a1,a2,a3,lengthA):
    cosineAlpha = a1 / lengthA
    cosineBeta = a2 / lengthA
    cosineGama = a3 / lengthA

    addCos = ( pow(cosineAlpha,2) + pow(cosineBeta,2) + pow(cosineGama,2) )

    if addCos == 1.0:
        print('\t**[ (COSINEALPHA)² + (COSINEBETA)² + (COSINEGAMA)² = 1 ]**\n')

    print('\t-- The [value] of the [CosineAlpha] is: ',format((cosineAlpha),'<10.2f'))
    print('\t-- The [value] of the [CosineBeta] is: ',format((cosineBeta),'<10.2f'))
    print('\t-- The [value] of the [CosineGama] is: ',format((cosineGama),'<10.2f'),'\n')
    angle_radiansA = math.acos(cosineAlpha)
    angle_radiansB = math.acos(cosineBeta)
    angle_radiansG = math.acos(cosineGama)
    angleAlpha_degreesA = math.degrees(angle_radiansA)
    angleBeta_degreesB = math.degrees(angle_radiansB)
    angleGama_degreesG = math.degrees(angle_radiansG)
    print('\t-- The [value] of the [AlphaAngle] is: ',format((angleAlpha_degreesA),'<10.2f'))
    print('\t-- The [value] of the [BetaAngle] is: ',format((angleBeta_degreesB),'<10.2f'))
    print('\t-- The [value] of the [GamaAngle] is: ',format((angleGama_degreesG),'<10.2f'),'\n')
    return
    
def directionAngles():
    print('\t- Type [1] to enter the [components] of vectorA.')
    print('\t- Type [2] to enter the [coordinates] of two givens points: P and Q.')
    number = vectornumber()
    
    if number == 1:
        print('\n\t- Attribute the [Components] of the [1º vectorA]!')
        vectorA = compVector()
        a1 = vectorA[0]
        a2 = vectorA[1]
        a3 = vectorA[2]
        lengthA = ( magnitudeTriVector(a1, a2, a3) )
        print('\t-- The [vectorA]: vectorA',vectorA)
        print('\t-- The [lenght] of the vectorA=|vectorA|: ', format((lengthA),'<10.2f'),'\n')
        directionAngleSub(a1,a2,a3,lengthA)
    elif number == 2:
        # update
        varint = 1 
        vectorA, lengthA = findVectorA(varint) # fix an error  
        a1 = vectorA[0]
        a2 = vectorA[1]
        a3 = vectorA[2]
        directionAngleSub(a1,a2,a3,lengthA)
    else:
        print('\n\t\t--[ YOU NOT TYPED NEITHER [1] OR [2] -- OK! ]--\n') 
    return
    

    
    
    

