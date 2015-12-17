from scriptlib import *

no_selection = False

try:
    sel = get_sel()
except:
    sel = ""
    no_selection = True
try:
    clipb = get_clip() # because we're about to clobber it
except:
    clipb=""

#keyboard.send_key("<delete>")
sel = "<blockquote>" + sel + "</blockquote>"
set_clip(sel)
time.sleep(0.01)
keyboard.send_keys("<ctrl>+v") # paste over the selection
set_clip(clipb) # restore previous contents (we hope)

# Put the cursor inside the <blockquote></blockquote> tags if the
# selection was empty
if no_selection:
    keyboard.send_keys("<ctrl>+<left>")
    time.sleep(0.01)
    keyboard.send_keys("<left><left>")