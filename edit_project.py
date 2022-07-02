from view_projects import view
def edit(user_id):
    all_projects=view(user_id)
    project_name = input('\nSelect one projct to edit : ')
    for l in all_projects:
        user_project = l.strip("\n")
        user_project = user_project.split(":")
        if user_project[1] == project_name and user_id==user_project[0]:
            print(all_projects)
            key_name = input('\n\nplease choose t for edit project tittle, d for edit project details  , g for edit project targrt, s for edit start date ,e for edit end date, a for edit all : ')
            if key_name == "t":
                newtittle= input("please enter new project name: ")
                user_project[1]= newtittle
            elif key_name == "d":
                proj_detail = input("please enter new proj_detail: ")
                user_project[2]= proj_detail
            elif key_name == "g":
                proj_target = input("please enter new proj_target: ")
                user_project[3]= proj_target
            elif key_name == "s":
                proj_start = input("please enter new start date: ")
                user_project[4]= proj_start
            elif key_name == "e":
                proj_end = input("please enter new end date: ")
                user_project[5] = proj_end
            elif key_name == "a":
                newtittle = input("please enter new project name: ")
                user_project[1] = newtittle
                proj_detail = input("please enter new proj_detail: ")
                user_project[2] = proj_detail
                proj_target = input("please enter new proj_target: ")
                user_project[3] = proj_target
                proj_start = input("please enter new start date: ")
                user_project[4] = proj_start
                proj_end = input("please enter new end date: ")
                user_project[5] = proj_end

            updated_project = ":".join(user_project)
            updated_project = f"{updated_project}\n"
            project_index = all_projects.index(l)
            print(project_index)
            all_projects[project_index] = updated_project
            break
    w = open("projects_data.txt", "w")
    w.writelines(all_projects)
    w.close()


edit(1)


