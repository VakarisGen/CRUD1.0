job_postings = [
    {'id':1,
     'position':'Duomenu analitikas',
     'salary':2000,
     'location':'Vilnius',
     'required_skills':'SQL, Python, PowerBI, Windows, Microsoft Excel'},
    {'id':2,
     'position':'LLM Specialistas',
     'salary':5600,
     'location':'Kaunas',
     'required_skills':'Python, HTML, Math, C++, C#'},
    {'id':3,
     'position':'Head of HR',
     'salary':3400,
     'location':'Klaipeda',
     'required_skills': 'Management, Microsoft Excel, Public speaking, Multitasking'}
]
id_counter = 3

while True:
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
    choice = input()
    match choice:
        case '1': # displaying existing posts
            print('Currently available job postings are:')
            for post in job_postings:
                print(f'{post["id"]}. {post['position']} | Salary: €{post['salary']:.2f} | Location:{post['location']} | Skills: {post['required_skills']}')
        case '2': # adding a new post
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
        case '3': # Editing a post
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
        case '4': # Deleting a post
            print('Deleting a post')
            print('Provide post id you want to delete:')
            del_id = int(input())
            for post in job_postings:
                if del_id == post['id']:
                    job_postings.remove(post)
                    print(f'Job post with id {del_id} was removed')
                    break
        case '5': # exiting a program
            break
