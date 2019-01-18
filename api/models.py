from datetime import datetime
'''This module contains our api data'''  

incident_list = []
class Incident:   
 def __init__(self, *args):
        self.flag_id = args[0]
        self.created_by = args[1]
        self.created_on = args[2]
        self.incident_type = args[3]
        self.location = args[4]
        self.comment = args[5]
        self.images = args[6]
        self.videos = args[7]

 def getflag(self,red_flag_id):
        for redflag in incident_list:
            if redflag['flag_id']== red_flag_id:

 
