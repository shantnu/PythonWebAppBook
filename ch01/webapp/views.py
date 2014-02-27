from webapp import webapp

@webapp.route('/')
def index():
    return "Hello, World!"