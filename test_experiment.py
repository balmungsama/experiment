#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on Wed Feb 28 01:29:41 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random as rand # to get the random character vector

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'test_experiment'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(2560, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "code_Init"
code_InitClock = core.Clock()
#count = 1

stim_dur = 50 #duration of stimulus presentation in ms
mask_dur = 34 #duration of the mask in ms
trialType_stim = ['t1', 't2'] #stimulus ondition types

sep_short = 4 # number of stimuli that should seperate T1 from T2
sep_long  = 8

#create an array of stimulus conditions trialType_stim = np.repeat(a = trialType_stim, repeats = 192 + 72) trialType_stim = np.concatenate((trialType_stim, trialType_stim))  #create an array of short/long interval conditions trialType_sep_long  = np.repeat(a = 'long' , repeats = 72 ) trialType_sep_short = np.repeat(a = 'short', repeats = 192) trialType_sep = np.concatenate((trialType_sep_long, trialType_sep_short)) trialType_sep = np.concatenate((trialType_sep, trialType_sep))  #merge this into a single array, defining all possible stimulus conditions trialType_mat = np.stack((trialType_stim, trialType_sep)) trialType_mat = np.transpose(trialType_mat)
trialType_stim = np.repeat(a = ['t2', 't1'], repeats = 192 + 72)

#create an array of short/long interval conditions
trialType_sep_long  = np.repeat(a = 'long' , repeats = 72 )
trialType_sep_short = np.repeat(a = 'short', repeats = 192)
trialType_sep = np.concatenate((trialType_sep_long, trialType_sep_short))
trialType_sep = np.concatenate((trialType_sep, trialType_sep))

#merge this into a single array, defining all possible stimulus conditions
trialType_mat = np.stack((trialType_stim, trialType_sep))
trialType_mat = np.transpose(trialType_mat)

# number of trials
ntrials = trialType_mat.shape[0]

# Initialize components for Routine "trial_def"
trial_defClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=4, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "disp_stimulus"
disp_stimulusClock = core.Clock()

text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'blue', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "code_Init"-------
t = 0
code_InitClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
code_InitComponents = []
for thisComponent in code_InitComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "code_Init"-------
while continueRoutine:
    # get current time
    t = code_InitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in code_InitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "code_Init"-------
for thisComponent in code_InitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "code_Init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=ntrials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_def"-------
    t = 0
    trial_defClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    trial_count = 0 # temporary value to see if it loops correctly
    stim_count  = 0 # keep track of which stimulus to display
    nstim = randint(15,19)
    
    trialType_cur = randint(0, np.shape(trialType_mat)[0]-1) # determine type of tral (eg. T2-present, long seperation)
    trialType_cur = trialType_mat[trialType_cur]
    stim_array    = [rand.choice(string.ascii_uppercase) for _ in range(nstim)] # begin building array of stimuli to be shown in this trial
    
    # determine the postions for the Target stimuli
    if trialType_cur[1] == 'long':
        t1_pos = np.random.choice(range(1,nstim - sep_long))
        t2_pos = t1_pos + sep_long
    elif trialType_cur[1] == 'short':
        t1_pos = np.random.choice(range(1,nstim - sep_short))
        t2_pos = t1_pos + sep_short
    
    # place the T1 target number into the stimulus array
    stim_array[t1_pos - 1] = np.random.choice(range(1,9))
    
    # put T2 in the stimulus vector
    if trialType_cur[0] == 't2':
        stim_array[t2_pos - 1] = np.random.choice(range(1,9))
    elif trialType_cur[0] == 't1':
        stim_array[t2_pos - 1] = ' '
    
    # the 20% chance of the trial including a blank stimulus
    if trialType_cur[0] == 't2':
        roll_die = np.random.choice(range(1,5))
        if roll_die == 1:
            blank_pos = range(1,nstim) 
            blank_pos.remove(t1_pos)
            blank_pos.remove(t2_pos)
            blank_pos = np.random.choice(blank_pos)
            
            stim_array[blank_pos - 1] = ' '
    text.setText(trial_count)
    # keep track of which components have finished
    trial_defComponents = [text]
    for thisComponent in trial_defComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_def"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_defClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_defComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_def"-------
    for thisComponent in trial_defComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_count = trial_count + 1
    
    # set up handler to look after randomisation of conditions etc
    stimuli = data.TrialHandler(nReps=nstim, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='stimuli')
    thisExp.addLoop(stimuli)  # add the loop to the experiment
    thisStimulus = stimuli.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
    if thisStimulus != None:
        for paramName in thisStimulus:
            exec('{} = thisStimulus[paramName]'.format(paramName))
    
    for thisStimulus in stimuli:
        currentLoop = stimuli
        # abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
        if thisStimulus != None:
            for paramName in thisStimulus:
                exec('{} = thisStimulus[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "disp_stimulus"-------
        t = 0
        disp_stimulusClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        stim_cur = stim_array[stim_count]
        text_2.setText(stim_cur)
        # keep track of which components have finished
        disp_stimulusComponents = [text_2]
        for thisComponent in disp_stimulusComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "disp_stimulus"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = disp_stimulusClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_2* updates
            if t >= 0.0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_2.status == STARTED and t >= frameRemains:
                text_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in disp_stimulusComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "disp_stimulus"-------
        for thisComponent in disp_stimulusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stim_count = stim_count + 1
        thisExp.nextEntry()
        
    # completed nstim repeats of 'stimuli'
    
    thisExp.nextEntry()
    
# completed ntrials repeats of 'trials'




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
