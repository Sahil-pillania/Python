'''Program to find out whether a student is pass or fail, if it requires total 40%
  and at least 33% marks in each subject to pass.'''

sub1 = int(input("Enter first subject marks:\n "))  # input from user
sub2 = int(input("Enter second subject marks:\n "))  # input from user
sub3 = int(input("Enter third subject marks:\n "))  # input from user
  

if(sub1<33 or sub2<33 or sub3<33):
      print("You are fail because you have less than 33% marks")

if(sub1+sub2+sub3)/3 <40:
      print("You are fail due to less than 40 percentage in result")
else:
    print("You are passed")      