from app.pages import bp
from flask.templating import render_template


@bp.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@bp.route('/creator/<int:step>', methods=['GET', 'POST'])
def creator_steps(step):
    if step==1:
        return render_template('creator1.html')
    elif step==2:
        return render_template('creator2.html')
    elif step==3:
        return render_template('creator3.html')

@bp.route('/creator')
def creator():
    return render_template('creator_homepage.html')

@bp.route('/creator/addgem')
def add_gem():
    return render_template('creator_addgem.html')

@bp.route('/gem')
def gem():
    return render_template('gem.html')


@bp.route('/tourist')
def tourist():
    return render_template('tourist_homepage.html')

@bp.route('/tourist/<int:step>', methods=['GET', 'POST'])
def tourist_steps(step):
    if step==1:
        return render_template('tourist1.html')
    elif step==2:
        return render_template('tourist2.html')