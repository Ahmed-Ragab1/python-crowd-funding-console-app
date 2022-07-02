from view_projects import view
import time

def search(user_id):
    all_projects=view(user_id)
    project_date = input('\nWrite project date (mm/dd/yyyy) : ')
    try:
        valid_date = time.strptime(project_date, '%m/%d/%Y')
        if valid_date:
            for l in all_projects:
                user_project = l.strip("\n")
                user_project = user_project.split(":")
                if user_project[4] == project_date:
                    print(user_project)
        else:
            print("\nYour data is invalid ,, please enter valid data :")

    except ValueError:
        print('Invalid date!')

search(1)