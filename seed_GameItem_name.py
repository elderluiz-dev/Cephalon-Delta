from app import app
from models.models import db, GameItem

sl1 = [
    "Caliban Prime",
    "Xaku Prime",
    "Voruna Prime",
    "Styanax Prime",
    "Gyre Prime",
    "Yareli Prime",
    "Lavos Prime",
    "Cedo Prime",
    "Trumna Prime",
    "Athodai Prime",
    "Afentis Prime",
    "Sevagoth Prime",
    "Quassus Prime",
    "Epitaph Prime",
    "Zylok Prime",
    "Khora Prime",
    "Burston Prime",
    "Braton Prime",
    "Orthos Prime",
    "Titania Prime",
    "Wukong Prime",
    "Equinox Prime",
    "Gara Prime",
    "Mesa Prime",
    "Harrow Prime",
    "Akarius Prime",
    "Akbolto Prime",
    "Ash Prime",
    "Atlas Prime",
    "Baruuk Prime",
    "Boar Prime",
    "Bronco Prime",
    "Carrier Prime",
    "Daikyu Prime",
    "Dethcube Prime",
    "Fang Prime",
    "Garuda Prime",
    "Gauss Prime",
    "Grendel Prime",
    "Kestrel Prime",
    "Kompressa Prime",
    "Nautilus Prime",
    "Okina Prime",
    "Protea Prime",
    "Sarofang Prime",
    "Perigale Prime",
    "Vadarya Prime"
]

with app.app_context():

    for i in sl1:
        item = GameItem(
            name=i,
        )

        db.session.add(item)

    db.session.commit()

print("Seed concluída!")