#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on May 22, 2018, at 11:25
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'test_experiment'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
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
    originPath=u'C:\\Users\\enter\\Documents\\Software\\gitrepos\\experiment\\test_experiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1851, 1234], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "code_Init"
code_InitClock = core.Clock()
# IMPORTING MY PACKAGES
import random as rand
import pandas as pd
import string

# keeping track
trial_count = 0
block_count = 0 

# USER_DEFINED OPTIONS
stim_dur = 50 #duration of stimulus presentation in ms
mask_dur = 34 #duration of the mask in ms
trialType_stim = ['t1', 't2'] #stimulus ondition types

sep_short = 4 # number of stimuli that should seperate T1 from T2
sep_long  = 8

#create an array of short/long interval conditions  

trialType_sep  = np.repeat(a = ['short', 'long'], repeats = [192, 72]) 

trialType_sep  = np.repeat(a = trialType_sep, repeats = len(trialType_stim)) 

trialType_stim = np.repeat(a = trialType_stim, repeats = 192 + 72)  

#create an array of short/long interval conditions  

trialType_mat  = np.stack((trialType_stim, trialType_sep)) 

trialType_mat = np.transpose(trialType_mat)

# number of trials
ntrials = trialType_mat.shape[0]

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_p1 = visual.TextStim(win=win, name='instruct_p1',
    text='Hello. Thank you for coming in today. \n\n For this task, you will be asked to observe a series of characters flash on the screen and try to identify any number(s) you see in the stream. The characters will appear quickly, so you will have to pay close attention. \n\n Sometimes a stream of characters will contain two numbers, and other times it will only contain one. Each stream will contain 15 to 19 characters and last for about a second.  \n\n When two numbers are presented, please enter the numbers via keyboard in the order they were presented. When only one number is presented, enter in the number you saw along with any random number. \n\n If you at any point are not sure which number(s) were presented, you can just guess. \n\n You will be presented two blocks of this task; each block lasting between 13 to 15 minutes.\n\n\n                                                        Press SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ready_block"
ready_blockClock = core.Clock()

ready = visual.TextStim(win=win, name='ready',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
go = visual.TextStim(win=win, name='go',
    text='GO',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
gap = visual.TextStim(win=win, name='gap',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "trial_def"
trial_defClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=0,
    depth=-1.0);

# Initialize components for Routine "disp_stimulus"
disp_stimulusClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
mask = visual.TextStim(win=win, name='mask',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rec_resp_T1"
rec_resp_T1Clock = core.Clock()
Probe_t1 = visual.TextStim(win=win, name='Probe_t1',
    text='What numbers did you see?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "rec_resp_T2"
rec_resp_T2Clock = core.Clock()
Probe_t2 = visual.TextStim(win=win, name='Probe_t2',
    text='What numbers did you see?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "delay"
delayClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

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

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
adv_p1 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instruct_p1, adv_p1]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_p1* updates
    if t >= 0.0 and instruct_p1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_p1.tStart = t
        instruct_p1.frameNStart = frameN  # exact frame index
        instruct_p1.setAutoDraw(True)
    
    # *adv_p1* updates
    if t >= 0.0 and adv_p1.status == NOT_STARTED:
        # keep track of start time/frame for later
        adv_p1.tStart = t
        adv_p1.frameNStart = frameN  # exact frame index
        adv_p1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if adv_p1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ready_block"-------
    t = 0
    ready_blockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    block_count = block_count + 1
    
    ready_txt = "Block " +  str(block_count)
    ready.setText(ready_txt + '\n\n' + "Ready?")
    # keep track of which components have finished
    ready_blockComponents = [ready, go, gap]
    for thisComponent in ready_blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ready_block"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ready_blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *ready* updates
        if t >= 0.0 and ready.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready.tStart = t
            ready.frameNStart = frameN  # exact frame index
            ready.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ready.status == STARTED and t >= frameRemains:
            ready.setAutoDraw(False)
        
        # *go* updates
        if t >= 1 and go.status == NOT_STARTED:
            # keep track of start time/frame for later
            go.tStart = t
            go.frameNStart = frameN  # exact frame index
            go.setAutoDraw(True)
        frameRemains = 1 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if go.status == STARTED and t >= frameRemains:
            go.setAutoDraw(False)
        
        # *gap* updates
        if t >= 1.5 and gap.status == NOT_STARTED:
            # keep track of start time/frame for later
            gap.tStart = t
            gap.frameNStart = frameN  # exact frame index
            gap.setAutoDraw(True)
        frameRemains = 1.5 + .2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gap.status == STARTED and t >= frameRemains:
            gap.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready_block"-------
    for thisComponent in ready_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
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
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        trial_count = trial_count + 1
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
        
        # create the columns to be saved
        sep_col   = [trialType_cur[1] for _ in range(nstim)]
        tnum_col  = [trialType_cur[0] for _ in range(nstim)]
        trial_col = [str(trial_count) for _ in range(nstim)]
        tnum_col  = [trialType_cur[0] for _ in range(nstim)] 
        stimCount_col = range(1,nstim + 1)
        
        stim_cond = [] 
        for elem in range(len(stim_array)):     
            # print(type(stim_array[elem]))
            if stim_array[elem] == ' ':
                stim_cond.append('mask')
            elif type(stim_array[elem]) is np.int64:
                stim_cond.append('target')
            elif type(stim_array[elem]) is str:
                stim_cond.append('distractor')
        
        # put this data into a dataframe
        trial_tab = np.vstack((trial_col, sep_col, tnum_col, stimCount_col, stim_array, stim_cond))
        trial_tab = np.transpose(trial_tab)
        trial_tab = pd.DataFrame(trial_tab)
        
        # save dataframe to conditions *.csv file
        trial_tab.to_csv("tmp_stimuli.csv", header = ['block', 'sep_dur', 'Tx', 'trial', 'stimulus', 'cond'], index = False)
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
            frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
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
        
        
        # set up handler to look after randomisation of conditions etc
        stim = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('tmp_stimuli.csv'),
            seed=None, name='stim')
        thisExp.addLoop(stim)  # add the loop to the experiment
        thisStim = stim.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStim.rgb)
        if thisStim != None:
            for paramName in thisStim:
                exec('{} = thisStim[paramName]'.format(paramName))
        
        for thisStim in stim:
            currentLoop = stim
            # abbreviate parameter names if possible (e.g. rgb = thisStim.rgb)
            if thisStim != None:
                for paramName in thisStim:
                    exec('{} = thisStim[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "disp_stimulus"-------
            t = 0
            disp_stimulusClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.084000)
            # update component parameters for each repeat
            text_2.setText(stimulus)
            # keep track of which components have finished
            disp_stimulusComponents = [text_2, mask]
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
                frameRemains = 0.0 + 0.05- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_2.status == STARTED and t >= frameRemains:
                    text_2.setAutoDraw(False)
                
                # *mask* updates
                if t >= .05 and mask.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    mask.tStart = t
                    mask.frameNStart = frameN  # exact frame index
                    mask.setAutoDraw(True)
                frameRemains = .05 + 0.034- win.monitorFramePeriod * 0.75  # most of one frame period left
                if mask.status == STARTED and t >= frameRemains:
                    mask.setAutoDraw(False)
                
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
            thisExp.nextEntry()
            
        # completed 1 repeats of 'stim'
        
        
        # ------Prepare to start Routine "rec_resp_T1"-------
        t = 0
        rec_resp_T1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        usr_input_t1 = event.BuilderKeyResponse()
        # keep track of which components have finished
        rec_resp_T1Components = [Probe_t1, usr_input_t1]
        for thisComponent in rec_resp_T1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "rec_resp_T1"-------
        while continueRoutine:
            # get current time
            t = rec_resp_T1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Probe_t1* updates
            if t >= 1 and Probe_t1.status == NOT_STARTED:
                # keep track of start time/frame for later
                Probe_t1.tStart = t
                Probe_t1.frameNStart = frameN  # exact frame index
                Probe_t1.setAutoDraw(True)
            
            # *usr_input_t1* updates
            if t >= 1 and usr_input_t1.status == NOT_STARTED:
                # keep track of start time/frame for later
                usr_input_t1.tStart = t
                usr_input_t1.frameNStart = frameN  # exact frame index
                usr_input_t1.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(usr_input_t1.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if usr_input_t1.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if usr_input_t1.keys == []:  # then this was the first keypress
                        usr_input_t1.keys = theseKeys[0]  # just the first key pressed
                        usr_input_t1.rt = usr_input_t1.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_resp_T1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rec_resp_T1"-------
        for thisComponent in rec_resp_T1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if usr_input_t1.keys in ['', [], None]:  # No response was made
            usr_input_t1.keys=None
        trials.addData('usr_input_t1.keys',usr_input_t1.keys)
        if usr_input_t1.keys != None:  # we had a response
            trials.addData('usr_input_t1.rt', usr_input_t1.rt)
        # the Routine "rec_resp_T1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rec_resp_T2"-------
        t = 0
        rec_resp_T2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        usr_input_t2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        rec_resp_T2Components = [Probe_t2, usr_input_t2]
        for thisComponent in rec_resp_T2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "rec_resp_T2"-------
        while continueRoutine:
            # get current time
            t = rec_resp_T2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Probe_t2* updates
            if t >= 0.0 and Probe_t2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Probe_t2.tStart = t
                Probe_t2.frameNStart = frameN  # exact frame index
                Probe_t2.setAutoDraw(True)
            
            # *usr_input_t2* updates
            if t >= 0.0 and usr_input_t2.status == NOT_STARTED:
                # keep track of start time/frame for later
                usr_input_t2.tStart = t
                usr_input_t2.frameNStart = frameN  # exact frame index
                usr_input_t2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(usr_input_t2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if usr_input_t2.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if usr_input_t2.keys == []:  # then this was the first keypress
                        usr_input_t2.keys = theseKeys[0]  # just the first key pressed
                        usr_input_t2.rt = usr_input_t2.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_resp_T2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rec_resp_T2"-------
        for thisComponent in rec_resp_T2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if usr_input_t2.keys in ['', [], None]:  # No response was made
            usr_input_t2.keys=None
        trials.addData('usr_input_t2.keys',usr_input_t2.keys)
        if usr_input_t2.keys != None:  # we had a response
            trials.addData('usr_input_t2.rt', usr_input_t2.rt)
        # the Routine "rec_resp_T2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "delay"-------
        t = 0
        delayClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        # keep track of which components have finished
        delayComponents = [blank]
        for thisComponent in delayComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "delay"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = delayClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank* updates
            if t >= 0.0 and blank.status == NOT_STARTED:
                # keep track of start time/frame for later
                blank.tStart = t
                blank.frameNStart = frameN  # exact frame index
                blank.setAutoDraw(True)
            frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blank.status == STARTED and t >= frameRemains:
                blank.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "delay"-------
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed ntrials repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'block'




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
