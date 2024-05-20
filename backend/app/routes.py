def setup_routes(app):
    @app.route('/')
    def home():
        return "Hello, Doqia!"

    @app.route('/another-route')
    def another_route():
        return "This is another route"