#create a class and function,and list out the items in the list
class multiplefunctions():
    def Subfields():
        Lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Subfields in AI are:")
        print('\n'.join(Lists))
        head="Subfields in AI are:"
        
#Create a function that checks whether the given number is Odd or Even

    def OddEven():
        num=int(input("Enter any number"))
        if(num%2==0):
            print(num,"is Even Number")
            message=num,"is Even Number"
        else:
            print(num,"is Odd Number")
            message=num,"is Odd Number"
        return message
   

# Create a function that tells eligibility of marriage for male and female according to their age limit like 21 for male and 18 for female

    def Eligible():
        gender=input("Your Gender")
        age=int(input("Your Age"))
        if(gender=="male"):
              if(age>=21):
                  print("Eligible")
                  indicate="Eligible"
              else:
                  print("Not Eligible")
                  indicate="Not Eligible"
        if(gender=="female"):
                if(age>=18):
                    print("Eligible")
                    indicate="Eligible"
                else:
                  print("Not Eligible")
                  indicate="Not Eligible"    
        return indicate
    

# calculate the percentage of your 10th mark

    def percentage():
        s1=int(input("Enter Subject1"))
        s2=int(input("Enter Subject2"))      
        s3=int(input("Enter Subject3"))
        s4=int(input("Enter Subject4"))
        s5=int(input("Enter Subject5"))
        print("Subject1=",s1)
        print("Subject2=",s2)
        print("Subject3=",s3)
        print("Subject4=",s4) 
        print("Subject5=",s5)
        total=s1+s2+s3+s4+s5
        print("Total=",total)
        percent=total/5
        print("Percentage",percent)
        return percent    
    

#print area and perimeter of triangle using class and functions

    def triangle():
            h=int(input("Enter height"))
            b=int(input("Enter breadth"))
            print("Height",h)
            print("Breadth",b)
            area=(h*b)/2
            print("Area formula: (Height*Breadth)/2")
            print("Area of Triangle:",area)
            h1=int(input("Enter height1"))
            h2=int(input("Enter height2"))
            b1=int(input("Enter breadth"))
            print("Height1",h1)
            print("Height2",h2)
            print("Breadth",b1)
            perimeter=(b1+h1+h2)
            print("Perimeter formula: Height1+Height2+Breadth")
            print("Perimeter of Triangle:",perimeter)
            return area,perimeter



