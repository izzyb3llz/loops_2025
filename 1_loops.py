# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print (len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])

for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
print(len(subjects))
for subject in subjects:
    print(subject)
# Challenge:
#stop printing the subjects when you reach history 
for subject in subjects:
    if subject=="History":
        break 
    else:
        print(subject)
#skip over science and print the rest\
for subject in subjects:
    if subject=="Science":
        continue
    else:
        print(subject)
# Use a for loop and range to print each subject along with its index:
for index in range (len(subjects)):
    print("Subject:"+str(index)+ ":" + subjects[index])
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
total=0 #do not keep it in the loop because if you do then the loop will continue to print 0
for number in numbers:
    total += number #+= means total + number =
print("Total:", total)
#sum up the numbers from 1-60000
new_numbers= list(range(1,600001))
total=0
for number in new_numbers:
    total+= number 
print("Total:", total)

new_list=list(range(5,26))
total_new=0
for x in new_list:
    total_new+= x
print("Total:", total_new)