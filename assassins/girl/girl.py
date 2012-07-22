class GIRL(object):
    def __init__(self, config):
        self.config = config

    ###### LOCATION-BASED SERVICES #####

    def verify_location(self, location):
        pass

    def get_same_area_users(self, location):
        pass

    ##### SCORING SERVICES #####

    def update_score(self, new_score, user):
        pass
