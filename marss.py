from datetime import *

class Student():

    def __init__(self,
                 last_name,
                 first_name,
                 birth_date,
                 grade,
                 gender,
                 language=None,
                 marss_id=None,
                 hispanic_latino=None,
                 state_ethnicity=None,
                 address=None,
                 city=None,
                 state=None,
                 zip_code=None,
                 resident_district=None,
                 enter_code=None,
                 lla=None,
                 percent_enrolled="999",
                 state_aid_category=None,
                 age=None,
                 start_date=None,
                 sped_status=None,
                 federal_setting=None,
                 instructional_setting=None,
                 primary_disablity=None,
                 end_code=None,
                 serving_district=None,

                 ):

        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.grade = grade
        self.gender = gender
        self.language = language
        self.marss_id = marss_id
        self.hispanic_latino = hispanic_latino
        self.state_ethnicity = state_ethnicity
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.resident_district = resident_district
        self.enter_code = enter_code
        self.lla = lla
        self.percent_enrolled = percent_enrolled
        self.state_aid_category = state_aid_category
        self.age = age
        self.start_date = start_date
        self.sped_status = sped_status
        self.federal_setting = federal_setting
        self.instructional_setting = instructional_setting
        self.primary_disabilty = primary_disablity
        self.end_code = end_code
        self.serving_district = serving_district

    def get_end_code(self):
        print("Remains blank until there is a change in the student's enrollment status.\n"
              "If no changes, use the last day of school")
        code_40 = input('If student was enrolled at the end of the school year: \n'
                        'Enter 40:')
        if code_40 in ['40']:
            self.end_code = 40
            return self.end_code
        code_50 = input('If there is a change in Spec Ed Status (Eval completed; Servs discontinued; etc\n'
                        'Enter 50: ')
        if code_50 in ['50']:
            self.end_code = 50
            return self.end_code
        code_25 = input('EC Evaluation only-- Child not eligible for services.\n'
                        'Enter 25: ')
        if code_25 in ['50']:
            self.end_code = 25
            return self.end_code
        code_transition = input('Transition from C to B;\n'
                                'Enter 27, 28, or 29:')
        if code_transition in ['27', '28', '29']:
            self.end_code = code_transition
            return self.end_code
        code_99 = input('Student  change unrelated to special education (ex. Resident District)\n'
                        'Enter 99: ')
        if code_99 in ['99']:
            self.end_code = 99
            return self.end_code
        else:
            print("These were the most common options.")
        print(73 * "-")
        input()




    def get_primary_disabilty(self):
        if self.sped_status == 2:
            print("Primary Disability is NONE while student is in eval.")
            self.primary_disabilty = None
            return self.primary_disabilty
        elif self.age in [1, 2]:
            print("Primary Disability must be 12 if the student is 3 or under.")
            print(self.first_name, "is", self.age, "the primary disability is now set to 12")
            self.primary_disabilty = 12
            return self.primary_disabilty
        elif self.age == 7:
            print("Student Primary Disability must not be 12")
            self.primary_disabilty = input("Enter disability code")
            return self.primary_disabilty
        elif self.age in [3,4,5,6]:
            print("Student's age is between 3 and 6:", str(self.age))
            self.primary_disabilty = input("Enter disability code: Usually 01, 11, or 12")
            return self.primary_disabilty
        else:
            print("Check your student's age.")

        print(73 * "-")
        input()

    def calculate_age(self):
        temp_birthday = datetime.strptime(self.birth_date, "%m %d %Y")
        today = date.today()
        self.age = today.year - temp_birthday.year - ((today.month, today.day) < (temp_birthday.month, temp_birthday.day))
        if self.age > 7:
            print("WARNING: This student is not eligible for ECSE services!")
            return self.age
        else:
            return self.age

    def get_instructional_setting(self):
        if self.sped_status !=  2:
            if self.age in [0, 1, 2]:
                print("Sped status is between 11-17")
                self.instructional_setting = input("Enter instructional setting: (number)")
            elif self.age in [3, 4, 5]:
                print("Student Age: ", str(self.age), "Therefore instructional setting is between 30-45")
                self.instructional_setting = input("Enter sped status: (number)")
            elif self.age in [6, 7]:
                self.instructional_setting = input("Instructional setting is between 1-8")
            else:
                print("Student not a valid ECSE student.")
        else:
            self.federal_setting = 0
            self.primary_disabilty = 0
            print("Federal Setting and Primary Diasabilty are both equal to zero when eval status is 2")
        print(73 * "-")
        input()

    def create_marss(self):
        print("Check to see if marss number already exists")
        self.marss_id = input(str("Resident District + Serving District + Next avaialble MARSS identifier. (13 digits total"))
        print(73 * "-")
        input()
        return self.marss_id


    def create_new_record(self):
        input("Please answer Y or N")
        initial_eval = input(str("Is this the childs first eval?"))
        completed_eval = input(str("Did the child complete eval?"))
        age_trigger = input(str("Did the child turn 3, 6, or 7?")) #change in federal setting
        discontinue_sped = input(str("Did the child discontinue special ed services?"))
        grade_change = input(str("Did the child make a grade change?"))
        status_change = input(str("Did the child have a change in special ed status and/or a state aid category?"))
        resident_district_change = input(str("Did the child have a change in resident district"))
        if initial_eval or completed_eval or age_trigger or discontinue_sped or \
                grade_change or status_change or resident_district_change == "Y":
            print("New record required")
        else:
            print("No new record required.")

    def status_start_date(self):
        # TODO Validate the start date, i.e. between july 1st and july 30th
        print(" ** NOTICE: Status start date may be any day between July 1st and June 30th **")
        print('-'*73)
        input()
        new_student = input("Is this a new student?")
        if new_student in ["Y", 'Yes', "yes", 'y']:
            print("If the student is new, start date is the date the parent gave permission to evaluate was recieved")
            self.start_date = input(str("Enter date the parent gave permission to evaluate. (mm dd yyyy)"))
            return self.start_date
        first_iep = input("Is this the student's first IEP?")
        if first_iep in ["Y", 'Yes', "yes", 'y']:
            print("The start date is the date the parent signed the IEP/IFSP and services began.")
            self.start_date = input(str("Enter the date parents signed the IEP/IFSP. (mm dd yyyy)"))
            return self.start_date
        age_changes = input("Did the child turn 3, 6, or 7")
        if age_changes in ["Yes", "yes", 'Y', 'y']:
            print("Change what 'Fed Settings' (ASK LISA ")
            self.start_date = input(str("Enter the date child turned 3,6, or 7 (mm dd yyyy)"))
            return self.start_date
        else:
            print("I'm out of ideas?")

    def get_last_location_codes(self):
        code_00 = input(str("Is the student enrolled in the same district as the previous year?"))
        if code_00 in ["Y", 'y', "Yes", 'yes']:
            print("LLA Code is 00")
            self.lla = 0
            print('-' * 73)
            return self.lla
        code_05 = input(str("Is the student 5 or younger AND in school for the first time?"))
        if code_05 in ["Y", 'y', "Yes", 'yes']:
            print("LLA Code is 05")
            self.lla = 5
            print('-' * 73)
            return self.lla
        code_22 = input(str("Has the student changed grade levels? \n"
                            " (or has student qualifed for special ed services for the first time?"))
        if code_22 in ["Y", 'y', "Yes", 'yes']:
            print("LLA Code is 22")
            self.lla = 22
            print('-' * 73)
            return self.lla
        code_23 = input(str("Did the student change their resident district?"))
        if code_23 in ["Y", 'y', "Yes", 'yes']:
            print("LLA Code is 23")
            self.lla = 23
            print('-' * 73)
            return self.lla
        code_24 = input(str("Student changed enrollment status(not specified above)"))
        if code_24 in ["Y", 'y', "Yes", 'yes']:
            print("LLA Code is 24")
            self.lla = 24
            print('-' * 73)
            return self.lla
        else:
            print("?")
        print(73 * "-")
        input()

    def get_state_aid_category(self):
        if self.state_aid_category == None:
            code_10 = input(str("If they are a member of our co-op: Y"))
            if code_10 in ["Y", "Yes", 'y', 'yes']:
                self.state_aid_category = 10
                return self.state_aid_category
            code_19 = input(str("Is tuition agreement is outside of one our districts. Then it is a 19: If yes enter Y"))
            if code_19 in ["19"]:
                self.state_aid_category = "19"
                return self.state_aid_category
            else:
                print("These are the acceptable choices. Re-think your position.")
        else:
            print("Your state aid category is", self.state_aid_category)
        print(73 * "-")
        input()

    def get_resident_district(self):
        print("Resident District Choices: \n"
              "1. 0162 Bagley\n"
              "2. 0998 BRIC\n"
              "3. 0032 Blackduck\n"
              "4. 0115 Cass Lake-Bena\n"
              "5. 2311 Clearbrook-Gonvick\n"
              "6. 0036 Kelliher\n"
              "7. 0390 Lake of the Woods\n"
              "8. 0306 Laporte\n"
              "9. 0362 Littlefork-Big Falls\n"
              "10. 0432 Mahnomen\n"
              "11. 0363 South Koochiching\n"
              "12. 0435 Waubun/Ogema\n"
              "13. Out of district\n"
              "14. Private School\n")
        district_choice = input("District Choice: (1 or 2 etc.)\n")
        if district_choice in ['1']:
            self.resident_district = "0162 Bagley"
            return self.resident_district
        elif district_choice in ['2']:
            self.resident_district = "0998 BRIC"
            return self.resident_district
        elif district_choice in ['3']:
            self.resident_district = "0032 Blackduck"
            return self.resident_district
        elif district_choice in ['4']:
            self.resident_district = "0115 Case Lake-Bena"
            return self.resident_district
        elif district_choice in ['5']:
            self.resident_district = "2311 Clearbrook-Gonvick"
            return self.resident_district
        elif district_choice in ['6']:
            self.resident_district = "0036 Kelliher"
            return self.resident_district
        elif district_choice in ['7']:
            self.resident_district = "0390 Lake of the Woods"
            return self.resident_district
        elif district_choice in ['8']:
            self.resident_district = "0306 Laporte"
            return self.resident_district
        elif district_choice in ['9']:
            self.resident_district = "Littlfork-Big Falls"
            return self.resident_district
        elif district_choice in ['10']:
            self.resident_district = "0432 Mahnomen"
            return self.resident_district
        elif district_choice in ['11']:
            self.resident_district = "0363 South Koochiching"
            return self.resident_district
        elif district_choice in ['12']:
            self.resident_district = "0435 Waubun/Ogema"
            return self.resident_district
        elif district_choice in ['13']:
            self.resident_district = "Outside of BRIC Districts"
            print("Your state aid category is 19")
            self.state_aid_category = 19
            input()
            return self.resident_district, self.state_aid_category
        elif district_choice in ['14']:
            self.resident_district = "Private School"
            return self.resident_district

    def get_student_information(self):
        print("Enter the information at the prompts.")
        self.language = input("Home Language: ")
        self.hispanic_latino = input("Hispanic or Latino? Y/N")
        self.state_ethnicity = input("State Ethnicity: ")
        self.address = input("Student Address: ")
        self.city = input("Student City: ")
        self.state = input("Student State: ")
        self.zip_code = input("Student Zip Code: ")
        self.serving_district = "0998 BRIC"
        return self.language, self.hispanic_latino, self.state_ethnicity, self.address, \
        self.city, self.state, self.zip_code, self.serving_district


    def get_sped_status(self):
        code_02 = input("Is the student currently in evaluation?")
        if code_02 in ["Y", "y", "Yes", "yes"]:
            self.sped_status = 2
            return self.sped_status
        code_6 = input("Has the student completed an evaluation and receive services from an outside service?")
        if code_6 in ["Y", "y", "Yes", "yes"]:
            self.sped_status = 6
            return self.sped_status
        code_4 = input("Has the student completed an evaluation and qualified for Special Ed services?")
        if code_4 in ["Y", "y", "Yes", "yes"]:
            self.sped_status = 4
            return self.sped_status
        # TODO "Spec Ed Evaluation Status and Start Dates on pg. 6 of Marss Procedure Power Point

    def __str__(self):
        return "Last Name: {}\n" \
               "First Name: {}\n" \
               "State Aid Category: {}\n"\
                "Age: {}\n"\
                "Sped Status: {}\n"\
                "Start Date: {}\n"\
                "Resident District: {}\n"\
                "Serving District: {}\n"\
                "Last Location Attended: {}\n"\
                "Instructional Setting: {}\n"\
                "Primary Disability: {}\n"\
                "End Code: {}\n "\
                .format(self.last_name, self.first_name, str(self.state_aid_category),
                        str(self.age), self.sped_status, self.start_date, self.resident_district, self.serving_district,
                        self.lla, self.instructional_setting, self.primary_disabilty, self.end_code)


students = [Student(
                        last_name="Kvale",
                        first_name="Eric",
                        birth_date="11 28 1980",
                        grade="EC",
                        gender="Male",
                        language="English",
                        marss_id="1234567891",
                        hispanic_latino="No",
                        state_ethnicity="White, not Hispanic",
                        address="123 Drive, NW",
                        city='Houghton',
                        state="Michigan",
                        zip_code="54310",
                        resident_district="Copper Harbor",

                        ),
            Student(
                last_name="Syverson",
                first_name="Oriana",
                birth_date="05 18 2015",
                grade="EC",
                gender="Female",
            ),
            Student(
                last_name="Adams",
                first_name="Michael",
                birth_date="08 03 2015",
                grade="EC",
                gender="Male",
            )
            ]


#create_student()
eric = students[0]
oriana = students[1]
michael = students[2]
# oriana.status_start_date()
# # age = Student.calculate_age(oriana)
# oriana.evaluation_status()
# oriana.get_state_aid_category()
# oriana.resident_district = input("What is the students resident district? ")
# # oriana.federal_setting = input("Federal Setting: (Also known as Instructional Setting): ")
# oriana.get_end_code()
# oriana.calculate_age()
# oriana.get_primary_disabilty()
# oriana.get_instructional_setting()
# state_aid = Student.get_state_aid_category(students[0])
# print(state_aid)

# for student in students:
#     print(student)


def get_menu_choice(name):
    def print_menu():       # Your menu design here
        print(30 * "-", "MARSS CODE HELPER", 30 * "-")
        print("1. Resident District")
        print("2. Sped Status")
        print("3. Primary Disability ")
        print("4. Instructional/Federal Setting ")
        print("5. Last Location Code")
        print("6. Status Start Date")
        print("7. State Aid Category")
        print("8. Student Information ")
        print("9. Show Student Data")
        print("10. Exit from the script ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-10]: ")
        name.calculate_age()
        if choice == '1':
            choice = ''
            int_choice = 1
            name.get_resident_district()
        elif choice == '2':
            choice = ''
            int_choice = 2
            name.get_sped_status()
        elif choice == '3':
            choice = ''
            int_choice = 3
            name.get_primary_disabilty()
        elif choice == '4':
            choice = ''
            int_choice = 4
            name.get_instructional_setting()
        elif choice == '5':
            choice = ''
            int_choice = 5
            name.get_last_location_codes()
        elif choice == '6':
            choice = ''
            int_choice = 6
            name.status_start_date()
        elif choice == '7':
            choice = ''
            int_choice = 7
            name.get_state_aid_category()
        elif choice == '8':
            choice = ''
            int_choice = 8
            name.get_student_information()
        elif choice == '9':
            choice = ''
            int_choice = 9
            print("-" * 73)
            print(name)
            print("-"*73)
            input()
        elif choice == '10':
            choice = ''
            int_choice = -1
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]


print(get_menu_choice(michael))