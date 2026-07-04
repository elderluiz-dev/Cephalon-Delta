from flask import render_template, redirect, url_for
from services.inventory_services import InventorySerices
from models.models import Inventory, InventoryPart, GameItem, PartItem, GamePartItem, db

class DeltaController():
    @staticmethod
    def index():
        items = GameItem.query.all()
        inventorys = Inventory.query.all()
        return render_template('index.html', items=items, inventorys=inventorys)
    
    @staticmethod
    def create(id):
        InventorySerices.create(id)
        return redirect(url_for('index'))
    
    @staticmethod
    def delete(id):
        InventorySerices.delete(id)
        return redirect(url_for('index'))
    
    @staticmethod
    def add(id):
        InventorySerices.add(id)
        return redirect(url_for('index'))
    
    @staticmethod
    def remove(id):
        InventorySerices.remove(id)        
        return redirect(url_for('index'))