#######################################################
#
#  Data_Array class
#
#  Author:  John Marley
#
#######################################################

class Data_Array():
    """
    Reads binary data from a file and holds it as an array of integers

    Members:
        dataFile : file to be read and edited
        dataArray : array of integers that holds data read from file

    Methods:
        __init__ : read file and create array

                Parameters:
                    filename : string representing name of file to open
                                - must include path and extension
                    backup : boolean to create backup file or not

        isData : returns True if dataArray is not empty

        get : returns data read from given index in dataArray

                Parameter:
                    address : index of data to read

        set : writes data to given indes in dataArray

                Parameter:
                    address : index to write
                    data : data to write

        open : open new dataFile and data Array
                Parameters:
                    filename : string representing name of file to open
                                - must include path and extension
                    backup : boolean to create backup file or not

        save : saves dataArray to dataFile

        close : closes dataFile

                Parameter:
                    save : bolean to save first or not

        backup : saves dataArray to a .bak with incremented revision number
                
                    
                  
    """

    # members need to exist before __init__ is called for tkinter event reasons
    dataArray = []
    dataFile = None
    filename = None
      
        
    def __init__(self, filename=None, backup=True):
        """ open file and create array """

        # re-initialize members
        self.dataArray = []
        self.dataFile = None
        self.filename = None
        
        # open file
        self.open(filename, backup)
          
    def get(self, address):
        """ return data at given address """
        
        if address < len(self.dataArray):
            return self.dataArray[address]
        else:
            print("Out of range")
            return None

    def set(self, address, data):
        """ set data at given address """
        
        if address < len(self.dataArray):
            self.dataArray[address] = data
        else:
            print("Out of range")

    def open(self, filename, backup=True):
        """ open file and populate data array """

        if self.dataFile != None:
            self.dataFile.close()
        
        # open file containing data and populate data array
        if filename != None:

            # strip extention from filename and save for backup use
            for i in filename:            
                if i == ".":
                    tmp_name = filename[:filename.index(i)]
                    break
            self.filename = tmp_name + "_"
        
            self.dataFile = open(filename, mode="rb+")
            binaryArray = self.dataFile.read()
            for b in binaryArray:
                self.dataArray.append(int(b))

            # create backup file (if parameter is True)
            if backup:
                self.backup()
                
        else:
            print("No file given")
                
    def save(self, s=True):
        """ write data to file """

        if self.dataFile != None and not self.dataFile.closed:
            if s:
                if self.dataArray != []:
                    binaryArray = bytearray(self.dataArray)
                    self.dataFile.seek(0,0)
                    self.dataFile.write(binaryArray)
                else:
                    print("Nothing to save")
        else:
            print("No file open")

    def close(self, s=False):
        """ close file.  save first if parameter = True """

        self.save(s)
        self.dataFile.close()
        self.dataArray = []

    def backup(self):
        """ write data to backup file """
        
        # create initial _1 revision    
        backname = self.filename + "1.bak"

        # increment revision number if needed
        loop = True
        count = 1
        while loop:

            # if backup revision already exists, increment number
            try:
                backfile = open(backname, mode="rb")
                backfile.close()
                backname = self.filename + str(count) + ".bak"
                count += 1
                        
            # create new backup file
            except:
                loop = False

                backfile = open(backname, mode="wb")

        # write data to backup file and close
        binaryArray = bytearray(self.dataArray)
        backfile.write(binaryArray)
        backfile.close()

    

        


    
