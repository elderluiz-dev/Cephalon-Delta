import requests
from models.models import GameItem, db
from app import app


with app.app_context():
    response = requests.get("https://api.warframe.market/v2/items")
    data = response.json()
    items = GameItem.query.all()
    n = 1


    for item in data["data"]:
        if "ducats" in item:
            ref_id = item["i18n"]["en"]["name"]
            has_ducats = item["ducats"]
            for item in items:
                if (item.name + " Set") == ref_id:
                    item.ducats = has_ducats

    db.session.commit()
    
print("Seed concluída!")