import csv
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import string
def get_subject_department():
    courses_df = pd.read_csv("2020-sp.csv")
    subject_dict={}
    subject_list = []
    for subject in courses_df["Subject"]:
        if not subject_list or subject != subject_list[-1]:
            subject_list.append(subject)
    for subject in subject_list:
        html = urlopen("https://courses.illinois.edu/schedule/2020/spring/" + subject).read()
        soup = BeautifulSoup(html, features='html.parser')
        element_li = soup.find_all("li")
        deptName = element_li[13].get_text()
        subject_dict[subject] = deptName
    return subject_dict

def get_full_name(subject):
    return subject_dict[subject]

def password_generator(size):
    total_char = string.ascii_lowercase + string.digits
    toReturn = ''
    for i in range(size):
        toReturn += random.choice(total_char)
    return toReturn

def generate_student():
    with open('Generated_Student_Info.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open('Students.csv', 'w', newline = '') as new_file:
            fieldnames = ['NetId', 'FirstName', 'LastName', 'PreferredWorkTime', 'SchoolYear', 'ContactInfo', 'OtherInfo']       
            csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)        
            csv_writer.writeheader()      
            pwt_list = ['early morning', 'morning', 'noon', 'afternoon', 'evening', 'late night']
            sy_list = ['freshman', 'sophomore', 'junior', 'senior', 'masters', 'PhD']
            netid_list = []
            for line in csv_reader:
                if len(line['First Name']) < 7:
                    netid = line['First Name'].lower() + line['Last Name'][0].lower() + str(random.randrange(10))
                else:
                    netid = line['First Name'][0].lower() + line['Last Name'][0].lower() + str(random.randrange(10))
                while netid in netid_list:
                    netid = netid + str(random.randrange(10))
                netid_list.append(netid)    
                pwt = random.choice(pwt_list)
                sy = random.choice(sy_list)
                csv_writer.writerow({'NetId': netid, 'FirstName': line['First Name'], 'LastName': line['Last Name'], 
                                    'PreferredWorkTime': pwt, 'SchoolYear': sy, 'ContactInfo': netid + "@illinois.edu", 
                                    'OtherInfo': line['OtherInfo']})

def generate_department():
    courses_df = pd.read_csv("2020-sp.csv")
    subject_list = []
    deptName_list = []
    deptHead_list = []
    deptOffice_list = []
    deptPhone_list = []
    for subject in courses_df["Subject"]:
        if not subject_list or subject != subject_list[-1]:
            subject_list.append(subject)
    for subject in subject_list:
        html = urlopen("https://courses.illinois.edu/schedule/2020/spring/" + subject).read()
        soup = BeautifulSoup(html, features='html.parser')
        element_li = soup.find_all("li")
        deptName = element_li[13].get_text()
        if deptName in deptName_list:
            continue
        deptName_list.append(deptName)
        deptHead_list.append(element_li[14].get_text().split(":")[1].strip())
        deptOffice_list.append(element_li[15].get_text().split(":")[1].strip())
        deptPhone_list.append(element_li[16].get_text().split(":")[1].strip())
        
    departments_dict = {'DeptName' : deptName_list, 'DeptHead' : deptHead_list, 'DeptOffice' : deptOffice_list, 'DeptPhone' : deptPhone_list}
    departments_df = pd.DataFrame(data = departments_dict)
    departments_df.to_csv("Departments.csv", index=False)

def generate_course():
    with open('2020-sp.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open('Courses.csv','w', newline = '') as new_file:
            fieldnames=['CRN','CourseTitle','CourseNumber','Department',
                        'Section','ScheduleType','Instructor','MeetingTime']
            
            csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            
            for line in csv_reader:
                if line['Start Time']=='ARRANGED':
                    time='ARRANGED'
                else:
                    time=line['Days of Week']+' '+line['Start Time']+'-'+line['End Time']
                csv_writer.writerow({'CRN':line['CRN'],
                                    'CourseTitle':line['Name'],
                                    'CourseNumber':line['Subject']+str(line['Number']),
                                    'Department':subject_dict[line['Subject']],
                                    'Section':line['Section'],
                                    'ScheduleType':line['Type'],
                                    'Instructor':line['Instructors'].split(";")[0],
                                    'MeetingTime':time
                                    })

def generate_instructor():
    with open('Courses.csv') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        
        with open('InstructorsOld.csv','w', newline = '') as new_file:
            fieldnames=['Name','DeptName']
            csv_writer=csv.DictWriter(new_file,fieldnames=fieldnames)
            csv_writer.writeheader()
        
            for line in csv_reader:
                if line['Instructor']=='':
                    continue
                csv_writer.writerow({
                    'Name':line['Instructor'],
                    'DeptName':line['Department']
                })

    with open('InstructorsOld.csv','r') as in_file, open('Instructors.csv','w') as out_file:
        seen = set() # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen: continue # skip duplicate
            seen.add(line)
            out_file.write(line)

def generate_Enrollment_And_Home():
    with open('tempCourses.csv') as course_file:
        course_reader = csv.DictReader(course_file)
        with open('Students.csv') as student_file: 
            with open('home.csv', 'w', newline= '') as home_file:
                home_field_name = ['NetId', 'Department']
                home_writer = csv.DictWriter(home_file, fieldnames = home_field_name)
                home_writer.writeheader()
                student_reader = csv.DictReader(student_file)
                with open('Enrollment.csv', 'w', newline= '') as new_file:
                    fieldnames = ['NetId', 'CRN']
                    enrollment_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                    enrollment_writer.writeheader()
                    major_name_list = ['CS', 'ECE', 'MATH', 'FIN', 'ECON']
                    cs_list = {}
                    ece_list = {}
                    fin_list = {}
                    math_list = {}
                    econ_list = {}
                    for line in course_reader:
                        if line['Department'] == 'CS':
                            if line['CourseNumber'] not in cs_list:
                                cs_list[line['CourseNumber']] = line['CRN'] 
                        elif line['Department'] == 'ECE':
                            if line['CourseNumber'] not in ece_list:
                                ece_list[line['CourseNumber']] = line['CRN']
                        elif line['Department'] == 'MATH':
                            if line['CourseNumber'] not in math_list:
                                math_list[line['CourseNumber']] = line['CRN']
                        elif line['Department'] == 'FIN':
                            if line['CourseNumber'] not in fin_list:
                                fin_list[line['CourseNumber']] = line['CRN']
                        elif line['Department'] == 'ECON':
                            if line['CourseNumber'] not in econ_list:
                                econ_list[line['CourseNumber']] = line['CRN']
                    major_list = [cs_list, ece_list, fin_list, math_list, econ_list]
                    for line in student_reader:
                        index = random.randrange(0, 5)
                        home_writer.writerow({'NetId': line['NetId'], 'Department': get_full_name(major_name_list[index])})
                        course_list = random.sample(list(major_list[index].values()), 4)
                        other_major = random.sample(major_list, 1)
                        other_course = random.sample(list(other_major[0].values()), 1)
                        for i in course_list:
                            enrollment_writer.writerow({'NetId': line['NetId'], 'CRN': i})
                        enrollment_writer.writerow({'NetId': line['NetId'], 'CRN': other_course[0]})

def generate_Login_Info():
    with open('LoginInfo.csv', 'w', newline= '') as login_file:
        login_field_name = ['AccountName', 'Password']
        login_writer = csv.DictWriter(login_file, fieldnames = login_field_name)
        login_writer.writeheader()
        with open('Students.csv') as student_file:
            student_reader = csv.DictReader(student_file)
            for line in student_reader:
                password = password_generator(10)
                login_writer.writerow({'AccountName': line['NetId'], 'Password': password})

if __name__ == "__main__":
    subject_dict = get_subject_department()
    generate_student()
    generate_department()
    generate_course()
    generate_instructor()
    generate_Login_Info()
    generate_Enrollment_And_Home()