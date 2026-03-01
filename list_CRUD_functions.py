def f_main_menu():
    print('')
    print('=|=|=|=|=|=|=|=|=|=|=|=|=')
    print('')
    print('1. Show job postings')
    print('2. Add job posting')
    print('3. Edit job posting')
    print('4. Delete job posting')
    print('5. Exit')
    print('')
    print('=|=|=|=|=|=|=|=|=|=|=|=|=')
    print('')

def f_show_job_postings(job_postings):
    print('Currently available job postings are:')
    for post in job_postings:
        print(
            f'{post["id"]}. {post['position']} | Salary: €{post['salary']:.2f} | Location:{post['location']} | Skills: {post['required_skills']}')

def f_add_job_posting(job_postings, id_counter):
    print('To add a job posting, please fill required information:')
    print('Job position:')
    position = input()
    print('Salary:')
    salary = float(input())
    print('Job location:')
    location = input()
    print('Required skills:')
    skills = input()
    id_counter += 1
    new_post = {
        'id': id_counter,
        'position': position,
        'salary': salary,
        'location': location,
        'required_skills': skills
    }
    job_postings.append(new_post)
    return id_counter

def f_edit_job_posting(job_postings):
    print('Jobs posting editor, please provide required information')
    print('Provide the posting id that needs to be edited:')
    edit_id = int(input())
    for post in job_postings:
        if post['id'] == edit_id:
            print('Enter a new position title:')
            post['position'] = input()
            print('Enter new salary:')
            post['salary'] = float(input())
            print('Enter new location:')
            post['location'] = input()
            print('Enter new required skills:')
            post['required_skills'] = input()
        else:
            print('Post with such id does not exist')

def f_delete_job_posting(job_postings):
    print('Deleting a post')
    print('Provide post id you want to delete:')
    del_id = int(input())
    for post in job_postings:
        if del_id == post['id']:
            job_postings.remove(post)
            print(f'Job post with id {del_id} was deleted')
            break