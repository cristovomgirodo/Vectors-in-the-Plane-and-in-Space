- 👋 Hi, I’m @cristovomgirodo
- 👀 I’m interested in Python programming...
- .. I'm beginner Python programmer that was learn the programm with goods books of Python3 programming...
- 🌱 I’m currently develop, test and use small or medium size Python program for learning...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
cristovomgirodo/cristovomgirodo is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
# Introduction

## Hello the all of the GitHub

The contents of this **Readme.md** is to present all instructions of the use  correct of the **runtoolsvectors.py and runvectors2dim.py programs**. Before of use the programs the user will duty have installed *the python3 interpreter*. 
**[Warning-1]**. No use the version: 2 of the python interpreter.

Below do a **small description theoretical** of the **symbols** used in representation of the vectors. In the main point of the mathematics as *Calculus* and *Linear Algebra* as too in *Analytic Geometry* the Vectors have  symbols to will be representeds. 

Some authors of Calculus do the analytic definition of vectors using **coordinates (x,y) for any point P in plane** to associate a unique **ordered pair <x,y>** to the **vector v = vectorOP** ( whose initial point is the origin O ) and the **coordinates (x,y,z) for any point Q in space** to associate a unique **ordered triple<x,y,z>** to the **vector w = vectorOQ**.

It is important to note that **the vectors <x,y>  and <x,y,z>** are **ordered pairs and triples of reals numbers**, are not **points (x,y) and (x,y,z) in the plane and space**. For the **vectors v = <x,y> and vector w = <x,y,z>**, the **numbers x and y** are the **components of the vector v** and  the **numbers x, y and z** are the **components of the vector w**.

### In the Linear Algebra a list of values 
```
v = (v1,v2,v3) is called a linear array or vector
```
### Any triples of points: P(p1,p2,p3) and Q(q1,q2,q3) in |R³ define the located vector from P to Q, written as vector PQ. 

### Vector PQ = Q – P = [ q1 – p1, q2 – p2, q3 - p3]

Neither always the developers of programming language use the same symbols as is represented in  mathematics when create new programming languages. The *reader* more interested in subject will can acess the best books of **Calculus, Linear Algebra, and Analytic Geometry of the higher education**. 

In Python programming language , **an list data structure** are represented to **a pair square bracket [ ]**.and **an tuple data structure** are represented to **a pair square parentheses ( )**. Python program may use a *list or tuple data structure* to represent a vector. Was use the tuple data structure only to represent the coordinates of the vertexes points: P, Q, and R of triangles and too the coordinates of the vertexes points: P, Q, R and S of parallelogram, parallelepiped and tetrahedron into code of the functions into modules. 

### The main point of the mathematics developed into the functions of the VectorModDev.py and VectorModule2Dim.py modules was use *definitions* and *theorems* that are:

#### 1. Operations (Addition and Subtraction) on Vectors in Plane and in Space.
#### 2. Given two points: P and Q in Plane and Space get to theorem the vector that represent the displacement, distance, midpoint between two points.
#### 3. Find the length of any vector
#### 4. The scalar product of two vectors in Plane and in Space.
#### 5. Calculate the Cosine as too the angle between two vectors using the scalar product
#### 6. Find the following dimensions: sideA=|vectorA|, sideB=|vectorB|, sideC=|vectorC|, Perimeter(P), and Area(A) of a triangle PQR given the points: P, Q, and R in Plane.
#### 7. The Cross Product of two vectors in Space.
#### 8. Get the height(h) and area(S) of an parallelogram PQRS given the two vectors.
#### 9. Find the volume(V) and the height(h) of the parallelepiped determined by vectors: a, b, and c using the triple scalar product.
#### 10. Calculate the area(A) of the triangle PQR given the points: P, Q, and R in Space.
#### 11. Find sinθ where θ is the angle between the vectors b and c.
#### 12. Givens the coordinates of two points:  P and Q in Plane or Space, find the vector a=vectorPQ and too your length.
#### 13. Determine the [Direction Cosines] and [Direction Angles] givens the Vector a or two points: P and Q in Space. 

#### When developed the VectorModDev.py and VectorModule2Dim.py modules, almost all the functions developed was use the Vectorial Algebra in a list data structure to reduce the size of the functions. As the Python lists are well powerful the runvectors2dim.py and runtoolsvectors.py programs  will process any calculus using the inner functions of the previous modules. *The functions: vectornumber(), introduce(), instruction1(), instruction2() and ResultantVector()* are the only that *was not use* in the *list data structure*.
 
The **runtoolsvectors.py and runvectors2dim.py programs** was developed to the programmers as also to teachers and  students of the higher education to  find speed answer when will solve the vectors problems. In **codes** of the **VectorModDev.py and VectorModule2Dim.py modules**, was do represent the **vertexes points: P, Q, R and S** and the **vectors: A, B, and C** of the following manner:

### Point P, Q, R, and S in the Plane: 

### Point P: P(xP,yP)
### Point Q: Q(xQ,yQ)
### Point R: R(xR,yR)
### Point S: S(xS,yS)

### Point P, Q, R, and S in the Space: 

### Point P: P(xP,yP,zP)
### Point Q: Q(xQ,yQ,zQ)
### Point R: R(xR,yR,zR)
### Point S: S(xS,yS,zS)

### To any values attribute to the [Coordinates]: xP, yP, zP, xQ, yQ, zQ, xR, yR, zR, xS, yS, zS by users.

### The vectors: A, B, and C in the Plane:

### [vectorA]: vectorA[xA,yA]
### [vectorB]: vectorB[xB,yB]
### [vectorC]: vectorC[xC,yC]

### The vectors: A, B, and C in the Space:

### [vectorA]: vectorA[xA,yA,zA]
### [vectorB]: vectorB[xB,yB,zB]
### [vectorC]: vectorC[xC,yC,zC]

### To any values attribute to the [Components]: xA, yA, zA, xB, yB, zB, xC, yC, zC by users.


**[Warning-2]** – Was standardize **the letters: A, B, and C to the vectors** and **P, Q, R, and S to points of the vertexes of triangles, parallelogram and parallelepiped into the code of the functions** of the  **VectorModDev.py and VectorModule2Dim.py modules**. 

All the development of the **functions** inside of the **VectorModDev.py and VectorModule2Dim.py modules** are isolate because of the use of **Vectors in the Plane and Space**. The *files:* **instruction1User.pdf and instruction2User.pdf** have all the **instructions** necessary of as use the **runvectors2dim.py and runtoolsvectors.py program** with *examples*. Are *examples selected and eases of use*. The **runtoolsvectors.py and runvectors2dim.py programs** too have **inner instructions** showed when are be used. *All the users* too will duty follow this instructions showed into as display. All *theory* with the **definitions and theorems of vectors** was be used in development of the **functions** inside of the **VectorModDev.py and VectorModule2Dim.py modules**.

#### The ResultantVector() function will find the Resultant(|R) Vector by means of the Decomposion Components. Any user that enter 2 or 3 or 4 or . . . or any number the vectors in polar form will get the Resultant(|R) Vector of propose problem. The ResultantVector() function was created to solve mechanics problems using vectors to the beginner students of the higher education  of  physics, mathematics, chemistry as too engineering. Was have origin when was buy and learned programm the powerful HP 32 SII RPN SCIENTIFIC Calculator. My repository have an *free copy* of the ATVUDE program to all know as too use. The ResultantVector() function is well more powerful than the ATVUDE program. The ResultantVector() function reside only in the VectorModule2Dim.py module. To use this function key [10] after run the runvectors2dim.py program.

**[Warning-3]** – Use the **runvectors2dim.py program** with the **functions** developed into the  **VectorModule2Dim.py module** to **solve problems in Plane** of the same manner with the **runtoolsvectors.py program** using the **functions** developed into the **VectorModDev.py module** to **solve problems in Space**.

When the **runtoolsvectors.py and runvectors2dim.py programs** process the solutions requested, *all the results will showed by reals numbers*. **No result will presented in root or as fraction**. *All the roots or fractions are processed before of the end result*.  

The **runtoolsvectors.py and runvectors2dim.py programs** *will not present no geometric design* of the *Vectors operations*. The full theory about Vectors will can be finded in the best new and old books of calculus. With the **runtoolsvectors.py and runvectors2dim.py programs** will help all the *developers(or programmers), teachers, students higher graduation* as too *any person of any field* the find the speed solution. 

#### Developed the runtoolsvectors.py and runvectors2dim.py programs to solve vectors problems that study. Before of the use, all the users will duty follow all the instructions of the files instruction1User.pdf and  instruction2User.pdf. Now be present the all to know as too do the download to use free. I’m be the only developer( or programmer ) of the VectorModDev.py and VectorModule2Dim.py modules and of the runtoolsvectors.py and runvectors2dim.py programs.

#### [Warning-4]:
The files: AlgorithmATVUDE.pdf, instructions1User.pdf, runvectors2dim.py, VectorModule2Dim.py, instructions2User.pdf, runtoolsvectors.py, and VectorModDev.py already was copy of the Vectors2Dim and Vectors3Dim directories in my computer to the my repository in the GitHub. I'm sorry the all.

#### [Warning-5]:
The files: instruction1User.pdf and instruction2User.pdf was do update with rename as: instruction1UserUpdate.pdf and instruction2UserUpdate.pdf.

#### [Warning-6]:
Before of present the [new version: 1.2] of the files: **instructions1-v1.2_User.pdf**, **instructions2-v1.2_User.pdf**, **runtoolsvectors.py**, **runvectors2dim.py**, **VectorModDev.py**, and **VectorModule2Dim.py** will be necessary *delete* the followings files: instructions1User.pdf, instructions2User.pdf, instructions1UserUpdate.pdf, instructions2UserUpdate.pdf because of *errors*. All the **contents** was *fixed and put into as
**new** files*: **instructions1-v1.2_User.pdf** and **instructions2-v1.2_User.pdf**. After will put *the news tutorials files*: instructions1-v1.2_User.pdf
and instructions2-v1.2_User.pdf into as repository. Too will be necessary *delete* the files: runtoolsvectors.py, runvectors2dim.py, VectorModDev.py, and VectorModule2Dim.py because of change into as codes.  

Welcome the all users of the GitHub to use the **new version: 1.2** of the new files: **instructions1-v1.2_User.pdf**, **instructions2-v1.2_User.pdf**, **runtoolsvectors.py**, **runvectors2dim.py**, **VectorModDev.py**, and **VectorModule2Dim.py**

#### [Warning-7]: 
The files: **instructions1-v1.2_User.pdf** and **instructions2-v1.2_User.pdf** was update because of *small errors*.

#### [Warning-8]:
Before of present the new [version: 1.3] of the files: **instructions1-v1.3_User.pdf**,  and **VectorModule2Dim.py** will be necessary *delete* the followings files: **instructions1.2_User.pdf**, **AlgorithmATVUDE.pdf**, **runvectors2dim.py**, and **VectorModule2Dim.py** because of upgrade of the [code] in the files: **runvectors2dim.py**, and **VectorModule2Dim.py**. The file: **AlgorithmATVUDE.pdf** was set to a only page. The name file: **UpdateVersion1.1.md** was renamed as **Changelog.md** to standard all the upgrade. After will put *the news files*: **AlgorithmATVUDE.pdf**, **Changelog.md**, **instructions1-v1.3_User.pdf**, **runvectors2dim.py** and **VectorModule2Dim.py** inside as repository.

#### [Note]:

The **instructions2-v1.2_User.pdf** file, **runtoolsvectors.py** program as too the **VectorModDev.py** module *was not upgrades* still.

Welcome the all users of the *GitHub* to use the new **[version: 1.3]** of the files: **AlgorithmATVUDE.pdf**, **Changelog.md**, **instructions1-v1.3_User.pdf**, **runvectors2dim.py**, and **VectorModule2Dim.py**

#### [Warning-9]:
Now present the new [version: 1.3] that will update the files: **README.md**, **Changelog.md**, **instructions2-v1.2_User.pdf** file, **runtoolsvectors.py** program as too the **VectorModDev.py** module. The new update files will **instructions2-v1.3_User.pdf**, **runtoolsvectors.py** program as too the **VectorModDev.py** module. The only *file renamed* was be **instructions2-v1.3_User.pdf**. The **Changelog.md** file have informations of all the changes in code of this update files. The *repository* now will have the **runvectors2dim.py** and **runtoolsvectors.py** *programs*, **VectorModDev.py** and **VectorModule2Dim.py** *module* as too the **instructions1-v1.3_User.pdf** and **instructions2-v1.3_User.pdf** *tutorials* in the same *version: 1.3*.

#### [Warning-10]: 
Because of the incomplete code in the **VectorModule2Dim.py** module this generate error result then was necessary refactor the new lines: 414-433 inside of **VectorModule2Dim.py** module file. The **instructions1-v1.3_User.pdf** file too was repair to use of all users. The **runvectors2dim.py** file is Ok!

#### [New Version: 2.0]:
Welcome the all in GitHub to know the release of the new [version: 2.0] of the **Vectors2DClassModule.py module**, **runVector2d.py program** and the **instructions1-v2.0_User.pdf** files. Inform that will not more possible *update* the old files: *runvectors2dim.py*, and *VectorModule2Dim.py* as in [version: 1.3] because of have been *refactoring* with the *new* **paradigm of the Python object-oriented programming** using only **the class sintax**. The *new files* will not have the same name. The *new code is not the same* because of **class definitions created have new atributes**. Created the following *new files*: **Vectors2DClassModule.py module**, **runVector2d.py program** and the **instructions1-v2.0_User.pdf** file in replacement to the previous files.

### The main point of the mathematics developed into *code* of the classes in Vectors2DClassModule.py module was use *definitions* and *theorems* that are:

####  1. Find the [Scalar Product: [a * b] between [two vectors].
####  2. Calculate the [Perimeter(P)], [Heights(h), and [Area(A)] of the TrianglePQR: Givens the [coordinates] of the [points: P(xP,yP), Q(xQ,yQ), and R(xR,yR)].
####  3. The [Area(S)] and [Heights: h1 and h2] of the [Parallelogram(PQRS)] with the [coordinates] of the [points: P(xP,yP), Q(xQ,yQ), R(xR,yR), and S(xS,yS)].
####  4. Find the [angle] between [two vectors] in |R² Plane. 
####  5. Calculate the [value] of the [CossineTheta] between the [two vectors]: A and B.
####  6. Find the three sides and [Inner Angles: ALPHA, BETA, and GAMA] of the [Triangle(PQR)] with the [coordinates] of the [points: P(xP,yP), Q(xQ,yQ), and R(xR,yR)]. 
####  7. Determine the following [Middle Points]: K(xK,yK), L(xL,yL), M(xM,yM)] and N(xN,yN)] between [ points: P(xP,yP), Q(xQ,yQ), R(xR,yR), and S(xS,yS) ] or in the sides: PQ,   ####     PR, and QR          of a Triangle(PQR).
####  8. Get the [Addition and Subtraction] of [Two Vectors: A and B].
####  9. Calculate the [Resultant(|R) Vector].
#### 10. Find the [VectorA and lenght|A|] with the [coordinates] of the [points: P(xP,yP), and Q(xQ,yQ)]
####     Get the [VectorB and lenght|B|] with the [coordinates] of the [points: P(xP,yP), and R(xR,yR)]
####     Find the [VectorC and lenght|C|] with the [coordinates] of the [points: Q(xQ,yQ), and R(xR,yR)]
#### 11. Get the [Addition] and [Subraction] between [Two Vectors: A and B] Multiplyed by scalars: [coeffic1 and coeffic2].
#### 12. Determine the [Medianas: PM, QL, and RK] of the triangle(PQR).
#### 13. Find the [Centroid: G(xG, yG)] of the triangle(PQR).
#### 14. Calculate the [ Vertices: P(xP.yP), Q(xQ,yQ), and R(xR,yR) ] of the triangle(PQR) with the [Coordinates] given of the [ Middle points: K(xK,yK), L(xL,yL), and M(xM,yM) ]. 
#### 15. Get the [Coordinates] of any a of the [ Points: D(xD,yD) or E(xE,yE), or F(xF,yF) ] that are meeted with the [bisectrixs: PD or QE or RF] in the sides: QR or PR or PQ of  
####     a Triangle(PQR).
#### 16. Determine any a of the [Inner bisectrixs: PD or QE or RF] of a Triangle(PQR). 

In any *Command Prompt Windows* or *Terminal Linux* use *only* the **runVector2d.py program** file to run the new **[version: 2.0]** of the **Vectors2DClassModule.py module**.To more details access the *new instructions* of the **instructions1-v2.0_User.pdf** file. In my **repository** will maintain all the files always created. The users will continue using as in the last. The new **instructions1-v2.0_User.pdf** file will have more new *Instructions* and *Examples* because of **Vectors2DClassModule.py module** file have *new* classes with methods in replacement of the functions always created in **VectorModule2Dim.py module** and too have more new **supplementary classes**. 

#### [Warning-1]: Never use the *runvectors2dim.py program* to run the *new* **Vectors2DClassModule.py module** file. 

Too add the following *new files*: **TrianglePQR.pdf** and **ParallelogramPQRS.pdf** in *repository* to all users view and follow the *Examples: 6(page: 18), New Example 7(page: 20), and too New Example 13 and 14 in pages: 36 and 54* of the **instructions1-v2.0_User.pdf** file. Continue *still* using the files: *runtoolsvectors.py program* with the *VectorModDev.py module*, and too the *instructions2-v1.3_User.pdf* to solve new problems. Inform the all that *still* was not possible begin the *refactor* this previous files. Because of be refactor and test the *new* **[version: 2.0]** of the **Vectors2DClassModule.py module** and **runVector2d.py program** files. Was a hard work. Without forecast of when will be ready to use the *[new version: 2.0]* of this previous files.  


###### Cristovom A. Girodo ( Earned the higher education degree in mathematics from the F.F.C.L.“Oswaldo Cruz” ).
