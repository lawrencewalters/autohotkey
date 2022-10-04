import mobilepass as mp
import credentials as creds

if __name__ == '__main__':
    credentials = creds.extract("./credentials.txt")
    code = mp.get_code(credentials["token_name"], credentials["pin"])
    print('MobilePASS code: ' + code)