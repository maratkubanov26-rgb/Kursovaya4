students_list = []

num_students_added = 0

while True:
    print("\n=== Main Menu ===")
    print("\n1. See students")
    print("2. Add a student")
    print("3. Search for a student")
    # subfolder: make it so u can search for students above a certain age
    print("4. Quit programm")

    user_input = input("\nChose your option (1-3): ")
    if user_input == "1":
        print(students_list)
    elif user_input == "2":
        student = {}
        name = input("Name: ")
        name = name.capitalize()
        student["name"] = name

        age = input("Age: ")
        student["age"] = int(age)

        city = input("City: ")
        student["city"] = city.capitalize()
        stdnt_gr_poh = input("Grades (if u can't enter this parameter - press enter): ").split(",")
        stdnt_gr = []
        try:
            for i in stdnt_gr_poh:
                stdnt_gr.append(int(i))
        except ValueError:
            print("please, enter grades divided by commas")

        summa = sum(stdnt_gr)
        quant_gr = len(stdnt_gr)
        stdnt_avr_gr = summa / quant_gr
        stdnt_avr_gr = round(stdnt_avr_gr, 1)

        student["average"] = stdnt_avr_gr

        ayushure = input(f"Are you sure you want to add this student to the list?:"
                         f"\nname - {name}"
                         f"\nage - {age}"
                         f"\ncity - {city}"
                         f"\ngrades - {stdnt_gr}"
                         f"\naverage grade - {stdnt_avr_gr}: Y/n")
        ayushure = ayushure.lower()
        if ayushure == "y":
            students_list.append(student)
            num_students_added += 1
            print("\nStudent added!")
        elif ayushure == "n":
            print("quitting the program. Do it right this time;)")
            break
        else:
            print("student not added"
                  "you needed to enter \"y\" or \"n\"")

    elif user_input == "4":
        print("exiting the main menu...")
        break

# код без try/except потому что переменные, созданные в этой функции не работают за её пределами
# я пока не понял как это исправить
