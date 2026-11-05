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