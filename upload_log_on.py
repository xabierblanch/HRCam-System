import os
import dropbox

#########################################################################
#########################################################################

#IDENTIFICADOR DEL SISTEMA -> IMPORTANT CANVIAR-HO CORRECTAMENT

ID = "HRCam4_"

#########################################################################
#########################################################################

if ID == "HRCam1_":
    TOKEN = "XAM6jFayu0AAAAAAAAAuUYxdjT1lVoesvD6MURwDlXe9ry7lLLs0YCwpwyHVW-7f"
elif ID == "HRCam2_":
    TOKEN = "XAM6jFayu0AAAAAAAAAuU1Z--dM0pzJhnMdHCXSbOLPXwkFnvxj_ztZSjlKg01vj"
elif ID == "HRCam3_":
    TOKEN = "XAM6jFayu0AAAAAAAAAuUsvD7VjX9tnBJuPWmsy1vPhIOToaQYMV0TbiiKu81HcD"
elif ID == "HRCam4_":
    TOKEN = "XAM6jFayu0AAAAAAAAAuVADgtqXxXqB_M_tZ0D9hUQ_Z5xNS8rthg2AsxcMm5rke"
elif ID == "HRCam5_":
    TOKEN = "XAM6jFayu0AAAAAAAAAuVQYnVMNUaW_0G8R6b9ITyhwWSf9e8YRg-s-XoK7Invpz"

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

