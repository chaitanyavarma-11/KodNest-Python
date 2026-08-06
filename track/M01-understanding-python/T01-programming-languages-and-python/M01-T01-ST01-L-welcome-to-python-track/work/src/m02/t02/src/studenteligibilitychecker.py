# Read marks, attendence and project completion status
marks=int(input()) 
attendence=int(input())
projects=input()
# Check the academic requirements
 
# Check the projects completion status
if marks>=60 and attendence>=75:
    if projects=="yes":
     print("Eligible")
    else:
      print(" Not Eligible")
else:
    print("Not Eligible")

