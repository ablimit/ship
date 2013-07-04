from django.template.loader import get_template
from django.template import Context
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

# qa ={"Technical":(("Why do capital expenditures increase assets (PP&E), while other cash outflows, like paying salary, taxes, etc., do not create any asset, and instead instantly create an expense on the income statement that reduces equity via retained earnings?" , "Capital expenditures are capitalized because of the timing of their estimated benefits the lemonade stand will benefit the firm for many years. The employees work, on the other hand, benefits the period in which the wages are generated only and should be expensed then. This is what differentiates an asset from an expense."),("Why are increases in accounts receivable a cash reduction on the cash flow  statement?" , "Since our cash flow statement starts with net income, an increase in accounts receivable is an adjustment to net income to reflect the fact that the company never actually received those funds.")),\
# "Defintion":(("What is working capital?" , "Working capital is defined as current assets minus current liabilities; it tells the financial statement user how much cash is tied up in the business through items such as  receivables and inventories and also how much cash is going to be needed to pay off short term obligations in the next 12 months."),("What is a deferred tax liability and why might one be created?" , "Deferred tax liability is a tax expense amount reported on a companys income statement that is not actually paid to the IRS in that time period, but is expected to be paid in the future. It arises because when a company actually pays less in taxes to the IRS than they show as an expense on their income statement in a reporting period. Differences in depreciation expense between book reporting (GAAP) and IRS reporting can lead to differences in income between the two, which ultimately leads to differences in tax expense reported in the financial statements and taxes payable to the IRS."),("What is a deferred tax asset and why might one be created?" , "Deferred tax asset arises when a company actually pays more in taxes to the IRS than they show as an expense on their income statement in a reporting period.")) }

def home(request):
    t = get_template('index.html')
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
    
def start(request):
    dic = {}
    dic["sectionname1"] = "Technical"  
    dic["sec1question1"] = "Why do capital expenditures increase assets (PP&E), while other cash outflows, like paying salary, taxes, etc., do not create any asset, and instead instantly create an expense on the income statement that reduces equity via retained earnings?"
    dic["sec1question2"] = "Why are increases in accounts receivable a cash reduction on the cash flow  statement?"
    dic["sectionname2"] = "Defintion"
    dic["sec2question1"] = "What is working capital?"
    dic["sec2question2"] = "What is a deferred tax liability and why might one be created?"

    return render_to_response('question.html',dic)
    

def qp(request):
    dic = {}
    dic["question"] = "Why do capital expenditures increase assets (PP&E), while other cash outflows, like paying salary, taxes, etc., do not create any asset, and instead instantly create an expense on the income statement that reduces equity via retained earnings?"

    return render_to_response('questionpaging.html', dic)   

def finished(request):
    # print to terminal
    print request.POST['section1question1answer']
  
    return HttpResponse(request.POST['section1question1answer'])
    
