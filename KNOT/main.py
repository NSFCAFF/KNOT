#%% --- IMPORTS --- %%#
### External ###
import numpy		as np
import time

### Internal ###
import __OPERATION	as OP
import __VISUALS	as VIS
import _INITIALIZE	as INIT
import _PREPARE		as PREP
import _RECOVER		as REC
import _SEGMENT		as SEG
import _TRACK		as TRK

#%% --- USER PARAMETERS --- %%#
# Update/Visualize which saved values? #
UPDATE = {'INI':False, 'PRE':False, 'REC':False, 'SEG':False, 'TRK':True}
VISUAL = {'INI':False, 'PRE':False, 'REC':False, 'SEG':False, 'TRK':True}

# Load in which images? #
CODES = ['roi_Test Bead_(300,300)_(256x256)_(f100-110)', 'roi_Test Cell_(200,230)_(256x256)_(f0-10)']
#CODES = ['roi_Test Cell_(200,230)_(256x256)_(f0-10)']

#%% INITIALIZATION %%#
for code in CODES:
	#%% INITIALIZATION %%#
	if(__name__ == '__main__'):
		# Make sure all needed folders exist #
		OP._MakeDir(OP.FOLD_APR)
		OP._MakeDir(OP.FOLD_KER)
		OP._MakeDir(OP.FOLD_IMG)

		OP._MakeDir(OP.FOLD_SIM)
		OP._MakeDir(OP.FOLD_TMP)
		OP._MakeDir(OP.FOLD_EVL)
		OP._MakeDir(OP.FOLD_MAT)

		OP._MakeDir(OP.FOLD_TRUE)

		OP._MakeCode(code)

		# Initialize Microscope #
		print('\n---------- Initialization ----------')
		scope = INIT.RUN(code, update=UPDATE['INI'], visual=VISUAL['INI'])

	#%% SNR BOOSTING %%#
	if(__name__ == '__main__'):
		print('\n---------- Pre-Processing ----------')
		img_, ker_, eps_ = PREP.RUN(scope, code=code, update=UPDATE['PRE'], visual=VISUAL['PRE'])

	if(__name__ == '__main__'):
		print('\n----------    Recovery    ----------')
		pos, wgt = REC.RUN(img_, ker_, eps_, code=code, update=UPDATE['REC'], visual=VISUAL['REC'])

	#%% IDENTIFICATION %%#
	if(__name__ == '__main__'):
		print('\n----------  Segmentation  ----------')
		clouds = SEG.RUN(pos, wgt, img_, code=code, update=UPDATE['SEG'], visual=VISUAL['SEG'])
	
	#%% TRACKING %%#
	if(__name__ == '__main__'):
		print('\n----------    Tracking    ----------')
		traj = TRK.RUN(clouds, scope.img, code=code, update=UPDATE['TRK'], visual=VISUAL['TRK'])
		print('\n');