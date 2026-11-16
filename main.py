# information about the user
userName
isDormanScholar = False
isDeanScholar = False
scholarTrack
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
enrollmentStatus
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
userInput
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
print("Welcome to the NJIT CS/DS Course Advisor!")
# ask for name
name = input("Enter your name: ")

# ask for student type (dorman/dean/normal)
scholar = input("Are you a Dorman Scholar, Dean Scholar, or Neither? ")
while is_valid(scholar, ["Dorman", "Dean", "Neither"]) == False:
    scholar = input("Invalid input. Enter Dorman, Dean, or Neither: ")

is_scholar = False
if scholar.lower() == "dorman":
    is_scholar = True
    track = input("Enter your Dorman track: ")
elif scholar.lower() == "dean":
    is_scholar = True

# ask about major (only t2o right now)
major = input("This program is only for CS majors. Are you a CS major? yes or no"): ").lower()
while is_valid(major, ["CS"]) == False:
     print("Invalid major. This program is only for CS majors")
# ask about completed courses
completed = []
num_completed = int(input("How many courses have you completed? "))

# honors courses specifically
if is_scholar == True and num_completed > 0:
    honors_taken = int(input("How many honors courses have you taken? "))

# add the completed courses in
for i in range(num_completed):
    course_code = input("Enter completed course code: ").upper()
    completed.append(course_code)
for course in completed: 
    if completed 

# Choose a niche you like twin
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