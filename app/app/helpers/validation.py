from app_models import Incident

class Validator(Incident):
    def validate(self):
        if  self.created_by.isspace():
            return 'Invalid Author!'
        elif  self.incident_type.isspace():
            return'Invalid incident type!'
        elif  self.location.isspace():
            return'Invalid location!'
        elif  self.comments.isspace():
            return'Invalid comments!'
        if  self.images.isspace():
            return 'Invalid image!'
        elif self.videos.isspace():
            return'Invalid video!'
        else:
            return None 