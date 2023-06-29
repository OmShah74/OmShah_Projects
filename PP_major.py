# import numpy as np
# import pandas as pd
# import csv
import matplotlib.pyplot as plt
import pandas as pd

print("**********************************************************************")
print("******************************WELCOME*********************************")
print("**********************************************************************")


print('\n')
od = pd.read_csv('student_data.csv')
df = pd.DataFrame(od)
# print(pd)


# Code for Faculty review
facrev = []
for i in df['Faculty review']:
    i = int(i)
    if 7.5 < i <= 10:
        facrev.append(i * 1.25)
    elif 5 < i <= 7.5:
        facrev.append(i * 1.25)
    elif 2.5 < i <= 5:
        facrev.append(i * 1.25)
    elif 0 < i <= 2.5:
        facrev.append(i * 1.25)
    else:
        facrev.append(0)

# code for time invested
time_inv = []
for i in df['Time Invested']:
    i = int(i)
    if 12 < i <= 15:
        time_inv.append(12.5)
    elif 9 < i <= 12:
        time_inv.append((5 / 6) * 12.5)
    elif 9 < i <= 12:
        time_inv.append((4 / 6) * 12.5)
    elif 6 < i <= 9:
        time_inv.append((3 / 6) * 12.5)
    elif 3 < i <= 6:
        time_inv.append((2 / 6) * 12.5)
    else:
        time_inv.append(3)

# Total points of extracurricular
exCur = []
for i, j in zip(facrev, time_inv):
    exCur.append(i + j)

# Code for GPA
Gpa = []
for i in df['GPA']:
    if i == 4:
        Gpa.append(25)
    elif 3.75 <= i < 4:
        Gpa.append((6 / 7) * 25)
    elif 3.5 <= i < 3.75:
        Gpa.append((5 / 7) * 25)
    elif 3.25 <= i < 3.5:
        Gpa.append((4 / 7) * 25)
    elif 3 <= i < 3.25:
        Gpa.append((3 / 7) * 25)
    elif 2.75 <= i < 3:
        Gpa.append((2 / 7) * 25)
    elif 2.5 <= i < 2.75:
        Gpa.append((1 / 7) * 25)
    else:
        Gpa.append(0)

# Code for internships
internships = []
for i in df['Internships']:
    i = int(i)
    if i == 4:
        internships.append(25)
    elif i == 3:
        internships.append(0.75 * 25)
    elif i == 2:
        internships.append(0.5 * 25)
    elif i == 1:
        internships.append(0.25 * 25)

# Code for skills
libasic, liint, liadv = [], [], []


def basicSkills(basic_count):
    if basic_count == 3:
        libasic.append(33)
    elif basic_count == 2:
        libasic.append(22)
    elif basic_count == 1:
        libasic.append(11)
    else:
        libasic.append(0)


def interSkills(inter_count):
    if inter_count == 5:
        liint.append(33)
    elif inter_count == 4:
        liint.append(26.4)
    elif inter_count == 3:
        liint.append(19.8)
    elif inter_count == 2:
        liint.append(13.2)
    elif inter_count == 1:
        liint.append(6.6)
    else:
        liint.append(0)


def advSkills(adv_count):
    if adv_count == 5:
        liadv.append(33)
    elif adv_count == 4:
        liadv.append(26.4)
    elif adv_count == 3:
        liadv.append(19.8)
    elif adv_count == 2:
        liadv.append(13.2)
    elif adv_count == 1:
        liadv.append(6.6)
    else:
        liadv.append(0)


basic = ['C++', 'Java', 'Python']
inter = ['Appdev', 'Webdev', 'DBMS', 'Cloud', 'Cyber']
adv = ['MLN', 'NLP', 'Fuzzylogic', 'Expertsystem', 'Datascience']
for i, j, k in zip(df['Basic'], df['Intermediate'], df['Advanced']):
    basic_count = sum(skill1 in i for skill1 in basic)
    inter_count = sum(skill2 in j for skill2 in inter)
    adv_count = sum(skill3 in k for skill3 in adv)
    basicSkills(basic_count)
    interSkills(inter_count)
    advSkills(adv_count)

Skills = []
for i, j, k in zip(libasic, liint, liadv):
    Skills.append(i + j + k)
# print('Skills:\n',Skills)
# print('Academics:\n',Gpa)
# print('Extra curricular:\n',exCur)
# print('Internships:\n',internships)

# Total
# percentages:
# Skills-35  Academics-25  Internships-25  Extracurricular-15
TotalRating = []
# for i,j,k,l in zip(Skills,Gpa,exCur,internships):
#     TotalRating.append((i*0.35)+(j)+(k)+(l*0.6))
# print('Total Rating:\n',TotalRating)

#  User input for percentage of different components of rating system
skper = float(input('Enter percentage for Skills\n'))
gpaper = float(input('Enter percentage for Academics\n'))
internper = float(input('Enter percentage for Internships\n'))
excurper = float(input('Enter percentage for Extracurricular activities\n'))
for i, j, k, l in zip(Skills, Gpa, exCur, internships):
    TotalRating.append((i * (skper / 99)) + (j * (gpaper / 25)) + (k * (internper / 25)) + (l * (excurper / 25)))
df['Rating'] = pd.DataFrame(TotalRating)


# display students data in sorted form
def sortStudsAsc(df, tipe, num):
    if tipe == 'ascending' or tipe == 'lowest':
        print('Sorted Ratings of students in ascending order over all branches:')
        f_plot = df.sort_values(by='Rating').head(num)
        print(f_plot)
        x1 = f_plot["Name"]
        y1 = f_plot["Rating"]
        plt.scatter(y1, x1)
        plt.xlabel("Ratings")
        plt.ylabel("Name of the student")
        plt.show()
    elif tipe == 'descending' or tipe == 'top':
        print('Sorted Ratings of students in descending order over all branches:')
        f_plot = df.sort_values(by='Rating', ascending=False).head(num)
        print(f_plot)
        x1 = f_plot["Name"]
        y1 = f_plot["Rating"]
        plt.scatter(y1, x1)
        plt.xlabel("Ratings")
        plt.ylabel("Name of the student")
        plt.show()


# display students name and branch sorted by skills
def sortSkills(df, Skills, tipe, num):
    skilldata = pd.DataFrame(df['Name'])
    skilldata['Branch'] = df['Branch']
    skilldata['Skills'] = pd.DataFrame(Skills)
    if (tipe == 'ascending' or tipe == 'lowest'):
        print('Students accross all branches sorted by increasing skills:')
        print(skilldata.sort_values(by='Skills').head(num))
    elif (tipe == 'descending' or tipe == 'top'):
        print('Students accross all branches sorted by decreasing skills:')
        print(skilldata.sort_values(by='Skills', ascending=False).head(num))


# display students name and branch sorted by internships
def sortInternships(df, tipe, num):
    skilldata = pd.DataFrame(df['Name'])
    skilldata['Branch'] = df['Branch']
    skilldata['Internships'] = df['Internships']
    if (tipe == 'ascending' or tipe == 'lowest'):
        print('Students accross all branches sorted by increasing internships:')
        print(skilldata.sort_values(by='Internships').head(num))
    elif (tipe == 'descending' or tipe == 'top'):
        print('Students accross all branches sorted by decreasing internships:')
        print(skilldata.sort_values(by='Internships', ascending=False).head(num))


# display students name and branch sorted by GPA
def sortGpa(df, tipe, num):
    skilldata = pd.DataFrame(df['Name'])
    skilldata['Branch'] = df['Branch']
    skilldata['GPA'] = df['GPA']
    if (tipe == 'ascending' or tipe == 'lowest'):
        print('Students accross all branches sorted by increasing GPA:')
        print(skilldata.sort_values(by='GPA').head(num))
    elif (tipe == 'descending' or tipe == 'top'):
        print('Students accross all branches sorted by decreasing GPA:')
        print(skilldata.sort_values(by='GPA', ascending=False).head(num))


# display top or bottom numbered num students in each branch/ inputed branch
def displayStudsPerBranchRating(df, num, bran, tipe):
    if tipe == 'top':
        if bran == 'CE':
            print('Top students in CE')
            topCE = pd.DataFrame(df['Name'].where(df.Branch == 'CE').dropna())
            topCE['Rating'] = df['Rating'].where(df.Branch == 'CE').dropna()
            f_plot = topCE.sort_values(by='Rating', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN CE", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('Top students in IT')
            topIT = pd.DataFrame(df['Name'].where(df.Branch == 'IT').dropna())
            topIT['Rating'] = df['Rating'].where(df.Branch == 'IT').dropna()
            f_plot = topIT.sort_values(by='Rating', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN IT", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('Top students in AI')
            topAI = pd.DataFrame(df['Name'].where(df.Branch == 'AI').dropna())
            topAI['Rating'] = df['Rating'].where(df.Branch == 'AI').dropna()
            f_plot = topAI.sort_values(by='Rating', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN AI", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('Top students in DS')
            topDS = pd.DataFrame(df['Name'].where(df.Branch == 'DS').dropna())
            topDS['Rating'] = df['Rating'].where(df.Branch == 'DS').dropna()
            f_plot = topDS.sort_values(by='Rating', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN DS", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('Top students in EXTC')
            topEXTC = pd.DataFrame(df['Name'].where(df.Branch == 'EXTC').dropna())
            topEXTC['Rating'] = df['Rating'].where(df.Branch == 'EXTC').dropna()
            f_plot = topEXTC.sort_values(by='Rating', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN EXTC", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

    elif tipe == 'lowest':
        if bran == 'CE':
            print('weak students in CE')
            weakCE = pd.DataFrame(df['Name'].where(df.Branch == 'CE').dropna())
            weakCE['Rating'] = df['Rating'].where(df.Branch == 'CE').dropna()
            f_plot = weakCE.sort_values(by='Rating').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN CE", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('weak students in IT')
            weakIT = pd.DataFrame(df['Name'].where(df.Branch == 'IT').dropna())
            weakIT['Rating'] = df['Rating'].where(df.Branch == 'IT').dropna()
            f_plot = weakIT.sort_values(by='Rating').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN IT", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('weak students in AI')
            weakAI = pd.DataFrame(df['Name'].where(df.Branch == 'AI').dropna())
            weakAI['Rating'] = df['Rating'].where(df.Branch == 'AI').dropna()
            f_plot = weakAI.sort_values(by='Rating').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN AI", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('weak students in DS')
            weakDS = pd.DataFrame(df['Name'].where(df.Branch == 'DS').dropna())
            weakDS['Rating'] = df['Rating'].where(df.Branch == 'DS').dropna()
            f_plot = weakDS.sort_values(by='Rating').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN DS", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('weak students in EXTC')
            weakEXTC = pd.DataFrame(df['Name'].where(df.Branch == 'EXTC').dropna())
            weakEXTC['Rating'] = df['Rating'].where(df.Branch == 'EXTC').dropna()
            f_plot = weakEXTC.sort_values(by='Rating').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Rating']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN CE", loc='left')
            plt.xlabel("Ratings")
            plt.ylabel("Name of the student")
            plt.show()


def displayStudsPerBranchGPA(df, num, bran, tipe):
    if tipe == 'top':
        if bran == 'CE':
            print('Top students in CE')
            topCE = pd.DataFrame(df['Name'].where(df.Branch == 'CE').dropna())
            topCE['GPA'] = df['GPA'].where(df.Branch == 'CE').dropna()
            f_plot = topCE.sort_values(by='GPA', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN CE BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('Top students in IT')
            topIT = pd.DataFrame(df['Name'].where(df.Branch == 'IT').dropna())
            topIT['GPA'] = df['GPA'].where(df.Branch == 'IT').dropna()
            f_plot = topIT.sort_values(by='GPA', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN IT BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('Top students in AI')
            topAI = pd.DataFrame(df['Name'].where(df.Branch == 'AI').dropna())
            topAI['GPA'] = df['GPA'].where(df.Branch == 'AI').dropna()
            f_plot = topAI.sort_values(by='GPA', ascending=False).head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN AI BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('Top students in DS')
            topDS = pd.DataFrame(df['Name'].where(df.Branch == 'DS').dropna())
            topDS['GPA'] = df['GPA'].where(df.Branch == 'DS').dropna()
            f_plot = (topDS.sort_values(by='GPA', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN DS", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('Top students in EXTC')
            topEXTC = pd.DataFrame(df['Name'].where(df.Branch == 'EXTC').dropna())
            topEXTC['GPA'] = df['GPA'].where(df.Branch == 'EXTC').dropna()
            f_plot = (topEXTC.sort_values(by='GPA', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN EXTC BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

    elif tipe == 'lowest':
        if bran == 'CE':
            print('weak students in CE')
            weakCE = pd.DataFrame(df['Name'].where(df.Branch == 'CE').dropna())
            weakCE['GPA'] = df['GPA'].where(df.Branch == 'CE').dropna()
            f_plot = (weakCE.sort_values(by='GPA').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN CE BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('weak students in IT')
            weakIT = pd.DataFrame(df['Name'].where(df.Branch == 'IT').dropna())
            weakIT['GPA'] = df['GPA'].where(df.Branch == 'IT').dropna()
            f_plot = (weakIT.sort_values(by='GPA').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN IT BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('weak students in AI')
            weakAI = pd.DataFrame(df['Name'].where(df.Branch == 'AI').dropna())
            weakAI['GPA'] = df['GPA'].where(df.Branch == 'AI').dropna()
            f_plot = (weakAI.sort_values(by='GPA').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN AI", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('weak students in DS')
            weakDS = pd.DataFrame(df['Name'].where(df.Branch == 'DS').dropna())
            weakDS['GPA'] = df['GPA'].where(df.Branch == 'DS').dropna()
            f_plot = (weakDS.sort_values(by='GPA').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN DS BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('weak students in EXTC')
            weakEXTC = pd.DataFrame(df['Name'].where(df.Branch == 'EXTC').dropna())
            weakEXTC['GPA'] = df['GPA'].where(df.Branch == 'EXTC').dropna()
            f_plot = (weakEXTC.sort_values(by='GPA').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['GPA']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN EXTC BY GPA", loc='left')
            plt.xlabel("GPA")
            plt.ylabel("Name of the student")
            plt.show()


def displayStudsPerBranchInter(df, num, bran, tipe):
    if tipe == 'top':
        if bran == 'CE':
            print('Top students in CE')
            topCE = pd.DataFrame(df['Name'].where(df.Branch == 'CE').dropna())
            topCE['Internships'] = df['Internships'].where(df.Branch == 'CE').dropna()
            f_plot = (topCE.sort_values(by='Internships', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN CE BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('Top students in IT')
            topIT = pd.DataFrame(df['Name'].where(df.Branch == 'IT').dropna())
            topIT['Internships'] = df['Internships'].where(df.Branch == 'IT').dropna()
            f_plot = (topIT.sort_values(by='Internships', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN IT BY INTERNSHIP", loc='left')
            plt.xlabel("Internship")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('Top students in AI')
            topAI = pd.DataFrame(df['Name'].where(df.Branch == 'AI').dropna())
            topAI['Internships'] = df['Internships'].where(df.Branch == 'AI').dropna()
            f_plot = (topAI.sort_values(by='Internships', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN AI BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('Top students in DS')
            topDS = pd.DataFrame(df['Name'].where(df.Branch == 'DS').dropna())
            topDS['Internships'] = df['Internships'].where(df.Branch == 'DS').dropna()
            f_plot = (topDS.sort_values(by='Internships', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN DS BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('Top students in EXTC')
            topEXTC = pd.DataFrame(df['Name'].where(df.Branch == 'EXTC').dropna())
            topEXTC['Internships'] = df['Internships'].where(df.Branch == 'EXTC').dropna()
            f_plot = (topEXTC.sort_values(by='Internships', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN CE BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

    elif tipe == 'lowest':
        if bran == 'CE':
            print('weak students in CE')
            weakCE = pd.DataFrame(df['Name'].where(df.Branch == 'CE').dropna())
            weakCE['Internships'] = df['Internships'].where(df.Branch == 'CE').dropna()
            f_plot = (weakCE.sort_values(by='Internships').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN CE BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('weak students in IT')
            weakIT = pd.DataFrame(df['Name'].where(df.Branch == 'IT').dropna())
            weakIT['Internships'] = df['Internships'].where(df.Branch == 'IT').dropna()
            f_plot = (weakIT.sort_values(by='Internships').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN IT BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('weak students in AI')
            weakAI = pd.DataFrame(df['Name'].where(df.Branch == 'AI').dropna())
            weakAI['Internships'] = df['Internships'].where(df.Branch == 'AI').dropna()
            f_plot = (weakAI.sort_values(by='Internships').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN AI BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('weak students in DS')
            weakDS = pd.DataFrame(df['Name'].where(df.Branch == 'DS').dropna())
            weakDS['Internships'] = df['Internships'].where(df.Branch == 'DS').dropna()
            f_plot = (weakDS.sort_values(by='Internships').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN DS BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('weak students in EXTC')
            weakEXTC = pd.DataFrame(df['Name'].where(df.Branch == 'EXTC').dropna())
            weakEXTC['Internships'] = df['Internships'].where(df.Branch == 'EXTC').dropna()
            f_plot = (weakEXTC.sort_values(by='Internships').head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Internships']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN EXTC BY INTERNSHIP", loc='left')
            plt.xlabel("Internships")
            plt.ylabel("Name of the student")
            plt.show()


def displayStudsPerBranchSkills(df, num, bran, Skills, tipe):
    df1 = df
    df1['Skills'] = pd.DataFrame(Skills)
    if tipe == 'top':
        if bran == 'CE':
            print('Top students in CE')
            topCE = pd.DataFrame(df1['Name'].where(df1.Branch == 'CE').dropna())
            topCE['Skills'] = df1['Skills'].where(df1.Branch == 'CE').dropna()
            f_plot = (topCE.sort_values(by='Skills', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN CE BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('Top students in IT')
            topIT = pd.DataFrame(df1['Name'].where(df1.Branch == 'IT').dropna())
            topIT['Skills'] = df1['Skills'].where(df1.Branch == 'IT').dropna()
            f_plot = (topIT.sort_values(by='Skills', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN IT BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('Top students in AI')
            topAI = pd.DataFrame(df1['Name'].where(df1.Branch == 'AI').dropna())
            topAI['Skills'] = df1['Skills'].where(df1.Branch == 'AI').dropna()
            f_plot = (topAI.sort_values(by='Skills', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN AI BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('Top students in DS')
            topDS = pd.DataFrame(df1['Name'].where(df1.Branch == 'DS').dropna())
            topDS['Skills'] = df1['Skills'].where(df1.Branch == 'DS').dropna()
            f_plot = (topDS.sort_values(by='Skills', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN DS BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('Top students in EXTC')
            topEXTC = pd.DataFrame(df1['Name'].where(df1.Branch == 'EXTC').dropna())
            topEXTC['Skills'] = df1['Skills'].where(df1.Branch == 'EXTC').dropna()
            f_plot = (topEXTC.sort_values(by='Skills', ascending=False).head(num))
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("TOP STUDENTS IN EXTC BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

    elif tipe == 'lowest':
        if bran == 'CE':
            print('weak students in CE')
            weakCE = pd.DataFrame(df1['Name'].where(df1.Branch == 'CE').dropna())
            weakCE['Skills'] = df1['Skills'].where(df1.Branch == 'CE').dropna()
            f_plot = weakCE.sort_values(by='Skills').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN CE BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'IT':
            print('weak students in IT')
            weakIT = pd.DataFrame(df1['Name'].where(df1.Branch == 'IT').dropna())
            weakIT['Skills'] = df1['Skills'].where(df1.Branch == 'IT').dropna()
            f_plot = weakIT.sort_values(by='Skills').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN IT BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'AI':
            print('weak students in AI')
            weakAI = pd.DataFrame(df1['Name'].where(df1.Branch == 'AI').dropna())
            weakAI['Skills'] = df1['Skills'].where(df1.Branch == 'AI').dropna()
            f_plot = weakAI.sort_values(by='Skills').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN AI BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'DS':
            print('weak students in DS')
            weakDS = pd.DataFrame(df1['Name'].where(df1.Branch == 'DS').dropna())
            weakDS['Skills'] = df1['Skills'].where(df1.Branch == 'DS').dropna()
            f_plot = weakDS.sort_values(by='Skills').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN DS BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

        elif bran == 'EXTC':
            print('weak students in EXTC')
            weakEXTC = pd.DataFrame(df1['Name'].where(df1.Branch == 'EXTC').dropna())
            weakEXTC['Skills'] = df1['Skills'].where(df1.Branch == 'EXTC').dropna()
            f_plot = weakEXTC.sort_values(by='Skills').head(num)
            print(f_plot)
            x1 = f_plot['Name']
            y1 = f_plot['Skills']
            plt.scatter(y1, x1)
            plt.title("LOWEST STUDENTS IN EXTC BY SKILLS", loc='left')
            plt.xlabel("Skills")
            plt.ylabel("Name of the student")
            plt.show()

adjective = ['sorted', 'top', 'lowest', 'most', 'ascending', 'descending', 'common']
labels = ['rating', 'branch', 'skill', 'gpa', 'internships', 'basic', 'intermediate', 'advanced', 'percentage', 'all']
while True:
    query = str(input('\nEnter query (enter "0" to exit)\n'))
    if query != '0':
        query=query.lower()
        listq=query.split()
        for i in listq:
            if i.isdigit():
                if int(i) in df['Rollno']:
                    print(df.loc[df['Rollno']==int(i),:])
                else:
                    print('The roll number dosent exist')
        if adjective[0] in query and adjective[4] in query:
            num = int(input('Till how many students\n'))
            sortStudsAsc(df, adjective[4], num)
        if adjective[0] in query and adjective[5] in query:
            num = int(input('Till how many students\n'))
            sortStudsAsc(df, adjective[5], num)
        if (adjective[4] in query or adjective[1] in query) and labels[2] in query and labels[-1] in query:
            num = int(input('Till how many students\n'))
            sortSkills(df, Skills, adjective[1], num)
        if (adjective[5] in query or adjective[2] in query) and labels[2] in query and labels[9] in query:
            num = int(input('Till how many students\n'))
            sortSkills(df, Skills, adjective[2], num)
        if (adjective[4] in query or adjective[1] in query) and labels[3] in query and labels[-1] in query:
            num = int(input('Till how many students\n'))
            sortGpa(df, adjective[1], num)
        if (adjective[5] in query or adjective[2] in query) and labels[3] in query and labels[-1] in query:
            num = int(input('Till how many students\n'))
            sortGpa(df, adjective[2], num)
        if (adjective[4] in query or adjective[1] in query) and labels[4] in query and labels[-1] in query:
            num = int(input('Till how many students\n'))
            sortInternships(df, adjective[1], num)
        if (adjective[5] in query or adjective[2] in query) and labels[4] in query and labels[-1] in query:
            num = int(input('Till how many students\n'))
            sortInternships(df, adjective[2], num)
        if adjective[1] in query and labels[1] in query and labels[0] in query and labels[-1] not in query and labels[
            3] not in query and labels[4] not in query and labels[2] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchRating(df, num, bran, adjective[1])
        if adjective[2] in query and labels[1] in query and labels[0] in query and labels[-1] not in query and labels[
            3] not in query and labels[4] not in query and labels[2] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchRating(df, num, bran, adjective[2])
        if adjective[1] in query and labels[3] in query and labels[1] in query and labels[-1] not in query and labels[
            0] not in query and labels[4] not in query and labels[2] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchGPA(df, num, bran, adjective[1])
        if adjective[2] in query and labels[3] in query and labels[1] in query and labels[-1] not in query and labels[
            0] not in query and labels[4] not in query and labels[2] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchGPA(df, num, bran, adjective[2])
        if adjective[1] in query and labels[4] in query and labels[1] in query and labels[-1] not in query and labels[
            0] not in query and labels[3] not in query and labels[2] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchInter(df, num, bran, adjective[1])
        if adjective[2] in query and labels[4] in query and labels[1] in query and labels[-1] not in query and labels[
            0] not in query and labels[3] not in query and labels[2] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchInter(df, num, bran, adjective[2])
        if adjective[1] in query and labels[2] in query and labels[1] in query and labels[-1] not in query and labels[
            0] not in query and labels[3] not in query and labels[4] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchSkills(df, num, bran, Skills, adjective[1])
        if adjective[2] in query and labels[2] in query and labels[1] in query and labels[-1] not in query and labels[
            0] not in query and labels[3] not in query and labels[4] not in query:
            num = int(input('Till how many students?\n'))
            bran = input('Enter branch\n')
            displayStudsPerBranchSkills(df, num, bran, Skills, adjective[1])
        else:
            print('Please enter another query')
    else:
        break