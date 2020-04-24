#######################################################
#
#  Base Converter
#
#   Displays a value in base 2, 8, 10, 16, and an arbitrary base
#
#   Author:  John Marley
#
#######################################################

from tkinter import Frame, Tk, Label, Button, Toplevel
from functools import partial
from math import log

# list of bases for conversion
baseList = [2, 8, 10, 16, 13]

class NumPad(object):
    """ dialog for number entry """

    def __init__(self, master, base, init):
        """ initialize dialog """
        
        self.master=master
        self.dialog = Toplevel(master)
        # set [X] behavior
        self.dialog.protocol("WM_DELETE_WINDOW",
                             self.Cancel)
        # create dialog frame
        self.frame = Frame(self.dialog)
        self.frame.focus()
        self.base = base
        self.Position(self.dialog)
        # member variables
        self.init = init
        self.symList = []
        # initial method calls
        self.Make_symList()
        self.Add_Widgets()

    def Position(widget, dialog, pos=(0.5, 0.5)):
        """
        determine where on screen dialog will open

        parameters:
            widget - self if called by __init__, None or some widget otherwise
            dialog -  Toplevel to be positioned
            pos - tuple containing relative screen position
                of dialog center - default: (0,5,0.5)
            
        called in __init__ method, so does not need to be expicitlly called when
            creating dialog.  However, Position can be used to position the main
            application window, too.
        """

        # hide dialog
        dialog.withdraw()
        # clean up dialog tasks
        dialog.update_idletasks()
        # get dialog dimensions
        #  get dialog gemometry ("widthxheight+offx+offy")
        temp_str = dialog.geometry()
        #  find index of "x"
        i = temp_str.index("x")
        # width is the geometry string before the "x" (divide by 2 to get center)
        d_x = int(temp_str[:i])/2
        #  remove the width and "x" from geometry string
        temp_str = temp_str[i+1:]
        #  find the index of the first "+"
        i = temp_str.index("+")
        #  height is the geometry string before the "+" (divide by 2 to get center)
        d_y = int(temp_str[:i])/2
        # get screen dimensions
        s_x = dialog.winfo_screenwidth()
        s_y = dialog.winfo_screenheight()
        # find offset to position dialog
        x = s_x*pos[0] - d_x
        y = s_y*pos[1] - d_y
        # position dialog    
        dialog.geometry("+%d+%d" % (x, y))
        # show dialog
        dialog.deiconify()

    def Cancel(self):
        """ set rtn to initial value and close the dialog window """
        
        self.rtn = self.init
        self.dialog.destroy()

    def Close(self):
        """ set rtn to display and close the dialog window """
        
        self.rtn = self.disp["text"]
        self.dialog.destroy()

    def Make_symList(self):
        """ create list of symbols from base """
        
        for i in range(self.base):
            if i < 10:
                # use 0-9
                self.symList.append(str(i)
                                    )
            elif i<37:
                # use letters for values over 9 (up to 36)
                self.symList.append(chr(55+i))

    def Add_Widgets(self):
        """ add widgets to frame """

        # display the value
        self.disp = Label(self.frame,
              text="",
              width=15
              )
        self.disp.grid(columnspan=4)
   
        # add value buttons
        for val in range (self.base):
            if self.base == 2:
                span = 2
            else:
                span = 1
            Button(self.frame,
                   text=self.symList[val],
                   width="3",
                   command=partial(self.Press,
                                   self.symList[val]
                                   )
                   ).grid(column=val%4*span,
                          row=int(val/4)+1,
                          columnspan=span)
        # add backspace button
        Button(self.frame,
               text="←",
               command=self.Bksp
               ).grid(columnspan=4)
        # add clear button
        Button(self.frame,
               text="clear",
               command=self.Clear
               ).grid(columnspan=4)
        # add nib button
        if self.base == 2:
            Button(self.frame,
                   text="new nibble",
                   command=partial(self.Press,
                                   "n")
                   ).grid(columnspan=4)
        #add accept button
        Button(self.frame,
               text="accept",
               command=self.Close
               ).grid(columnspan=4)

    def Press(self, sym):
        """
        append character to the display
        parameter: sym - the character to be appended
        """
        
        temp = self.disp["text"]
        # base 2 is a special case
        if self.base != 2:
            # append character to display, but don't allow leading zeros
            if not((temp == "") & (sym == "0")):
                self.disp["text"] = temp+sym
        else:
            # split string into nibbles
            nibList = temp.split(" ")
            # nib button not pressed
            if sym != "n":
                # get the last nibble
                tmp2 = nibList.pop()
                # strip leading zeros
                i = tmp2.find("1")
                if i == -1:
                    tmp2 = ""
                else:
                    tmp2 = tmp2[i:]
                # if the last nibble is still 4 bits, put it back and start fresh
                if len(tmp2) == 4:
                    nibList.append(tmp2)
                    tmp2 = ""
                # append character
                tmp2 += sym
                # pad nibble with leadin zeros
                tmp2 = tmp2.zfill(4)
            # nib button was pressed
            else:
                if (nibList[0] != "0000") and (nibList[0] != ""):
                    # start a new nibble
                    tmp2 = "0000"
                else:
                    tmp2 = None
            # create string of nibbles separated by space
            temp = ""
            for nib in nibList:
                temp += nib + " "
            # append last nibble
            if tmp2 != None:
                temp += tmp2
            else:
                temp = temp[:-1]
            # set display to string of nibbles
            self.disp["text"] = temp
        # widen dialog if needed
        self.Resize()
                
    def Bksp(self):
        """ delete the last character on the display """
        
        if self.disp["text"] != "":
            # binary is a special case
            if self.base != 2:
                self.disp["text"] = self.disp["text"][:-1]
            else:
                # split string into nibbles
                nibList = self.disp["text"].split(" ")
                # remove nibble if zero
                if nibList[-1] == "0000":
                    nibList = nibList[:-1]
                # otherwise remove last bit of nibble
                else:
                    nibList[-1] = "0" + nibList[-1][:-1]
                # set display to nibbles
                temp = ""
                for nib in nibList:
                    temp += nib + " "
                self.disp["text"] = temp[:-1]
                
    def Clear(self):
        """ dclear the display """
        
        self.disp["text"] = ""
            
    def Resize(self):
        """ Change frame width if needed """

        # get height
        geo = self.dialog.geometry()
        y = int(geo[geo.find("x")+1:geo.find("+")])
        # find needed width
        w = len(self.disp["text"])
        if w > 15:
            self.disp["width"] = w
        x = self.disp["width"]*8
        #change frame width
        self.dialog.geometry("%dx%d" % (x,y))

    def Go(self):
        """ returnable method to be called in main program """
        
        # make modal
        self.dialog.transient(self.master)
        self.dialog.grab_set()
        # show dialog frame
        self.frame.grid()
        # wait for dialog to close
        self.dialog.wait_window(self.dialog)
        # return value
        return self.rtn

class Converter(Frame):
    """ main app frame """
    
    def __init__(self, master, *args, **kwargs):
        """ initialize Converter """

        # symbol check
        self.check="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # member variables
        self.last = len(baseList)-1
        self.val = 0

        # initialize frame
        Frame.__init__(self,
                       master,
                       *args,
                       **kwargs)
        self.master.title("Conveter")

        # add widgets
        self.Add_Widgets()

        # calculate needed frame size
        self.Resize()
        
    def Add_Widgets(self):
        """ add stuff to frame """

        self.btnList = []
        last = len(baseList)-1

        # add labels and buttons by iterating over base list
        for i in range (len(baseList)
                        ):
            base = baseList[i]
            # label for arbitrary base needs a variable
            self.arb_label = None
            if i != last:
                Label(self,
                      text="base: " + str(base)
                      ).pack(anchor="w")
            else:
                self.arb_label = Label(self,
                                       text="arbitrary base: "+str(base)
                                       )
                self.arb_label.pack(anchor="w")
            # add buttons
            self.btnList.append(Button(self,
                                       text="0",
                                       width="20",
                                       command=partial(self.Convert,
                                                       base
                                                       )
                                       )
                                )
            self.btnList[baseList.index(base)].pack()

        # add label and button to change arbitrary base
        Label(self,
              text="change arbitrary base (max 36)"
              ).pack(anchor="w")
        self.arb = Button(self,
                          text=str(baseList[last]),
                          width="20",
                          command=self.Get_Base
                          )
        self.arb.pack()

    def Get_Base(self):
        """ change the arbitrary base """

        # create numpad to enter value
        init = baseList[self.last]
        base = int(NumPad(None,
                          10,
                          init
                            ).Go()
                    )

        # check for valid range
        if 1 < base < 37:
            # change base in bases list
            baseList[self.last] = base
            # change arbitrary base button command
            self.btnList[self.last]["command"]=partial(self.Convert,
                                               baseList[self.last]
                                               )
            # change arbitrary base label
            self.arb_label["text"] = "arbitrary base: "+str(base)
            # change arbitrary base change button text
            self.arb["text"]=str(base)
            # recalculate displayed values from the current value
            self.Populate(self.val) 
        else:
            # if not in valid range, do nothing
            pass

    def Convert(self, base):
        """
        calculate base conversion
        parameter: base - the base to use in the conversion
        """

        # create numpad to enter number string
        init = self.btnList[baseList.index(base)]["text"]
        num_string = NumPad(None,
                            base,
                            init
                            ).Go()
        # remove spaces from base-2 strings
        if base == 2:
            num_string = num_string.replace( " ", "")
        # running sum
        self.val = 0
        # current position in string
        pos = len(num_string) - 1
        # iterate through string to convert to base-10 number
        for sym in num_string:
            # keep running sum of positional power * base-10 value of symbol
            self.val += (base**pos) * self.Num(sym)  # Num() returns base-10 value for given symbol
            pos -= 1
        # perform the conversion for each base
        self.Populate(self.val)

    def Populate(self, val):
        """
        perform the conversion for each base
        parameter: val - the base-10 value to convert to each base
        """

        try:
            # iterate through bases list
            for i in range(len(baseList)
                           ):
                # index of current base
                base = baseList[i]
                # converted value to display
                num_string = ""
                # running value for calculations
                temp = val
                # leftmost position in converted value
                count = int(log(val)/log(base)
                                )
                # perform calulation as long as there are positions in the value
                    # no positions left if the next position would be less than 1
                while base**(count) > 1/base:
                    # power of current postion
                    pwr = base**(count)
                    # base-10 value at current position
                        #  integer-part of running value / positional power
                    num = int(temp/pwr)
                    # string for display
                        # add each symbol to string until all positions filled
                    num_string += self.Chr(num) # Chr() returns symbol for given base-10 value
                    # subtract position value from running value
                    temp -= num*pwr
                    # move one position right
                    count -= 1
                # break binary into nibbles
                if base == 2:
                    tmp = list(num_string)
                    j = len(tmp) - 4
                    while j > 0:
                        tmp.insert(j, " ")
                        j -= 4
                    num_string = ""
                    for ch in tmp:
                        num_string += ch
                    j = num_string.find(" ")
                    if -1 < j < 4:
                        num_string = num_string.zfill(len(num_string)+4-j)
                    elif len(num_string) < 4:
                        num_string = num_string.zfill(4)
                  
                # update button text with string
                self.btnList[i]["text"]=num_string
                # widen button if string is more than 20 characters
                if len(num_string) > 20:
                    self.btnList[i]["width"]=len(num_string)
                else:
                    self.btnList[i]["width"]=str(20)
                self.Resize()
        except:
            pass

    def Resize(self):
        """ Change frame size based on number and width of buttons """
        
        # find needed width
        x = 240
        for btn in self.btnList:
            tmp = btn["width"]*10
            if tmp > x:
                x = tmp
        # find needed height
        y = len(self.btnList)*60 + 80
        #change frame dimensions
        self.master.geometry("%dx%d" % (x,y))
        
    
    def Num(self, sym):
        """
        return base-10 value for given symbol
        parameter: sym - given symbol
        """
        
        return self.check.index(sym)   


    def Chr(self, val):
        """
        return symbol for given base-10 value
        parameter: val - given value
        """

        return self.check[val]

root = Tk()
frame = Converter(root)
frame.pack()
NumPad.Position(frame, root)
root.mainloop()
