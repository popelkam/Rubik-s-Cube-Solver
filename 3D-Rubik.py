from visual import*

btLength = 2 
ctLength = 1.9 
thickness = 0.01
cubeLength = btLength*3

btbox = box(pos =(1, 1/2, 2),size =(cubeLength,cubeLength,cubeLength),color=(0, 0, 0))
##box( pos = vector( 0, 0, 0 ), size = vector( 1, 1, 0.01 ) )
##box( pos = vector( 0, 0, 0 ), size = vector( 0.01, 1, 1 ) )


for row in arange(0,3):
   for col in arange(0,3):
      
       wallLeft = box( pos=vector( -2, row * btLength-2, col * btLength), material = materials.emissive,
        size=vector(thickness, ctLength, ctLength),
        color = ( 0, 0, 1 ))
       
       wallRight = box( pos=vector( cubeLength-2, row * btLength-2, col * btLength), material = materials.emissive,
        size=vector(thickness, ctLength, ctLength),
        color = ( 0, 1, 0 ) )
       
       wallBotom = box( pos=vector( row * btLength +btLength / -2.0, -1 - btLength, col * btLength), material = materials.emissive,
        size=vector(ctLength, thickness, ctLength),
        color = ( 1, 0.5, 0, ) )
       
       wallTop = box( pos=vector( row * btLength + btLength / -2.0, cubeLength /btLength, col * btLength ), material = materials.emissive,
        size=vector(ctLength, thickness, ctLength),
        color = ( 1, 0, 0 ) )
       
       wallBack = box( pos=vector( row * btLength + btLength /-2.0, col * btLength-2,  -btLength / btLength), material = materials.emissive,
        size=vector(ctLength, ctLength, thickness),
        color = ( 1, 1, 0) )
       
       wallFront = box( pos=vector( row * btLength + btLength/-2.0, col * btLength-2, cubeLength - btLength / 2.0 ), material = materials.emissive,
        size=vector(ctLength, ctLength, thickness),
        color = ( 1, 1, 1 ) )

