from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from django.core.context_processors import csrf

# custom libraries
from linkedin import linkedin
from linkedin import server
from shiputils import prettyTable

# qa ={"Technical":(("Why do capital expenditures increase assets (PP&E), while other cash outflows, like paying salary, taxes, etc., do not create any asset, and instead instantly create an expense on the income statement that reduces equity via retained earnings?" , "Capital expenditures are capitalized because of the timing of their estimated benefits the lemonade stand will benefit the firm for many years. The employees work, on the other hand, benefits the period in which the wages are generated only and should be expensed then. This is what differentiates an asset from an expense."),("Why are increases in accounts receivable a cash reduction on the cash flow  statement?" , "Since our cash flow statement starts with net income, an increase in accounts receivable is an adjustment to net income to reflect the fact that the company never actually received those funds.")),\
# "Defintion":(("What is working capital?" , "Working capital is defined as current assets minus current liabilities; it tells the financial statement user how much cash is tied up in the business through items such as  receivables and inventories and also how much cash is going to be needed to pay off short term obligations in the next 12 months."),("What is a deferred tax liability and why might one be created?" , "Deferred tax liability is a tax expense amount reported on a companys income statement that is not actually paid to the IRS in that time period, but is expected to be paid in the future. It arises because when a company actually pays less in taxes to the IRS than they show as an expense on their income statement in a reporting period. Differences in depreciation expense between book reporting (GAAP) and IRS reporting can lead to differences in income between the two, which ultimately leads to differences in tax expense reported in the financial statements and taxes payable to the IRS."),("What is a deferred tax asset and why might one be created?" , "Deferred tax asset arises when a company actually pays more in taxes to the IRS than they show as an expense on their income statement in a reporting period.")) }
#test = {("question1":"Tell me a little about yourself"), ("question2": "Why do you want to be an investment banker?"), ("question3": = "Why do capital expenditures increase assets (PP&E), while other cash outflows, like paying salary, taxes, etc., do not create any asset, and instead instantly create an expense on the income statement that reduces equity via retained earnings?"), ("question4":"Why are increases in accounts receivable a cash reduction on the cash flow  statement?"), ("question5":"What is working capital?")}

#global variables 
application = None
authentication = None  

def home(request):
    t = get_template('home.html')
    homepage= t.render(Context())
    return HttpResponse(homepage)
    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
	
def dashboard(request):
    dic = {}
    message = "";
    if 'Field' in request.GET: 
    	dic["Field"] = request.GET['Field'] 
    if 'Level' in request.GET: 
    	dic["Level"] = request.GET['Level'] 
    if 'Keywords' in request.GET:
    	dic["Keywords"] = request.GET['Keywords'] 

    return render_to_response('dashboard.html',dic)	

def getQuestions(request):
    #dic = {}
    #message = ""
    questions = json.dumps(qa)
    return HttpResponse(questions,mimetype="application/json")
    
def start1(request):  
    dic = {}
    dic["question1"] = "Tell me a little about yourself"
    
    return render_to_response('interview1.html', dic)
    
def start2(request):
    dic = {}  
    dic["question2"] = "Why do you want to be an investment banker?"
    
    return render_to_response('interview2.html',dic)

def start3(request):
    dic = {}  
    dic["question3"] = "Why do capital expenditures increase assets (PP&E), while other cash outflows, like paying salary, taxes, etc., do not create any asset, and instead instantly create an expense on the income statement that reduces equity via retained earnings?"
    
    return render_to_response('interview3.html',dic)

def start4(request):
    dic = {}  
    dic["question4"] = "Why are increases in accounts receivable a cash reduction on the cash flow  statement?"
    
    return render_to_response('interview4.html',dic)            

def start5(request):
    dic = {}  
    dic["question5"] = "What is working capital?"
    
    return render_to_response('interview5.html',dic)        


def feedback(request):

    dic = {}
    dic["question1answer"] = request.GET['question1answer']
    dic["question2answer"] = request.GET['question2answer']
    dic["question3answer"] = request.GET['question3answer']
    dic["question4answer"] = request.GET['question4answer']
    dic["question5answer"] = request.GET['question5answer']
    persisttoDB(dic)
    
    return render_to_response('feedback.html', dic)     

def summary(request):
    dic = {}
    dic["question1answer"] = request.GET['question1answer']
    dic["question2answer"] = request.GET['question2answer']
    dic["question3answer"] = request.GET['question3answer']
    dic["question4answer"] = request.GET['question4answer']
    dic["question5answer"] = request.GET['question5answer']
    persistoDB
    
    return render_to_response('summary.html', dic)

def persisttoDB(data):
    for key in data:
        print data[key] 
        
def linkedinlogin(request):
    global application 
    global authentication 
    
    API_KEY = 'fnv6hgzvzb8o'
    API_SECRET = 'WeSpyxZaKm8dCnnF'
    RETURN_URL = 'http://127.0.0.1:8000/'

    authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    print authentication.authorization_url  # open this url on your browser 
    application = linkedin.LinkedInApplication(authentication)
    # print "Ablimit requested this:", authentication.authorization_url  
    return HttpResponseRedirect(authentication.authorization_url)  
    #response = HttpResponseRedirect(authentication.authorization_url) 
    #print response
    
    #authentication.authorization_code = response.GET['code']
    #print "This is authoriztion code:", authentication.authorization_code
    #authentication.get_access_token()

def getuserinfo(request):
    global authentication
    global application
    authentication.authorization_code = request.GET['code']
    # print "This is the code:", authentication.authorization_code 
    authentication.get_access_token() 
    # print application.get_profile()
    profiledic = application.get_profile(selectors=['positions']) 
    
    return HttpResponse(prettyTable(profiledic))
    #return render_to_response('linkedinprofile.html',profiledic)	
    

