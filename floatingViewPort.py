import maya.cmds as cmds

#Change the camera assigned to the view port
def changeCamera(item):
	cmds.modelEditor('editor', edit=True, camera=item)

#Toggle between visualization options. On enables resolution gate and remove joints, cameras, ikHandles, grid, and nurbs curves. Off disables resolution and enables the other options.
def toggleGate(item):
    selCamera=cmds.modelEditor('editor', query=True, camera=True)
    if item:
	    cmds.camera(selCamera, edit=True, displayGateMask=True, displayResolution=True, overscan=1.3)
	    cmds.modelEditor('editor', edit=True, nurbsCurves=False, cameras=False, joints=False, ikHandles=False, grid=False)
    else:
	    cmds.camera(selCamera, edit=True, displayGateMask=False, displayResolution=False, overscan=1.0)
	    cmds.modelEditor('editor', edit=True, nurbsCurves=True, cameras=True, joints=True, ikHandles=True, grid=True)

def reloadCameras(*args):
    cameras = cmds.listCameras(perspective=True)
    opCamera=cmds.optionMenu('opCamera', label='Camera: ', changeCommand=changeCamera, parent='column')
    for each in range(len(cameras)):
        cmds.menuItem(label=cameras[each], parent=opCamera)

#Create the button menu.
def createMenu(*args):
    #Get all the cameras available in the scene
	cameras = cmds.listCameras(perspective=True)
	
	#Check to see if the menu exists (only for refreshing cameras - adding/removing cameras and still keep the same menu order)
	if cmds.optionMenu('opCamera', exists=True):
	    cmds.deleteUI('opCamera')
	    cmds.deleteUI('viz')
	    cmds.deleteUI('wireframe')
	    cmds.deleteUI('points')
	    cmds.deleteUI('bound')
	    cmds.deleteUI('smooth')
	    cmds.deleteUI('flat')
	    cmds.deleteUI('reload')
	    
	#Populate the cameras for selection
	opCamera=cmds.optionMenu('opCamera', label='Camera: ', changeCommand=changeCamera, parent='column')
	for each in range(len(cameras)):
	    cmds.menuItem(label=cameras[each], parent='opCamera')
	#Checkbox option to change visualization options on the selected camera
	cmds.checkBox('viz', label='Viz', parent='column', onCommand=toggleGate, offCommand=toggleGate)
	
	#Add buttons to change display type
	cmds.button('wireframe', label='Wireframe', command= "cmds.modelEditor('editor', edit=True, displayAppearance='wireframe')", parent='column')
	cmds.button('points', label='Points', command= "cmds.modelEditor('editor', edit=True, displayAppearance='points')", parent='column')
	cmds.button('bound', label='Bounding Box', command= "cmds.modelEditor('editor', edit=True, displayAppearance='boundingBox')", parent='column')
	cmds.button('smooth', label='Smooth Shaded', command= "cmds.modelEditor('editor', edit=True, displayAppearance='smoothShaded')", parent='column')
	cmds.button('flat', label='Flat Shaded', command= "cmds.modelEditor('editor', edit=True, displayAppearance='flatShaded')", parent='column')
	cmds.button('reload', label='Reload Cameras', command=createMenu, parent='column')
    
#Main method to create the View Port
def createViewPort():
    if cmds.window('window', exists=True):
    	cmds.deleteUI('window')
    
    cameras = cmds.listCameras(perspective=True)
    window = cmds.window('window', title='View Port', sizeable=True)
    form = cmds.formLayout('form')
    editor = cmds.modelEditor('editor', camera=cameras[0])
    column = cmds.rowLayout('column', numberOfColumns=8)
    
    createMenu()
    
    #    Set up the window layout attachments.
    cmds.formLayout( form, edit=True, attachForm=[('column', 'top', 0), ('column', 'left', 0), (editor, 'left', 0), (editor, 'bottom', 0), (editor, 'right', 0)], attachNone=[('column', 'bottom'), ('column', 'right')], attachControl=(editor, 'top', 0, 'column'))
    cmds.showWindow( 'window' )