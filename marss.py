

class EcseStudent():

    def __init__(self, last_name, first_name, grade, gender, age, resident_district, marss_id):

        self.age = age
        self.grade = grade
        self.gender = gender
        self.last_name = last_name
        self.first_name = first_name
        self.resident_district = resident_district
        self.marss_id = marss_id

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
        new_student = input(str("New student?"))
        first_iep = input(str("First IEP/IFSP?"))
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

    def state_aid_category(self):
        code_00 = input(str("Is the student a resident of your district?"))
        code_01 = input(str("Open Enrolled?"))
        code_11 = input(str("Non-tuition parent initiated agreement (missed open enrollment deadline? \n"
                            "Pre-K students (EC) CANNOT open enroll unless currently on an IEP/IFSP \n"
                            "Non-resident Pre-K students must be evaluated by their resident district \n"
                            "(non-resident districts cannot receive funding for Pre-K special ed evaluation services"))
        code_19 = input(str("Is tuition agreement (includes Foster Care placements) \n"
                            "Pre-K spec ed evaluation exception for students in foster care."))
        if code_00 == "Y":
            print("Code 00")
        elif code_01 == "Y":
            print("Code 01")
        elif code_11 == "Y":
            print("Code 11")
        elif code_19 == "Y":
            print("Code 19")
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
            eval_status = 2
            return eval_status

        qualified = input("Has the student qualified for evaluation? ")
        if qualified == "Y":
            eval_status = 1
            lla = 22
            return eval_status, lla

        #TODO "Spec Ed Evaluation Status and Start Dates on pg. 6 of Marss Procedure Power Point


    def __str__(self):
        return self.last_name + ", " + self.first_name

class VPK(EcseStudent):
    pass


class HK(EcseStudent):

    Age = [5, 6, 7]
    AcademicKC = bool(True)  #Academic Kindergarten Class
    IEP = bool(True)
    IFSP = bool(True)


def create_student():
    first_name = input(str("What is the students first name?"))
    last_name = input(str("What is the students last name?"))
    grade = input(str("What is the students grade?"))
    gender = input(str("What is the students gender?"))
    age = input(str("What is the students age?"))
    resident_district = input(str("What is the students resident district?"))
    marss_id = input(str("What is the students marss id?"))

    student_id = EcseStudent(last_name, first_name, grade, gender, age, resident_district, marss_id)
    return student_id


kid1 = EcseStudent("Kvale", "Eric", "4", "Male", "8", "Houghton", "1234567891011")





