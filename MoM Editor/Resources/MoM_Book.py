#######################################################
#
#  MoM_Book
#
#  ttk Tabbed Notebook extention for Master of Magic save editor
#
#  Author:  John Marley
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
from Resources.My_Widgets import PopupDialog, MultiCheckButton, EditLabel
from Resources.Data_Array import *
from Resources.MoM_Helper_Methods import *
from Resources.MoM_Save_Game_Stuff import *

class Book(Notebook):
    """ Tabbed Notebook extention for Master of Magic save editor """
   
    def __init__(self,master=None):
        """ class constructor (duh) """
        
        Notebook.__init__(self,master)
        self.data = Data_Array
        self.place(anchor="nw", relheight=1, relwidth=0.87, relx=0.13, rely=0)
        self.wiz_num = 0
        self.abil_states = [IntVar() for i in range(18)]
        self.spell_states = [IntVar() for i in range(len(Spells))]
        self.city_var = StringVar()
        self.wiz_cities = []
        self.wiz_cit_num = []
        self.circle_var = IntVar()
        self.fort_var = IntVar()
        self.building_states = [IntVar() for i in range(len(Buildings))]
        self.city_map = [Image for i in range(21)]
        self.city_map_show = [Image for i in range(21)]

        self.add_Tabs()

    def Open(self, filename, backup=True):
        """open file to edit (create instance of data) """

        self.data = Data_Array(filename, backup)
 
    def add_Tabs(self):
        self.wizard = Frame(self)
        self.Wiz_Tab()
        self.spells = Frame(self)
        self.Spell_Tab()
        self.cities = Frame(self)
        self.City_Tab()
        self.units = Frame(self)
        self.Units_Tab()
        self.heroes = Frame(self)
        self.Heroes_Tab()
        self.items = Frame(self)
        self.Items_Tab()
        self.add(self.wizard, text="  Wizard  ")
        self.add(self.spells, text="  Spells  ")
        self.add(self.cities, text="  Citys  ")
        self.add(self.units, text="  Units  ")
        self.add(self.heroes, text="  Heroes  ")
        self.add(self.items, text="  Items  ")

    ################  Wizard Data Tab ##################
    def Wiz_Tab(self):      
        """ create widgets for Wizard Data Tab """

        # labels for wizard name
        
        Label(self.wizard,
              text = "Name :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0,
                      rely=0
                      )
        
        self.wizard.name_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised"
                                       )
        self.wizard.name_label.place(anchor="nw",
                                     height=25,
                                     width=165,
                                     relx=0.05,
                                     rely=0
                                     )
        self.wizard.name_label.bind("<ButtonRelease-1>", partial(self.Change_Text, "wiz", 20))

        # labels for wizard gold
        
        Label(self.wizard,
              text = "Gold :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0,
                      rely=0.10
                      )

        self.wizard.gold_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised",
                                       anchor="e",
                                       padding = [0,0,4,0]
                                       )
        self.wizard.gold_label.place(anchor="nw",
                                     height=25,
                                     width=48,
                                     relx=0.046,
                                     rely=0.10
                                     )
        self.wizard.gold_label.bind("<ButtonRelease-1>", partial(self.Change_Value, "wiz", Wiz_Offs["gold"], "New Gold:"))

        # labels for wizard mana
        Label(self.wizard,
              text = "Mana :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0,
                      rely=0.16
                      )

        self.wizard.mana_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised",
                                       anchor="e",
                                       padding = [0,0,4,0]
                                       )
        self.wizard.mana_label.place(anchor="nw",
                                     height=25,
                                     width=48,
                                     relx=0.046,
                                     rely=0.16
                                     )
        self.wizard.mana_label.bind("<ButtonRelease-1>", partial(self.Change_Value, "wiz", Wiz_Offs["mana"], "New Mana:"))

        # labels for wizard skill
        Label(self.wizard,
              text = "Skill :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0,
                      rely=0.22
                      )

        self.wizard.skill_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised",
                                       anchor="e",
                                       padding = [0,0,4,0]
                                       )
        self.wizard.skill_label.place(anchor="nw",
                                     height=25,
                                     width=48,
                                     relx=0.046,
                                     rely=0.22
                                     )
        self.wizard.skill_label.bind("<ButtonRelease-1>", partial(self.Change_Value, "wiz", Wiz_Offs["skill"],"New Skill:"))

        # labels for current spell being cast
        Label(self.wizard,
              text = "Current casting :"
              ).place(anchor="nw",
                      height=25,
                      width=105,
                      relx=0,
                      rely=0.36
                      )

        self.wizard.cast_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised",
                                       )
        self.wizard.cast_label.place(anchor="nw",
                                     height=25,
                                     width=165,
                                     relx=0.03,
                                     rely=0.40
                                     )

        #labels for casting remaining
        Label(self.wizard,
              text = "Casting remaining :"
              ).place(anchor="nw",
                      height=25,
                      width=108,
                      relx=0,
                      rely=0.44
                      )

        self.wizard.cast_rem_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised",
                                       anchor="e",
                                       padding = [0,0,4,0]
                                       )
        self.wizard.cast_rem_label.place(anchor="nw",
                                     height=25,
                                     width=48,
                                     relx=0.03,
                                     rely=0.48
                                     )
        self.wizard.cast_rem_label.bind("<ButtonRelease-1>", partial(self.Change_Value, "wiz", Wiz_Offs["cast_rem"], "New remaining:"))

        # labels for current spell being researched
        Label(self.wizard,
              text = "Current Researching :"
              ).place(anchor="nw",
                      height=25,
                      width=150,
                      relx=0,
                      rely=0.54
                      )

        self.wizard.rsch_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised",
                                       )
        self.wizard.rsch_label.place(anchor="nw",
                                     height=25,
                                     width=165,
                                     relx=0.03,
                                     rely=0.58
                                     )

        #labels for research remaining
        Label(self.wizard,
              text = "Research remaining :"
              ).place(anchor="nw",
                      height=25,
                      width=108,
                      relx=0,
                      rely=0.62
                      )

        self.wizard.rsch_rem_label = Label(self.wizard,
                                       text = "",
                                       relief = "raised",
                                       anchor="e",
                                       padding = [0,0,4,0]
                                       )
        self.wizard.rsch_rem_label.place(anchor="nw",
                                     height=25,
                                     width=48,
                                     relx=0.03,
                                     rely=0.66
                                     )
        self.wizard.rsch_rem_label.bind("<ButtonRelease-1>", partial(self.Change_Value, "wiz", Wiz_Offs["rsch_rem"], "New remaining:"))

        # labels for spellbooks
        Label(self.wizard,
              text = "Spellbooks :"
              ).place(anchor="nw",
                      height=25,
                      width=105,
                      relx=0.25,
                      rely=0.10
                      )

        for i in range(5):       
            Label(self.wizard,
                  text = Spellbooks[i] + " :"
                  ).place(anchor="nw",
                          height=25,
                          width=105,
                          relx=0.28,
                          rely=0.16 + 0.06 * i
                          )

        self.wizard.book_label = []
        for i in range(5):
            self.wizard.book_label.append(Label(self.wizard,
                                                relief = "raised",
                                                anchor="e",
                                                padding = [0,0,4,0]
                                                )
                                          )
        for i in range(5):
            self.wizard.book_label[i].place(anchor="nw",
                                     height=25,
                                     width=26,
                                     relx=0.34,
                                     rely=0.16 + 0.06*i
                                     )
            self.wizard.book_label[i].bind("<ButtonRelease-1>", partial(self.Change_Value, "wiz", Wiz_Offs["spellbooks"]+(2*i), "New Books:"))


        # labels for abilites
        self.wizard.abil_label = []

        Label(self.wizard,
              text = "Abilities :"
              ).place(anchor="nw",
                      height=25,
                      width=105,
                      relx=0.5,
                      rely=0.10
                      )

        for i in range(18):
            self.wizard.abil_label.append(Checkbutton(self.wizard,
                                               text = Abilities[i],
                                               var = self.abil_states[i],
                                               command = self.Change_Abils
                                               )
                                   )
            


        for i in range(9):
            self.wizard.abil_label[i].place(anchor="nw",
                                     height=25,
                                     width=110,
                                     relx=0.53,
                                     rely=0.16 + 0.06*i
                                     )
                                   
        for i in range(9,18):
            self.wizard.abil_label[i].place(anchor="nw",
                                     height=25,
                                     width=110,
                                     relx=0.78,
                                     rely=0.16 + 0.06*(i-9)
                                     )

    ################  Spell Data Tab ##################
    def Spell_Tab(self):      
        """ create widgets for Spell Data Tab """

        # create spell category labels
        for i in range(5):
            Label(self.spells,
                  text=Spellbooks[i]
                  ).place(anchor="nw",
                          height=25,
                          width=75,
                          relx=0.02+i*0.168,
                          rely=0.01
                          )
            Label(self.spells,
                  text="Arcane"
                  ).place(anchor="nw",
                          height=25,
                          width=75,
                          relx=0.86,
                          rely=0.01
                          )

            # create spell lists
            self.spells.spell_list = []
            for i in range(len(Spells)):
                self.spells.spell_list.append(MultiCheckButton(self.spells,
                                                               width=16,
                                                               text = Spells[i],
                                                               state_sym = Spell_Status,
                                                               skip_states = [3]
                                                               )
                                              )
            

            for i in range(len(Spells)):
                self.spells.spell_list[i].place(anchor="nw",
                                               height=22,
                                               width=150,
                                               relx=0.03+0.168*int(i/40),
                                               rely=0.0375+0.0235*(i%40)
                                               )
                self.spells.spell_list[i].lbl.bind("<ButtonRelease-1>", self.Change_Spell, add="+")
        
            # create legend for statuses
            temp = ["Unknowable",
                    "Researchable",
                    "Known",
                    "On Research Page"
                    ]
            
            for i in range(len(Spell_Status)):
                Label(self.spells,
                      text = Spell_Status[i] + " : " + temp[i],
                      ).place(anchor="nw",
                              height = 25,
                              relx = 0.87,
                              rely = 0.66 + 0.024*i
                              )
            
    ################  City Data Tab ##################
    def City_Tab(self):      
        """ create widgets for City Data Tab """

        # city-to-edit selection menu
        self.cities.city_sel = OptionMenu(self.cities,
                                          self.city_var,
                                          "<empty>")
        self.cities.city_sel.place(anchor="nw",
                                   height=25,
                                   width=100,
                                   relx=0.01,
                                   rely=0.01
                                   )

        # separator
        self.cities.separator = Separator(self.cities,
                                          orient="vertical")
        self.cities.separator.place(relx=0.15,
                                     rely = 0.01,
                                     height = 800
                                     )

        # city name
        
        Label(self.cities,
              text = "Name :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0.16,
                      rely=0.02
                      )
        
        self.cities.name_label = Label(self.cities,
                                       text = "",
                                       relief = "raised"
                                       )
        self.cities.name_label.place(anchor="nw",
                                     height=25,
                                     width=90,
                                     relx=0.20,
                                     rely=0.02
                                     )
        self.cities.name_label.bind("<ButtonRelease-1>", partial(self.Change_Text, "cit", 13))

        # plane
        Label(self.cities,
            text = "Plane :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0.16,
                      rely=0.10
                      )

        self.cities.plane_label = Label(self.cities,
                                        text="",
                                        relief="raised"
                                        )
        self.cities.plane_label.place(anchor="nw",
                                      height=25,
                                      width=56,
                                      relx=0.20,
                                      rely=0.10
                                      )

        self.cities.plane_label.bind("<ButtonRelease-1>", partial(self.Move_City))


        # x coordinate
        Label(self.cities,
            text = "X :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0.16,
                      rely=0.15
                      )

        self.cities.x_label = Label(self.cities,
                                    text="",
                                    relief="raised"
                                    )
        self.cities.x_label.place(anchor="nw",
                                  height=25,
                                  width=40,
                                  relx=0.20,
                                  rely=0.15
                                  )

        self.cities.x_label.bind("<ButtonRelease-1>", partial(self.Move_City))

        # y coordinate
        Label(self.cities,
            text = "Y :"
              ).place(anchor="nw",
                      height=25,
                      width=48,
                      relx=0.16,
                      rely=0.20
                      )

        self.cities.y_label = Label(self.cities,
                                    text="",
                                    relief="raised"
                                    )
        self.cities.y_label.place(anchor="nw",
                                  height=25,
                                  width=40,
                                  relx=0.20,
                                  rely=0.20
                                  )

        self.cities.y_label.bind("<ButtonRelease-1>", partial(self.Move_City))

        # has summoning circle?
        self.cities.circle_label = Checkbutton(self.cities,
                                               text="Summoning Circle",
                                               var=self.circle_var,
                                               command=self.Set_Circle
                                               )
        self.cities.circle_label.place(anchor="nw",
                                       height=25,
                                       width=160,
                                       relx=0.40,
                                       rely=0.15
                                       )
        
        # has fortress?
        self.cities.fort_label = Checkbutton(self.cities,
                                             text="Wizard Fortress",
                                             var=self.fort_var,
                                             command=self.Set_Fortress
                                             )
        self.cities.fort_label.place(anchor="nw",
                                     height=25,
                                     width=160,
                                     relx=0.40,
                                     rely=0.10
                                     )

        # Buildings
        self.cities.building_label = []

        Label(self.cities,
              text = "Buildings :"
              ).place(anchor="nw",
                      height=25,
                      width=105,
                      relx=0.6,
                      rely=0.06
                      )
 
        for i in range(len(Buildings)):
            self.cities.building_label.append(Checkbutton(self.cities,
                                                          text = Buildings[i],
                                                          var = self.building_states[i],
                                                          )
                                              )
            


        half_list = int(len(Buildings)/2)
        for i in range(half_list):
            self.cities.building_label[i].place(anchor="nw",
                                                height=25,
                                                width=125,
                                                relx=0.63,
                                                rely=0.10 + 0.05*i
                                                )
                                   
        for i in range(half_list,len(Buildings)):
            self.cities.building_label[i].place(anchor="nw",
                                                height=25,
                                                width=150,
                                                relx=0.80,
                                                rely=0.10 + 0.05*(i-half_list)
                                                )

        for i in range(len(Buildings)):
            self.cities.building_label[i].bind("<ButtonRelease-1>", partial(self.Change_Buildings))


        # map tiles
        self.cities.map_offs = [-121,-120,-119,-62,-61,-60,-59,-58,-2,-1,0,1,2,58,59,60,61,62,119,120,121]

        self.cities.map_frame = Label(self.cities
                                      )
        self.cities.map_frame.place(anchor="nw",
                                    height= 250,
                                    width=250,
                                    relx=0.2,
                                    rely=0.5
                                    )
                                    
        self.cities.map_label = []

        for i in range(21):
            self.cities.map_label.append(Label(self.cities.map_frame,
                                               text="",
                                               relief="solid",
                                               anchor="center"
                                               )
                                         )

        for i in range(3):
            self.cities.map_label[i].place(anchor="nw",
                                           height=50,
                                           width=50,
                                           x=49+49*i,
                                           y=0
                                           )
        for i in range(5):
            self.cities.map_label[i+3].place(anchor="nw",
                                             height=50,
                                             width=50,
                                             x=49*i,
                                             y=49
                                             )
        for i in range(5):
            self.cities.map_label[i+8].place(anchor="nw",
                                             height=50,
                                             width=50,
                                             x=49*i,
                                             y=98
                                             )
        for i in range(5):
            self.cities.map_label[i+13].place(anchor="nw",
                                              height=50,
                                              width=50,
                                              x=49*i,
                                              y=147
                                              )
        for i in range(3):
            self.cities.map_label[i+18].place(anchor="nw",
                                              height=50,
                                              width=50,
                                              x=49+49*i,
                                              y=196
                                              )

        for i in range(21):
            self.cities.map_label[i].bind("<ButtonRelease-1>", partial(self.Change_Map, i))
            self.cities.map_label[i].bind("<ButtonRelease-3>", partial(self.Change_Road, i))
        
        # change city data when new city is selected
        self.city_var.trace("w", self.Pop_City)
    
    ################  Units Data Tab ##################
    def Units_Tab(self):      
        """ create widgets for Units Data Tab """
        pass

    ################  Heroes Data Tab ##################
    def Heroes_Tab(self):      
        """ create widgets for Heroes Data Tab """

        def Populate():
            pass
        
        self.hero_list = []
        self.hero_num = IntVar()
        for i in range(6):
            self.hero_list.append(Radiobutton(self.heroes,
                                              text="Empty",
                                              variable=self.hero_num,
                                              value=i,
                                              command=Populate
                                              )
                                  )
        for i in range(6):
            self.hero_list[i].place(anchor="nw",
                                    width=100,
                                    height=25,
                                    relx=0.01,
                                    rely=0.03+0.06*i
                                    )

        Label(self.heroes,
              text="Name :"
              ).place(anchor="nw",
                      height=25,
                      width=70,
                      relx=0.2,
                      rely=0.06
                      )

        self.hero_name = Label(self.heroes,
                               text="",
                               width=25,
                               relief = "raised"

                               )
        self.hero_name.place(anchor="nw",
                             height=25,
                             width=100,
                             relx=0.21,
                             rely=0.10
                             )

    ################  Items Data Tab ##################
    def Items_Tab(self):      
        """ create widgets for Items Data Tab """
        pass

    #################################
    # Methods
    #################################
    
    def Change_Text(self, typ, length, event=None):
        """ edit wizard name """

        # only if there is a wizard selcted to edit
        if self.wizard.name_label["text"] != "":
            # wizard number    
            wiz = self.wiz_num
            
            # starting data address of text

            # if wizard data (or hero name, which is in the wizard data block
            if typ == "wiz":
                text_addr = Wiz_Start + Wiz_Block*wiz + Wiz_Offs["name"]
            elif typ == "cit":
                cit_num = self.wiz_cities.index(self.city_var.get())
                cit = self.wiz_cit_num[cit_num]
                text_addr = City_Start + City_Block*cit + City_Offs["name"]
            # open a queryBox for new name
            text = PopupDialog().queryBox("Enter new name")
            
            # if a name was entered, update fields
            if text:
                # change the Notebook label that called the method
                event.widget['text'] = text
                
                # change the name in the wizard list if editing wizard name
                if typ == "wiz":
                    self.master.wiz[wiz]["text"] = text
                    
                # change name in city list if changing city name
                elif typ == "cit":
                    m = self.cities.city_sel.children['!menu']
                    m.delete(cit_num)
                    m.insert_command(cit_num, label=text,command=lambda v=self.city_var,l=text:v.set(l))
                    self.wiz_cities[cit_num] = text
                    self.city_var.set(text)
                    
                # change the name in the file data 
                for l in range(length):
                    if l < len(text):
                        # overwrite data array bytes 
                        self.data.set(text_addr+l, ord(text[l]))
                    else:
                        # fill the remaining name data with zeros
                        self.data.set(text_addr+l,0)
 
          
    def Change_Value(self, typ, offset, msg=None, event=None):
        """ edit wizard selected value """
                                     
        # only if there is a wizard selcted to edit
        if self.wizard.name_label["text"] != "":

            # valid flag
            okay = True
            
            # of bytes in data array that hold value (2 is typical)
            num_bytes = 2
 
            # starting data addresses

            # changing wizard data
            if typ == "wiz":
                addr = Wiz_Start + Wiz_Block*self.wiz_num + offset
                
            # changing city data
            elif typ == "cit":
                addr = self.city_addr + offset
                
            # create a numBox to enter new value
            val = PopupDialog().numBox(neg="False",real="False", msg=msg)

            if val and (typ == "cit"):
                if offset == City_Offs["X"]:
                    if val < Map_Width:
                        num_bytes = 1
                    else:
                        okay = False
                elif offset == City_Offs["Y"]:
                    if val < Map_Height:
                        num_bytes = 1
                    else:
                        okay = False
                        
            # if a value was entered
            if val and okay:
                # change label
                event.widget["text"] = str(val)

                # skill is different.
                #    the square of skill is stored in 4 byte
                if offset == Wiz_Offs["skill"]:
                    val *= val
                    num_bytes = 4
                
                byte_lst = []
                # calcultate "little-end first" byte storage for value
                for i in range(num_bytes):
                    pwr = i+1
                    tmp = val%(256**pwr)
                    byte_lst.append(int(tmp/(256**i)))
                    val -= tmp
                for i in range(num_bytes):
                    # overwrite byte storage 
                    self.data.set(addr+i, byte_lst[i])
                            
    def Change_Abils(self, event=None):
        """ edit wizard abilities """
        
        # only if there is a wizard selcted to edit
        if self.wizard.name_label["text"] != "":
            # starting data address
            addr = Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["abils"]
            
            for i in range(18):
                self.data.dataArray.pop(addr+i)
                #write new value byet to data
                self.data.dataArray.insert(addr+i, self.abil_states[i].get())

    def Change_Spell(self, event=None):
        """ edit wizard spell list """
        
        # only if there is a wizard selcted to edit
        if self.wizard.name_label["text"] != "":
            # wizard number    
            wiz = self.wiz_num

            # starting data address
            i = self.spells.spell_list.index(event.widget.master)
            addr = Wiz_Start+Wiz_Block*wiz+Wiz_Offs["spells"]+i
            
            # overwrite data value
            self.data.set(addr, self.spells.spell_list[i].Get())

    def Change_Plane(self, event=None):
        """ change a city's plane """

        fort = self.isFort()
        circle = self.isCircle()
                
        p = PopupDialog(self).boolBox("Choose plane", "Arcanus", "Myrror");
        if p:
            self.cities.plane_label["text"] = "Arcanus"
            self.data.set(self.city_addr+City_Offs["plane"], 0)
            if fort:
                self.data.set(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["plane"], 0)
            if circle:
                self.data.set(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_plane"], 0)
        else:
            self.cities.plane_label["text"] = "Myrror"
            self.data.set(self.city_addr+City_Offs["plane"], 1)
            if fort:
                self.data.set(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["plane"], 1)
            if circle:
                self.data.set(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_plane"], 1)
        

    def Pop_City(self, *args):
        """ populate the City tab with data for selected city """

        if self.city_var.get() != "<empty>":
            # calculate and store address of current city
            cit_num = self.wiz_cities.index(self.city_var.get())
            self.city_addr = City_Start + City_Block*self.wiz_cit_num[cit_num]
            self.map_addr =  self.data.get(self.city_addr+City_Offs["X"]) + self.data.get(self.city_addr+City_Offs["Y"])*Map_Width

            # set Myrror flag
            myr_flag = False
            if self.data.get(self.city_addr+City_Offs["plane"]) == 1:
                myr_flag = True

            # populate name
            self.cities.name_label["text"] = self.city_var.get()

            # populate plane
            if not myr_flag:
                self.cities.plane_label["text"] = "Arcanus"
            else:
                self.cities.plane_label["text"] = "Myrror"
                
            # populate coordinates
            self.cities.x_label["text"] = str(self.data.get(self.city_addr+City_Offs["X"]))
            self.cities.y_label["text"] = str(self.data.get(self.city_addr+City_Offs["Y"]))

            # set summoning circle checkbutton
            if self.isCircle():
                self.circle_var.set(1)
            else:
                self.circle_var.set(0)
                                
           # set fortress checkbutton
            if self.isFort():
                self.fort_var.set(1)
            else:
                self.fort_var.set(0)

            # set building checkbuttons
            for i in range(len(Buildings)):
                if 0 <= self.data.get(self.city_addr+City_Offs["buildings"]+i) <= 1:
                    self.building_states[i].set(1)
                else:
                    self.building_states[i].set(0)

            # create map

            for i in range(21):

                addr = self.map_addr+self.cities.map_offs[i]

                # determine plane maps to use
                if not myr_flag:
                    dep = self.data.get(Bonus_Start_Arc+self.map_addr+self.cities.map_offs[i])
                    plane_start = Terrain_Start_Arc
                    flag_start = Flag_Start_Arc
                else:
                    dep = self.data.get(Bonus_Start_Myr+self.map_addr+self.cities.map_offs[i])
                    plane_start = Terrain_Start_Myr
                    flag_start = Flag_Start_Myr

                # terrain tiles
                self.ter_tiles = Image.open(Tile_File)
                
                # find tile in master image
                width = 20
                buf=3

                n = self.data.get(plane_start+addr*2) + self.data.get(plane_start+addr*2+1)*256

                if myr_flag:
                    n += 888

                n = Tiles(n)

                left = buf + (width+buf)*n
                right = left + width

                tile = self.ter_tiles.crop((left,3,right,20))
                tile = tile.convert("RGBA")

                # store unmodified terrain tile 
                self.city_map[i] = tile.copy()
                
                # add bonus deposits 
                if i != 10:
                    for k, v in Map_Bonuses.items():
                        if v == dep and dep != 0:
                            # create filename of bounus deposit image
                            bonus = Merge_Strings(Bonus_Path, k, ".png")
                            Mask(tile,Image.open(bonus))


                    road = False
                    ench = False
                    if self.data.get(flag_start+addr) & Terr_Flags["road"]:
                        road = True
                        if self.data.get(flag_start+addr) & Terr_Flags["enchanted road"]:
                            ench = True

                    if road:
                        if ench:
                            Mask(tile, Image.open(Merge_Strings(Road_Path, "EnRoad None.png")))
                        else:
                            Mask(tile, Image.open(Merge_Strings(Road_Path, "Road None.png")))
                        for d in Directions:
                            if self.data.get(flag_start+addr+Around[Directions.index(d)]) & Terr_Flags["road"]:
                                if ench:
                                    Mask(tile, Image.open(Merge_Strings(Road_Path, "EnRoad ",d,".png")))
                                else:
                                    Mask(tile, Image.open(Merge_Strings(Road_Path, "Road ",d,".png")))

                # draw city
                else:
                    if self.data.get(self.city_addr+City_Offs["size"]) < 2:
                        town = Town_Path + "Village.png"
                        Mask(tile,Image.open(town))
                    elif self.data.get(self.city_addr+City_Offs["size"]) < 4:
                        town = Town_Path + "Town.png"
                        Mask(tile,Image.open(town))
                    elif self.data.get(self.city_addr+City_Offs["size"]) < 5:
                        town = Town_Path + "Town2.png"
                        Mask(tile,Image.open(town))
                    else:
                        town = Town_Path + "City.png"
                        Mask(tile,Image.open(town))
                        
                # show modified terrain tile on map
                self.city_map_show[i] = ImageTk.PhotoImage(tile.resize((50,50)))              
                self.cities.map_label[i]["image"] = self.city_map_show[i]


    def Move_City(self, event=None):
        """ change the X or Y coordinate of a city """

        fort = self.isFort()
        circle = self.isCircle()

        oldPlane = str(self.data.get(self.city_addr+City_Offs["plane"]))
        oldX = str(self.data.get(self.city_addr+City_Offs["X"]))
        oldY = str(self.data.get(self.city_addr+City_Offs["Y"]))

        # change plane if needed
        if str(event.widget) == ".!app.!book.!frame3.!label4":
            p = PopupDialog(self).boolBox("Choose plane", "Arcanus", "Myrror");
            if p:
                self.cities.plane_label["text"] = "Arcanus"
                self.data.set(self.city_addr+City_Offs["plane"], 0)
            else:
                self.cities.plane_label["text"] = "Myrror"
                self.data.set(self.city_addr+City_Offs["plane"], 1)

        event.widget = self.cities.x_label
        self.Change_Value("cit", City_Offs["X"], "New X:", event)

        event.widget = self.cities.y_label        
        self.Change_Value("cit", City_Offs["Y"], "New Y:", event)

        self.map_addr = self.data.get(self.city_addr+City_Offs["X"]) + self.data.get(self.city_addr+City_Offs["Y"])*Map_Width

        if (str(self.data.get(self.city_addr+City_Offs["plane"])) != oldPlane) or \
                (str(self.data.get(self.city_addr+City_Offs["X"])) != oldX) or \
                    (str(self.data.get(self.city_addr+City_Offs["Y"])) != oldY):

            # change fortress coordinates if needed
            if fort:
                self.Set_Fortress()

            # change circle coordinates if needed
            if circle:
                self.Set_Circle() 

            # put a road in the new city location
            self.Make_Road(self.map_addr, self.data.get(self.city_addr+City_Offs["plane"]))

            # re-populate the city data to update the map
            self.Pop_City()
            
    def isFort(self):
        """ determine if the wizard's fortress is in city """
        
        fort = False
        if self.data.get(self.city_addr + City_Offs["X"]) == self.data.get(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["X"]):
            if self.data.get(self.city_addr + City_Offs["Y"]) == self.data.get(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["Y"]):
                if self.data.get(self.city_addr + City_Offs["plane"]) == self.data.get(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["plane"]):
                    fort = True

        return fort

    def isCircle(self):
        """ determine if the wizard's summoning circle is in city """
        
        circle = False
        if self.data.get(self.city_addr + City_Offs["X"]) == self.data.get(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_X"]):
            if self.data.get(self.city_addr + City_Offs["Y"]) == self.data.get(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_Y"]):
                if self.data.get(self.city_addr + City_Offs["plane"]) == self.data.get(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_plane"]):
                    circle = True

        return circle

    def Set_Circle(self):
        """ set the summoning circle in city """
        
        if self.city_var.get() != "<empty>":
            if self.isCircle():
                self.circle_var.set(1)
            else:
                self.data.set(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_X"], self.data.get(self.city_addr+City_Offs["X"]))
                self.data.set(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_Y"], self.data.get(self.city_addr+City_Offs["Y"]))
                self.data.set(Wiz_Start+Wiz_Block*self.wiz_num+Wiz_Offs["circle_plane"], self.data.get(self.city_addr+City_Offs["plane"]))
                   
    def Set_Fortress(self, event=None):
        """ set the wizard's fortress in city """
        
        if self.city_var.get() != "<empty>":
            if self.isFort():
                self.fort_var.set(1)
            else:
                self.data.set(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["X"], self.data.get(self.city_addr+City_Offs["X"]))
                self.data.set(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["Y"], self.data.get(self.city_addr+City_Offs["Y"]))
                self.data.set(Fort_Start+Fort_Block*self.wiz_num+Fort_Offs["plane"], self.data.get(self.city_addr+City_Offs["plane"]))
            
               
    def Make_Road(self, addr, plane, ench=False):
        """ put a road on a map tile """

        # find starting point on plane
        if plane == 1:
            ench = True
            start = Move_Start_Myr + addr
            flag = Flag_Start_Myr + addr
        else:
            start = Move_Start_Arc + addr
            flag = Flag_Start_Arc + addr

        # iterate over movement maps and set cost to 1
        for typ, off in Mov_Map_Offs.items():
            if not ench:
                self.data.set(start+Mov_Block*off, 1)
            else:
                self.data.set(start+Mov_Block*off, 0)

        # set road terrain flag
        self.data.set(flag, self.data.get(flag) | Terr_Flags["road"])
        if ench:
            self.data.set(flag, self.data.get(flag) | Terr_Flags["enchanted road"])

           
    def Change_Buildings(self, event):
        """change buildings present in city """
        
        def Replace(i):
            if i in replace_list:
                self.building_states[i-1].set(1)
                self.data.set(self.city_addr+City_Offs["buildings"]+i-1, 0)
                Replace(i-1)

        okay = True

        # indices of buildings that replace others
        replace_list = [1,3,4,7,10,11,14,20,21,22,24,25,27]

        # find index and current state of selected building
        i = Buildings.index(event.widget["text"])
        curr_state = eself.data.get(self.city_addr+City_Offs["buildings"]+i)

        # hadling de-selecting buildings
        if self.building_states[i].get() == 1:

            # a building that has been replaced can't be de-selcted
            if curr_state == Building_States["replaced"]:
                self.building_states[i].set(0)
                okay = False

            if okay:
                self.data.set(self.city_addr+City_Offs["buildings"]+i, -1)
                if i in replace_list:
                    self.data.set(self.city_addr+City_Offs["buildings"]+i-1, 1)

        # handling selecting buildings
        else:
            self.data.set(self.city_addr+City_Offs["buildings"]+i, 1)
            Replace(i)           

    def Change_Map(self, i, event):
        """ change bonus deposits around city """

        # can't put bounus deposits on city tile
        if i != 10:

            # create popup dialog with bounuse
            b = PopupDialog().selectBox("", Map_Bonuses, True)
            if b:   
                tile = self.city_map[i].copy()
                
                # add bonus deposits
                if b[0] != "Nothing":
                    bonus = Bonus_Path + b[0] + ".png"
                    bonus_img = Image.open(bonus)
                    tile.paste(bonus_img,mask=bonus_img)
                
                self.city_map_show[i] = ImageTk.PhotoImage(tile.resize((50,50)))              
                self.cities.map_label[i]["image"] = self.city_map_show[i]
                
                # write bouns to edit array        
                if self.data.get(self.city_addr + City_Offs["plane"]) == 0:
                    self.data.set(Bonus_Start_Arc+self.map_addr+self.cities.map_offs[i], b[1])
                else:
                    self.data.set(Bonus_Start_Myr+self.map_addr+self.cities.map_offs[i], b[1])

    def Change_Road(self, i, event):
        """ change roads around city """

        ench = False
        
        road_dict = {"Road":1, "Enchanted Road":2}
#        if i != 10:
#            road_dict["No Road"] = 0

        r = PopupDialog().selectBox("", road_dict, True)
        if r:
            # use blank if no road
#            if r[1] == 0:
#                r[0] = "    "

            if r[1] == 2:
                ench = True
            txt = event.widget["text"]
            
            # remove old road type and add new (except city tile)
            if i != 10:
                txt = r[0][:4] + txt[4:]
                event.widget["text"] = txt

            self.Make_Road(self.map_addr+self.cities.map_offs[i], self.data.get(self.city_addr+City_Offs["plane"]), ench)

           
