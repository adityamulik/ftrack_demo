import ftrack_api
import arrow
import json

def get_key(path):
  with open(path) as f:
    return json.load(f)

key = get_key("./secret.json")

session = ftrack_api.Session(
  server_url='https://self-aditya.ftrackapp.com',
  api_key=key['API_Key'],
  api_user='adi.mulik2011@gmail.com'
)

# print(session.types.keys())

projects = session.query('Project')

# print(projects[0].keys())

for project in projects:
  # print(project['name'])
  pass

active_projs = session.query('Project where status is active')

for project in active_projs:
  print(project['name'])

print(active_projs[0]['name'])

hidden_projs = session.query('Project where status is hidden')

for project in hidden_projs:
  print(f"Set Project as Hidden: {project['name']}")

# active_projects_ending_before_next_week = session.query(
#    'Project where status is active and end_date before "{0}"'
#    .format(arrow.now().replace(weeks=+1))
# )

# print(active_projects_ending_before_next_week)

def create_sequence(name, desc):
    """
      Create a sequence and
      appended to a project.
    """

    # Retrieve main project
    main_project = session.query('Project').first()

    new_sequence = session.create('Sequence', {
      'name': name
    })

    new_sequence['description'] = desc

    new_sequence['parent'] = main_project
    
    main_project['children'].append(new_sequence)

    try:
      session.commit()
      print(f"Sequence {new_sequence['name']} appended to the project {main_project['name']}!")
    except:
      print(f"Duplicate Entry Error!")


create_sequence('Demo Interview Sequence', 'This is just a demo interview sequence!')