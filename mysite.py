import webapp2
import views


app = webapp2.WSGIApplication([('/', views.MainPage),
                              ],
                              debug=True)
