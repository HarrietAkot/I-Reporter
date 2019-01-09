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

#  def create_red_flag(created_by, incident_type, location, comments):
#          pass

      
#         # incident_list.append(incident)
#         # return incident

# def get_all_red_flags(self):
#         return self.incident_list

# def get_specific_red_flag(self, red_flag_id):
#         red_flag_by_id = [redflag for redflag in self.incident_list if redflag['flag_id'] == red_flag_id]
#         return red_flag_by_id

    
# def edit_red_flag_location(self,red_flag_id,location_msg):
#         red_flag_to_change_location = [redflag for redflag in self.incident_list if redflag['flag_id']== red_flag_id]
#         red_flag_to_change_location[0]['location'] = location_msg
#         return red_flag_to_change_location

# def edit_red_flag_comment(self,red_flag_id,comment_msg):
#         red_flag_to_change_comment = [redflag for redflag in self.incident_list if redflag['flag_id']==red_flag_id]
#         red_flag_to_change_comment[0]['comment'] = comment_msg
#         return red_flag_to_change_comment

# def remove_red_flag(self,red_flag_id):
#         completed_redflag = [redflag for redflag in self.incident_list if redflag['flag_id']==red_flag_id]
#         self.incident_list.remove(completed_redflag[0])
#         return self.incident_list


