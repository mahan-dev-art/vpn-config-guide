from flask import Blueprint, render_template, abort, request
from app.services.content import ContentStore
main_bp=Blueprint('main',__name__)
store=ContentStore()
@main_bp.get('/')
def index(): return render_template('index.html',configs=store.configs,apps=store.apps)
@main_bp.get('/tutorial/<app_slug>/<platform>')
def tutorial(app_slug,platform):
    a=store.get_app(app_slug); td=store.get_tutorial(app_slug,platform)
    if not a or not td: abort(404)
    c=store.get_config(request.args.get('config','')) if request.args.get('config') else None
    return render_template('tutorial.html',app_info=a,tutorial=td,selected_config=c)
@main_bp.app_errorhandler(404)
def nf(_): return render_template('404.html'),404
