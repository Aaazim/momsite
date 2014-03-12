import os
import jinja2
import webapp2

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

        template = jinja_environment.get_template('mom.html')
        self.response.out.write(template.render(template_values))

