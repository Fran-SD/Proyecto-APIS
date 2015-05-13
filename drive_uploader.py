import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow


# Copia las credenciales que corresponden.
CLIENT_ID = '454591361276-jcff7gtu0llmbrc3efg3kuq23g13d7hg.apps.googleusercontent.com'
CLIENT_SECRET = '93hZNZCHFlHHEjofB4KM-vZE'


OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redireccion de la app instalada.

REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Ruta de los archivos a subir.

FILENAME = 'tweet_by_lang'
FILENAME1 = 'tweet_by_prg_language_1'

# Realiza el login accediendo a la URL que proporciona y comprobando el codigo de autorizacion introducido posteriormente.
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                           redirect_uri=REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Crea un objeto "httplib2.Http" y lo autoriza con nuestras credenciales.

http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Subida de archivos.

media_body = MediaFileUpload(FILENAME, mimetype='image/png', resumable=True)
body = {
  'title': 'tweet_by_lang',
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)

media_body = MediaFileUpload(FILENAME1,mimetype='image/png',resumable=True)
body = {
	'title': 'tweet_by_prg_language_1'
}

file = drive_service.files().insert(body=body,media_body=media_body).execute()
pprint.pprint(file)


