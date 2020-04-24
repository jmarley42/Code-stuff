#######################################################
#
#  MoM saved-game editor
#
#   Edits a saved=game file for the MicroProse game Master of Magic
#        (from 1995)
#
#   Author:  John Marley
#
#######################################################

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
from array import array
from math import ceil, floor, sqrt
from PIL import Image, ImageTk
from Resources.MoM_Book import * # these are the helper methods

# root for tkinter objects
root = Tk()

# Main window and menu options
class App(Frame):

    wiz = []
    wiz_num = IntVar()
    
    def __init__(self, master=None):
        """ constructor """

        # intiialize Frame 
        Frame.__init__(self, master)

        # set [X] button to call exit method
        self.master.protocol("WM_DELETE_WINDOW", partial(self.Exit, True))

        # set window title and geometry, show frame
        self.master.title("Master of Magic Saved-game Editor")
        self.master.geometry("1400x800")
        self.place(relheight=1, relwidth=1, x=0, y=0)

        # create widgets
        self.createWidgets()    

    def createWidgets(self):
        """ create menu, wizards radio-buttons, and notebook """
        
        # Menu bar
        
        self.menuBar = Menu(self)
        self.fileMenu = Menu(self.menuBar, tearoff=0)

        self.fileMenu.add_command(label="Open", command=self.Open)
        self.fileMenu.add_command(label="Save", command=self.Save)
        self.fileMenu.add_command(label="Close", command=self.Close)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.Exit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.menuBar)

        # Wizards radiobuttons
        for i in range(5):
            self.wiz.append(Radiobutton(self,
                                        text="Wizard " + str(i),
                                        value=i, variable=self.wiz_num,
                                        command=self.Select))

        for i in range(5):
            self.wiz[i].place(anchor="nw", height=30, relwidth=0.2, relx=0.01, rely=0.01+i*.06)

        # Tabbed NoteBook
        self.notes = Book(self)

    def Open(self):
        """ Open file for editing """

        # create open dialog to select file
        filename = filedialog.askopenfilename(initialdir=path, filetypes=[("saved game files",".GAM")])
        
        # ask to make backup
        b = messagebox.askyesno("Save ", "           Back up file?")
        
        # if a file is selected, open it into notes 
        if filename != "":
            self.notes.Open(filename,b)
            
        # if there is editable data, populate the wizard list
        if self.notes.data.dataFile != None and self.notes.data.dataArray != []:
            for i in range(5):
                name = ""
                for data in range(20):
                    name = name + chr(self.notes.data.get(Wiz_Start+i*Wiz_Block+Wiz_Offs["name"]+data))
                self.wiz[i]["text"] = name
            self.wiz_num.set(0)
            self.Select()

    def Save(self):
        """ Save data to file """

        if self.notes.data.dataFile == None or self.notes.data.dataFile.closed:
            messagebox.showwarning("", "No file currently open")
        else:
            # confirm and write to file
            if messagebox.askyesno("Save file", "           Save current file? \n (Changes cannot be undone)"):
                self.notes.data.save()
            
    def Close(self):
        """ Clear data without saving """

        if self.notes.data.dataFile == None or self.notes.data.dataFile.closed:
            messagebox.showwarning("", "No file currently open")
        else:
            # confirm, close the file, and clear the Frame
            s = messagebox.askyesno("Close file", "          Close current file? \n (unsaved changes will be lost)")
            self.notes.data.close(s)
            # clear wizard list
            for i in range(5):
                name = "Wizard " + str(i)
                self.wiz[i]["text"] = name
            self.Select()
         
    def Exit(self, X=False):
        """ close editor without saving (if no file open or [X] button was pressed don't even ask) """

        # confirm and exit
        if self.notes.data.dataFile == None or X:
            root.destroy()
        elif messagebox.askyesno("Exit", "              Exit Editor? \n (unsaved changes will be lost)"):
            self.notes.data.close()            
            root.destroy()

    def Select(self):
        """ select wizard to edit """

        # only if there is data to edit
        if self.notes.data.dataArray != []:
            # wizard number (position in wizard list)
            wiz = self.wiz_num.get()

            # *****************************
            # remember wizard number
            # *****************************
            self.notes.wiz_num = wiz

            # *****************************
            # populate Wizard tab data
            # *****************************
            
            # write wizard name on tab
            
            name = ""
            for i in range(20):
                name = name + chr(self.notes.data.get(Calc_Addr("wiz",wiz,"name")+i))   
            self.notes.wizard.name_label["text"] = name
            
            # write wizard gold on tab
            
            gold = 0
            for i in range(2):
                gold += self.notes.data.get(Calc_Addr("wiz",wiz,"gold")+i)*(256**i)
            self.notes.wizard.gold_label["text"] = str(gold)
            
            # write wizard mana on tab
            
            mana = 0
            for i in range(2):
                mana += self.notes.data.get(Calc_Addr("wiz",wiz,"mana")+i)*(256**i)
            self.notes.wizard.mana_label["text"] = str(mana)
            
            # write wizard skill on tab
            
            skill = 0
            for i in range(4):
                skill += self.notes.data.get(Calc_Addr("wiz",wiz,"skill")+i)*(256**i)
            root_skill = sqrt(skill)
            if root_skill - floor(root_skill) < 0.5:
                skill = floor(root_skill)
            else:
                skill = ceil(root_skill)
            self.notes.wizard.skill_label["text"] = str(skill)
            
            # write spell being cast on tab
            
            spell = -1
            for i in range(2):
                spell += self.notes.data.get(Calc_Addr("wiz",wiz,"spell_cast")+i)*(256**i)
            if spell < 0:
                self.notes.wizard.cast_label["text"] = "None"
            else:
                self.notes.wizard.cast_label["text"] = Spells[spell]

            # write casting remaining on tab

            rem = 0
            for i in range(2):
                rem += self.notes.data.get(Calc_Addr("wiz",wiz,"cast_rem")+i)*(256**i)
            self.notes.wizard.cast_rem_label["text"] = str(rem)

            # write spell being researched on tab
            
            spell = -1
            for i in range(2):
                spell += self.notes.data.get(Calc_Addr("wiz",wiz,"spell_rsch")+i)*(256**i)
            if spell < 0:
                self.notes.wizard.rsch_label["text"] = "None"
            else:
                self.notes.wizard.rsch_label["text"] = Spells[spell]

            # write research remaining on tab
            
            rem = 0
            for i in range(2):
                rem += self.notes.data.get(Calc_Addr("wiz",wiz,"rsch_rem")+i)*(256**i)
            self.notes.wizard.rsch_rem_label["text"] = str(rem)

            # populate spellbooks on tab
            for i in range(5):
                books = self.notes.data.get(Calc_Addr("wiz",wiz,"spellbooks")+(2*i))
                self.notes.wizard.book_label[i]["text"] = str(books)
 
            # populate ability list

            for i in range(18): 
                self.notes.abil_states[i].set(self.notes.data.get(Calc_Addr("wiz",wiz,"abils")+i))



            # *****************************
            # populate Spells tab data
            # *****************************
            
            for i in range(len(Spells)):
                self.notes.spells.spell_list[i].Set(self.notes.data.get(Calc_Addr("wiz",wiz,"spells")+i))

            # *****************************
            # populate Cities tab (just the list)
            # *****************************
            
            # find total number of cites
            num_cities = self.notes.data.get(Num_Cities) + 16*self.notes.data.get(Num_Cities+1)
            
            self.notes.wiz_cities = []
            self.notes.wiz_cit_num = []

            # test each city
            for cit in range(num_cities):
                name = ""

                # if the city belongs to the current wizard, put its name and position in the lists
                if self.notes.data.get(Calc_Addr("cit",cit,"owner")) == wiz:
                    for i in range(13):
                        if self.notes.data.get(Calc_Addr("cit",cit,"name")+i) != 0:
                            name = name + chr(self.notes.data.get(Calc_Addr("cit",cit,"name")+i))                 
                    self.notes.wiz_cities.append(name)
                    self.notes.wiz_cit_num.append(cit)
            
            # put all the names in the list of cities on the dropdown menu
            m = self.notes.cities.city_sel.children['!menu']
            m.delete(0,END)
            for val in self.notes.wiz_cities:
                m.add_command(label=val,command=lambda v=self.notes.city_var,l=val:v.set(l))
            if len(self.notes.wiz_cities) > 0:
                self.notes.city_var.set(self.notes.wiz_cities[0])
            
            
        else:
            # clear Wizard tab data
            self.notes.wizard.name_label["text"] = ""
            self.notes.wizard.gold_label["text"] = ""
            self.notes.wizard.mana_label["text"] = ""
            self.notes.wizard.skill_label["text"] = ""
            self.notes.wizard.cast_label["text"] = ""
            self.notes.wizard.cast_rem_label["text"] = ""
            self.notes.wizard.rsch_label["text"] = ""
            self.notes.wizard.rsch_rem_label["text"] = ""
            for i in range(5):
                self.notes.wizard.book_label[i]["text"] = ""
            for i in range(18):
                self.notes.abil_states[i].set(0)

            # clear Spells tab data
            for spell in self.notes.spells.spell_list:
                spell.Set(0)

            # clear Cities tab data
            m = self.notes.cities.city_sel.children['!menu']
            m.delete(0,END)
            self.notes.city_var.set("<empty>")
            self.notes.cities.name_label["text"] = ""
            self.notes.cities.plane_label["text"] = ""
            self.notes.cities.x_label["text"] = ""
            self.notes.circle_var.set(0)
            self.notes.fort_var.set(0)
            self.notes.cities.y_label["text"] = ""
            for i in range(len(Buildings)):
                self.notes.building_states[i].set(0)
            for i in range(21):
                self.notes.cities.map_label[i]["image"] = ""
            

app = App(root)
app.mainloop()
