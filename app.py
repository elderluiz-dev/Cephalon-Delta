import os
from flask import Flask
from configs import Configs
from models.models import db
from controllers.CephalonDelta import DeltaController
from flask_migrate import Migrate

app = Flask(__name__, 
            template_folder=os.path.join('views', 'templates'), 
            static_folder=os.path.join('views', 'static')
            )

app.config.from_object(Configs)

db.init_app(app)
with app.app_context():
    db.create_all()

# ROTAS
app.add_url_rule('/', 'index', DeltaController.index)
app.add_url_rule('/create/<int:id>', 'create', DeltaController.create, methods=["POST"])
app.add_url_rule('/delete/<int:id>', 'delete', DeltaController.delete, methods=["POST"])
app.add_url_rule('/add/<int:id>', 'add', DeltaController.add, methods=['POST'])
app.add_url_rule('/remove/<int:id>', 'remove', DeltaController.remove, methods=['POST'])


migrate = Migrate(app, db)
if __name__ == "__main__":
    app.run(debug=True)