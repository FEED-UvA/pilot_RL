#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.2),
    on Wed Oct 17 11:49:40 2018
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
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'pilot_RL'  # from the Builder filename that created this script
expInfo = {'participant': '99', 'participant_gender': 'F', 'skip_practice': 'False', 'skip_ratings': 'False'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'logs/sub-%s/sub-%s_events' % (expInfo['participant'], expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lukas/projects/FEED/pilot_RL/pilot_RL.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='mbp', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "welcome_1"
welcome_1Clock = core.Clock()
import os
import os.path as op
import pandas as pd
import shutil
import yaml
import sys
from glob import glob

# Load params
with open('params.yml', 'r') as params:
    custom_params = yaml.load(params)
    text_size = custom_params['text_size']
    wrap_width = custom_params['wrap_width']

    if sys.platform == 'darwin':
        wrap_width = 30

    face_size = custom_params['face_size']
    n_trials = int(custom_params['n_trials'])

# Define variables dependent on subject
subj_info_df = pd.read_csv('subject_info.csv')
sub_nr = expInfo['participant']
this_subj_df = subj_info_df.query('subject_id == @sub_nr')

RL_order = this_subj_df['RL_order'].values[0]
face_gender = this_subj_df['face_gender'].values[0]

# Create new subject dir in which to store stims/logs
sub_dir = op.join('logs', 'sub-%s' % sub_nr)
if not op.isdir(sub_dir):
    os.makedirs(sub_dir)

# Remove existing stuff
existing_imgs = glob(op.join(sub_dir, '*.png'))
existing_csvs = glob(op.join(sub_dir, '*.csv'))
_ = [os.remove(f) for f in existing_imgs]
_ = [os.remove(f) for f in existing_csvs]

rewards_file = op.join(sub_dir, 'rewards.txt')
if op.isfile(rewards_file):
    os.remove(rewards_file)
else:
    open(rewards_file, 'a').close()

if sys.platform[:3] == 'win':
    sys.path.append(op.abspath('deps'))
    stims_file = 'stims_windows.csv'
else:
    stims_file = 'stims.csv'
welcome_txt_1 = visual.TextStim(win=win, name='welcome_txt_1',
    text='Welkom bij dit experiment!\n\nDit experiment gaat over de perceptie van gezichten en de invloed van associatief leren.\n\nHet experiment bestaat uit twee fases:\n- een uitgebreide beoordelings-fase\n- een leer-fase met een korte beoordelingsfase (x2)\n\nDe leer-fase (met korte beoordeling daarna) doe je twee keer.',
    font='Arial',
    pos=(0, 5), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
setup_RL_image = visual.ImageStim(
    win=win, name='setup_RL_image',
    image='pilot_RL_setup.png', mask=None,
    ori=0, pos=(0, -3), size=(28, 7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
welcome_txt_1_2 = visual.TextStim(win=win, name='welcome_txt_1_2',
    text='(Druk op een willekeurige knop om door te gaan.)',
    font='Arial',
    pos=(0, -10), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "welcome_2"
welcome_2Clock = core.Clock()
welcome_txt_2 = visual.TextStim(win=win, name='welcome_txt_2',
    text="In de eerste fase ga je gezichten beoordelen\nop een aantal eigenschappen (aantrekkelijkheid, betrouwbaarheid, etc.).\nDit duurt zo'n 10 minuten.\n\n(Druk op een willekeurige toets om verder te gaan.)",
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "welcome_3"
welcome_3Clock = core.Clock()
welcome_txt_3 = visual.TextStim(win=win, name='welcome_txt_3',
    text='Je zal de gezichten beoordelen op een schaal.\nJe gebruikt de volgende knoppen:\n\n- F: pointer naar LINKS\n- J: pointer naar RECHTS\n- spatie: keuze bevestigen\n\nEr is geen tijdsdruk.\n\n(Druk op een willekeurige toets om een voorbeeld te zien.)',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "example_scale"
example_scaleClock = core.Clock()
practice_image = visual.ImageStim(
    win=win, name='practice_image',
    image='stims/practice_stims/trump.jpg', mask=None,
    ori=0, pos=(0, 2), size=face_size,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
example_scale_hint = visual.TextStim(win=win, name='example_scale_hint',
    text='Dit is om te "oefenen"!\n\n(F = links, J = rechts, spatie = bevestig)\n',
    font='Arial',
    pos=(0, 10), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
example_scale_1 = visual.RatingScale(win=win, name='example_scale_1', leftKeys=['f'],
rightKeys=['j'],
acceptKeys=['space'],
mouseOnly=False,
singleClick=False,
labels=['Heel onaantrekkelijk', '', 'Heel aantrekkelijk'],
low=-4,
high=4,
markerStart=0,
showAccept=False,
pos=(0, -0.5),
scale='Hoe aantrekkelijk vind je dit gezicht?',
tickMarks=[-4, 0, 4],
stretch=1.3)

# Initialize components for Routine "welcome_4"
welcome_4Clock = core.Clock()
welcome_txt_4 = visual.TextStim(win=win, name='welcome_txt_4',
    text='Als de beoordelings-fase duidelijk is,\ndan kunnen we beginnen.\n\n(Druk op een knop om de eerste sessie te beginnen!)',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "pre_rating_instruct"
pre_rating_instructClock = core.Clock()
rating_df = pd.read_csv(stims_file, index_col='stim_file')

pre_rating_instruct_common = visual.TextStim(win=win, name='pre_rating_instruct_common',
    text='Bij de gezichten die straks in beeld komen\nmoet je de volgende vraag beantwoorden:',
    font='Arial',
    pos=(0, 8), height=(text_size + 0.5), wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
pre_rating_instruct_txt = visual.TextStim(win=win, name='pre_rating_instruct_txt',
    text='default text',
    font='Arial',
    pos=(0, 1), height=(text_size + 0.5), wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
question_details_txt = visual.TextStim(win=win, name='question_details_txt',
    text='default text',
    font='Arial',
    pos=(0, -3), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
click_to_continue = visual.TextStim(win=win, name='click_to_continue',
    text='(Als de vraag duidelijk is, druk dan op een willekeurige toets om te beginnen.)',
    font='Arial',
    pos=(0, -8), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "pre_rating"
pre_ratingClock = core.Clock()
pre_rating_img = visual.ImageStim(
    win=win, name='pre_rating_img',
    image='sin', mask=None,
    ori=0, pos=(0, 1), size=face_size,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pre_rating_scale = visual.RatingScale(win=win, name='pre_rating_scale', marker='slider', size=1.0, pos=[0.0, -0.5], labels=[''], scale='', markerStart='0', showAccept=False)


# Initialize components for Routine "pause_rating"
pause_ratingClock = core.Clock()
pause_rating_text = visual.TextStim(win=win, name='pause_rating_text',
    text='Als je wilt, kan je nu even pauze nemen.\n\n(Om door te gaan, druk op een willekeurige toets.)\n',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "select_faces"
select_facesClock = core.Clock()


# Initialize components for Routine "instruct_RL_1"
instruct_RL_1Clock = core.Clock()

instruct_RL_1_txt = visual.TextStim(win=win, name='instruct_RL_1_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instruct_RL_2"
instruct_RL_2Clock = core.Clock()
instruct_RL_2_txt_3 = visual.TextStim(win=win, name='instruct_RL_2_txt_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instruct_RL_2_1"
instruct_RL_2_1Clock = core.Clock()
instruct_RL_2_txt_4 = visual.TextStim(win=win, name='instruct_RL_2_txt_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instruct_RL_2_2"
instruct_RL_2_2Clock = core.Clock()
instruct_RL_2_txt = visual.TextStim(win=win, name='instruct_RL_2_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instruct_RL_3"
instruct_RL_3Clock = core.Clock()

instruct_RL_3_txt = visual.TextStim(win=win, name='instruct_RL_3_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instruct_RL_5"
instruct_RL_5Clock = core.Clock()

instruct_RL_5_txt = visual.TextStim(win=win, name='instruct_RL_5_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "pre_fix"
pre_fixClock = core.Clock()

pre_fix_icon = visual.GratingStim(
    win=win, name='pre_fix_icon',
    tex='sin', mask='raisedCos',
    ori=0, pos=(0,0), size=(0.3, 0.3), sf=0, phase=0.0,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "practice_RL_trial"
practice_RL_trialClock = core.Clock()
feedback_ori = 0
feedback_txt = 'Not set!'
feedback_color = 'White'
feedback_sign_opacity = 0
practice_left_face = visual.ImageStim(
    win=win, name='practice_left_face',
    image='sin', mask=None,
    ori=0, pos=(-5, 0), size=(7, 7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
practice_right_face = visual.ImageStim(
    win=win, name='practice_right_face',
    image='sin', mask=None,
    ori=0, pos=(5, 0), size=(7, 7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
practice_response_prompt = visual.TextStim(win=win, name='practice_response_prompt',
    text='Kies links ("f") of rechts ("j").\nJe hebt 3 seconden om te antwoorden!',
    font='Arial',
    pos=(0, -6), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
fix_practice = visual.GratingStim(
    win=win, name='fix_practice',
    tex='sin', mask='raisedCos',
    ori=0, pos=(0, 0), size=(0.3, 0.3), sf=0, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=512, interpolate=True, depth=-5.0)
practice_money = custom_params['RL_params']['start_amount']

# Initialize components for Routine "practice_RL_feedback"
practice_RL_feedbackClock = core.Clock()
practice_feedback_sign = visual.ShapeStim(
    win=win, name='practice_feedback_sign', vertices='cross',
    size=(1, 1),
    ori=1.0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
practice_feedback_written_txt = visual.TextStim(win=win, name='practice_feedback_written_txt',
    text='default text',
    font='Arial',
    pos=(0, -1), height=text_size, wrapWidth=wrap_width, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "begin_real_RL"
begin_real_RLClock = core.Clock()


begin_real_RL_txt = visual.TextStim(win=win, name='begin_real_RL_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "begin_real_RL2"
begin_real_RL2Clock = core.Clock()

begin_real_RL_txt_2 = visual.TextStim(win=win, name='begin_real_RL_txt_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "pre_fix_2"
pre_fix_2Clock = core.Clock()
pre_fix_icon2 = visual.GratingStim(
    win=win, name='pre_fix_icon2',
    tex='sin', mask='raisedCos',
    ori=0, pos=(0, 0), size=(0.3, 0.3), sf=0, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "real_RL_trial"
real_RL_trialClock = core.Clock()
feedback_ori = 0
feedback_txt = 'Not set!'
feedback_color = 'White'
feedback_sign_opacity = 0
counter_RL = 1
real_left_face = visual.ImageStim(
    win=win, name='real_left_face',
    image='sin', mask=None,
    ori=0, pos=(-5, 0), size=face_size,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
real_right_face = visual.ImageStim(
    win=win, name='real_right_face',
    image='sin', mask=None,
    ori=0, pos=(5, 0), size=face_size,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
fix_real = visual.GratingStim(
    win=win, name='fix_real',
    tex='sin', mask='raisedCos',
    ori=0, pos=(0, 0), size=(0.3, 0.3), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=512, interpolate=True, depth=-4.0)
real_money = dict(plusmin=custom_params['RL_params']['start_amount'],
                  plusneu=custom_params['RL_params']['start_amount'])

# Initialize components for Routine "real_RL_feedback"
real_RL_feedbackClock = core.Clock()
real_feedback_sign = visual.ShapeStim(
    win=win, name='real_feedback_sign', vertices='cross',
    size=(1, 1),
    ori=1.0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
real_feedback_written_txt = visual.TextStim(win=win, name='real_feedback_written_txt',
    text='default text',
    font='Arial',
    pos=(0, -1), height=text_size, wrapWidth=wrap_width, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "pause_RL"
pause_RLClock = core.Clock()

pause_txt = visual.TextStim(win=win, name='pause_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "overview_money"
overview_moneyClock = core.Clock()
overview_money_txt = visual.TextStim(win=win, name='overview_money_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "post_rating_intro"
post_rating_introClock = core.Clock()
post_rating_intro_txt = visual.TextStim(win=win, name='post_rating_intro_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "post_rating_instruct"
post_rating_instructClock = core.Clock()


post_rating_instruct_common = visual.TextStim(win=win, name='post_rating_instruct_common',
    text='Bij de gezichten die straks in beeld komen\nmoet je de volgende vraag beantwoorden:',
    font='Arial',
    pos=(0, 8), height=(text_size + 0.5), wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
pre_rating_instruct_txt_2 = visual.TextStim(win=win, name='pre_rating_instruct_txt_2',
    text='default text',
    font='Arial',
    pos=(0, 1), height=(text_size + 0.5), wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
rating_press_to_continue_2 = visual.TextStim(win=win, name='rating_press_to_continue_2',
    text='default text',
    font='Arial',
    pos=(0, -3), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
click_to_continue_2 = visual.TextStim(win=win, name='click_to_continue_2',
    text='(Als de vraag duidelijk is, druk dan op een willekeurige toets om te beginnen.)',
    font='Arial',
    pos=(0, -8), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "post_rating"
post_ratingClock = core.Clock()
post_rating_img = visual.ImageStim(
    win=win, name='post_rating_img',
    image='sin', mask=None,
    ori=0, pos=(0, 1), size=face_size,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
post_rating_scale = visual.RatingScale(win=win, name='post_rating_scale', marker='slider', size=1.0, pos=[0.0, -0.5], labels=[''], scale='', markerStart='0', showAccept=False)

# Initialize components for Routine "end_of_session"
end_of_sessionClock = core.Clock()
end_of_session_txt = visual.TextStim(win=win, name='end_of_session_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=wrap_width, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanks_txt = visual.TextStim(win=win, name='thanks_txt',
    text='Bedankt voor je deelname!\nDe taak zal vanzelf afsluiten.',
    font='Arial',
    pos=(0, 0), height=text_size, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_1"-------
t = 0
welcome_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

welcome_resp_1 = event.BuilderKeyResponse()
# keep track of which components have finished
welcome_1Components = [welcome_txt_1, setup_RL_image, welcome_txt_1_2, welcome_resp_1]
for thisComponent in welcome_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome_1"-------
while continueRoutine:
    # get current time
    t = welcome_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *welcome_txt_1* updates
    if t >= 0.0 and welcome_txt_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_txt_1.tStart = t
        welcome_txt_1.frameNStart = frameN  # exact frame index
        welcome_txt_1.setAutoDraw(True)
    
    # *setup_RL_image* updates
    if t >= 0.0 and setup_RL_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        setup_RL_image.tStart = t
        setup_RL_image.frameNStart = frameN  # exact frame index
        setup_RL_image.setAutoDraw(True)
    
    # *welcome_txt_1_2* updates
    if t >= 0.0 and welcome_txt_1_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_txt_1_2.tStart = t
        welcome_txt_1_2.frameNStart = frameN  # exact frame index
        welcome_txt_1_2.setAutoDraw(True)
    
    # *welcome_resp_1* updates
    if t >= 0.0 and welcome_resp_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_resp_1.tStart = t
        welcome_resp_1.frameNStart = frameN  # exact frame index
        welcome_resp_1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if welcome_resp_1.status == STARTED:
        theseKeys = event.getKeys()
        
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
    for thisComponent in welcome_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_1"-------
for thisComponent in welcome_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "welcome_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_2"-------
t = 0
welcome_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
welcome_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
welcome_2Components = [welcome_txt_2, welcome_resp_2]
for thisComponent in welcome_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome_2"-------
while continueRoutine:
    # get current time
    t = welcome_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_txt_2* updates
    if t >= 0.0 and welcome_txt_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_txt_2.tStart = t
        welcome_txt_2.frameNStart = frameN  # exact frame index
        welcome_txt_2.setAutoDraw(True)
    
    # *welcome_resp_2* updates
    if t >= 0.0 and welcome_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_resp_2.tStart = t
        welcome_resp_2.frameNStart = frameN  # exact frame index
        welcome_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if welcome_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
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
    for thisComponent in welcome_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_2"-------
for thisComponent in welcome_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_3"-------
t = 0
welcome_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruct_cont_5 = event.BuilderKeyResponse()
# keep track of which components have finished
welcome_3Components = [welcome_txt_3, instruct_cont_5]
for thisComponent in welcome_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome_3"-------
while continueRoutine:
    # get current time
    t = welcome_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_txt_3* updates
    if t >= 0.0 and welcome_txt_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_txt_3.tStart = t
        welcome_txt_3.frameNStart = frameN  # exact frame index
        welcome_txt_3.setAutoDraw(True)
    
    # *instruct_cont_5* updates
    if t >= 0.0 and instruct_cont_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_cont_5.tStart = t
        instruct_cont_5.frameNStart = frameN  # exact frame index
        instruct_cont_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instruct_cont_5.status == STARTED:
        theseKeys = event.getKeys()
        
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
    for thisComponent in welcome_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_3"-------
for thisComponent in welcome_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "example_scale"-------
t = 0
example_scaleClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
example_scale_1.reset()
# keep track of which components have finished
example_scaleComponents = [practice_image, example_scale_hint, example_scale_1]
for thisComponent in example_scaleComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "example_scale"-------
while continueRoutine:
    # get current time
    t = example_scaleClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_image* updates
    if t >= 0.0 and practice_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        practice_image.tStart = t
        practice_image.frameNStart = frameN  # exact frame index
        practice_image.setAutoDraw(True)
    
    # *example_scale_hint* updates
    if t >= 0.0 and example_scale_hint.status == NOT_STARTED:
        # keep track of start time/frame for later
        example_scale_hint.tStart = t
        example_scale_hint.frameNStart = frameN  # exact frame index
        example_scale_hint.setAutoDraw(True)
    # *example_scale_1* updates
    if t >= 0.0 and example_scale_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        example_scale_1.tStart = t
        example_scale_1.frameNStart = frameN  # exact frame index
        example_scale_1.setAutoDraw(True)
    continueRoutine &= example_scale_1.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "example_scale"-------
for thisComponent in example_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "example_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_4"-------
t = 0
welcome_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruct_cont_6 = event.BuilderKeyResponse()
# keep track of which components have finished
welcome_4Components = [welcome_txt_4, instruct_cont_6]
for thisComponent in welcome_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome_4"-------
while continueRoutine:
    # get current time
    t = welcome_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_txt_4* updates
    if t >= 0.0 and welcome_txt_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_txt_4.tStart = t
        welcome_txt_4.frameNStart = frameN  # exact frame index
        welcome_txt_4.setAutoDraw(True)
    
    # *instruct_cont_6* updates
    if t >= 0.0 and instruct_cont_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_cont_6.tStart = t
        instruct_cont_6.frameNStart = frameN  # exact frame index
        instruct_cont_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instruct_cont_6.status == STARTED:
        theseKeys = event.getKeys()
        
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
    for thisComponent in welcome_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_4"-------
for thisComponent in welcome_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pre_rating_scales_loop = data.TrialHandler(nReps=(0 if expInfo['skip_ratings'] == 'True' else 1), method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ratings.csv'),
    seed=None, name='pre_rating_scales_loop')
thisExp.addLoop(pre_rating_scales_loop)  # add the loop to the experiment
thisPre_rating_scales_loop = pre_rating_scales_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPre_rating_scales_loop.rgb)
if thisPre_rating_scales_loop != None:
    for paramName in thisPre_rating_scales_loop:
        exec('{} = thisPre_rating_scales_loop[paramName]'.format(paramName))

for thisPre_rating_scales_loop in pre_rating_scales_loop:
    currentLoop = pre_rating_scales_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPre_rating_scales_loop.rgb)
    if thisPre_rating_scales_loop != None:
        for paramName in thisPre_rating_scales_loop:
            exec('{} = thisPre_rating_scales_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pre_rating_instruct"-------
    t = 0
    pre_rating_instructClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    from custom_rating_scales import construct_rating_scale
    pre_rating_scale = construct_rating_scale(rating_attribute, low_high=[rating_low, rating_high], win=win)
    
    if not rating_question_details:
        rating_question_details = ''
    pre_rating_instruct_txt.setText(rating_question)
    question_details_txt.setText(rating_question_details)
    pre_rating_instruct_continue = event.BuilderKeyResponse()
    # keep track of which components have finished
    pre_rating_instructComponents = [pre_rating_instruct_common, pre_rating_instruct_txt, question_details_txt, click_to_continue, pre_rating_instruct_continue]
    for thisComponent in pre_rating_instructComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pre_rating_instruct"-------
    while continueRoutine:
        # get current time
        t = pre_rating_instructClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *pre_rating_instruct_common* updates
        if t >= 0.0 and pre_rating_instruct_common.status == NOT_STARTED:
            # keep track of start time/frame for later
            pre_rating_instruct_common.tStart = t
            pre_rating_instruct_common.frameNStart = frameN  # exact frame index
            pre_rating_instruct_common.setAutoDraw(True)
        
        # *pre_rating_instruct_txt* updates
        if t >= 0.0 and pre_rating_instruct_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            pre_rating_instruct_txt.tStart = t
            pre_rating_instruct_txt.frameNStart = frameN  # exact frame index
            pre_rating_instruct_txt.setAutoDraw(True)
        
        # *question_details_txt* updates
        if t >= 0.0 and question_details_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            question_details_txt.tStart = t
            question_details_txt.frameNStart = frameN  # exact frame index
            question_details_txt.setAutoDraw(True)
        
        # *click_to_continue* updates
        if t >= 0.0 and click_to_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            click_to_continue.tStart = t
            click_to_continue.frameNStart = frameN  # exact frame index
            click_to_continue.setAutoDraw(True)
        
        # *pre_rating_instruct_continue* updates
        if t >= 0.0 and pre_rating_instruct_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            pre_rating_instruct_continue.tStart = t
            pre_rating_instruct_continue.frameNStart = frameN  # exact frame index
            pre_rating_instruct_continue.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if pre_rating_instruct_continue.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in pre_rating_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre_rating_instruct"-------
    for thisComponent in pre_rating_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "pre_rating_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    pre_rating_stims_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(stims_file),
        seed=None, name='pre_rating_stims_loop')
    thisExp.addLoop(pre_rating_stims_loop)  # add the loop to the experiment
    thisPre_rating_stims_loop = pre_rating_stims_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPre_rating_stims_loop.rgb)
    if thisPre_rating_stims_loop != None:
        for paramName in thisPre_rating_stims_loop:
            exec('{} = thisPre_rating_stims_loop[paramName]'.format(paramName))
    
    for thisPre_rating_stims_loop in pre_rating_stims_loop:
        currentLoop = pre_rating_stims_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPre_rating_stims_loop.rgb)
        if thisPre_rating_stims_loop != None:
            for paramName in thisPre_rating_stims_loop:
                exec('{} = thisPre_rating_stims_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pre_rating"-------
        t = 0
        pre_ratingClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        pre_rating_img.setImage(stim_file)
        pre_rating_scale.reset()
        
        # keep track of which components have finished
        pre_ratingComponents = [pre_rating_img, pre_rating_scale]
        for thisComponent in pre_ratingComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "pre_rating"-------
        while continueRoutine:
            # get current time
            t = pre_ratingClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pre_rating_img* updates
            if t >= 0.5 and pre_rating_img.status == NOT_STARTED:
                # keep track of start time/frame for later
                pre_rating_img.tStart = t
                pre_rating_img.frameNStart = frameN  # exact frame index
                pre_rating_img.setAutoDraw(True)
            # *pre_rating_scale* updates
            if t >= 0.5 and pre_rating_scale.status == NOT_STARTED:
                # keep track of start time/frame for later
                pre_rating_scale.tStart = t
                pre_rating_scale.frameNStart = frameN  # exact frame index
                pre_rating_scale.setAutoDraw(True)
            continueRoutine &= pre_rating_scale.noResponse  # a response ends the trial
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pre_ratingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pre_rating"-------
        for thisComponent in pre_ratingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for pre_rating_stims_loop (TrialHandler)
        pre_rating_stims_loop.addData('pre_rating_scale.response', pre_rating_scale.getRating())
        pre_rating_stims_loop.addData('pre_rating_scale.rt', pre_rating_scale.getRT())
        rating_df.loc[stim_file, rating_attribute] = pre_rating_scale.getRating()
        # the Routine "pre_rating" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'pre_rating_stims_loop'
    
    
    # ------Prepare to start Routine "pause_rating"-------
    t = 0
    pause_ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    pause_rating_response = event.BuilderKeyResponse()
    # keep track of which components have finished
    pause_ratingComponents = [pause_rating_text, pause_rating_response]
    for thisComponent in pause_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pause_rating"-------
    while continueRoutine:
        # get current time
        t = pause_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pause_rating_text* updates
        if t >= 0.0 and pause_rating_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            pause_rating_text.tStart = t
            pause_rating_text.frameNStart = frameN  # exact frame index
            pause_rating_text.setAutoDraw(True)
        
        # *pause_rating_response* updates
        if t >= 0.0 and pause_rating_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            pause_rating_response.tStart = t
            pause_rating_response.frameNStart = frameN  # exact frame index
            pause_rating_response.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if pause_rating_response.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in pause_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause_rating"-------
    for thisComponent in pause_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pause_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed (0 if expInfo['skip_ratings'] == 'True' else 1) repeats of 'pre_rating_scales_loop'


# ------Prepare to start Routine "select_faces"-------
t = 0
select_facesClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
import os
import os.path as op
import pandas as pd
import shutil
import yaml
from glob import glob
from face_selection import select_stim_based_on_similarity

rating_df.to_csv(op.join(sub_dir, 'sub-%s_face-ratings.csv' % sub_nr))

if expInfo['skip_ratings']:
    print("Trying to find existing ratings for subject %s" % sub_nr)
    rating_df = pd.read_csv(op.join('test_data', 'sub-%s_face-ratings.csv' % sub_nr))

    if sys.platform[:3] == 'win':
        rating_df.stim_file = rating_df.stim_file.str.replace('/', '\\')

selected_pairs = select_stim_based_on_similarity(rating_df, face_gender=face_gender,
                                                 distance_metric=custom_params['distance_metric'])
reward_prob = [[['80', '20'], ['64', '36']], [['80', '20'], ['64', '36']]]

session_df = dict(stim_csv=[], trial_csv=[], RL_wrong_instruction=[],
                  RL_wrong_instruction_n=[], feedback_txt_incorrect=[],
                  RL_session_notice=[], session_name=[])
for i, this_RL_session in enumerate(RL_order.split('_')):

    learning_template = pd.read_csv('learning_template.csv')
    testing_template = pd.read_csv('testing_template.csv')

    # Loop over stimuli (4 faces for this session)
    stim_df = dict(stim_file=[], reward_prob=[])
    for ii, this_pair in enumerate(selected_pairs[i]):

        for iii, this_stim in enumerate(this_pair):
            this_reward_prob = reward_prob[i][ii][iii]
            orig_name = op.basename(this_stim).split('.')[0]
            new_name = '%s_rewardprob-%s_session-%s.png' % (orig_name, this_reward_prob, this_RL_session)
            new_file = op.join(sub_dir, new_name)
            shutil.copy(this_stim, new_file)

            stim_df['stim_file'].append(new_file)
            stim_df['reward_prob'].append(this_reward_prob)

            learning_template = learning_template.replace('rewardprob-%s' % this_reward_prob, new_file)
            testing_template = testing_template.replace('rewardprob-%s' % this_reward_prob, new_file)

    stim_df = pd.DataFrame(stim_df)
    stim_file = op.join(sub_dir, 'stims_session-%s.csv' % this_RL_session)
    stim_df.to_csv(stim_file, index=False)

    learning_file = op.join(sub_dir, 'trials_phase-learning_session-%s.csv' % this_RL_session)
    learning_template.to_csv(learning_file, index=False)
    testing_file = op.join(sub_dir, 'trials_phase-testing_session-%s.csv' % this_RL_session)
    testing_template.to_csv(testing_file, index=False)
    session_df['trial_csv'].append(learning_file)
    session_df['stim_csv'].append(stim_file)
    session_df['session_name'].append(this_RL_session)

    if this_RL_session == 'plusmin':
        session_df['RL_wrong_instruction'].append('VERLIES je %.1f euro.' % custom_params['RL_params']['lose_amount'])
        session_df['RL_wrong_instruction_n'].append('gestraft wordt, doordat je %.1f euro verliest.' % custom_params['RL_params']['lose_amount'])
        session_df['feedback_txt_incorrect'].append('(%.1f euro verloren)' % custom_params['RL_params']['lose_amount'])
    else:
        session_df['RL_wrong_instruction'].append('win je niks.')
        session_df['RL_wrong_instruction_n'].append('dat je niks wint.')
        session_df['feedback_txt_incorrect'].append('(0 euro gewonnen)')

    if i == 0:
        session_df['RL_session_notice'].append(' ')
    elif i == 1 and this_RL_session == 'plusmin':
        session_df['RL_session_notice'].append("Let op: in de eerste sessie won je niks als je keus fout was, "
                                               "maar in deze sessie VERLIES je %.1f euro als je het fout hebt!" % custom_params['RL_params']['lose_amount'])
    elif i == 1 and this_RL_session == 'plusneu':
        session_df['RL_session_notice'].append("Let op: in de eerste sessie verloor je %.1f euro als je keus fout was, "
                                               "maar in deze sessie win/verlies je NIKS als je het fout hebt!" % custom_params['RL_params']['lose_amount'])

session_df['number_str'] = ['eerste', 'tweede']
session_df['practice_reps'] = [1, 0]
session_df = pd.DataFrame(session_df)
session_file = op.join(sub_dir, 'sessions_phase-learning.csv')
session_df.to_csv(session_file, index=False)

# Check sequence
if RL_order == 'plusmin_plusneu':
    pass
elif RL_order == 'plusneu_plusmin':
    pass
else:
    raise ValueError("Cannot determine RL_order (should be 'plusmin_plusneu' or 'plusneu_plusmin')!") 
# keep track of which components have finished
select_facesComponents = []
for thisComponent in select_facesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "select_faces"-------
while continueRoutine:
    # get current time
    t = select_facesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in select_facesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "select_faces"-------
for thisComponent in select_facesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "select_faces" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
session_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(session_file),
    seed=None, name='session_loop')
thisExp.addLoop(session_loop)  # add the loop to the experiment
thisSession_loop = session_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSession_loop.rgb)
if thisSession_loop != None:
    for paramName in thisSession_loop:
        exec('{} = thisSession_loop[paramName]'.format(paramName))

for thisSession_loop in session_loop:
    currentLoop = session_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSession_loop.rgb)
    if thisSession_loop != None:
        for paramName in thisSession_loop:
            exec('{} = thisSession_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instruct_RL_1"-------
    t = 0
    instruct_RL_1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if number_str == 'eerste':
        practice_skip_txt_1 = """
    Dit is het begin van fase 2, waarin je een leer-taakje gaat doen.
    
    Deze taak zullen we uitgebreid uitleggen en 
    die zal je eerst even oefenen voordat je
    gaat beginnen aan de echte taak.
    
    (Druk op een willekeurig toets om verder te gaan.)
    """
    else:
        practice_skip_txt_1 = """
    Nu ga je wederom een leer-taakje doen,
    maar net iets anders dan in de eerste sessie.
    
    (Druk op een willekeurig toets om verder te gaan.)
    """
    
    instruct_RL_1_txt.setText(practice_skip_txt_1)
    instruct_RL_1_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    instruct_RL_1Components = [instruct_RL_1_txt, instruct_RL_1_resp]
    for thisComponent in instruct_RL_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instruct_RL_1"-------
    while continueRoutine:
        # get current time
        t = instruct_RL_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *instruct_RL_1_txt* updates
        if t >= 0.0 and instruct_RL_1_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_1_txt.tStart = t
            instruct_RL_1_txt.frameNStart = frameN  # exact frame index
            instruct_RL_1_txt.setAutoDraw(True)
        
        # *instruct_RL_1_resp* updates
        if t >= 0.0 and instruct_RL_1_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_1_resp.tStart = t
            instruct_RL_1_resp.frameNStart = frameN  # exact frame index
            instruct_RL_1_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instruct_RL_1_resp.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in instruct_RL_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct_RL_1"-------
    for thisComponent in instruct_RL_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instruct_RL_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruct_RL_2"-------
    t = 0
    instruct_RL_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instruct_RL_2_txt_3.setText('Tijdens deze taak zie je steeds twee gezichten tegelijkertijd.\nEén van de gezichten is steeds ‘correct’ en de andere ‘incorrect’.\nIn het begin zul je niet weten welke van de twee gezichten ‘correct’\nof ‘incorrect’ is.\n\nProbeer steeds zo accuraat mogelijk te raden welke van de twee\ngezichten ‘correct’ is, door deze met links ("F" toets)\nof rechts ("J" toets) te selecteren.\n\n(Druk op een willekeurige knop om verder te gaan.)')
    instruct_RL_2_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instruct_RL_2Components = [instruct_RL_2_txt_3, instruct_RL_2_resp_2]
    for thisComponent in instruct_RL_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instruct_RL_2"-------
    while continueRoutine:
        # get current time
        t = instruct_RL_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_RL_2_txt_3* updates
        if t >= 0.0 and instruct_RL_2_txt_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_2_txt_3.tStart = t
            instruct_RL_2_txt_3.frameNStart = frameN  # exact frame index
            instruct_RL_2_txt_3.setAutoDraw(True)
        
        # *instruct_RL_2_resp_2* updates
        if t >= 0.0 and instruct_RL_2_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_2_resp_2.tStart = t
            instruct_RL_2_resp_2.frameNStart = frameN  # exact frame index
            instruct_RL_2_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instruct_RL_2_resp_2.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in instruct_RL_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct_RL_2"-------
    for thisComponent in instruct_RL_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instruct_RL_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruct_RL_2_1"-------
    t = 0
    instruct_RL_2_1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instruct_RL_2_txt_4.setText("Let op! Er bestaan geen absoluut ‘correcte’ antwoorden,\nmaar sommige gezichten hebben een hogere kans om gevolgd\nte worden door een ‘correct’ feedback (groen plus-symbool).\n\nProbeer steeds het gezicht te selecteren met het hoogste\nkans op de 'correct' feedback.\n\nJe hebt 3 seconden om te kiezen.\n\n(Druk op een willekeurige knop om verder te gaan.)")
    instruct_RL_2_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instruct_RL_2_1Components = [instruct_RL_2_txt_4, instruct_RL_2_resp_3]
    for thisComponent in instruct_RL_2_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instruct_RL_2_1"-------
    while continueRoutine:
        # get current time
        t = instruct_RL_2_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_RL_2_txt_4* updates
        if t >= 0.0 and instruct_RL_2_txt_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_2_txt_4.tStart = t
            instruct_RL_2_txt_4.frameNStart = frameN  # exact frame index
            instruct_RL_2_txt_4.setAutoDraw(True)
        
        # *instruct_RL_2_resp_3* updates
        if t >= 0.0 and instruct_RL_2_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_2_resp_3.tStart = t
            instruct_RL_2_resp_3.frameNStart = frameN  # exact frame index
            instruct_RL_2_resp_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instruct_RL_2_resp_3.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in instruct_RL_2_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct_RL_2_1"-------
    for thisComponent in instruct_RL_2_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instruct_RL_2_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruct_RL_2_2"-------
    t = 0
    instruct_RL_2_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instruct_RL_2_txt.setText("""
Na je keuze krijg je direct feedback op je keuze.
Als je keuze 'correct' is, dan zie je een groen plus teken (+)
en WIN je %.1f euro.

Als je keuze 'incorrect' is, dan zie je een rood kruis (x)
en %s

(Druk op een willekeurige toets om verder te gaan.)
""" % (custom_params['RL_params']['win_amount'], RL_wrong_instruction))
    instruct_RL_2_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    instruct_RL_2_2Components = [instruct_RL_2_txt, instruct_RL_2_resp]
    for thisComponent in instruct_RL_2_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instruct_RL_2_2"-------
    while continueRoutine:
        # get current time
        t = instruct_RL_2_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_RL_2_txt* updates
        if t >= 0.0 and instruct_RL_2_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_2_txt.tStart = t
            instruct_RL_2_txt.frameNStart = frameN  # exact frame index
            instruct_RL_2_txt.setAutoDraw(True)
        
        # *instruct_RL_2_resp* updates
        if t >= 0.0 and instruct_RL_2_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_2_resp.tStart = t
            instruct_RL_2_resp.frameNStart = frameN  # exact frame index
            instruct_RL_2_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instruct_RL_2_resp.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in instruct_RL_2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct_RL_2_2"-------
    for thisComponent in instruct_RL_2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instruct_RL_2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruct_RL_3"-------
    t = 0
    instruct_RL_3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if number_str == 'tweede':
        continueRoutine = False
    instruct_RL_3_txt.setText("""
Je begint met %i euro, maar dit bedrag kan je dus opbouwen
door te leren welke gezichten gekoppeld zijn met een hogere
kans op beloning. Het gemiddelde bedrag dat je verdient tijdens
de twee sessies mag je ook daadwerkelijk mee naar huis nemen
(afgerond op de hele euro)!

%s

(Druk op een willekeurige toets om verder te gaan.)
""" % (custom_params['RL_params']['start_amount'], RL_session_notice))
    instruct_RL_3_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    instruct_RL_3Components = [instruct_RL_3_txt, instruct_RL_3_resp]
    for thisComponent in instruct_RL_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instruct_RL_3"-------
    while continueRoutine:
        # get current time
        t = instruct_RL_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *instruct_RL_3_txt* updates
        if t >= 0.0 and instruct_RL_3_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_3_txt.tStart = t
            instruct_RL_3_txt.frameNStart = frameN  # exact frame index
            instruct_RL_3_txt.setAutoDraw(True)
        
        # *instruct_RL_3_resp* updates
        if t >= 0.0 and instruct_RL_3_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_3_resp.tStart = t
            instruct_RL_3_resp.frameNStart = frameN  # exact frame index
            instruct_RL_3_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instruct_RL_3_resp.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in instruct_RL_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct_RL_3"-------
    for thisComponent in instruct_RL_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instruct_RL_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruct_RL_5"-------
    t = 0
    instruct_RL_5Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if number_str == 'eerste':
        practice_skip_txt = """
    Om het nog iets moeilijker te maken, krijg je straks
    niet één combinatie van 2 gezichten, maar TWEE combinaties
    van 2 gezichten! Je moet dus van iedere combinatie proberen
    te leren welke van de twee het meest "waardevolle" gezicht is!
    
    Om te checken of je het snapt, ga je dit leer-taakje even oefenen.
    Je krijg twee combinaties van gezichten te zien:
    
    1. Barack Obama vs. Bill Clinton,
    2. Donald Trump vs. George Bush
    
    De oefenfase duurt ongeveer 5 minuutjes. Ter herinnering:
    
    Om het LINKER gezicht te kiezen, druk op de F toets.
    Om het RECHTER gezicht te kiezen, druk op de J toets.
    
    (Druk op een willekeurige knop om te beginnen met de oefenronde!)
    """
        practice_reps = 1
    else:
        practice_skip_txt = """We slaan de oefenronde deze keer over.
    
    (Druk op een willekeurige toets om verder te gaan.)"""
        practice_reps = 0
    
    if expInfo['skip_practice'] == 'True':
        practice_reps = 0
    instruct_RL_5_txt.setText(practice_skip_txt)
    instruct_RL_5_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    instruct_RL_5Components = [instruct_RL_5_txt, instruct_RL_5_resp]
    for thisComponent in instruct_RL_5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instruct_RL_5"-------
    while continueRoutine:
        # get current time
        t = instruct_RL_5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *instruct_RL_5_txt* updates
        if t >= 0.0 and instruct_RL_5_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_5_txt.tStart = t
            instruct_RL_5_txt.frameNStart = frameN  # exact frame index
            instruct_RL_5_txt.setAutoDraw(True)
        
        # *instruct_RL_5_resp* updates
        if t >= 0.0 and instruct_RL_5_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruct_RL_5_resp.tStart = t
            instruct_RL_5_resp.frameNStart = frameN  # exact frame index
            instruct_RL_5_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instruct_RL_5_resp.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in instruct_RL_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct_RL_5"-------
    for thisComponent in instruct_RL_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instruct_RL_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pre_fix"-------
    t = 0
    pre_fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if number_str == 'tweede':
        continueRoutine = False
    # keep track of which components have finished
    pre_fixComponents = [pre_fix_icon]
    for thisComponent in pre_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pre_fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pre_fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *pre_fix_icon* updates
        if t >= 0.0 and pre_fix_icon.status == NOT_STARTED:
            # keep track of start time/frame for later
            pre_fix_icon.tStart = t
            pre_fix_icon.frameNStart = frameN  # exact frame index
            pre_fix_icon.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if pre_fix_icon.status == STARTED and t >= frameRemains:
            pre_fix_icon.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre_fix"-------
    for thisComponent in pre_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # set up handler to look after randomisation of conditions etc
    practice_trials = data.TrialHandler(nReps=practice_reps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('practice_trials.csv'),
        seed=None, name='practice_trials')
    thisExp.addLoop(practice_trials)  # add the loop to the experiment
    thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    for thisPractice_trial in practice_trials:
        currentLoop = practice_trials
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                exec('{} = thisPractice_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice_RL_trial"-------
        t = 0
        practice_RL_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        
        practice_left_face.setImage(left_face)
        practice_right_face.setImage(right_face)
        practice_response = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        practice_RL_trialComponents = [practice_left_face, practice_right_face, practice_response_prompt, practice_response, fix_practice]
        for thisComponent in practice_RL_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practice_RL_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practice_RL_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *practice_left_face* updates
            if t >= 1 and practice_left_face.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_left_face.tStart = t
                practice_left_face.frameNStart = frameN  # exact frame index
                practice_left_face.setAutoDraw(True)
            frameRemains = 1 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_left_face.status == STARTED and t >= frameRemains:
                practice_left_face.setAutoDraw(False)
            
            # *practice_right_face* updates
            if t >= 1 and practice_right_face.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_right_face.tStart = t
                practice_right_face.frameNStart = frameN  # exact frame index
                practice_right_face.setAutoDraw(True)
            frameRemains = 1 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_right_face.status == STARTED and t >= frameRemains:
                practice_right_face.setAutoDraw(False)
            
            # *practice_response_prompt* updates
            if t >= 1 and practice_response_prompt.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_response_prompt.tStart = t
                practice_response_prompt.frameNStart = frameN  # exact frame index
                practice_response_prompt.setAutoDraw(True)
            frameRemains = 1 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_response_prompt.status == STARTED and t >= frameRemains:
                practice_response_prompt.setAutoDraw(False)
            
            # *practice_response* updates
            if t >= 1 and practice_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_response.tStart = t
                practice_response.frameNStart = frameN  # exact frame index
                practice_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(practice_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 1 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_response.status == STARTED and t >= frameRemains:
                practice_response.status = STOPPED
            if practice_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    practice_response.keys = theseKeys[-1]  # just the last key pressed
                    practice_response.rt = practice_response.clock.getTime()
                    # was this 'correct'?
                    if (practice_response.keys == str(rewarded_resp)) or (practice_response.keys == rewarded_resp):
                        practice_response.corr = 1
                    else:
                        practice_response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *fix_practice* updates
            if t >= 0 and fix_practice.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix_practice.tStart = t
                fix_practice.frameNStart = frameN  # exact frame index
                fix_practice.setAutoDraw(True)
            frameRemains = 0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fix_practice.status == STARTED and t >= frameRemains:
                fix_practice.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_RL_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_RL_trial"-------
        for thisComponent in practice_RL_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if practice_response.keys in (None, []):
            feedback_txt = 'Too slow!'
            feedback_color = 'White'
            feedback_sign_opacity = 0
        elif practice_response.corr:
            feedback_txt = '(%.1f euro gewonnen)' % custom_params['RL_params']['win_amount']
            feedback_ori = 0
            feedback_color = 'Green'
            feedback_sign_opacity = 1
        elif not practice_response.corr:
            feedback_txt = feedback_txt_incorrect
            feedback_ori = 45
            feedback_color = 'Red'
            feedback_sign_opacity = 1
        
        # check responses
        if practice_response.keys in ['', [], None]:  # No response was made
            practice_response.keys=None
            # was no response the correct answer?!
            if str(rewarded_resp).lower() == 'none':
               practice_response.corr = 1  # correct non-response
            else:
               practice_response.corr = 0  # failed to respond (incorrectly)
        # store data for practice_trials (TrialHandler)
        practice_trials.addData('practice_response.keys',practice_response.keys)
        practice_trials.addData('practice_response.corr', practice_response.corr)
        if practice_response.keys != None:  # we had a response
            practice_trials.addData('practice_response.rt', practice_response.rt)
        if practice_response.keys in (None, []):
            practice_money += 0
        else:
            if practice_response.corr:
                practice_money += custom_params['RL_params']['win_amount']
            else:
                if session_name == 'plusneu':
                    practice_money += 0
                elif session_name == 'plusmin':
                    practice_money -= custom_params['RL_params']['lose_amount']
            
        
        # ------Prepare to start Routine "practice_RL_feedback"-------
        t = 0
        practice_RL_feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        practice_feedback_sign.setOpacity(feedback_sign_opacity)
        practice_feedback_sign.setOri(feedback_ori)
        practice_feedback_sign.setFillColor(feedback_color)
        practice_feedback_sign.setLineColor(feedback_color)
        practice_feedback_written_txt.setColor(feedback_color, colorSpace='rgb')
        practice_feedback_written_txt.setText(feedback_txt)
        # keep track of which components have finished
        practice_RL_feedbackComponents = [practice_feedback_sign, practice_feedback_written_txt]
        for thisComponent in practice_RL_feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practice_RL_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practice_RL_feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_feedback_sign* updates
            if t >= 0.0 and practice_feedback_sign.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_feedback_sign.tStart = t
                practice_feedback_sign.frameNStart = frameN  # exact frame index
                practice_feedback_sign.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_feedback_sign.status == STARTED and t >= frameRemains:
                practice_feedback_sign.setAutoDraw(False)
            
            # *practice_feedback_written_txt* updates
            if t >= 0.0 and practice_feedback_written_txt.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_feedback_written_txt.tStart = t
                practice_feedback_written_txt.frameNStart = frameN  # exact frame index
                practice_feedback_written_txt.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_feedback_written_txt.status == STARTED and t >= frameRemains:
                practice_feedback_written_txt.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_RL_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_RL_feedback"-------
        for thisComponent in practice_RL_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed practice_reps repeats of 'practice_trials'
    
    
    # ------Prepare to start Routine "begin_real_RL"-------
    t = 0
    begin_real_RLClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if number_str == 'eerste':
        practice_skip_txt_3 = """
    Dit was de oefentaak. Je begon met %i euro,
    maar je bent geeindigd met %.1f euro!
    
    Zoals je misschien wel gemerkt (geleerd)
    hebt, was Obama meer "waardevol" dan Clinton en
    was Bush meer "waardevol" dan Trump.
    
    Is alles duidelijk?
    Zo niet, laat de proefleider dit dan weten!
    
    (Druk op een willekeurige toets om verder te gaan.)""" % (custom_params['RL_params']['start_amount'], practice_money)
    else:
        if session_name == 'plusmin':
            tmp_txt = '%.1f euro VERLIEST' % custom_params['RL_params']['lose_amount']
        else:
            tmp_txt = 'GEEN geld verliest'
    
        practice_skip_txt_3 = """
    Ter herinnering: het enige verschil met de eerste sessie is
    dat je deze keer %s bij een fout antwoord!
    
    (Druk op een willekeurige toets om te beginnen met de taak!)
    """ % tmp_txt
    with open(rewards_file, 'a') as rewards_file_f:
        rewards_file_f.write('Practice rewards: %.1f\n' % practice_money)
        
    begin_real_RL_txt.setText(practice_skip_txt_3)
    begin_real_RL_continue = event.BuilderKeyResponse()
    # keep track of which components have finished
    begin_real_RLComponents = [begin_real_RL_txt, begin_real_RL_continue]
    for thisComponent in begin_real_RLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "begin_real_RL"-------
    while continueRoutine:
        # get current time
        t = begin_real_RLClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        
        # *begin_real_RL_txt* updates
        if t >= 0.0 and begin_real_RL_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin_real_RL_txt.tStart = t
            begin_real_RL_txt.frameNStart = frameN  # exact frame index
            begin_real_RL_txt.setAutoDraw(True)
        
        # *begin_real_RL_continue* updates
        if t >= 0.0 and begin_real_RL_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin_real_RL_continue.tStart = t
            begin_real_RL_continue.frameNStart = frameN  # exact frame index
            begin_real_RL_continue.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if begin_real_RL_continue.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in begin_real_RLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "begin_real_RL"-------
    for thisComponent in begin_real_RLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # the Routine "begin_real_RL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "begin_real_RL2"-------
    t = 0
    begin_real_RL2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if number_str == 'eerste':
    
        practice_skip_txt_4 = """
    Als alles duidelijk is, dan kan je beginnen met de echte leer-taak!
    
    In plaats van Amerikaanse (ex)presidenten, krijg je nu dezelfde
    gezichten te zien als die je beoordeeld hebt in de vorige fase.
    In totaal krijg je TWEE combinaties van 2 gezichten.
    
    In tegenstelling tot bij de oefentaak, telt het bedrag dat je
    hierbij verdiend WEL mee voor het uiteindelijke bedrag dat je
    mee naar huis mag nemen.
    
    Let op, de echte leer-taak duurt ongeveer 10-15 minuten (met pauzes tussendoor).
    Succes!
    
    (Druk op een toets om te beginnen met de echte taak.)
    """
    else:
        continueRoutine = False
    begin_real_RL_txt_2.setText(practice_skip_txt_4)
    begin_real_RL_continue_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    begin_real_RL2Components = [begin_real_RL_txt_2, begin_real_RL_continue_2]
    for thisComponent in begin_real_RL2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "begin_real_RL2"-------
    while continueRoutine:
        # get current time
        t = begin_real_RL2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *begin_real_RL_txt_2* updates
        if t >= 0.0 and begin_real_RL_txt_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin_real_RL_txt_2.tStart = t
            begin_real_RL_txt_2.frameNStart = frameN  # exact frame index
            begin_real_RL_txt_2.setAutoDraw(True)
        
        # *begin_real_RL_continue_2* updates
        if t >= 0.0 and begin_real_RL_continue_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin_real_RL_continue_2.tStart = t
            begin_real_RL_continue_2.frameNStart = frameN  # exact frame index
            begin_real_RL_continue_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if begin_real_RL_continue_2.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in begin_real_RL2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "begin_real_RL2"-------
    for thisComponent in begin_real_RL2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "begin_real_RL2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pre_fix_2"-------
    t = 0
    pre_fix_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pre_fix_2Components = [pre_fix_icon2]
    for thisComponent in pre_fix_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pre_fix_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pre_fix_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pre_fix_icon2* updates
        if t >= 0.0 and pre_fix_icon2.status == NOT_STARTED:
            # keep track of start time/frame for later
            pre_fix_icon2.tStart = t
            pre_fix_icon2.frameNStart = frameN  # exact frame index
            pre_fix_icon2.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if pre_fix_icon2.status == STARTED and t >= frameRemains:
            pre_fix_icon2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_fix_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre_fix_2"-------
    for thisComponent in pre_fix_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    real_trials = data.TrialHandler(nReps=(int(n_trials / 50)), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(trial_csv),
        seed=None, name='real_trials')
    thisExp.addLoop(real_trials)  # add the loop to the experiment
    thisReal_trial = real_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReal_trial.rgb)
    if thisReal_trial != None:
        for paramName in thisReal_trial:
            exec('{} = thisReal_trial[paramName]'.format(paramName))
    
    for thisReal_trial in real_trials:
        currentLoop = real_trials
        # abbreviate parameter names if possible (e.g. rgb = thisReal_trial.rgb)
        if thisReal_trial != None:
            for paramName in thisReal_trial:
                exec('{} = thisReal_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "real_RL_trial"-------
        t = 0
        real_RL_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        
        real_left_face.setImage(left_face)
        real_right_face.setImage(right_face)
        real_RL_response = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        real_RL_trialComponents = [real_left_face, real_right_face, real_RL_response, fix_real]
        for thisComponent in real_RL_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "real_RL_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = real_RL_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *real_left_face* updates
            if t >= 1 and real_left_face.status == NOT_STARTED:
                # keep track of start time/frame for later
                real_left_face.tStart = t
                real_left_face.frameNStart = frameN  # exact frame index
                real_left_face.setAutoDraw(True)
            frameRemains = 1 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if real_left_face.status == STARTED and t >= frameRemains:
                real_left_face.setAutoDraw(False)
            
            # *real_right_face* updates
            if t >= 1 and real_right_face.status == NOT_STARTED:
                # keep track of start time/frame for later
                real_right_face.tStart = t
                real_right_face.frameNStart = frameN  # exact frame index
                real_right_face.setAutoDraw(True)
            frameRemains = 1 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if real_right_face.status == STARTED and t >= frameRemains:
                real_right_face.setAutoDraw(False)
            
            # *real_RL_response* updates
            if t >= 1 and real_RL_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                real_RL_response.tStart = t
                real_RL_response.frameNStart = frameN  # exact frame index
                real_RL_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(real_RL_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 1 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if real_RL_response.status == STARTED and t >= frameRemains:
                real_RL_response.status = STOPPED
            if real_RL_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    real_RL_response.keys = theseKeys[-1]  # just the last key pressed
                    real_RL_response.rt = real_RL_response.clock.getTime()
                    # was this 'correct'?
                    if (real_RL_response.keys == str(rewarded_resp)) or (real_RL_response.keys == rewarded_resp):
                        real_RL_response.corr = 1
                    else:
                        real_RL_response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *fix_real* updates
            if t >= 0 and fix_real.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix_real.tStart = t
                fix_real.frameNStart = frameN  # exact frame index
                fix_real.setAutoDraw(True)
            frameRemains = 0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fix_real.status == STARTED and t >= frameRemains:
                fix_real.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in real_RL_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "real_RL_trial"-------
        for thisComponent in real_RL_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if real_RL_response.keys in (None, []):
            feedback_txt = 'Too slow!'
            feedback_color = 'White'
            feedback_sign_opacity = 0
        elif real_RL_response.corr:
            feedback_txt = '(%.1f euro gewonnen)' % custom_params['RL_params']['win_amount']
            feedback_ori = 0
            feedback_color = 'Green'
            feedback_sign_opacity = 1
        elif not real_RL_response.corr:
            feedback_txt = feedback_txt_incorrect
            feedback_ori = 45
            feedback_color = 'Red'
            feedback_sign_opacity = 1
        
        # check responses
        if real_RL_response.keys in ['', [], None]:  # No response was made
            real_RL_response.keys=None
            # was no response the correct answer?!
            if str(rewarded_resp).lower() == 'none':
               real_RL_response.corr = 1  # correct non-response
            else:
               real_RL_response.corr = 0  # failed to respond (incorrectly)
        # store data for real_trials (TrialHandler)
        real_trials.addData('real_RL_response.keys',real_RL_response.keys)
        real_trials.addData('real_RL_response.corr', real_RL_response.corr)
        if real_RL_response.keys != None:  # we had a response
            real_trials.addData('real_RL_response.rt', real_RL_response.rt)
        if real_RL_response.corr in (None, []):
            real_money[session_name] += 0
        else:
            if real_RL_response.corr:
                real_money[session_name] += custom_params['RL_params']['win_amount']
            else:
                if session_name == 'plusneu':
                    real_money[session_name] += 0
                elif session_name == 'plusmin':
                    real_money[session_name] -= custom_params['RL_params']['lose_amount']
        
        # ------Prepare to start Routine "real_RL_feedback"-------
        t = 0
        real_RL_feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        real_feedback_sign.setOpacity(feedback_sign_opacity)
        real_feedback_sign.setOri(feedback_ori)
        real_feedback_sign.setFillColor(feedback_color)
        real_feedback_sign.setLineColor(feedback_color)
        real_feedback_written_txt.setColor(feedback_color, colorSpace='rgb')
        real_feedback_written_txt.setText(feedback_txt)
        # keep track of which components have finished
        real_RL_feedbackComponents = [real_feedback_sign, real_feedback_written_txt]
        for thisComponent in real_RL_feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "real_RL_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = real_RL_feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *real_feedback_sign* updates
            if t >= 0 and real_feedback_sign.status == NOT_STARTED:
                # keep track of start time/frame for later
                real_feedback_sign.tStart = t
                real_feedback_sign.frameNStart = frameN  # exact frame index
                real_feedback_sign.setAutoDraw(True)
            frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if real_feedback_sign.status == STARTED and t >= frameRemains:
                real_feedback_sign.setAutoDraw(False)
            
            # *real_feedback_written_txt* updates
            if t >= 0 and real_feedback_written_txt.status == NOT_STARTED:
                # keep track of start time/frame for later
                real_feedback_written_txt.tStart = t
                real_feedback_written_txt.frameNStart = frameN  # exact frame index
                real_feedback_written_txt.setAutoDraw(True)
            frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if real_feedback_written_txt.status == STARTED and t >= frameRemains:
                real_feedback_written_txt.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in real_RL_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "real_RL_feedback"-------
        for thisComponent in real_RL_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "pause_RL"-------
        t = 0
        pause_RLClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if (real_trials.thisN + 1) % 34 != 0:
            continueRoutine = False
        pause_txt.setText("""Je kan even pauze nemen als je wilt!
Het bedrag dat je deze sessie tot nu toe hebt verdiend: %.1f euro

(Druk op een toets om weer verder te gaan.)""" % real_money[session_name])
        key_resp_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        pause_RLComponents = [pause_txt, key_resp_2]
        for thisComponent in pause_RLComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "pause_RL"-------
        while continueRoutine:
            # get current time
            t = pause_RLClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *pause_txt* updates
            if t >= 0.0 and pause_txt.status == NOT_STARTED:
                # keep track of start time/frame for later
                pause_txt.tStart = t
                pause_txt.frameNStart = frameN  # exact frame index
                pause_txt.setAutoDraw(True)
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys()
                
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
            for thisComponent in pause_RLComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pause_RL"-------
        for thisComponent in pause_RLComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "pause_RL" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed (int(n_trials / 50)) repeats of 'real_trials'
    
    
    # ------Prepare to start Routine "overview_money"-------
    t = 0
    overview_moneyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    overview_money_txt.setText("""Deze sessie heb je in totaal %.1f euro verdiend!

(Druk op een toets om door te gaan.)
""" % real_money[session_name]
)
    overview_money_resp = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    overview_moneyComponents = [overview_money_txt, overview_money_resp]
    for thisComponent in overview_moneyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "overview_money"-------
    while continueRoutine:
        # get current time
        t = overview_moneyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *overview_money_txt* updates
        if t >= 0.0 and overview_money_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            overview_money_txt.tStart = t
            overview_money_txt.frameNStart = frameN  # exact frame index
            overview_money_txt.setAutoDraw(True)
        
        # *overview_money_resp* updates
        if t >= 0.0 and overview_money_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            overview_money_resp.tStart = t
            overview_money_resp.frameNStart = frameN  # exact frame index
            overview_money_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if overview_money_resp.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in overview_moneyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "overview_money"-------
    for thisComponent in overview_moneyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    with open(rewards_file, 'a') as rewards_file_f:
        rewards_file_f.write('%s rewards: %.1f\n' % (session_name, real_money[session_name]))
        
    # the Routine "overview_money" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "post_rating_intro"-------
    t = 0
    post_rating_introClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    post_rating_intro_txt.setText('Nu ga je weer de gezichten beoordelen, zoals in fase 1.\n\n(Druk op een willekeurige knop om te beginnen.)')
    post_rating_intro_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    post_rating_introComponents = [post_rating_intro_txt, post_rating_intro_resp]
    for thisComponent in post_rating_introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "post_rating_intro"-------
    while continueRoutine:
        # get current time
        t = post_rating_introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *post_rating_intro_txt* updates
        if t >= 0.0 and post_rating_intro_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            post_rating_intro_txt.tStart = t
            post_rating_intro_txt.frameNStart = frameN  # exact frame index
            post_rating_intro_txt.setAutoDraw(True)
        
        # *post_rating_intro_resp* updates
        if t >= 0.0 and post_rating_intro_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            post_rating_intro_resp.tStart = t
            post_rating_intro_resp.frameNStart = frameN  # exact frame index
            post_rating_intro_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if post_rating_intro_resp.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in post_rating_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "post_rating_intro"-------
    for thisComponent in post_rating_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "post_rating_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    post_rating_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ratings.csv'),
        seed=None, name='post_rating_loop')
    thisExp.addLoop(post_rating_loop)  # add the loop to the experiment
    thisPost_rating_loop = post_rating_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPost_rating_loop.rgb)
    if thisPost_rating_loop != None:
        for paramName in thisPost_rating_loop:
            exec('{} = thisPost_rating_loop[paramName]'.format(paramName))
    
    for thisPost_rating_loop in post_rating_loop:
        currentLoop = post_rating_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPost_rating_loop.rgb)
        if thisPost_rating_loop != None:
            for paramName in thisPost_rating_loop:
                exec('{} = thisPost_rating_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "post_rating_instruct"-------
        t = 0
        post_rating_instructClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        from custom_rating_scales import construct_rating_scale
        post_rating_scale = construct_rating_scale(rating_attribute, low_high=[rating_low, rating_high], win=win)
        
        if not rating_question_details:
            rating_question_details = ''
        pre_rating_instruct_txt_2.setText(rating_question)
        rating_press_to_continue_2.setText(rating_question_details)
        post_rating_instruct_continue = event.BuilderKeyResponse()
        # keep track of which components have finished
        post_rating_instructComponents = [post_rating_instruct_common, pre_rating_instruct_txt_2, rating_press_to_continue_2, click_to_continue_2, post_rating_instruct_continue]
        for thisComponent in post_rating_instructComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "post_rating_instruct"-------
        while continueRoutine:
            # get current time
            t = post_rating_instructClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *post_rating_instruct_common* updates
            if t >= 0.0 and post_rating_instruct_common.status == NOT_STARTED:
                # keep track of start time/frame for later
                post_rating_instruct_common.tStart = t
                post_rating_instruct_common.frameNStart = frameN  # exact frame index
                post_rating_instruct_common.setAutoDraw(True)
            
            # *pre_rating_instruct_txt_2* updates
            if t >= 0.0 and pre_rating_instruct_txt_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                pre_rating_instruct_txt_2.tStart = t
                pre_rating_instruct_txt_2.frameNStart = frameN  # exact frame index
                pre_rating_instruct_txt_2.setAutoDraw(True)
            
            # *rating_press_to_continue_2* updates
            if t >= 0.0 and rating_press_to_continue_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                rating_press_to_continue_2.tStart = t
                rating_press_to_continue_2.frameNStart = frameN  # exact frame index
                rating_press_to_continue_2.setAutoDraw(True)
            
            # *click_to_continue_2* updates
            if t >= 0.0 and click_to_continue_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                click_to_continue_2.tStart = t
                click_to_continue_2.frameNStart = frameN  # exact frame index
                click_to_continue_2.setAutoDraw(True)
            
            # *post_rating_instruct_continue* updates
            if t >= 0.0 and post_rating_instruct_continue.status == NOT_STARTED:
                # keep track of start time/frame for later
                post_rating_instruct_continue.tStart = t
                post_rating_instruct_continue.frameNStart = frameN  # exact frame index
                post_rating_instruct_continue.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if post_rating_instruct_continue.status == STARTED:
                theseKeys = event.getKeys()
                
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
            for thisComponent in post_rating_instructComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "post_rating_instruct"-------
        for thisComponent in post_rating_instructComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "post_rating_instruct" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        post_neutral_face_loop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(stim_csv),
            seed=None, name='post_neutral_face_loop')
        thisExp.addLoop(post_neutral_face_loop)  # add the loop to the experiment
        thisPost_neutral_face_loop = post_neutral_face_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPost_neutral_face_loop.rgb)
        if thisPost_neutral_face_loop != None:
            for paramName in thisPost_neutral_face_loop:
                exec('{} = thisPost_neutral_face_loop[paramName]'.format(paramName))
        
        for thisPost_neutral_face_loop in post_neutral_face_loop:
            currentLoop = post_neutral_face_loop
            # abbreviate parameter names if possible (e.g. rgb = thisPost_neutral_face_loop.rgb)
            if thisPost_neutral_face_loop != None:
                for paramName in thisPost_neutral_face_loop:
                    exec('{} = thisPost_neutral_face_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "post_rating"-------
            t = 0
            post_ratingClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            post_rating_img.setImage(stim_file)
            post_rating_scale.reset()
            # keep track of which components have finished
            post_ratingComponents = [post_rating_img, post_rating_scale]
            for thisComponent in post_ratingComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "post_rating"-------
            while continueRoutine:
                # get current time
                t = post_ratingClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *post_rating_img* updates
                if t >= 0.5 and post_rating_img.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    post_rating_img.tStart = t
                    post_rating_img.frameNStart = frameN  # exact frame index
                    post_rating_img.setAutoDraw(True)
                # *post_rating_scale* updates
                if t >= 0.5 and post_rating_scale.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    post_rating_scale.tStart = t
                    post_rating_scale.frameNStart = frameN  # exact frame index
                    post_rating_scale.setAutoDraw(True)
                continueRoutine &= post_rating_scale.noResponse  # a response ends the trial
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in post_ratingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "post_rating"-------
            for thisComponent in post_ratingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for post_neutral_face_loop (TrialHandler)
            post_neutral_face_loop.addData('post_rating_scale.response', post_rating_scale.getRating())
            post_neutral_face_loop.addData('post_rating_scale.rt', post_rating_scale.getRT())
            # the Routine "post_rating" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'post_neutral_face_loop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'post_rating_loop'
    
    
    # ------Prepare to start Routine "end_of_session"-------
    t = 0
    end_of_sessionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    end_of_session_txt.setText("""Dit was het einde van de %s sessie!

(Drop op een willekeurige toets om door te gaan.)""" % number_str)
    end_of_session_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    end_of_sessionComponents = [end_of_session_txt, end_of_session_resp]
    for thisComponent in end_of_sessionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "end_of_session"-------
    while continueRoutine:
        # get current time
        t = end_of_sessionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_of_session_txt* updates
        if t >= 0.0 and end_of_session_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_of_session_txt.tStart = t
            end_of_session_txt.frameNStart = frameN  # exact frame index
            end_of_session_txt.setAutoDraw(True)
        
        # *end_of_session_resp* updates
        if t >= 0.0 and end_of_session_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_of_session_resp.tStart = t
            end_of_session_resp.frameNStart = frameN  # exact frame index
            end_of_session_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if end_of_session_resp.status == STARTED:
            theseKeys = event.getKeys()
            
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
        for thisComponent in end_of_sessionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_of_session"-------
    for thisComponent in end_of_sessionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "end_of_session" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'session_loop'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanks_txt]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_txt* updates
    if t >= 0.0 and thanks_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_txt.tStart = t
        thanks_txt.frameNStart = frameN  # exact frame index
        thanks_txt.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanks_txt.status == STARTED and t >= frameRemains:
        thanks_txt.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


















# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
