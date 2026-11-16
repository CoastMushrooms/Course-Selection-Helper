''''
This program basically looks through the text file and gets the NJIT CS
courses and credit info, then compares it to the student's completed courses
to determine what they need to do. 

what needs to be added
- Course prereqs need to be checked
- Seperate gen eds and cs requirements
- Check course eligibility
- Graduation check
'''

# information about the user
isDormanScholar = False
isDeanScholar = False
scholarTrack = ""
# hasMinor = False
# numberOfMinors = 0
# minors = []
# numberOfMajors = 0
# majors = []
isUndeclared = False

#information about the user's courses and credits
completedCourses = []
numberOfCompletedCourses = 0
honorsCoursesTaken = 0
hasHonorsCredits = False
academicInterests = []
numberOfCredits = 0

# information about user enrollment and other student catgories
maxCredits = 0
enrollmentStatus = ""
isPartTime = False
isFullTime = False
reconsiderEnrollment = False

# stored information about offered courses
allCourses = []
courseNames = []
courseCredits = []
coursePrerequisites = []
eligibleMajors = []
programRequirements = []
courseProfessors = []
availableSemesters = []
courseSections = []
courseTimes = []
honorsSections = []

# information about what users need to get done
requiredCourses = []
generalEducationRequirements = []
majorRequirements = []
# minorRequirements = []
trackRequirements = []
remainingRequirements = []
completedRequirements = []

'''
# course information provided to user of what elective information and types they need
allElectives = []
electivesByCategory = []
selectedElectives = []
electivesToRecommend = []
electiveRequirements = []
numberOfElectivesNeeded = 0
'''

# courses the user is recommended to take and eligible to take
eligibleCourses = []
recommendedCourses = []
recommendedGenEdCourses = []
recommendedMajorCourses = []
# recommendedMinorCourses = []
recommendedTrackCourses = []
coursesToTake = []
coursesWithCredit = []

selectedCourses = []
swappedCourses = []
numberOfCoursesToSwap = 0
totalSelectedCredits = 0
remainingCredits = 0

# schedule builder 
schedule = []
selectedSections = []
currentCourse = ""
currentSection = ""
courseStartTime = []
courseEndTime = []
scheduleConflict = False
hasTimeConflict = False
isWithinCreditLimit = True
scheduleComplete = False

# counters
userInput = ""
isValid = False
loopCounter = 0
courseCounter = 0
electiveCounter = 0
# minorCounter = 0
majorCounter = 0
swapCounter = 0

# program running variables
continueProgram = True
restartQuestions = False
userWantsScheduleBuilder = False
userWantsToSwap = False
userWantsToReconsider = False

# global check if choices matches allowed option
def is_valid(user_input, valid_options):
    for option in valid_options:
        if user_input.upper() == option.upper():
            return True
    return False

# load information from file
def load_course_data():
    all_courses = []
    file = open("CS Major Courses.txt", "r")

    for line in file:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")
        # store everything from the file
        department = parts[0]
        course_number = parts[1]
        credits = int(parts[2])
        # course name gotten
        course_name = ",".join(parts[3:])
        course_code = department + " " + course_number
        # store course as a list
        course = [course_code, credits, course_name]
        # add it
        all_courses.append(course)

    file.close()
    return all_courses

# get student info
def get_user_info():
    print("Welcome to the NJIT CS Course Advisor!")
    # info in
    name = input("Enter your name: ")
    scholar = input("Are you a Dorman Scholar, Dean Scholar, or Neither? ")
    
    # forces a decision 
    while not is_valid(scholar, ["Dorman", "Dean", "Neither"]):
        scholar = input("Invalid input. Enter Dorman, Dean, or Neither: ")

    is_scholar = False
    track = ""

    # scholar trigger for special condition
    if scholar.lower() == "dorman":
        is_scholar = True
        track = input("Enter your Dorman track: ")
    elif scholar.lower() == "dean":
        is_scholar = True

    # eh it's restrictive rn but whatever
    major = input("Enter your major (CS): ").upper()

    while not is_valid(major, ["CS"]):
        major = input("Invalid major. Enter CS: ").upper()

    # tuple with all this info
    return name, scholar, is_scholar, track, major

# get completed courses
def get_completed_courses(is_scholar):
    completed_courses = []

    num_completed = int(input("How many courses have you completed or have credit for? "))

    if is_scholar and num_completed > 0:
        honors_taken = int(input("How many honors courses have you taken? "))
    else:
        honors_taken = 0

    # loop that adds them in
    for i in range(num_completed):
        course = input("Enter completed course code (example: CS 100): ").upper()
        completed_courses.append(course)

    return completed_courses, honors_taken

# get max creds
def get_max_credits(is_scholar):
    keep_asking = True

    while keep_asking:
        max_credits = int(input("Maximum credits you want to take next semester: "))

        # part timers
        if max_credits < 12:
            if is_scholar:
                answer = input("You may lose Scholar eligibility. Reconsider? (yes/no): ")
            else:
                answer = input("You will be considered part-time. Reconsider? (yes/no): ")
            if answer.lower() == "no":
                keep_asking = False
        # overtimers
        elif max_credits > 19 or (max_credits > 17 and not is_scholar):
            answer = input("You may have to pay extra overload tuition. Reconsider? (yes/no): ")
            if answer.lower() == "no":
                keep_asking = False
        # normal student
        else:
            keep_asking = False

    return max_credits

# find courses uncompleted
def find_remaining_courses(all_courses, completed_courses):
    remaining_courses = []
    # checks each in list
    for course in all_courses:
        if course[0].upper() not in completed_courses:
            remaining_courses.append(course)

    return remaining_courses

# recommend courses based on creds
def recommend_courses(remaining_courses, max_credits):
    recommended_courses = []
    total_credits = 0

    # add them in if fits the conditions
    for course in remaining_courses:
        course_code = course[0]
        credits = course[1]
        course_name = course[2]
        if total_credits + credits <= max_credits:
            recommended_courses.append(course)
            total_credits += credits

    return recommended_courses, total_credits

# display recommended courses
def display_courses(recommended_courses, total_credits):
    print("\nRECOMMENDED COURSES")

    if len(recommended_courses) == 0:
        print("No courses could be recommended.")
        return
    for course in recommended_courses:
        print("\nCourse:", course[0])
        print("Course Name:", course[2])
        print("Credits:", course[1])

    print("\nTotal Recommended Credits:", total_credits)

# main program
def main():
    # load course info
    all_courses = load_course_data()

    # get student info and store it
    name, scholar, is_scholar, track, major = get_user_info()

    # get completed courses
    completed_courses, honors_taken = get_completed_courses(is_scholar)

    # get cred limit
    max_credits = get_max_credits(is_scholar)

    # get remaining courses
    remaining_courses = find_remaining_courses(all_courses, completed_courses)

    # see if student did all the courses in the file
    if len(remaining_courses) == 0:
        print("\nCongrats", name + "! You have completed all courses in the file!")
        return

    # recommend courses and store it
    recommended_courses, total_credits = recommend_courses(remaining_courses, max_credits)

    # display everything yaya
    print("\nHello", name + "!")
    print("Major:", major)
    print("Scholar Status:", scholar)

    if scholar.lower() == "dorman":
        print("Dorman Track:", track)

    display_courses(recommended_courses, total_credits)

# run main
main()
