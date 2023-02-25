from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
import numpy, random
import settings

expInfo = {'Name':'HAL', 'Test': 0}
expInfo['dateStr'] = data.getDateStr()  # add the current time
# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='Info', fixed=['dateStr'])
if dlg.OK:
    filename = expInfo['Name'] + "_" + expInfo['dateStr']
else:
    core.quit()  # the user hit cancel so exit

print(filename)
#create a window
mywin = visual.Window([settings.screen_width,settings.screen_width], 
                      fullscr=True, screen=0, monitor="testMonitor", 
                      color=[-1,-1,-1], units="pix")
#create some stimuli
grating = visual.GratingStim(win=mywin, mask="circle", size=500, pos=[0.0,0.0], sf=3)
fixation = visual.GratingStim(win=mywin, size=100, pos=[0.0,0.0], sf=0, rgb=-1)
#draw the stimuli and update the window
grating.draw()
fixation.draw()
mywin.update()
#pause, so you get a chance to see it!
core.wait(3.0)