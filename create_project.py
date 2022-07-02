import time
# from project import menu

def create(user_id):

    title = input("Title : ")
    details = input("Details : ")
    total_target = input("Total target : ")
    start_time = input("Start Date (mm/dd/yyyy) : ")
    end_time = input("End Date (mm/dd/yyyy) : ")

    try:
        valid_date1 = time.strptime(start_time, '%m/%d/%Y')
        valid_date2 = time.strptime(end_time, '%m/%d/%Y')

        if valid_date1 and valid_date2:
            try:
                users_projects = open("projects_data.txt", "a")
            except Exception as e:
                print(e)
            else:
                user_data = f"{user_id}:{title}:{details}:{total_target}:{start_time}:{end_time}\n"
                users_projects.write(user_data)
                users_projects.close()
                print('Your project is created successfully')
    except Exception as e:
        print(e)
        print("\nYour data is invalid ,, please enter valid data :")
        create(user_id)

