from psychopy import visual, core  # import some libraries from PsychoPy
import settings
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