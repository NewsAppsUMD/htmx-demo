from peewee import *
from flask import Flask, render_template, request, flash, redirect, url_for
from playhouse.flask_utils import PaginatedQuery

app = Flask(__name__)
app.secret_key = "3209djno3eu98u3e"
db = SqliteDatabase('testudo.db')

class Course(Model):
    id = CharField()
    title = CharField()
    description = TextField()
    term = CharField()
    department = CharField()
    instructors = CharField()
    seats = IntegerField()

    class Meta:
        table_name = "courses"
        database = db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terms')
def terms():
    terms = Course.select(Course.term.distinct()).order_by(Course.term.desc())
    return render_template('terms.html', terms=terms)

@app.route('/terms/<term>')
def term(term):
    departments = Course.select(Course.department.distinct()).where(Course.term == term).order_by(Course.department)
    return render_template('term.html', term=term, departments=departments)

@app.route('/departments')
def departments():
    departments = Course.select(Course.department.distinct()).order_by(Course.department)
    return render_template('departments.html', departments=departments)

@app.route('/departments/<department>')
def department(department):
    courses = Course.select().where(Course.department == department).order_by(Course.term.desc())
    return render_template('department.html', courses=courses, department=department)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get("query", "").strip()
    page = int(request.form.get("page", 1))
    courses = Course.select().where(Course.title.contains(query)).order_by(Course.term.desc())
    total_pages = (courses.count() + 9) // 10  # Calculate the total number of pages
    paginated_courses = courses.paginate(page, 10)
    next_url = url_for("search", page=page + 1) if page < total_pages else None
    return render_template("search_results.html", courses=paginated_courses, next_url=next_url, page=page)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
