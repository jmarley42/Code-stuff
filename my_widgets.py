############################################################
# Custom tkinter/ttk widgets 
###############################
# Author: John Marley
###############################
# EditLabel - a button that opens an Entry to change its text
#             .Get() method returns text
# ToggleButton - a button that holds "on" and "off" status
#                .Status() method returns the boolean status 
# PopupDialog - a collection of dialog boxes, 
#
#               defined dialogs:
#                   msgBox - displays a message and an OK button, modal
#                   queryBox - displays a question and an Entry, modal
#                              returns text from Entry
#                   boolBox - displays a question and yes/no buttons, modal
#                             returns boolean determined by button press
#                   numBox - displays a numeric keypad, modal
#                           returns displayed float on <=>
#                   timerBox - displays a timer that calls a function when done
#                   tipBox - displays a text label when mouse hovers over master
############################################################

from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from threading import Timer
from time import monotonic
from functools import partial

class MultiCheckButton(Label):
    """
    Label extension that incorporates more than two states

    Parameters:
        master - the paent widget
        state_sym - the sybols for (and number of) states
        skip_states - list of states to skip/ignore
        Label Keywords and arguments

    methods:
        Cycle() - steps to the next higher state (circular)
        Set() - sets the state
        Get() - returns the state
        methods are not normally called manually.

    notes:
        events externally bound to the widget must be bound to widget.lbl
        methods called by those events must refer to event.widget.master
    """

    def __init__(self, *args,**kwargs):
        """ construcor method """

        self.state = 0
        try:
            self.state_sym = kwargs['state_sym']
            del kwargs['state_sym']
        except:
              self.state_sym = ["⬜","⛝"]  

        try:
            self.skip_states = kwargs['skip_states']
            del kwargs['skip_states']
        except:
            self.skip_states = []

        try:
            kwargs["text"] = "     " + kwargs["text"]
        except:
            print("Didn't work")
            
            
        # initialize container widget
        Label.__init__(self,
                       *args,
                       **kwargs
                       )
        
        # create display label
        self.lbl = Label(self,
                         text=self.state_sym[self.state],
                         anchor="w",
                         relief = "flat",
                         width=len(self.state_sym[0])+1
                         )
        self.lbl.grid(row=0,
                      column=1
                      )
        self.lbl.bind("<ButtonRelease-1>",
                      self.Cycle,
                      add="+"
                      )

    def Cycle(self, event=None):
        tmp = self.state
        skip = False
        if self.state in self.skip_states:
            skip = True
        elif self.state < len(self.state_sym)-1:
            self.state += 1
        else:
            self.state = 0
        count = 0
        while (self.state in self.skip_states) and not skip:
            count += 1
            if self.state < len(self.state_sym)-1:
                self.state += 1
            else:
                self.state = 0
            if count > len(self.state_sym):
                self.state = tmp
        self.lbl["text"] = self.state_sym[self.state] + " " + self["text"]

    def Set(self, state):
        if state < len(self.state_sym):
            self.state = state
            self.lbl["text"] = self.state_sym[self.state] + " " + self["text"]
        else:
            print("Invalid state value")

    def Get(self):
        return self.state
        
        
          
    
class EditLabel(Label):
    """
    Label extention that incorporates an Entry

    Parameters:
        master - the parent of the dialog (usually the Tk() application)
        Label keword arguments (width defaults to 20)

    Methods:
        Get()  - returns the current text
        Set(string) - procedurally change the current text
        methods inherited from Label 
        
    """ 
    
    def __init__(self, *args,**kwargs):
        """ construcor method """

        # initialize container widget
        Label.__init__(self,
                       *args,
                       **kwargs
                       )
        
        self["width"] = len(self["text"])+1

        # create display label
        self.lbl = Label(self,
                         text=self["text"],
                         anchor="w",
                         relief = "raised",
                         width=int(self["width"])
                         )
        self.lbl.grid(row=0,
                      column=1
                      )
        self.lbl.bind("<ButtonRelease-1>",
                      self.Edit,
                      add="+"
                      )

        # create Entry (but don't show yet)
        self.txt = StringVar()
        self.txt.set(self["text"])
        self.box = Entry(self, textvariable=self.txt, width=int(self["width"]))

    def Edit(self, event=None):
        """ show Entry, update label, and hide Entry """
        
        # internal helper methods
        def Change(self, box, event=None):
            """ change EditLabel text and hide the Entry"""
            self.lbl["width"] = len(box.get())
            self.lbl["text"] = box.get()
            self.box.grid_remove()

        def Hide(self, box, event=None):
            """ hide the Entry without changing text"""
            self.txt.set(self.lbl["text"])
            self.box.grid_remove()

        # bind relevant events to Entry
        self.box.bind("<Return>", partial(Change, self, self.box), add="+")
        self.box.bind("<FocusOut>", partial(Hide, self, self.box), add="+")
        self.box.bind("<Escape>", partial(Hide, self, self.box), add="+")

        # display Entry with keyboard focus and text selected
        self.box.focus()
        self.box.select_range(0,"end")
        self.box.grid(row=0, column=1)

    def Get(self):
        """ return contents of EditLabel """
        return self.lbl["text"]

    def Set(self, txt):
        """ procedurally set contents of EditLabel """
        self.lbl["text"] = txt
        self.txt.set(txt)

############################################################
############################################################

class ToggleButton(Label):
    """
    Label extensionacts as a button that toggles boolean statuses

    Parameters:
        master - the parent of the widget (usually a Frame)
        hotkey - optional keword argument defining a hotkey (duh)
        Label keword arguments

    Methods:
        Status()  - returns True (pressed) or False (raised)
        methods inherited from Label
    """
    
    def __init__(self, *args, **kwargs):

        # if a hotkey is set, remember it and remove it from kwargs
        #  (or Label._init_ will throw an error)
        if "hotkey" in kwargs:
            hotkey = kwargs["hotkey"]
            del kwargs["hotkey"]
        else:
            hotkey = None

        # initialize button
        Label.__init__(self, *args, **kwargs)
        # set a minimum button width of 3 characters
        if len(self["text"]) < 3:
            self["width"] = 3
        # add some space around text
        self["padding"] = "10 4"
        # set initial state to "not pressed"
        self.status = False
        self["relief"]="raised"
        # bind button event
        self.bind("<ButtonRelease-1>", self.Select, add="+")
        # if a hotkey was set, bind it to the toplevel window 
        if hotkey != None:
            self.winfo_toplevel().bind(hotkey, self.Select)

    def Select(self, event=None):
        """ toggles button status when clicked """
        
        # toggle buttn state
        if not self.status:
            self.status = True
            self["relief"]="sunken"
        else:
            self.status = False
            self["relief"]="raised"
        #generate a virtual event for the parent widget
        self.event_generate("<<Toggle>>", data=self, when="tail")

    def Status(self):
        """ return button status """
        
        return self.status

############################################################
############################################################

class PopupDialog(object):
    """
    A collection of popup dialogs

    Parameters:
        master - the parent of the dialog (usually the Tk() application, or None)
        title - title to display on dialog - default: None
        pos - tuple containing relative x and y screen positons  - default: (0.5, 0.5)

    Methods:

        Position - positions the window on the screen according to pos
            parameters:
                widget - self if called by __init__, None or some widget otherwise
                dialog -  Toplevel to be positioned
                pos - tuple containing relative x and y screen positons - default: (0.5,0.5)
                
            called in __init__ method, so does not need to be expicitlly
            called when creating dialog.  However, Position can be used to position
            the main application window, too.
            
            use example:
                PopupDialog.Position(app, root, (0.5, 0.1))

        msgBox - displays a message and an "Okay" button, modal

            parameters -
                msg - string containing message
                btn - text for button
        
            use example -
                PopupDialog(master).msgBox("Message")

        queryBox - displays a question and an Entry to respond, modal
        
            Returns a string containing Entry text.

            parameters -
                query - string containing question
        
            use example:
                answer = PopupDialog(master).queryBox("Question")

        boolBox - displays  question, and two buttons with customizable text, modal

            Returns a boolean associated with the buttons

            parameters -
                query - string containing question
                txt1 - string containing text for True response - default: Yes
                txt2 - string containing text for False response - default: No
            
            use example:
                yesno = PopupDialog(master).boolBox("Question", "Why not", "No Way")

        numBox - displays a numeric keypad, modal

             Eeturns a float.
        
            use example:
                value = PopupDialog(master).numBox()

        timerBox - displays a timer that Calls a function when complete, not modal
        
            start, stop, and reset buttons
            also has a toggle button to change from one-shot to recycling
            and a button to change the interval
            create as an instance

            parameters:
                kind - "one_shot", "recycling", "auto_one", "auto_rec"
                    "auto_" indicates autostarting - default: "one_shot"
                interval - timer interval in seconds - default: 5
                function - function to be called when timer finishes - default: None
                *ar - fomal arguments to be passed to function
                **kw - keyword arguments to be passed to function

            use example:
                tmr = PopupDialog(master).timerBox("recycling", 5, my_function, "Hi", msg="There")

        tipBox - displays a simple label when mouse hovers over master widget

            parameters:
                msg - text to display

            requires additional bindings and methods in creation of master widget
            
            use example (right click) -
            
                def Open_Tip(master, msg, event=None):
                    nonlocal tip
                    tip = PopupDialog(master)
                    tip.tipBox(msg)
                        
                def Close_Tip(event=None):
                    try:
                        tip.Close()
                    except:
                        pass

                self.btn.bind("<ButtonRelease-3>", partial(Open_Tip, self.btn, "Text here"), add="+")
                self.btn.bind("<Leave>", Close_Tip, add="+")

    """

    # initialize PopupDialog
    def __init__(self, master=None, title=None, pos=(0.5, 0.5)):
        # set internal variables
        self.rtn = None
        self.master=master
        self.dialog = Toplevel(master)
        # set the title if present
        if title != None:
            self.dialog.title(title)
        else:
            self.dialog.title("")
        # make dialog not resizable
        self.dialog.resizable(width=False, height=False)
        # set [X] behavior
        self.dialog.protocol("WM_DELETE_WINDOW", self.Cancel)
        # create and position dialog frame
        self.frame = Frame(self.dialog, padding=15)
        self.Position(self.dialog, pos)
        # give focus to dialog frame
        self.frame.focus()

    def Position(widget, dialog, pos=(0, 0)):
        """
        determine where on screen dialog will open

        parameters:
            widget - self if called by __init__, None or some widget otherwise
            dialog -  Toplevel to be positioned
            pos - tuple containing relative x and y of UL corner - default: (0,0)
            
        called in __init__ method, so does not need to be expicitlly
        called when creating dialog.  However, Position can be used to position
        the main application window, too.
        
        use example:
            PopupDialog.Position(app, root, (0.5, 0.1))
        """

        # hide dialog
        dialog.withdraw()
        # complete any unfinished tasks
        dialog.update_idletasks()
        # calculate desired screen position
        x = dialog.winfo_screenwidth()*pos[0]
        y = dialog.winfo_screenheight()*pos[1]
        # move dialog to desired position   
        dialog.geometry("+%d+%d" % (x, y))
        # show dialog
        dialog.deiconify()

    def Cancel(self, event=None):
        """ set return value to None and destroy the dialog window """
        self.rtn = None
        self.dialog.destroy()

    def Close(self, event=None):
        """ destroy the dialog window. """
        self.dialog.destroy()
        
    ###############################

    def msgBox(self, msg="", btn="OK"):
        """
        displays a message and an OK button, modal

        parameters -
            msg - string containing message - default: nothing
            btn - text for button - default: "OK"
    
        use example -
            PopupDialog(master).msgBox("Message")
        """
        
        # make modal
        self.dialog.transient(self.master)
        self.dialog.grab_set()

        # show dialog
        self.frame.pack()
              
        #display message
        Label(self.frame, text=msg).pack(pady=10)
        
        # display ok button
        Button(self.frame, text=btn,command=self.Close).pack()

        # bind <Return> key
        self.dialog.bind("<Return>", partial(self.Close))
        
        # wait for close
        self.dialog.wait_window(self.dialog)

    ###############################

    def queryBox(self, query, ans = None, pwd=None):
        """
        displays a question and an Entry to respond, modal
        
        Returns a string containing Entry text.
            
        parameters -
            query - string containing question
            ans - initial answer text
                - default: None
            pwd - character mask (will show mask chr instead of entered text)
                - default: None
    
        use example:
            answer = PopupDialog(master).queryBox("Question")
        """

        # set internal variables
        self.ans = ans
        self.pwd = pwd
        
        # make modal
        self.dialog.transient(self.master)
        self.dialog.grab_set()

        # show dialog
        self.frame.pack()
      
        # internal helper methods
        def Change(self, box, event=None):
            """ set return value to Entry text and destroy the dialog """
            self.rtn = box.get()
            self.Close()

        # create and show question label
        Label(self.dialog, text=query).pack(padx=10, pady=10)

        # create Entry 
        box = Entry(self.dialog, show=self.pwd)
        # if an initial answer was given, put it in the Entry and select it
        if self.ans != None:
            box.insert(0, self.ans)
            box.select_range(0, END)
        # give focus to Entry
        box.focus()
        # bind <Return> and <Escape> keys        
        box.bind("<Return>", partial(Change, self, box))
        box.bind("<Escape>", self.Cancel)
        # show Entry
        box.pack(padx=10, pady=10)
        # wait for response
        self.dialog.wait_window(self.dialog)
        # return response
        return self.rtn

    ###############################

    def boolBox(self, query, txt1="Yes", txt2="No"):
        """
        displays a question and returns a boolean, modal

        parameters -
            query - string containing question
            txt1 - string containing text for True response - default: Yes
            txt2 - string containing text for False response - default: No
            
        use example:
            yesno = PopupDialog(master).boolBox("Question", "Why not", "No Way")

        """

        # make modal
        self.dialog.transient(self.master)
        self.dialog.grab_set()

        # show dialog
        self.frame.grid()

        # internal functions for boolean return
        def Yes(event=None):
            """ set return value to True and destroy dialog """
            self.rtn = True
            self.Close()

        def No(event=None):
            """ set return value to False and destroy dialog """
            self.rtn = False
            self.Close()
        
        # create and show question Label
        Label(self.dialog, text=query).grid(row=0, column=0,
                                            padx=10, pady=10, columnspan=2)

        # add buttons
        Button(self.dialog, text=txt1, command=Yes).grid(row=1, column=0,
                                                         padx=(10,5), pady=5)
        Button(self.dialog, text=txt2, command=No).grid(row=1, column=1,
                                                        padx=(5,10), pady=5)
        # bind <Return> and <Escape> keys        
        self.dialog.bind("<Return>", Yes)
        self.dialog.bind("<Escape>", No)
        # wait for response
        self.dialog.wait_window(self.dialog)
        # return response
        return self.rtn

    ###############################

    def numBox(self, msg=None, neg="True", real="True"):
        """
        displays a numeric keypad and returns a number

        parameters -
            neg - allow negative numbers
                - default: True
            real - allow floating point numbers 
                - default: True
    
        use example:
            value = PopupDialog(master).numBox()
        """

        # set internal variables
        self.neg = neg
        self.real = real
        self.rtn = 0
        
        # make modal
        self.dialog.transient(self.master)
        self.dialog.grab_set()

        # visual style for display Label
        s = Style()
        s.configure("dsp.TLabel", relief="groove",
                            padding="10 2", anchor="center", background="white")

        # show dialog    
        self.frame.grid()

        # internal helper methods
        def Clear(event=None):
            """ clear the return value and the display """
            self.rtn = 0
            display["text"] = "0"

        def Key_Choose(event):
            """ handler for key events """
            try:
                # set n to ASCII value of key pressed
                n =  ord(event.char)
                #if a number was pressed update value
                if n in range(48, 58):
                    Update_Val(n-48)
                # if 'space' was pressed reset display
                elif n == 32:
                    Clear()
                # if '-' was pressed (and negatives are allowed) negate the displayed value
                elif (n == 45) and self.neg:
                    Neg()
                # if '.' was pressed (and reals are allowed) display a decimal point
                elif (n == 46) and self.real:
                    Update_Val(".")
            # ignore non-character keys
            except:
                pass

        def Neg():
            # negate value
            self.rtn = -1*self.rtn
            # negate the display
            if display["text"].startswith("-"):
                display["text"] = display["text"][1:]
            else:
                display["text"] = "-" + display["text"]

        def Bksp(event=None):
            # if at least one digit has been entered
            if display["text"] != "0":
                # if value is more than one digit long, delete last digit
                if len(display["text"]) > 1:
                    display["text"] =display["text"][:-1]
                # if val is one digit, replace it with 0
                else:
                    display["text"] = "0"
                # set value to displayed text
                try:
                    self.rtn=float(display["text"])
                except:
                    self.rtn=0

        def Update_Val(n):
            # if first digit....            
            if (display["text"] == "0"):
                # if decimal point, append it to the display
                if n == ".":
                    display["text"] = display["text"] + n
                # otherwise replace with selected number
                else:
                    display["text"] = str(n)
            # if not first, append to display
            else:
                # don't append a decimal point if there already is one
                if (n == "."):
                    if not("." in display["text"])  :
                        display["text"] = display["text"] + n
                else:
                    display["text"] = display["text"] + str(n)
            # save new number to rtn
            self.rtn=float(display["text"])
            # give focus to dialog frame (so buttons don't keep focus)
            self.frame.focus_set()

        # create and show message label if needed
        if msg:
            Label(self.frame, text=msg, width=17, justify="left").grid(row=0, column=0, columnspan=3)


        # create and show display label
        display = Label(self.frame, text="0",width=13,style="dsp.TLabel")
        display.grid(row=1, column=0, columnspan=3)

        # add buttons for digits 1 thru 9
        for n in range(9):
            Button(self.frame, text=str(n+1),
                   command=partial(Update_Val, n+1), width=4).grid(column=n%3,
                                                               row=2+int(n/3))
               
        # add button for 0
        Button(self.frame, text="0",
                   command=partial(Update_Val, 0), width=4).grid(column=1, row=5)

        # add button for '.'
        if real == "True":
            Button(self.frame, text=".",
                       command=partial(Update_Val, "."), width=4).grid(column=0, row=5)

        # add button for negation
        if neg == "True":
            Button(self.frame, text="±", command=Neg, width=4).grid(column=2, row=5)           
            
        # add button for backspace
        Button(self.frame, text="←", command=Bksp, width=4).grid(column=0, row=6)
            
        # add button for <Clear>
        Button(self.frame, text="C", command=Clear, width=4).grid(column=1, row=6)

        # add button for <Done>
        Button(self.frame, text="=", command=self.Close, width=4).grid(column=2, row=6)

        # bind keyboard events
        self.dialog.bind("<Return>", self.Close)
        self.dialog.bind("<Escape>", self.Cancel)
        self.dialog.bind("<Key>", Key_Choose)
        self.dialog.bind("<BackSpace>", Bksp)

        # wait for window to close             
        self.dialog.wait_window(self.dialog)

        # return value (float if reals allowed, integer if not)
        if (not self.rtn) | (self.real == "True"):
            return self.rtn
        else:
            return int(self.rtn)

    ###############################

    def timerBox(self, interval=5, kind="one_shot", function=None, *ar, **kw):
        """
        displays a timer that calls a function when done

        also has a toggle button to change from one-shot to recycling
        and a button to change the interval
        create as an instance

        parameters:
            interval - timer interval in seconds - default: 5
            kind - "one_shot", "recycling", "auto_one", "auto_rec"
                "auto_" indicates autostarting - default: "one_shot"
            function - function to be called when timer finishes - default: None
            *ar - fomal arguments to be passed to function
            **kw - keyword arguments to be passed to function

        use example:
            tmr = PopupDialog(master).timerBox(5, "recycling", my_function, "Hi", msg="There")

        """

        #  set internal variables
        rem = interval  # remaining time
        keep_going = False  # running flag
        rpt_flag =  False  # recycling flag
        clk = 0  # montonic clock value
    
        # Start/Stop button images
        self.start_img = PhotoImage()
        self.start_img.put(b"R0lGODlhGQAOAPcAAAAAAAEBAgECAgUFBQQECQgICAoLCwsLFwkTEw0QEw0RFA0RFQwSFQwSFhAQECMjIyoqKioqKyosLiQvNiUwNSYwNiYwNy8xNC03PTw8PCAgQCAkQCIlRSArQCAtQCkpUyAyQCA5QCQ5SyY6Sy44QCg6Sys8Sy4+TCkzUyBAQCRAQC1AQCtAVzBATjJCTzpESjdMXjNQUEBAQEBESUBPXEtUWExVWVBQUFJXWlpaWldvb1tjaWNkZ2hoaGlqamR6enN4fXR6fkBggFBtim9vn3Z9gXp6pm+Hn36LloiJiY6Um5qampycnYeWoqerrqqusLCxscPFx8fIytfX19jY2OXm5gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAZAA4AAAjgAJFE+UewoEGCMmQIMZhQxj8aF3IwOWgwxoABHIYQvHFxQAwXCRxEKOKkCsUNAAAQmEFQRUoAG1woABAAg40gT6gY1PDS4b8UL0O0mBmAgtEaPnb2JAg0ZYoTRCtIrSDgAQ+CPFP6bAoghYkFNCeInSCggAQl/7IC2PoyRQkGYcVaMJABCkEQL1cQ9PDSwwi4Aca+SGKQawqsLzWMaBCWBBCKhhGn1CCCcYAdFJm2lQyAcgMIPTJrBnCABcEOB1J2gIFjyRTR/34gQIDCCMEfH2b/aCIFdkEdOo4YJAL8X0AAOw==")

        self.stop_img = PhotoImage()
        self.stop_img.put(b"R0lGODlhGQAOAPcAAAAAAAAAAQECAgICAwIDBAQGCAYHCQUHCgYICQYICgUICwcJDAgKCwkMDg0PEw8WGw4WHBATGBAUGBAWGhAWGxMYHhEaIhIcJRMdJhYcIRcfJBYfJRgfIxgfJBggIxggJBsgJRwhJxkjKxkkLB0jKR4jKh0lKx0mKx4rNxwrOSEqNiMvNyQvNiMtOiIvOCUwNSUwNiUwNyMyPSIyPykzPSk1PSM0QSQ5SyY6SyU7Tik2RSo3Ris4SCo4SSk7Sys8Sys/Tiw5SS88TC4+TDA8RjA7SjA9TSxHXjBATjJCTzZGVDBEWTtKVkVYaQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAZAA4AAAi7AP8JHNiEBokQRJgoJBICRIkiAyNKVJKBgQETNTKeQFCggQqJIP8lmTAgQIcYKD8ECLCgRUiJI0tygEFTpQAHO15GREIyAIcXQD0EGCDBiM6BQ3rOrDlUgpCjAn9QIOCThVWVAyIEgfrPx9SqVjs05cEVxwOqHKyyEEs0J1QcEKh2UMtWgg6uN+IG0LCi74amd6HmpbrBheG/RAMfzWFBQQERMiKPOJCgQg+uR1JcsDADiGcbGDCgWAIyIAA7")

        # helper functions
        def Set_Rpt(event=None):
            """ toggle between one-shot and recycling """
            nonlocal rpt_flag
            if rpt_flag:
                # if "recycling", set to "one shot"
                rpt_btn["text"]="One-Shot Timer"
                rpt_flag = False
            else:
                # if "one shot" set to "recycling"
                rpt_btn["text"]="Recycling Timer"
                rpt_flag = True

        def Timing():
            """
            main timing function

            repeatedly creates a 0.01 second timer and decrements remaing time when finished
            """
            nonlocal rem, keep_going,clk
            # initialize return value (not actually going to return anything, so using it fo timer)
            self.rtn = None
            # update remaining time by subtracting elapsed time between current and previous monotonic clock readings
            rem = rem - (monotonic()-clk)
            
            # if there is time remaining, update display and take new montonic clock reading
            if rem>0:
                rem_lbl["text"]="Time left: {:.2f}s".format(rem)
                clk = monotonic()
            # otherwise...
            else:
                # set remaining time (and display) to interval
                rem = interval
                rem_lbl["text"]="Time left: {:.2f}s".format(interval)
                # call function if set
                if function != None:
                    function(*ar, **kw)
                # stop timer if one-shot timer
                if not rpt_flag:
                    keep_going = False

            # if still running, create and start a 0.01 second timer
            if keep_going:
                self.rtn=Timer(0.01, Timing)
                self.rtn.start()

        def Start():
            """ start timer, or (if already running) pause (stop but don't change remaining time) """
            nonlocal keep_going, clk
            # if flag is set to running..
            if keep_going:
                # set flag to not running
                keep_going = False
                # cancel current 0.01 second timer (if there is one)
                try:
                    self.rtn.cancel()
                except:
                    pass
            # if flag set to not runnning...
            else:
                # set flag to running
                keep_going = True
                clk = monotonic()
                # create and start a 0.01 second timer
                self.rtn=Timer(0.01, Timing)
                self.rtn.start()
            
        def Stop():
            """ stop timer and reset remaining time """
            nonlocal keep_going, rem
            # set flag to not running 
            keep_going = False
            # set remaining time (and display) to interval
            rem = interval
            rem_lbl["text"]="Time left: {:.2f}s".format(interval)
            # cancel current 0.01 second timer (if there is one)
            try:
                self.rtn.cancel()
            except:
                pass

        def Cancel(event=None):
            """ cancel 0.01 second timer (if there is one) and call PopupDialog cancel """
            try:
                self.rtn.cancel()
            except:
                pass
            self.Cancel()

        def New_Int(event=None):
            """ change the timer interval """
            nonlocal interval, rem
            # remember old interval
            old = interval
            # change interval to new value
            interval = PopupDialog(self.dialog).numBox()
            # if new interval exists (and greater than zero)...
            if (interval != None) and (interval > 0):
                # change interval button text
                int_btn["text"] = "Interval: {:.2f}s".format(interval)
                # chage remaining time and label (unless the timer is running)
                if not keep_going:
                    rem = interval
                    rem_lbl["text"]="Time left: {:.2f}s".format(interval)
            # otherwise set interval back to previous value
            else:
                interval = old
                   
        # re-assign [X] behavior
        self.dialog.protocol("WM_DELETE_WINDOW", Cancel)

        # show dialog
        self.frame.grid()

        # create and show repeat/one-shot button
        rpt_btn = Button(self.frame, text="One-Shot Timer", command=Set_Rpt)
        rpt_btn.grid()

        # create and show interval button
        int_btn = Button(self.frame,text="Interval: {:.2f}s".format(interval), command=New_Int)
        int_btn.grid()


        # create and show time-remaining label
        rem_lbl = Label(self.frame, text="Time left: {:.2f}s".format(interval))
        rem_lbl.grid(columnspan=2)
 
        # create and show Start/Pause Button
        Button(self.frame, image=self.start_img, command=Start,width=6).grid(columnspan=2)

        # create and show Stop Button
        Button(self.frame, image=self.stop_img, command=Stop,width=6).grid(columnspan=2)

        # if kind is recycling...
        if kind=="recycling":
            # set to repeating
            Set_Rpt()
            # complete any pending tasks
            self.dialog.update_idletasks()
        # if kind is auto-starting one shot...
        elif kind=="auto_one":
            # start the timer
            Start()
        # if kind is auto-starting recycling...
        elif kind=="auto_rec":
            # set to repeating
            Set_Rpt()
            # complete any pending tasks
            self.dialog.update_idletasks()
            # start the timer
            Start()

    ###############################

    def tipBox(self, msg="tip text", coord=(0,0)):
        """
        display a tooltip label for master widget

        parameters -
            msg - text to display
            coord - location to display tooltip

        requires additional bindings and methods in creation of master widget
        
        use example (code in master widget) -

            def Open_Tip(master, msg, event=None):
                nonlocal tip
                tip = PopupDialog(master)
                tip.tipBox(msg)
                     
            def Close_Tip(event=None):
                try:
                    tip.Close()
                except:
                    pass

            self.btn.bind("<Enter>", partial(Open_Tip, self.btn, "Text here"), add="+")
            self.btn.bind("<Leave>", Close_Tip, add="+")

        """

        # set style
        self.s = Style()
        self.s.configure("tip.TLabel",
                         relief="sunken",
                         background="white",
                         padding="10 4")
        self.s.configure("tip.TFrame",
                         relief="raised",
                         background="orange",
                         padding="10 4")

        # show dialog
        self.frame["padding"] = 5
        self.frame["style"]="tip.TFrame"
        self.frame.grid()
        
        # set dialog to no-border
        self.dialog.overrideredirect(1)
                            
        # position dialog
        rx = coord[0]/self.dialog.winfo_screenwidth()        
        ry = coord[1]/self.dialog.winfo_screenheight()
        self.Position(self.dialog, pos=(rx,ry))
     


        # create and show message label
        lbl = Label(self.frame, text=msg)
        lbl["style"] = "tip.TLabel"
        lbl.grid()     

    ###############################

    def selectBox(self, query, txt_dict={"Yes":1,"No":0}, both=False):
        """
        displays a query/message and s customizeable number of selections, modal

        returns  chosen selection

        parameters -
            query - string containing question/message
            txt_dict - dictionary containing text for selections(keys) and returns (values)
            both = Flag for return
                       True -> return both key and value
                       False -> return value only

        use example:
            

        """

        # make modal
        self.dialog.transient(self.master)
        self.dialog.grab_set()

        # show dialog
        self.frame.grid()

        # internal function
        def Select(key,val):
            if both:
                self.rtn = [key, val]
            else:
                self.rtn = val
            self.Close()
            
        # create and show question Label
        Label(self.dialog, text=query).grid(padx=10, pady=10, columnspan=2)
        
        # add buttons 
        for k, v in txt_dict.items():
            Button(self.frame,
                   text=k,
                   command=partial(Select, k, v)
                   ).grid()
 
        # wait for window to close             
        self.dialog.wait_window(self.dialog)

        # return selected value 
        return self.rtn
