from _apps.endpoints.registration.app import app


@app.route('/')
def main():
    return '<h1>Hello</h1>'


@app.route('/about')
def about():
    return '<h1>About</h1>'

