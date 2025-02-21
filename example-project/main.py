import taikunpycore
import taikunpy
import json

# Create the authentication wrapper
client = taikunpy.TaikunClient().api_client

# Print info about user
user_info = taikunpycore.UsersApi(client).users_user_info()
print("User Info:", user_info.data.username)
# print(json.dumps(user_info.to_dict(), indent=4))

# Print json information about the first project.
# list_projects = taikunpycore.ProjectsApi(client).projects_list(limit=1)
# print(json.dumps(list_projects.to_dict(), indent=4))

# Print json information about the available kubernetes profiles
# list_k8sprofiles = taikunpycore.KubernetesProfilesApi(client).kubernetesprofiles_list(limit=1)
# print(json.dumps(list_k8sprofiles.to_dict(), indent=4))

