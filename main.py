# information about the user
userName=''
isDormanScholar = False
isDeanScholar = False
scholarTrack=''
hasMinor = False
numberOfMinors = 0
minors = []
numberOfMajors = 0
majors = []
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
enrollmentStatus=''
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
minorRequirements = []
trackRequirements = []
remainingRequirements = []
completedRequirements = []

# course information provided to user of what elective information and types they need
allElectives = []
electivesByCategory = []
selectedElectives = []
electivesToRecommend = []
electiveRequirements = []
numberOfElectivesNeeded = 0

# courses the user is recommended to take and eligible to take
eligibleCourses = []
recommendedCourses = []
recommendedGenEdCourses = []
recommendedMajorCourses = []
recommendedMinorCourses = []
recommendedTrackCourses = []
coursesToTake = []
coursesWithCredit = []

selectedCourses = []
swappedCourses = []
numberOfCoursesToSwap = 0
totalSelectedCredits = 0
remainingCredits = 0

# schedule builder (might not be possible anymore)
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
userInput=''
isValid = False
loopCounter = 0
courseCounter = 0
electiveCounter = 0
minorCounter = 0
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

# display welcome message
print("Welcome to the NJIT CS Course Advisor!")
# ask for name
name = input("Enter your name: ")
while name=='':
    name=input('Invalid input. Please enter your name: ')

# ask for student type (dorman/dean/normal)
scholar = input("Are you a Dorman Scholar, Dean Scholar, or Neither? ")
while is_valid(scholar, ["Dorman", "Dean", "Neither"]) == False:
    scholar = input("Invalid input. Enter Dorman, Dean, or Neither: ")
# ask for honor track if dorman student
is_scholar = False
if scholar.lower() == "dorman":
    is_scholar = True
    tracks=['multidisciplinary', 'global studies', 'medical humanities', 'leadership & civic engagement', 'interdisciplinary digital studies']
    track = input("Enter your Dorman track: ").strip().lower()
    while track not in tracks:
        track=input('Invalid track. The options are multidisciplinary, global studies, medical humanities, leadership & civic engagement, and interdisciplinary digital studies. Enter your Dorman track: ')

elif scholar.lower() == "dean":
    is_scholar = True

# make sure that student is a CS major
import sys
major = input("This program is only for CS majors. Are you a CS major? Enter yes or no: ").strip().lower()
while is_valid(major, ['yes']) == False:
     reevaluate=input("Invalid major. This program is only for CS majors. Would you like to reconsider? Enter yes or no: ").strip().lower()
     if reevaluate=='yes':
         major=input("This program is only for CS majors. Are you a CS major? Enter yes or no: ").strip().lower()
         if is_valid(major,['yes'])==True:
             break
     else: 
         print('Your major is not applicable for our program. Thank you.')
         sys.exit()
         break
     
# ask about completed courses
completed = []
num_completed = int(input("How many courses have you completed? "))

# honors courses specifically
if is_scholar == True and num_completed > 0:
    honors_taken = int(input("How many honors courses have you taken? "))

# add the completed courses in (lowkey this might not be the best i changed it i might have made it worse -sana)
for i in range(num_completed):
    course_code = input("Enter completed course code in the format, CS 100. For physics, please type in the format, PHYS 111 and 111A: ").strip().strip('.')
    confirm='no'
    while confirm=='no':
        confirm=input(f'You entered course {course_code} please confirm if it is correct (yes/no): ')
        if confirm=='yes':
            continue
        course_code = input("Reenter completed course code in the format CS 100. For physics, please type in the format, PHYS 111 and 111A: ").strip().strip('.')
    completed.append(course_code)
print(f'You have completed these courses: {completed}')

# open and read file for required CS courses
ReqCS_File=open("CS Major Courses.txt","r")
ReqCS_Lines=ReqCS_File.readlines()
ReqCS_File.close()
reqCourses=[]
for reqCourse in ReqCS_Lines:
    reqCourses.append(reqCourse)
for reqCourse in reqCourses:
    info=reqCourse.split(',')
    requiredCourses.append((info[0],info[1],info[2]))

# remove completed courses from required CS courses list
reqDisplayed=[]
for compCourse in completed: 
    for reqCourse in requiredCourses:
        if reqCourse[0]==compCourse:
            requiredCourses.remove(reqCourse)
            break
for reqCourse in requiredCourses:
    reqDisplayed.append(reqCourse[0])
print(f'Remaining required courses are: {reqDisplayed}')

#Asks which courses were honors to account for honors requirements (ABCD Groups): in progress
'''
if is_scholar:
    if honors_taken==1:
        for i in range(honors_taken):
                honors_course=input('Enter the honors course you have taken in format, CS 100: ')
                
    elif honors_taken>1:
        for i in range(honors_taken):
            input('Enter the honors courses you have taken in format, CS 100: ')
'''

# Choose a niche you like twin (maybe no more)
interest = input("Choose an interest (AI, Web, or None): ")
while is_valid(interest, ["AI", "Web", "None"]) == False:
    interest = input("Invalid interest. Choose AI, Web, or None: ")

# ask for max credits and warn if they're part time or over credits
# no stops ts
keep_asking = True
while keep_asking == True:
    max_credits = int(input("Max credits you want to take next semester: "))
    # part time
    if max_credits < 12:
        if is_scholar == True:
            ans = input("You will lose Scholar eligibility under 12 credits. Reconsider? (yes/no): ")
        else:
            ans = input("You will be part-time under 12 credits. Reconsider? (yes/no): ")
        if ans.lower() == "no":
            keep_asking = False
    # too many credits
    elif max_credits > 19 or (max_credits > 17 and is_scholar == False):
        ans = input("You will have to pay extra overload tuition. Reconsider? (yes/no): ")
        if ans.lower() == "no":
            keep_asking = False
    # no warning needed
    else:
        keep_asking = False

# store all NJIT CS courses

# filter courses user did

# find remaining required courses and matching electives, check prereqs
# if they'r edone they graduate
# display these

# Stretch goal and build that
# print it out