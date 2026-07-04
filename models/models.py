from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# INFOS DO JOGO
class GameItem(db.Model):
    __tablename__ = "GameItem"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    parts = db.relationship('GamePartItem', back_populates='item')
    item_type = db.Column(db.String(100))
    ducats = db.Column(db.Integer)
    
    @property
    def slug(self):
        slug = self.name.replace(" ", "")
        return slug

    @property
    def image_url(self):
        slug = self.name.replace(" ", "")

        if self.item_type == "Warframe":
            return f"https://wiki.warframe.com/images/{slug}_Thumb.png"
        
        return f"https://wiki.warframe.com/images/{slug}.png"
        

class PartItem(db.Model):
    __tablename__ = "PartItem"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    game_item_part = db.relationship('GamePartItem', back_populates='part')

class GamePartItem(db.Model):
    __tablename__ = "GamePartItem"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('GameItem.id'))
    part_id = db.Column(db.Integer, db.ForeignKey('PartItem.id'))
    item = db.relationship('GameItem', back_populates='parts')
    part = db.relationship('PartItem', back_populates='game_item_part')


    


# INFOS DO USUARIO
class Inventory(db.Model):
    __tablename__ = "Inventory"
    id = db.Column(db.Integer, primary_key=True)
    game_item_id = db.Column(db.Integer, db.ForeignKey('GameItem.id'))
    game_item = db.relationship('GameItem')
    inventory_parts = db.relationship('InventoryPart', back_populates='inventory', cascade="all, delete-orphan")

class InventoryPart(db.Model):
    __tablename__ = "InventoryPart"
    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('Inventory.id'))
    item_part_id = db.Column(db.Integer, db.ForeignKey('GamePartItem.id'))
    count = db.Column(db.Integer, default=0)
    inventory = db.relationship('Inventory', back_populates='inventory_parts')
    item_part = db.relationship('GamePartItem')