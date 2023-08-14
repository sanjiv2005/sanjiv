import HMS

def DisplayMenu():
    print("Welcome to Alberta Hospital (AH) Management system\n")
    while True:
        option = int(input("Select from the following options, or select 0 to stop:\n"
          "1-\tDoctors\n2-\tFacilities\n3-\tLaboratories\n4-\tPatients\n\n "))
        if option==1:
            print("\nDoctor's Menu:")
            choice = eval(input("1- Display Doctor's list\n2- Search for Doctor by ID\n3- Search for Doctor by name\n"
                                "4- Add doctor\n5- Edit doctor Info\n6- Back to the Main Menu"))

            if choice==1:
                HMS.displayDoctorList()
            elif choice==2:
                srchid = input("enter the doctor id:\n")
                HMS.searchDoctorById(srchid)
            elif choice==3:
                srchname = input("enter the doctor name:\n")
                HMS.searchDoctorByName(srchname)
            elif choice == 4:
                id = input("Enter the doctor's ID:\n")
                name = input("Enter the doctor's name:\n")
                specialization = input("Enter the doctor's speciality:\n")
                workingtime = input("Enter the doctor's timing (e.g., 7am-10pm):\n")
                qualification = input("Enter the doctor's qualification:\n")
                roomnumber = input("Enter the doctor's room number:\n")
                doc = HMS.Doctor(id, name, specialization, workingtime, qualification, roomnumber)
                HMS.addDoctor(doc)
            elif choice == 5:
                editid = input("Please enter the id of a doctor that you want to edit their information:\n")

DisplayMenu()