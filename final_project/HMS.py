class Doctor:
    def __init__(self,id,name,specialization,workingtime,qualification,roomnumber):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.workingtime = workingtime
        self.qualification = qualification
        self.roomnumber = roomnumber


    def getID(self):
        return self.id

    def getName(self):
        return self.name
    def getSpecialization(self):
        return self.specialization
    def getworkingTime(self):
        return self.workingtime
    def getQualification(self):
        return self.qualification
    def getroomNumber(self):
        return self.roomnumber
# setter methods
    def setID(self,id):
        self.id = id
    def setName(self,name):
        self.name = name


def addDoctor(doc):
    file = open("doctors.txt","a")
    file.write(f"\n{doc.getID()}"+"_"+doc.getName()+"_"+doc.getSpecialization()+"_"+doc.getworkingTime()+"_"
               +doc.getQualification()+"_"+doc.getroomNumber())
    print("file is updated successfully")
    file.close()
def displayDoctorList():
    getlines = []
    results = []
    file = open("doctors.txt", "r")
    for line in file:
        getlines.append(line)
    for line in getlines:
        ls=line.replace("_"," ")
        results.append(ls)
    print(results[0])
    print(results[1])
       # ls = line.replace("_", " ")
        #print(ls)
    file.close()
def searchDoctorById(srchid):
    getlines = []
    results = []
    file = open("doctors.txt","r")
    for line in file:
        getlines.append(line)
    for line in getlines:
        #ls=line.replace("_"," ")
        if srchid in line:
            results.append(line)
        if not results:
            print("record not found")
        else:
            print(results)
        file.close()
def searchDoctorByName(srchname):
    getlines = []
    results = []
    file = open("doctors.txt", "r")
    for line in file:
        getlines.append(line)
    for line in getlines:
        # ls=line.replace("_"," ")
        if srchname in line:
            results.append(line)
        if not results:
            print("record not found")
        else:
            print(results)
        file.close()





