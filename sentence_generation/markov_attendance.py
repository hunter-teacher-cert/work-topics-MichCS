import random
attendance_chain = {
    'early': ['early', 'early', 'early', 'early', 'early', 'early', 'early', 'early', 'early', 'late'],
    'late': ['early', 'late']
}

attendance = [random.choice(list(attendance_chain.keys()))]

for i in range(10):
    attendance.append(random.choice(attendance_chain[attendance[i]]))

print(attendance)