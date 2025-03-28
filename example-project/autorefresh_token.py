import taikunpycore
import taikunpy
import json
import time

client_wrapper = taikunpy.TaikunClient(auto_refresh_minutes=1)  # refresh every 1 minute
client = client_wrapper.api_client

user_info = taikunpycore.UsersApi(client).users_user_info()
print("User Info:", user_info.data.username)
print(json.dumps(client_wrapper.connection_info, indent=4))

# Keep alive to see auto-refresh in action
print("Waiting to observe token refreshes...")
time.sleep(130)

client_wrapper.stop_auto_refresh()
