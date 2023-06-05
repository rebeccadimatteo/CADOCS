import enum
import datetime
import re


class CadocsIntents(enum.Enum):
   GetSmells = "get_smells"
   GetSmellsDate = "get_smells_date"
   Report = "report"
   Info = "info"

def is_valid_link(url):
   regex_eq = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
   ck_url = re.findall(regex_eq, url)
   if ck_url:
      return True
   else:
      return False

def is_valid_date(date):
   result_date = re.findall('\d{2}/\d{2}/\d{4}',date)
   if(result_date):
      date_parts = result_date[0].split("/")

      is_correct = None

      try:
         newDate = datetime.datetime(int(date_parts[2]),int(date_parts[0]),int(date_parts[1]))
         is_correct = True
      except ValueError:
         is_correct = False
      return is_correct
   return False