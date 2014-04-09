import os
import jinja2
import webapp2
from google.appengine.api import mail

# TODO: move em to settings.
DIRNAME = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(DIRNAME))


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': 'foo',
            'url': 'foo',
            'url_linktext': '',
        }


        template = jinja_environment.get_template('mom.html')
        self.response.out.write(template.render(template_values))
    def post(self):
    	template_values = {
               
            'message': 'Thanks for your response, We will get back to you.',    
        }
        send_mail(self.request)
        send_confirmation_mail(self.request)
        template = jinja_environment.get_template('mom.html')
        self.response.out.write(template.render(template_values))



def send_mail(request):
    body= 'Subject: %s \n %s' %(request.POST['subject'], request.POST['message'])
    subject="Update on your site docktor-ishrat: by %s [%s]" %(request.POST['name'], request.POST['email'])  
    mail.send_mail(sender="Mohammad Rafi<confessin@gmail.com>",
                  to="Ishrat Alim<ishrat_alim@yahoo.com>, Mohammad Aazim <warcode91@gmail.com>",
                  subject=subject,
                  body=body)
    return

def send_confirmation_mail(request):
    body= 'Thanks for reaching to us, We will get back to you shortly.'
    subject='Message receipt confirmation from docktor-ishrat'
    mail.send_mail(sender="Admin [docktor-ishrat] <confessin@gmail.com>",
                  to=request.POST['email'],
                  subject=subject,
                  body=body)
    return