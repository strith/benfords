from flask import render_template

def error_templates(app):
    def render_status(status):
        code = getattr(status, 'code', 500)
        return render_template('{0}.html'.format(code)), code

    for error in [400, 404, 500]:
        app.errorhandler(error)(render_status)