import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect


APP_KEY = "p5w29rjp68u3vjf"
APP_SECRET = "sj5iexe9gs0x91x"

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
except Exception as e:
    print('Error: %s' % (e,))
    exit(1)

dbx = dropbox.Dropbox(oauth2_access_token=oauth_result.access_token)
dbx.users_get_current_account()
print("Successfully set up client!")