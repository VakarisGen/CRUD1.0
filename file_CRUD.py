from file_CRUD_functions import *

job_postings = load_file()
id_counter = 3

while True:
    f_main_menu()
    choice = input()
    match choice:
        case '1': # displaying existing posts
            f_show_job_postings(job_postings)
        case '2': # adding a new post
            id_counter = f_add_job_posting_file(job_postings, id_counter)
        case '3': # Editing a post
            f_edit_job_posting(job_postings)
        case '4': # Deleting a post
            f_delete_job_posting(job_postings)
        case '5': # exiting a program
            break
        case _:
            print("Wrong choice, try again")