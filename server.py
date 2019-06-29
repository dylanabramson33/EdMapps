from waitress import serve

from readydata.wsgi import application

if __name__ == '__main__':
    serve(application, port='80')
