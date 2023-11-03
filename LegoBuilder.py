from maya import cmds



window = cmds.window(title="Lego Duilder", menuBar=True, width=300)
cmds.columnLayout("Block")
cmds.intSliderGrp("blockWidth", label="Block Width", field=True, min=1, max=10, v=4)
cmds.intSliderGrp("blockDepth", label="Block Depth", field=True, min=1, max=10, v=2)
cmds.button(label="Create Block", c="createLegoBlock()")
cmds.showWindow(window)

def createLegoBlock():
	

	width = cmds.intSliderGrp("blockWidth", q=True, v=True)
	depth = cmds.intSliderGrp("blockDepth", q=True, v=True)
	
	sizeY = 0.96
	sizeX = width * 0.8
	sizeZ = depth * 0.8
	
	#create main block
	block = cmds.polyCube(h=sizeY, w=sizeX, d=sizeZ, sx=width, sz=depth)
	
	#create nubs top
	for i in range(width):
		for j in range(depth):
			nub = cmds.polyCylinder(r=0.25, h=0.2)
			cmds.move(sizeY/2.0, moveY=True, a=True)
			cmds.move((-sizeX/2.0 + (i+0.5)*0.77), moveX=True, a=True)
			cmds.move((-sizeZ/2.0 + (j+0.5)*0.8), moveZ=True, a=True)
				
			block = cmds.polyCBoolOp(block, nub, ch=False)
	
	#remove bottom
	tmp = cmds.polyCube(h=sizeY, w=sizeX-0.12 * 2, d=sizeZ-0.12 * 2, sx=1, sz=1)
	cmds.move(-0.1, moveY=True)
	block = cmds.polyCBoolOp(block, tmp, op=2, ch=False)
	
	#create nubs bottom
	for i in range(width-1):
		for j in range(depth-1):
			innerNubs = cmds.polyCylinder(r=0.3255, h=0.7, sx=10)
			center = cmds.polyCylinder(r=0.25, h=1, sx=10)
			innerNubs = cmds.polyCBoolOp(innerNubs, center, op=2, ch=False)
			
			cmds.move(-0.05, moveY=True, a=True)
			cmds.move((-sizeX/2.0 + (i+1)*0.8), moveX=True, a=True)
			cmds.move((-sizeZ/2.0 + (j+1)*0.8), moveZ=True, a=True)	
			
			block = cmds.polyCBoolOp(block, innerNubs, op=1, ch=False)
			
	return block

