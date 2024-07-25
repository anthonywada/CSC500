Room_Number = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411
}

Instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

Meeting_Time = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

course_number = input("Enter a course number: ").upper()
try:
  print(f"Room Number: {Room_Number[course_number]}\nInstructor: {Instructors[course_number]}\nMeeting Time: {Meeting_Time[course_number]}")
except KeyError:
  print("Course Number not found")
