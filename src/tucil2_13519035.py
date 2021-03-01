# print screen awal
def printStartScreen():
    print('                   _                      _   ')
    print('                  | |                    | |  ')
    print(' _ __  _   _  ___ | |__    ___  ___  _ __| |_ ')
    print("| '_ \| | | |/ _ \| '_ \  / __|/ _ \| '__| __|")
    print('| | | | |_| | (_) | | | | \__ \ (_) | |  | |_ ')
    print('|_| |_|\__, |\___/|_| |_| |___/\___/|_|   \__|')
    print('        __/ |                                 ')
    print('       |___/                                  ')
    print()

# cek graph siklik
def isGraphCyclic(graph):
    for node in graph:
        # cek ada in degree 0
        if len(node) == 1: 
            return False
    
    return True

# cek prereq dari course
def courseHaveNoPrereqs(course):
    return len(course) == 1

# hitung jumlah course tanpa prereq dalam satu semester
def countDegreeZeroInSemester():
    degreeZeroInSameSemester = 0
    for course in listOfCoursesAndPrereqs: 
        if courseHaveNoPrereqs(course):
                degreeZeroInSameSemester += 1
    return degreeZeroInSameSemester

# simpan course tanpa prereq dalam satu semester
def storeDegreeZeroInSemester():
    sameSemester = []
    for course in listOfCoursesAndPrereqs: 
        if courseHaveNoPrereqs(course):
                sameSemester.append(course)
    
    return sameSemester

# hapus course tanpa prereq
def removeDegreeZeroCourse():
    tempCourse = ''.join(courseNode)
    solution.append(tempCourse)
    for courses in listOfCoursesAndPrereqs:
        for course in courses:
            if course == tempCourse:
                courses.remove(tempCourse)

# print solusi
def printSolution(solution):
    courseIndex = 0
    semester = 1
    for num in courseCountPerSemester:
        print('Semester ' + str(semester) + ': ')
        for i in range(num):
            if i != num-1:
                print(solution[courseIndex] + ', ', end='')
            else:
                print(solution[courseIndex]) 
            courseIndex += 1
        semester += 1
    
# printStartScreen()
filename = input('Masukkan nama file yang ingin diproses (tanpa .txt) : ')
listOfCoursesAndPrereqs = []

# setup 
with open('testfiles/' + filename + '.txt') as file:
    removeChars = ',.'
    for line in file:
        for char in removeChars:
            line = line.replace(char, '')
        
        listOfCoursesAndPrereqs.append((line.strip()).split())

file.close()

totalCourses = len(listOfCoursesAndPrereqs)
solution = []
courseCountPerSemester = []
coursesPerSemester = []

for i in range(len(listOfCoursesAndPrereqs)):
    if isGraphCyclic(listOfCoursesAndPrereqs):
        break
    for courseNode in listOfCoursesAndPrereqs:
        if isGraphCyclic(listOfCoursesAndPrereqs):
            break

        if courseCountPerSemester == [] or sum(courseCountPerSemester) == len(solution):
            degreeZeroCountInSameSemester = countDegreeZeroInSemester()
            degreeZeroCoursesInSameSemester = storeDegreeZeroInSemester()
            courseCountPerSemester.append(degreeZeroCountInSameSemester)
        
        if courseHaveNoPrereqs(courseNode) and courseNode in degreeZeroCoursesInSameSemester:
            removeDegreeZeroCourse()

printSolution(solution)