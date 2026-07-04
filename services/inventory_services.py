from models.models import GameItem, Inventory, InventoryPart, db

class InventorySerices:
    @staticmethod
    def create(id):
        game_item = GameItem.query.get_or_404(id)
        inventory = Inventory(game_item_id=game_item.id)
        db.session.add(inventory)
        db.session.flush()

        for game_part in game_item.parts:
            inventory_part = InventoryPart(inventory_id=inventory.id, item_part_id=game_part.id)
            db.session.add(inventory_part)
            
        db.session.commit()
    
    @staticmethod
    def delete(id):
        inventory = Inventory.query.get_or_404(id)
        db.session.delete(inventory)
        db.session.commit()

    @staticmethod
    def add(id):
        part = InventoryPart.query.get_or_404(id)
        part.count += 1

        db.session.commit()

    @staticmethod
    def remove(id):
        part = InventoryPart.query.get_or_404(id)

        if part.count > 0:
            part.count -= 1

        db.session.commit()
