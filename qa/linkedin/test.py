from linkedin import linkedin

def linkedinlogin():
    global app
    API_KEY = 'fnv6hgzvzb8o'
    API_SECRET = 'WeSpyxZaKm8dCnnF'
    RETURN_URL = 'http://127.0.0.1:8000/userinfo'

    authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    print authentication.authorization_url  # open this url on your browser 
    application = linkedin.LinkedInApplication(authentication)
    print application
    return (authentication.authorization_url, application)
   
linkedinlogin()
