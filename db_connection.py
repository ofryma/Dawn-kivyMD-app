from kivy.network.urlrequest import UrlRequest
import urllib



######## API SECTION #######


endpoint = 'https://dawnapi.herokuapp.com/'

# for tests
# endpoint = 'http://localhost:3000/'

def getData(query):
    '''
        This function will return the first match from the database, according
        to the query object

        the query variable is an json object that contains the field to look by
        and the values to look
        example:
        user_to_find = {
            'first_name': 'Ofry',
            'last_name': 'Makdasy',
            'username': 'ofryma'
        }

    '''


    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}test')
    req.wait()
    return req.result

def add_patient(sign_user):
    query = sign_user.user_info()
    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}signuser?{params}')
    req.wait()
    
    return req.result

def verify_patient(query):
    '''
       This function will verify the login details (username and password)
       against the database, and will return True is the user is in the database
       and False if it is not
    '''


    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}verifyuser?{params}')
    req.wait()
    # print(req.result)
    return req.result

def update_patient(query,update_fields):

    query = {**query, **update_fields}
    query['questions'] = ','.join(query['questions'])
    query['diagnose'] = ','.join(query['diagnose'])
    params = urllib.parse.urlencode(query)
    req = UrlRequest(f'{endpoint}updateuser?{params}')
    req.wait()
    # print(req.result)
    return req.result


#
# from pymongo import MongoClient
#
#
# class DataBase():
#     #    def build(self):
#     #        return Builder.load_file('login.kv')
#
#     def get_database(self):
#         CONNECTION_STRING = "mongodb+srv://dawn-user-01:dawn-password-01@cluster01.vlzzyf3.mongodb.net/test1"
#         client = MongoClient(CONNECTION_STRING)
#         return client['dawn']
#
#     def patient_db(self):
#         dbname = self.get_database()
#         patient_coll = dbname["patients"]
#         return patient_coll
#
#     def add_patient(self, firstname, email, username, password, date_of_birth, height, weight, diagnose):
#         document = {
#             'First name': firstname,
#             'Email': email,
#             'Username': username,
#             'Password': password,
#             'Date of birth': date_of_birth,
#             #        'Date': datetime.datetime.now(),
#             'Height': height,
#             'Weight': weight,
#             'Diagnose': diagnose
#         }
#
#         return self.patient_db().insert_one(document)
