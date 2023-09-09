from oauth2client.service_account import ServiceAccountCredentials
import gspread_dataframe as gd
import pandas as pd
import gspread
from bucket import bucket
import gsheet

class gsheet:
    def __init__(self):
        pass
    
    def pushData(self,df,spreadsheet_key,wks_name,append = False, clean=True):
        scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_dict(scope)
            client = gspread.authorize(creds)
            g_sheets=client.open_by_url('https://docs.google.com/spreadsheets/d/{}'.format(spreadsheet_key))
            if append:
                prev_df = gd.get_as_dataframe(g_sheets.worksheet(wks_name))
                #in output sheet we have to delete all row except first(which needs to be clear)
                if len(prev_df)>0 :
                    df = pd.concat([prev_df,df])
            google_status = gd.set_with_dataframe(g_sheets.worksheet(wks_name), df, resize=clean)
        except Exception as e:
            print(str(e))
            return False
        else:
            if type(google_status)==str and "code" in google_status:
                return False
            else:
                return True