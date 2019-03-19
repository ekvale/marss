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
                 eval_status=None,
                 lla=None,
                 percent_enrolled="999",
                 state_aid_category=None,
                 age=None,
                 start_date=None,
                 sped_status=None,
                 federal_setting=None,
                 instructional_setting=None,
                 primary_disablity=None

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
        self.eval_status = eval_status
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

    def get_primary_disabilty(self):
        if self.eval_status == 2:
            print("Primary Disability is NONE while student is in eval.")
            self.primary_disabilty = None
        elif self.age in [1,2,3]:
            print("Primary Disability must be 12 if the student is 3 or under.")
            self.primary_disabilty = 12
        elif self.age == 7:
            print("Student Primary Disability must not be 12")
            self.primary_disabilty = input("Enter disability code")
        else:
            print("Student's age is between 4 and 6:", str(self.age))
            self.primary_disabilty = input("Enter disability code")

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
        if self.age != None:
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
            print("Define student age before calling this function.")


    def create_marss(self):
        print("Check to see if marss number already exists")
        self.marss_id = input(str("Resident District + Serving District + Next avaialble MARSS identifier. (13 digits total"))
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
        print("Status start date may be any day between July 1st and June 30th")
        new_student = input(str("New student? Start date is the date the consent to evaluate was recieved. Enter Y: "))
        if new_student in ["Y", 'yes', "y"]:
            temp_start_date = input("Date the consent to evaluate was recieved: (mm dd yyyy)")
            print(temp_start_date)
            self.start_date = temp_start_date
            return self.start_date

        first_iep = input(str("First IEP/IFSP? Enter Y: "))
        if first_iep in ["Y", 'yes', "y"]:
            outside_services = input("Is the student also receiving outside services? Enter Y: ")
            temp_start_date = input("Date the consent to evaluate was recieved: (mm dd yyyy)")
            print(temp_start_date)
            self.start_date = temp_start_date
            if outside_services in ["Y", 'yes', "y"]:
                self.sped_status = 6
                return self.sped_status, self.start_date
            else:
                self.sped_status = 4
            return self.start_date, self.sped_status
        age_changes = input("Did the child turn 3, 6, or 7?")
        if new_student == "Y":
            print("If the student is new, start date is the date the parent gave permission to evaluate was recieved")
            start_date = input(str("Enter date the parent gave permission to evaluate"))
            return start_date
        elif first_iep == "Y":
            print("Date the parent signs the IEP/IFSP and services begin.")
            start_date = input(str("Enter the date the parent signed the IEP/IFSP."))
            return start_date
        elif age_changes == "Y":
            print("Change what 'Fed Settings' ")
            start_date = input(str("Enter the date child turned 3,6, or 7"))
            return start_date
        else:
            print("I'm out of ideas?")

    def last_location_codes(self):
        code_00 = input(str("Is the student enrolled in the same district as the previous year?"))
        code_05 = input(str("Is the student 5 or younger AND in school for the first time?"))
        code_22 = input(str("Has the student changed grade levels? \n"
                            " (or has student qualifed for special ed services for the first time?"))
        code_23 = input(str("Did the student change their resident district?"))
        code_24 = input(str("Student changed enrollment status(not specified above)"))
        if code_00 == "Y":
            print("Chose Code 0")
        elif code_05 == "Y":
            print("Chose Code 5")
        elif code_22 == "Y":
            print("Chose Code 22")
        elif code_23 == "Y":
            print("Chose Code 23")
        elif code_24 == "Y":
            print("Chose Code 24")
        else:
            print("?")

    def get_state_aid_category(self):
        code_00 = input(str("Is the student a resident of your district? If yes enter: 00"))
        code_01 = input(str("Open Enrolled? If yes enter: 01"))
        code_11 = input(str("Non-tuition parent initiated agreement (missed open enrollment deadline? If yes enter: 11"))
        code_19 = input(str("Is tuition agreement (includes Foster Care placements) If yes enter 19:"))
        print(code_00)
        if code_00 in ["00"]:
            self.state_aid_category = "00"
            return self.state_aid_category
        elif code_01 in ["01"]:
            self.state_aid_category = "01"
            return self.state_aid_category
        elif code_11 in ["11"]:
            self.state_aid_category = "11"
            return self.state_aid_category
        elif code_19 in ["19"]:
            self.state_aid_category = "19"
            return self.state_aid_category
        else:
            print("?")

    def resident_district(self):
        print("Usually your district number - student lives within your district's boundries")
        input()
        print("Exception: Student's parents live outside the district boundaries-- \n"
              "Non-resident special education students bring in significant revenue")
        input()
        print("Tuition agreements are required for non-resident students. Serving district completes the tuition agreement \n"
              "and sends to the resident district.")
        input()
        print("Resident district signs, agreeing to cover costs for that student, and returns to the serving district.")
        input()
        print("If a spec ed student is discovered to be a non-resident, \n"
              "and no tuition agreement was completed - the resident district is not required to pay")
        input()
        print("If parental rights have been terminated, the student is claimed as a resident.")
        input()
        print("If a parent(s) location is unknown, the student is claimed as a resident.")

    def evaluation_status(self):
        in_eval = input("Is the student currently in evaluation?")
        if in_eval == 'Y':
            self.eval_status = 2
            return self.eval_status

        qualified = input("Has the student qualified for evaluation? ")
        if qualified == "Y":
            self.eval_status = 1
            lla = 22
            return self.eval_status, lla

        # TODO "Spec Ed Evaluation Status and Start Dates on pg. 6 of Marss Procedure Power Point

    def __str__(self):
        return "Last Name: {}\n" \
               "First Name: {}\n" \
               "Eval Status: {}\n" \
               "State Aid Category: {}\n"\
                "Age: {}\n"\
                "Sped Status: {}\n"\
                "Start Date: {}\n"\
                "Resident District: {}\n"\
                "Instructional Setting: {}\n"\
                "Primary Disability: {}\n"\
                .format(self.last_name, self.first_name, str(self.eval_status), str(self.state_aid_category),
                        str(self.age),self.sped_status, self.start_date, self.resident_district,
                        self.instructional_setting, self.primary_disabilty)


def create_student():
    first_name = input(str("What is the students first name?"))
    last_name = input(str("What is the students last name?"))
    birth_date = input(str("What is the students birthdate? (mm dd yyyy)"))
    grade = input(str("What is the students grade?"))
    gender = input(str("What is the students gender?"))

    students.append(Student(last_name, first_name, birth_date, grade, gender))




# last_name, first_name, birth_date, grade, gender, language, marss_id, resident_district, eval_status, race, state_ethnicity, address, city, state, zip,
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
                        eval_status="4"

                        ),
            Student(
                last_name="Syverson",
                first_name="Oriana",
                birth_date="05 18 2015",
                grade="EC",
                gender="Female",
            )
            ]


#create_student()
eric = students[0]
oriana = students[1]
# oriana.status_start_date()
# age = Student.calculate_age(oriana)
# oriana.evaluation_status()
# oriana.get_state_aid_category()
# oriana.resident_district = input("What is the students resident district? ")
# oriana.federal_setting = input("Federal Setting: (Also known as Instructional Setting): ")
oriana.calculate_age()
oriana.get_primary_disabilty()
oriana.get_instructional_setting()

print(oriana)
# state_aid = Student.get_state_aid_category(students[0])
# print(state_aid)

# for student in students:
#     print(student)