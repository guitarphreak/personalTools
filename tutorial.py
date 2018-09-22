import maya.cmds as cmds
import sys

def createLocators(*args):
    #Check for valid amount of locators (not null).
    if (cmds.textField('numLocators', query=True, text=True) == ''):
        print 'No locators created. Please enter the amount of locators required.'
        return
    #If amount of locators is not null, convert it to a number.        
    varLocators = int(cmds.textField('numLocators', query=True, text=True))
    sel = cmds.radioButtonGrp('radioGroup', query=True, select=True)
    if (varLocators > 0):
        #Check for valid x,y,z tuple.        
        xPos = cmds.textField('xValue', query=True, text=True)
        yPos = cmds.textField('yValue', query=True, text=True)
        zPos = cmds.textField('zValue', query=True, text=True)
        print sel
        if ((xPos == '') | (yPos == '') | (zPos == '')):
            print 'Please enter the complete X,Y,Z tuple to indicate the position.'
            return
        #Check if positioning Linear is selected.
        if sel == 1:
            print 'linear'
            for i in range(0, varLocators):
                i += 1
                cmds.spaceLocator(position=(int(xPos),int(yPos),int(zPos)), name='locator_%d' %(i+1))
            return
        #Check if positioning Relative is selected.            
        elif sel == 2:
            print 'relative'
            for i in range(0, varLocators):
                i += 1
                cmds.spaceLocator(position=(int(xPos),int(yPos),int(zPos)), relative=True, name='locator_%d' %(i+1))
            return
        #Check if positioning Absolute is selected.
        elif sel == 3:
            print 'absolute'
            for i in range(0, varLocators):
                i += 1
                cmds.spaceLocator(position=(int(xPos),int(yPos),int(zPos)), absolute=True, name='locator_%d' %(i+1))
            return
        #Check for a valid positioning method.
        elif sel == 0:
            print 'Please choose one of the positioning methods'
            return
    #Check for valid amount of locators.
    elif (varLocators <= 0):
        print 'The minimum amount of locators is 1'
    return

#Deletes the window upon pressing the Cancel button.
def deleteWindow(*args):
    cmds.deleteUI('locatorUI')

#If the UI window already exists delete it to create a new one.
if cmds.window('locatorUI', exists=True):
    cmds.deleteUI('locatorUI')
    
window = cmds.window('locatorUI', title = 'Locator Creator', width=230, height=300, mnb=False, mxb=False, sizeable=False)
#General layout for the window
mainLayout = cmds.columnLayout(rowSpacing=10, columnWidth=230, columnAlign='center')
cmds.separator(width=230, height=20, parent = mainLayout)

#Enter the number of locators needed
scndLayout = cmds.rowLayout(numberOfColumns=2, columnWidth2=(100,60), parent = mainLayout)
cmds.text(label='Number of Locators:', parent = scndLayout)
cmds.textField('numLocators', width=40, height=20, parent = scndLayout)

#Enter the desired positioning of the locators
thirdLayout = cmds.rowLayout(numberOfColumns=3, columnWidth3=(45,80,80), parent = mainLayout)
cmds.text(label='Position:', parent = thirdLayout)
cmds.radioButtonGrp('radioGroup', numberOfRadioButtons=3, columnWidth3=(50,65,40), labelArray3=['Linear','Relative','Absolute'], parent = thirdLayout)

#Enter the x,y,z coordinates to create the locators
fourthLayout = cmds.rowLayout(numberOfColumns=6, columnWidth6=(20,40,20,40,20,40), parent = mainLayout)
cmds.text(label='X', align='right', parent = fourthLayout)
cmds.textField('xValue', width=30, height=20, parent = fourthLayout, text='0')
cmds.text(label='Y', align='right', parent = fourthLayout)
cmds.textField('yValue', width=30, height=20, parent = fourthLayout, text='0')
cmds.text(label='Z', align='right', parent = fourthLayout)
cmds.textField('zValue', width=30, height=20, parent = fourthLayout, text='0')

#Create/Cancel buttons
fifthLayout = cmds.rowLayout(numberOfColumns=2, columnWidth2=(100,100), columnAlign2=('center','center'), parent = mainLayout)
cmds.button(label='Create', width=60, command=createLocators, parent = fifthLayout)
cmds.button(label='Cancel', width=60, parent = fifthLayout, command=deleteWindow)
cmds.separator(width=230, height=15, parent = mainLayout)
cmds.showWindow(window)