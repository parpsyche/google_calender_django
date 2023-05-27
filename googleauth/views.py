from django.shortcuts import HttpResponse
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

global creds
def request(request):
    
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    pickle.dump(creds,open('user_token.pkl','wb'))
    return HttpResponse(creds,"Successful")



def redirect(request):
    creds=pickle.load(open('user_token.pkl','rb'))
    service = build('calendar', 'v3', credentials=creds)
    result = service.calendarList().list().execute()
    return HttpResponse(result['items'])