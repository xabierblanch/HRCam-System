import os
import dropbox

#########################################################################
#########################################################################

#IDENTIFICADOR DEL SISTEMA -> IMPORTANT CANVIAR-HO CORRECTAMENT

ID = "HRCam4_"

#########################################################################
#########################################################################

if ID == "HRCam1_":
    TOKEN = "TOKEN"
elif ID == "HRCam2_":
    TOKEN = "TOKEN"
elif ID == "HRCam3_":
    TOKEN = "TOKEN"
elif ID == "HRCam4_":
    TOKEN = "TOKEN"
elif ID == "HRCam5_":
    TOKEN = "TOKEN"

arrel_directori = '/home/pi/log_on/'

def dropbox_upload():
    for file in os.listdir('/home/pi/log_on'):
        f=open(arrel_directori + file, 'rb')
        try:
           dbx = dropbox.Dropbox(TOKEN)
           res=dbx.files_upload(f.read(),'/log/' + file, mode=dropbox.files.WriteMode.overwrite)
           print('log', res.name, 'penjat correctament')
        except dropbox.exceptions.ApiError as err:
           print('*** API error', err)
           return none

dropbox_upload()

