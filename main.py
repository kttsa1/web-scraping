import urllib.request

def instructor_lectures(department, instructor):
    """
    searches Lou's List for lectures of a specific department and instructor
    no repeats of class names
    :param department: name of department, all caps
    :param instructor: name of instructor
    :return: name of classes the professor teaches
    """
    url = "https://cs1110.cs.virginia.edu/files/louslist/" + department
    all_courses = urllib.request.urlopen(url)

    # get list of all lecture courses
    lecture_list = []
    for row in all_courses:
        row = row.decode('utf-8')
        classes = row.strip().split('|')
        if classes[5] == 'Lecture':
            lecture_list.append(classes)

    instructor_courses = []
    for course in lecture_list:
        if course[4] == instructor or course[4] == instructor + "+1":
            if course[3] not in instructor_courses:
                instructor_courses.append(course[3])

    return instructor_courses


def compatible_classes(first_class, second_class, needs_open_space=False):
    """
    checks if the two courses occur at the same time
    if they occur at the same time, return False
    otherwise True
    """
    compatibility = False

    # get department name, course number, and section number
    department1 = ''
    department2 = ''
    for char1 in first_class:
        if char1.isalpha() == True:
            department1 += char1
    for char2 in second_class:
        if char2.isalpha() == True:
            department2 += char2
    course_number1 = first_class[-8:-4]
    course_number2 = second_class[-8:-4]
    section_number1 = first_class[-3:]
    section_number2 = second_class[-3:]

    # open urls based on department given, then identify the class within the file
    url = "https://cs1110.cs.virginia.edu/files/louslist/"
    courses1 = urllib.request.urlopen(url + department1)
    courses2 = urllib.request.urlopen(url + department2)

    found1 = False
    found2 = False
    for row1 in courses1:
        row1 = row1.decode('utf-8')
        classes1 = row1.strip().split('|')
        if (classes1[1] == course_number1) and (classes1[2] == section_number1):  # identifies class
            course1 = classes1
            found1 = True
    if found1 != True:
        compatibility = False
        return compatibility

    for row2 in courses2:
        row2 = row2.decode('utf-8')
        classes2 = row2.strip().split('|')
        if classes2[1] == course_number2 and classes2[2] == section_number2:  # identifies class
            course2 = classes2
            found2 = True
    if found2 != True:
        compatibility = False
        return compatibility

    ################## CONDITIONS FOR COMPATIBILITY##################
    # if they are the same class
    if first_class == second_class:
        compatibility = False
        return compatibility

    # if either class is full
    if needs_open_space == True:
        if int(course1[-2]) >= int(course1[-1]) or int(course2[-2]) >= int(course2[-1]):
            compatibility = False
            return compatibility

    # find dates and times for the two classes and make lists containing dates and times
    course1_times = []
    course2_times = []
    days_of_the_week = {7: "Mo", 8: "Tu", 9: "Wed", 10: "Th", 11: "Fri"}
    for i in range(7, 12):
        if course1[i] == "true":
            course1_times.append(days_of_the_week[i])
        if course2[i] == "true":
            course2_times.append(days_of_the_week[i])

    course1_times.append([course1[12], course1[13]])
    course2_times.append([course2[12], course2[13]])

    # check if the days of the week overlap at all
    days_overlap = False
    times_overlap = False
    for j in range(0, len(course1_times) - 1):
        for k in range(0, len(course2_times) - 1):
            if course1_times[j] == course2_times[k]:
                days_overlap = True

    # if days overlap, check times
    if days_overlap == True:
        for i in range(-2, 0):
            for j in range(-2, 0):
                if course1_times[-1][i] == course2_times[-1][j]:
                    times_overlap = True
                    compatibility = False
                    return compatibility
    else:
        compatibility = True
        return compatibility

    # if times_overlap != True:
        #check for overlapping times that are not same start/end time
    if times_overlap == False:
        compatibility = True

    return compatibility

#
# print(compatible_classes('CS 1110-001', 'CS 2110-001', True))