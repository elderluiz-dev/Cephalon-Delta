from app import app
from models.models import GameItem, GamePartItem, db

WARFRAME_PARTS = [1, 2, 3, 4]
PRIMARY_PARTS = [1, 5, 6, 7]
MELEE_PARTS = [1, 8, 9]
SECONDARY_PARTS = [1, 5, 6]
SENTINEL_PARTS = [1, 10, 11]

#EXCEPTIONS
DUAL_PISTOLS = [1, 5, 6, 12]
SPEARS = [1, 6, 8, 9]
GLAIVES = [1, 8, 13]
BOWS = [1, 13, 14, 15, 16]

PARTS_BY_TYPE = {
    "Warframe": WARFRAME_PARTS,
    "Primary": PRIMARY_PARTS,
    "Melee": MELEE_PARTS,
    "Secondary": SECONDARY_PARTS,
    "Sentinel": SENTINEL_PARTS,
    "DualPistols": DUAL_PISTOLS,
    "Spear": SPEARS,
    "Glaive": GLAIVES,
    "Bow": BOWS,
}

with app.app_context():

    items = GameItem.query.all()

    for item in items:
        parts = PARTS_BY_TYPE.get(item.item_type)

        if not parts:
            continue

        for part_id in parts:
            db.session.add(
                GamePartItem(
                    item_id=item.id,
                    part_id=part_id
                )
            )

    db.session.commit()
    print("Seed concluída!")