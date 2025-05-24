from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin_app.models import db, User, Product

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


admin = Admin(app, name='Quản trị hệ thống', template_mode='bootstrap4')

class UserAdmin(ModelView):
    column_exclude_list = ['is_admin']
    form_excluded_columns = ['is_admin']
    can_create = True
    can_edit = True
    can_delete = True

class ProductAdmin(ModelView):
    column_list = ['id', 'name', 'price', 'stock']
    column_searchable_list = ['name']
    column_filters = ['price', 'stock']
    can_create = True
    can_edit = True
    can_delete = True

admin.add_view(UserAdmin(User, db.session))
admin.add_view(ProductAdmin(Product, db.session))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
