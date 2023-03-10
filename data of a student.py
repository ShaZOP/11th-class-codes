#q7
stRecord = ['Raman','A - 36',[56,98,99,72,69],78.8]
print("The percentage is",stRecord[3],' %')
print("Marks in the 5th subject is ",stRecord[2][4])
print("The max marks",max(stRecord[-2]))
print("The roll number of the student is ",stRecord[1])
stRecord.pop(0)
stRecord.insert(0,"Raghav")
print(stRecord)

