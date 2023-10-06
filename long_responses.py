import random


Admission="Yes,Admissions are open.you can find the registration form in our website"
Department='''There are 4 department in our college.They are\n 1.Computer Science and Engineering\n 2.Electronics and Communication Engineering\n 3.Civil Engineering\n 4.Mechanical Engineering
'''
Total_Seats="Totally there are 480 intakes each year that includes 120 in each departments available in our college "
Fees="Tution Fee:2,00,000 \n Hostel Fees:1,20,000\n Mess and Transport Fee:50,000"
Passspercentage="Pass Percentage of 2022-2023 is  99.3"
HPackage="Nethaji P got highest package salary of 1.2 crore."
LPackage="Kumar E got lowest package salary of 20 lakhs"
Grade="Our college is NAC A++ College "
Location="our college is in Egmore,Chennai."
Duty="I am college enquiry helping bot.My work is to answer your questions."
Faculty="Strength of our Teaching Faculty is 50 and all are PHD holders"
Placement="In our college, 90 percentage of students got placed and the other students opted for thier higher studies "
Lab="There are more than 10 labs including Cyber Security lab,AIML lab ,Physics lab,Chemistry lab,Workshop and etc... "
Transport="Yes,Transport facilities are available"
Food="yes, food is available"
FoodType="Yes, both Veg and Non-veg are available"
Eligiblity="You can join our college if marks obtained in each Physics,Chemistry,Mathematics should be greater than 90 percentage"
Dresscode="Formals and Shoe for Boys"
Specialtraining="The special training offered in our college are\n 1.Japnese language\n 2.German language\n 3.Product development\n 3.Cyber Security practices\n 4.Full stack devolopment and etc...."
Website="Our college website is \n wwww.NPTYcoll.com "
Company="Our promising Recruiters are\n ZOHO\t AMAZON\t INFOSIS\t HCL\t IBM\t TCS\t ORACLE\t COGNIZANT\t GOOGLE\t MICROSOFT\n VIRTUSA\t WIPRO\t HITACHI\t ATOS\t CAPGEMINI\t HUBSTREAM\t LTI\t KAAR TECHNOLOGY\t DELTAX\t SUNTEC"
Code="Our Counselling code is 1128"
Work="My work is to answer your simple Queries"

def unknown():
    response = ["Could you please re-phrase that? ",
                "please refer our college website for further informations"][ random.randrange(2)]
    return response