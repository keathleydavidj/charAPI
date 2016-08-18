import web
import json

urls = (
    '/api/v1/reqA', 'get_A',
    '/api/v1/reqB', 'get_B'
)

app = web.application(urls, globals())

class get_A:
    def GET(self):
        pyDict = {'one' :1, 'two' :2}
        web.header('content-Type', 'application/json')
        return json.dumps(pyDict)

class get_B:
    def GET(self):
        pyDict = {'three' :3, 'four' :4}
        web.header('content-Type', 'application/json')
        return json.dumps(pyDict)

        if __name__ == "__main__":
            app.run()