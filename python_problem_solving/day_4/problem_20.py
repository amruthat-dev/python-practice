marks = int(input("Enter your marks: "))
entrance_exam_marks = int(input("Enter your entrance exam marks: "))
if marks >= 90:
    print(f"Well done! your marks are {marks}. you will get the direct admission in the college.")
else:
    print("cheke your marks and entrance exam marks for normal admission eligibility.")

    if marks >= 75 and entrance_exam_marks >= 60:
        print(f"Congratulations! you are admission is Approved in the college.")
    elif marks >= 75 and entrance_exam_marks < 60:
        print(f"Sorry, you are not eligible for admission.Your entrance exam marks are {entrance_exam_marks}. You need at least 60 marks in the entrance exam for admission.")
    elif marks < 75 and entrance_exam_marks >= 60:
        print(f"Sorry, you are not eligible for admission. Your marks are {marks}. You need at least 75 marks for admission.")
    else:
        print(f"Sorry, you are not eligible for admission. Your marks are {marks} and your entrance exam marks are {entrance_exam_marks}. You need at least 75 marks and 60 marks in the entrance exam for admission.")
