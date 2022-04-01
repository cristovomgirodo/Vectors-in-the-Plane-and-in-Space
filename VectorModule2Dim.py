###################################################################
#
# VetorModule2Dim.py modulo
# Developed by Cristovom A. Girodo
# Date: 20220330 -- Stable Version: 1.1
#
###################################################################

import math

def vectornumber():
    while True:
        try:
            coeffic1 = int(input("\t[º>º] What is the new value? "))
            print('\t     **[The typed number]:',coeffic1,'is a [valid integer number!]\n]')
            return coeffic1
        except ValueError as err:
            print('\t    /////')
            print('\t    @<@ [Warning!]:',err)
            print('\t    \~/ [TYPE AN [NEW INTEGER NUMBER] IN NEXT INSTRUCTION -- OK!]\n')

def introduce():
    while True:
        try:
            coeffic = float(input("\t-_- What is the new value? "))
            print('\t     **[The typed number]:',coeffic,'is a [valid float number!]\n]')
            return coeffic
        except ValueError as err:
            print('\t    /////')
            print('\t    º<º [Warning!]:',err)
            print('\t    \~/ [TYPE AN NEW INTEGER OR FLOAT NUMBER IN NEXT INSTRUCTION -- OK!]\n')

def instruction1():
    print("\n\t- Enter with the [new value] of the [angle] in degree? ")
    return

def instruction2():
    print("\t- Provide the [new value] of the [radius] of vector? ")
    return

# The function ResultantVector() is the end version: 4.0 

def ResultantVector():

    i, Rx, Ry, Vx, Vy = 1, 0, 0, 0, 0  # locals variables
    
    print('\n\t+ How much [Vectors] will necessary to get the [Resultant(R) Vector]?\n')
    numb = vectornumber()

    while i <= numb:
        if i == 1:
            print('\t**[Warning]**')
            print('\t- All the [Vectorials Components] will can be:')
            print('\t  [positive] or [negative] or Zero!\n')
		      
        def subRotine():
            instruction1()
            value_angle_degrees = introduce()
            value_angle_radians = math.radians(value_angle_degrees)
            instruction2()
            rdvect = introduce()
            return value_angle_degrees, value_angle_radians, rdvect  # locals variables

        print("\n\t+ What are the arguments: [angle] and [radius] of the(",i,")[vector]?")
        angle_degrees, angle_radians, radius = subRotine()

        while angle_degrees == 0 and radius == 0:
            print('\n\n\t //////')
            print('\t º < º [ WARNING! ]')
            print('\t \ - /\n')
            print('\t**[ No exist none [vector] when the [coefficients]:')
            print('\t**[angle_degrees = 0] and [radius = 0] -- Ok! ]**\n')
            print('\t-[ Enter with [New values] to the [coefficients]:')
            print('\t-[angle_degrees] = ? and [radius] = ? ] --\n')
            angle_degrees, angle_radians, radius = subRotine()

        Vx = radius * math.cos(angle_radians)
        Vy = radius * math.sin(angle_radians)
        
        print("\n\t\t\t_-_ . . .[Running]. . . _-_\n","\n\t* [answer] *\n")
        print("\t- The component of the ", i, "vector: Vx(",i,") = ", format(Vx,"<10.2f"))
        print("\t- The component of the ", i, "vector: Vy(",i,") = ", format(Vy,"<10.2f"), "\n")
        Rx = Vx + Rx
        Ry = Vy + Ry
        
        if i == numb:
            resultant_vector = magnitudeBiVector(Rx,Ry)
            arg = Ry / Rx
            angle_radians = math.atan(arg)
            theta_degrees = math.degrees(angle_radians)
            print("\n\t+ The sum of all the components of x_axis: Rx = ",format(Rx,"<10.2f"))
            print("\t+ The sum of all the components of y_axis: Ry = ",format(Ry,"<10.2f"))
            print("\n\n\t+ The resultant vector: [Resultant(R)_Vector] = ", format(resultant_vector,"<10.2f"))
            print("\t+ The theta angle [theta_degrees] = ", format(theta_degrees,"<10.2f"))
        
        i = i + 1

    print("\n\n\t**[End Processing of the [ RESULTANTVECTOR.PY FUNCTION ]--Ok! ]**\n")

    return

def pointCoord():
    # This function pointCoord() only will enter all the coordinates: x, y of any point.
    #
    
    point = []  # create a list named point
    
    for j in range(1, 3):
       
        if j == 1:
            print("\n\t* Introduce the %dº" %j,"[Coordinate(x)].")
            u = introduce()
            point.append(u)      
        elif j == 2:
            print("\n\t* Enter with the %dº" %j,"[Coordinate(y)].")
            v = introduce()
            point.append(v)  
            return point

def coordinatesPoint(number):
    print('\n\t-- Enter the [coordinates]: (xP, yP) of the (point P)? ')
    pointP = pointCoord()
    print('\t-- Introduce the [coordinates]: (xQ, yQ) of the (point Q)? ')
    pointQ = pointCoord()

    if number == 2:
        return pointP, pointQ
    elif number == 3:
        print('\t-- Provide the [coordinates]: (xR, yR) of the (point R)? ')
        pointR = pointCoord()
        return pointP, pointQ, pointR
    
def compVector():

    vectorComponents = []

    for h in range(1,3):
        
        if h == 1:
            print('\n\t- Enter the %dº' %h,'[Component(x)]!')
            u = introduce()
            vectorComponents.append(u)     
        elif h == 2:
            print('\n\t- Introduce the %dº' %h,'[Component(y)]!')
            v = introduce()
            vectorComponents.append(v)
            return vectorComponents
            
def componentsVector():
    print('\n\t- Attribute the [Components] of the [1º vectorA]!')
    vectA = compVector()
    print('\n\t- Provide the [Components] of the [2º vectorB]!')
    vectB = compVector()
    return vectA, vectB

def magnitudeBiVector(x,y):
    magbivector = math.sqrt(math.pow(x,2) + math.pow(y,2))
    return magbivector

def subQdRoot(hip,cat):
    height = math.sqrt( math.pow(hip,2) - math.pow(cat,2) )
    return height

def answer():
    print('\n\t*[ANSWER]*\n')
    return

def scalarProduct(number):
    # Given the Scalar Product of vectors: a and b
    
    if number == 1 or number == 2:
        # Enter teh components of the vectors: a and b
        vectorA, vectorB = componentsVector()
        
        print('\n\t-- The [vectorA]: vectorA', vectorA)
        print('\t-- The [vectorB]: vectorB', vectorB, '\n')
        
        vectorAB = []
        scalarProduct = 0
        answer()
        
        for i in range(0, 2):
            term = vectorA[i] * vectorB[i]
            scalarProduct = scalarProduct + term
            vectorAB.append(term)

        if number == 1:
            return scalarProduct, vectorAB
        
        elif number == 2:
            a1 = vectorA[0]
            a2 = vectorA[1]
            normA = ( magnitudeBiVector(a1, a2) )
            b1 = vectorB[0]
            b2 = vectorB[1]
            normB = ( magnitudeBiVector(b1, b2) )
            modAxBproduct = normA * normB
            cosineThetaRadians = scalarProduct / modAxBproduct
            return normA, normB, scalarProduct, vectorAB, cosineThetaRadians
                
    elif number == 3:
        # Given coordinates of  the points: P, Q, and R vertics of trianglePQR
        coordP, coordQ, coordR = coordinatesPoint(number)
        
        xP=xQ=xR=yP=yQ=yR = 0
        
        for cP in range(0,2):
            if cP == 0:
                xP = coordP[cP]
                xQ = coordQ[cP]
                xR = coordR[cP]
            elif cP == 1:
                yP = coordP[cP]
                yQ = coordQ[cP]
                yR = coordR[cP]
                    
        PointP = (xP,yP)
        print('\n\t- The (Point P): P',PointP)
        PointQ = (xQ,yQ)
        print('\t- The (Point Q): Q',PointQ)
        PointR = (xR,yR)
        print('\t- The (Point R): R',PointR)
        answer()

        vectorQR = []
        vectorRP = []
        vectorPQ = []
        
        for h in range (0,2):
            comp0 = coordR[h] - coordQ[h]
            vectorQR.append(comp0)
            comp1 = coordP[h] - coordR[h]
            vectorRP.append(comp1)
            comp3 = coordQ[h] - coordP[h]
            vectorPQ.append(comp3)

        vectorA = vectorQR
        vectorB = vectorRP
        vectorC = vectorPQ
        
        # The Area = ( |b1*c2 -b2*c1| ) / 2
        b1 = vectorB[0]
        b2 = vectorB[1]
        c1 = vectorC[0]
        c2 = vectorC[1]
        term0 = vectorB[0] * vectorC[1]
        term1 = vectorB[1] * vectorC[0]
        add = term0 - term1
        Area = ( abs(add) ) / 2

        compX = vectorQR[0]
        compY = vectorQR[1]
        # sideA = modQR
        sideA = magnitudeBiVector(compX, compY)
        compX = vectorRP[0]
        compY = vectorRP[1]
        # sideB = modRP
        sideB = magnitudeBiVector(compX, compY)
        compX = vectorPQ[0]
        compY = vectorPQ[1]
        # sideC = modPQ
        sideC = magnitudeBiVector(compX, compY)

        Perimeter = sideA + sideB + sideC
        
        # vectorCxA = vectorPQºQR
        # vectorAxB = vectorQRºRP
        # vectorBxC = vectorRPºPQ
        
        vectorPQºQR = []
        vectorQRºRP = []
        vectorRPºPQ = []

        ScalarProd0 = 0
        ScalarProd1 = 0
        ScalarProd2 = 0
        
       # Find the Scalars Procucts
        for j in range(0, 2):
            term0 = vectorPQ[j] * vectorQR[j]
            ScalarProd0 = ScalarProd0 + term0
            vectorPQºQR.append(term0)
            term1 = vectorQR[j] * vectorRP[j]
            ScalarProd1 = ScalarProd1 + term1
            vectorQRºRP.append(term1)
            term2 = vectorRP[j] * vectorPQ[j]
            ScalarProd2 = ScalarProd2 + term2
            vectorRPºPQ.append(term2)
          
        # Find the component of c along a
        cat1 = ( ScalarProd0 / sideA )
        hip1 = sideC
        h1 = subQdRoot(hip1, cat1)
        # Find the component of a along b
        cat2 = ( ScalarProd1 / sideB )
        hip2 = sideA
        h2 = subQdRoot(hip2, cat2)
        # Find the component of b along c
        cat3 = ( ScalarProd2 / sideC )
        hip3 = sideB
        h3 = subQdRoot(hip3, cat3)

        print('\t-- The [vectorA] = vectorQR', vectorQR)
        print('\t-- The [vectorB] = vectorRP', vectorRP)
        print('\t-- The [vectorC] = vectorPQ', vectorPQ,'\n')
        print('\t-- The [sideA of the triangle(PQR)] is:',format(sideA,"<10.2f"))
        print('\t-- The [sideB of the triangle(PQR)] is:',format(sideB,"<10.2f"))
        print('\t-- The [sideC of the triangle(PQR)] is:',format(sideC,"<10.2f"),'\n')
        print('\t-- The [terms] of the [Scalar Product(PQºQR)] is:',vectorPQºQR)
        print('\t-- The [terms] of the [Scalar Product(QRºRP)] is:',vectorQRºRP)
        print('\t-- The [terms] of the [Scalar Product(RPºPQ)] is:',vectorRPºPQ,'\n')
        print('\t-- The [Scalar Product(PQºQR)] is:',format(ScalarProd0,"<10.2f"))
        print('\t-- The [Scalar Product(QRºRP)] is:',format(ScalarProd1,"<10.2f"))
        print('\t-- The [Scalar Product(RPºPQ)] is:',format(ScalarProd2,"<10.2f"),'\n')
        print('\t-- The [Perimeter] of the [triangle(PQR)] is',format(Perimeter,"<10.2f"))
        print('\t-- The [Height(h1) relative as sideQR] is',format( h1,"<10.2f"))
        print('\t-- The [Height(h2) relative as sideRP] is',format( h2,"<10.2f"))
        print('\t-- The [Height(h3) relative as sidePQ] is',format( h3,"<10.2f"))
        print('\t-- The [Area(A)] of the [triangle(PQR)] is',format(Area,"<10.2f"),'\n')

    elif number == 4:
        # Given the coordinates of the points: P, Q, R, and S. The vertices of the parallelogramPQRS
        varint = 3
        coordP, coordQ, coordR = coordinatesPoint(varint)
        print('\t-- Provide the [coordinates]: (xS, yS) of the (point S)? ')
        coordS = pointCoord()
        
        xP=xQ=xR=xS=yP=yQ= yR=yS = 0
        
        for cP in range(0,2):
            if cP == 0:
                xP = coordP[cP]
                xQ = coordQ[cP]
                xR = coordR[cP]
                xS = coordS[cP]
            elif cP == 1:
                yP = coordP[cP]
                yQ = coordQ[cP]
                yR = coordR[cP]
                yS = coordS[cP]
                    
        PointP = (xP,yP)
        print('\n\t- The (Point P): P',PointP)
        PointQ = (xQ,yQ)
        print('\t- The (Point Q): Q',PointQ)
        PointR = (xR,yR)
        print('\t- The (Point R): R',PointR)
        PointS = (xS,yS)
        print('\t- The (Point S): S',PointS)
        answer()
        
        vectorPQ = []
        vectorPS = []
        
        for k in range (0,2):
            comp0 = coordQ[k] - coordP[k]
            vectorPQ.append(comp0)
            comp1 = coordS[k] - coordP[k]
            vectorPS.append(comp1)

        compX = vectorPQ[0]
        compY = vectorPQ[1]
        # sideA = modPQ
        sideA = magnitudeBiVector(compX, compY)
        compX = vectorPS[0]
        compY = vectorPS[1]
        # sideB = modPS
        sideB = magnitudeBiVector(compX, compY)
        Perimeter = ( sideA +sideB ) * 2

        vectorPSºPQ = []
        ScalarProd0 = 0
        
        for j in range(0, 2):
            term0 =  vectorPS[j] * vectorPQ[j] 
            ScalarProd0 = ScalarProd0 + term0
            vectorPSºPQ.append(term0)

        # Find the component of b along a
        cat0 = (  ScalarProd0 / sideA )
        hip0 = sideB
        height_h = subQdRoot(hip0, cat0)

        EquatArea = ( (vectorPQ[0] * vectorPS[1]) - (vectorPQ[1] * vectorPS[0]) )

        print('\n\t-- The [vectorPQ]:vectorPQ',vectorPQ)
        print('\t-- The [vectorPS]:vectorPS',vectorPS,'\n')
        print('\t-- The [sideA] relative as [vector|PQ|]:',format(sideA,"<10.2f"))
        print('\t-- The [sideB] relative as [vector|PS|]:',format(sideB,"<10.2f"))
        print('\t-- The [Perimeter(P)] is:',format(Perimeter,"<10.2f"),'\n')
        print('\t-- The [terms] of the Scalar Product(vectorPSºPQ)] is:',vectorPSºPQ)
        print('\t-- The [Scalar Product(PQºPS)] is:',ScalarProd0)
        print('\t-- The [Height(h)] relative as [sideA]=|vectorPQ| is:', format(height_h,"<10.2f"))
        print('\t-- The [Area(S)] of the [Parallelogram(PQRS)]:',format(abs(EquatArea),"<10.2f"),'\n')

    return

def angleVectors():
    varint = 2
    modvectorA, modvectorB, Scalarproduct, vectorAxB, cosineRadians = scalarProduct(varint)
    angle_radians = math.acos(cosineRadians)
    angleTheta_degrees = math.degrees(angle_radians)
    return modvectorA, modvectorB, Scalarproduct, vectorAxB, angleTheta_degrees

def cosineTheta():
    varint = 2
    modvectorA, modvectorB, Scalarproduct, vectorAxB, cosineRadians = scalarProduct(varint)
    return modvectorA, modvectorB, Scalarproduct, vectorAxB, cosineRadians

def innerAngleTriangle():
    varint = 3
    pointP, pointQ, pointR = coordinatesPoint(varint)
    pointA, pointB, pointC = pointP, pointQ, pointR

    xP=xQ=xR=yP=yQ=yR = 0
    for coord in range(0,2):
        if coord == 0:
            xP = pointP[coord]
            xQ = pointQ[coord]
            xR = pointR[coord] 
        elif coord == 1:
            yP = pointP[coord]
            yQ = pointQ[coord]
            yR = pointR[coord]  
                
    PointP = (xP,yP)
    print('\n\t- The (Point P): P',PointP)
    PointQ = (xQ,yQ)
    print('\t- The (Point Q): Q',PointQ)
    PointR = (xR,yR)
    print('\t- The (Point R): R',PointR)
    answer()
    
    for op in range (0,3):
        # Will find the scalar product: b * c
        if op == 0:
            vectorAC = []
            vectorAB = []
            
            for p in range (0,2):
                compAC = ( pointC[p] - pointA[p] )
                vectorAC.append(compAC)
                compAB = ( pointB[p] - pointA[p] )
                vectorAB.append(compAB)
                
            vectorB = vectorAC
            vectorC = vectorAB
            
            print('\t- The [vectorB]=vectorPR',vectorB)
            print('\t- The [vectorC]=vectorPQ',vectorC,'\n')

            scalarProductBC = 0
            vectorBC = []
            
            for d0 in range (0,2):
                term0 = vectorAC[d0] * vectorAB[d0]
                scalarProductBC = scalarProductBC + term0
                vectorBC.append(term0)

            b1 = vectorB[0]
            b2 = vectorB[1]
            normB = ( magnitudeBiVector(b1, b2) )
            c1 = vectorC[0]
            c2 = vectorC[1]
            normC = ( magnitudeBiVector(c1, c2) )
            normBxCproduct = ( normB * normC )
            CossineA = ( scalarProductBC / normBxCproduct )
            angle_radians = math.acos(CossineA)
            AngleAlpha_degrees = math.degrees(angle_radians)
            print('\t- The Scalar Product: [b * c] is:',format((scalarProductBC),'<10.2f'))
            print('\t- The value of the [ANGLE ALPHA] was calculate is:', format((AngleAlpha_degrees),'<10.2f'),'\n')

        elif op == 1:
            # Will find the scalar product: a * c
            vectorBC = []
            vectorBA = []

            for q in range (0,2):
                compBC = ( pointC[q] - pointB[q] )
                vectorBC.append(compBC)
                compBA = ( pointA[q] - pointB[q] )
                vectorBA.append(compBA)

            vectorA = vectorBC
            vectorC = vectorBA
            
            print('\t- The [vectorA]=vectorQR',vectorA)
            print('\t- The [vectorC]=vectorQP',vectorC,'\n')

            scalarProductAC = 0
            vectorAC = []

            for d1 in range (0,2):
                term1 = vectorBC[d1] * vectorBA[d1]
                scalarProductAC = scalarProductAC + term1
                vectorAC.append(term1)

            a1 = vectorA[0]
            a2 = vectorA[1]
            normA = ( magnitudeBiVector(a1, a2) )
            c1 = vectorC[0]
            c2 = vectorC[1]
            normC = ( magnitudeBiVector(c1, c2) )
            normAxCproduct = ( normA * normC )
            CossineB = ( scalarProductAC / normAxCproduct )
            angle_radians = math.acos(CossineB)
            AngleBeta_degrees = math.degrees(angle_radians)
            print('\t- The Scalar Product: [a * c] is:',format((scalarProductAC),'<10.2f'))
            print('\t- The value of the [ANGLE BETA] was calculate is:', format((AngleBeta_degrees),'<10.2f'),'\n')

        elif op == 2:
            # Will find the scalar product: a * b
            vectorCB = []
            vectorCA = []

            for r in range (0,2):
                compCB = ( pointB[r] - pointC[r] )
                vectorCB.append(compCB)
                compCA = ( pointA[r] - pointC[r] )
                vectorCA.append(compCA)

            vectorA = vectorCB
            vectorB = vectorCA
            
            print('\t- The [vectorA]=vectorRQ',vectorA)
            print('\t- The [vectorB]=vectorRP',vectorB,'\n')

            scalarProductAB = 0
            vectorAB = []

            for d2 in range (0,2):
                term2 = vectorCB[d2] * vectorCA[d2]
                scalarProductAB = scalarProductAB + term2
                vectorAB.append(term2)

            a1 = vectorA[0]
            a2 = vectorA[1]
            normA = ( magnitudeBiVector(a1, a2) )
            b1 = vectorB[0]
            b2 = vectorB[1]
            normB = ( magnitudeBiVector(b1, b2) )
            normAxBproduct = ( normA * normB )
            CossineC = ( scalarProductAB / normAxBproduct )
            angle_radians = math.acos(CossineC)
            AngleGama_degrees = math.degrees(angle_radians)
            
            print('\t- The Scalar Product: [a * b] is:',format((scalarProductAB),'<10.2f'))
            print('\t- The value of the [ANGLE GAMA] was calculate is:', format((AngleGama_degrees),'<10.2f'),'\n')

            if AngleAlpha_degrees == AngleBeta_degrees and AngleAlpha_degrees == AngleGama_degrees and AngleBeta_degrees == AngleGama_degrees:
                print('\n\t\t-- The triangle is [Equilateral]!','\n')
            elif AngleAlpha_degrees == AngleBeta_degrees or AngleAlpha_degrees == AngleGama_degrees or AngleBeta_degrees == AngleGama_degrees:
                print('\n\t\t-- The triangle is [Isosceles]!','\n')
            elif AngleAlpha_degrees != AngleBeta_degrees and AngleAlpha_degrees != AngleGama_degrees and AngleBeta_degrees != AngleGama_degrees:
                print('\n\t\t-- The triangle is [Scalene]!','\n')

            addInnerAngle = AngleAlpha_degrees + AngleBeta_degrees + AngleGama_degrees

            print('\t- THE [ADD] OF THE [INNER ANGLES] OF THE [TRIANGLE-PQR] is:',format((addInnerAngle),'<10.2f'),'\n')
            print('\n\t\t--[END CALCULUS-OK!]--\n')
            
    return

def addSubtraction():
    vectorA, vectorB = componentsVector()
    print('\n\t-- The [vectorA]: vectorA', vectorA)
    print('\t-- The [vectorB]: vectorB', vectorB, '\n')
    addition = []
    subtraction = []
    answer()

    for j in range(0,2):
        add = ( vectorA[j] + vectorB[j] )
        addition.append(add)
        subt = ( vectorA[j] - vectorB[j] )
        subtraction.append(subt)
        
    return addition, subtraction

def enterCoordPointPQ():
    # Given any two points: P and Q find the vector A
    varint = 2
    pointP, pointQ = coordinatesPoint(varint)
    
    xP=yP=xQ=yQ=0
    for coord in range(0,2):
        if coord == 0:
            xP = pointP[coord]
            xQ = pointQ[coord]
        elif coord == 1:
            yP = pointP[coord]
            yQ = pointQ[coord]

    PointP = (xP,yP)
    print('\n\t- The (Point P): P',PointP)
    PointQ = (xQ,yQ)
    print('\t- The (Point Q): Q',PointQ,'\n')
    return pointP, pointQ, xP, yP, xQ, yQ

def findVectorA():
    pointP, pointQ, xP, yP, xQ, yQ = enterCoordPointPQ()
    vectorPQ = []

    for f in range (0,2):
        coord = pointQ[f] - pointP[f]
        vectorPQ.append(coord)
        
    vectorA =  vectorPQ
    a1 = vectorA[0]
    a2 = vectorA[1]
    normA = ( magnitudeBiVector(a1, a2) )
    answer()
    print('\t-- The [vectorA]: vectorA=vectorPQ',vectorA)
    print('\t-- The [lenght] of the vectorA=|vectorA|: ', format((normA),'<10.2f'),'\n')
    return vectorA

def enterCoordPointPR():
    # Given any two points: P and R find the vector B
    print('\n\t-- Enter the [coordinates]: (xP, yP) of the (point P)? ')
    pointP = pointCoord()
    print('\n\t-- Provide the [coordinates]: (xR, yR) of the (point R)? ')
    pointR = pointCoord()
    
    xP=yP=xR=yR=0
    for coord in range(0,2):
        if coord == 0:
            xP = pointP[coord]
            xR = pointR[coord]
        elif coord == 1:
            yP = pointP[coord]
            yR = pointR[coord]

    PointP = (xP,yP)
    print('\n\t- The (Point P): P',PointP)
    PointR = (xR,yR)
    print('\t- The (Point R): R',PointR,'\n')
    return pointP, pointR, xP, yP, xR, yR 

def findVectorB():
    pointP, pointR, xP, yP, xR, yR  = enterCoordPointPR()
    vectorPR = []

    for f in range (0,2):
        coord = pointR[f] - pointP[f]
        vectorPR.append(coord)
        
    vectorB =  vectorPR
    b1 = vectorB[0]
    b2 = vectorB[1]
    normB = ( magnitudeBiVector(b1, b2) )
    answer()
    print('\t-- The [vectorB]: vectorB=vectorPR',vectorB)
    print('\t-- The [lenght] of the vectorB=|vectorB|: ', format((normB),'<10.2f'),'\n')
    return vectorB
   
def distanceTwoPoints():
    # Will calculate the distance(D) between the points: P and Q
    pointP, pointQ, xP, yP, xQ, yQ = enterCoordPointPQ()
    vectPQ = []
    vectCQD = []
    addQD = 0

    for f in range (0,2):
        coord = pointQ[f] - pointP[f]
        vectPQ.append(coord)
        coordQD = pow(coord,2)
        vectCQD.append(coordQD)
        addQD = addQD + coordQD
        
    length = math.sqrt(addQD)
    answer()
    
    return vectPQ, vectCQD, length

def midPoint():
    # Will find the midpoint M(xM,yM) between the points: P and Q
    varint = 2
    pointP, pointQ, xP, yP, xQ, yQ = enterCoordPointPQ()
    
    vectorMidPoint = []
    xM=yM=0

    for j in range(0,2):
        coord = ( ( pointP[j] + pointQ[j] ) / 2 )
        vectorMidPoint.append(coord)
        if j == 0:
            xM = vectorMidPoint[j]
        elif j == 1:
            yM = vectorMidPoint[j]
        
    PointM = (xM,yM)
    answer()

    return PointM

def formaComponent():
    print('\n\t- To enter the [Components] of the [vectors] type [1].')
    print('\t- To introduce the [Coordinates] of the [points] type [2].')
    number = vectornumber()
    if number == 1:
        print('\n\t- Provide the [Components] of the [vectors]: vectorA and vectorB.')
        vectorA, vectorB = componentsVector()
    elif number == 2:
        print('\n\t- Give the [Coordinates] of the [givens points: P and Q].')
        vectorA = findVectorA()
        print('\t- Enter the [Coordinates] of the [givens points: P and R].')
        vectorB = findVectorB()
          
    print('\n\t-- The [vectorA]: vectorA', vectorA)
    print('\t-- The [vectorB]: vectorB', vectorB, '\n')

    print('\t- Enter with new [value] to the (1º)[coefficient]?')
    coeffic1 = introduce()
    print('\t- Give the new [value] to the (2º)[coefficient]?')
    coeffic2 = introduce()

    vectorAcoeffic1 = []
    vectorBcoeffic2 = []

    for p in range(0,2):
        num1prod = vectorA[p] * coeffic1
        vectorAcoeffic1.append(num1prod)
        num2prod = vectorB[p] * coeffic2
        vectorBcoeffic2.append(num2prod)

    answer()
    print(' + The [product]: [vectorA]*[scalar(coeffic1)]=vectorAcoeffic1',vectorAcoeffic1)
    print(' + The [product]: [vectorB]*[scalar(coeffic2)]=vectorBcoeffic2',vectorBcoeffic2,'\n')
    Addition = []
    Subtraction = []
    for q in range(0,2):
        termA = ( vectorAcoeffic1[q] + vectorBcoeffic2[q] )
        Addition.append(termA)
        termS = ( vectorAcoeffic1[q] - vectorBcoeffic2[q] )
        Subtraction.append(termS)

    print(' -- The [Addition]=[vectorA(coeffic1)+vectorB(coeffic2)]', Addition)
    print(' -- The [Subtraction]=[vectorA(coeffic1)-vectorB(coeffic2)]', Subtraction,'\n')

    A0 = Addition[0]
    A1 = Addition[1]
    lengthA = magnitudeBiVector(A0,A1)
    S0 = Subtraction[0]
    S1 = Subtraction[1]
    lengthS = magnitudeBiVector(S0,S1)
    print(' -- The [length] of the |vectorAddition| is:',format((lengthA),'<10.2f'))
    print(' -- The [length] of the |vectorSubtraction| is:',format(( lengthS),'<10.2f'),'\n')
    return


