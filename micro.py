"""
http://127.0.0.1:5000/add_contacts
http://127.0.0.1:5000/read_contacts
http://127.0.0.1:5000/update_contacts/1
http://127.0.0.1:5000/delete_contacts/1

"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tarun2003@localhost:3306/contact_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False) 
    phone = db.Column(db.String(15), nullable=False)
    
    def return_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'phone': self.phone
        }


@app.route('/')
def create_app():
    return "Welcome to the Contact Management System!"


@app.route('/add_contacts/',methods=['POST'])
def create_contact():
    data  = request.json()
    new_contact = Contact(
        
        name = data['name'],
        age = data['age'],
        phone = data['phone'],
        email =data['email']
        )
        
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message":"Contact added Successfullly"}),201

@app.route('/read_contacts/',methods=['GET'])
def read_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.return_dict() for contact in contacts]), 200

@app.route('/update_contacts/<int:id>',methods =['PUT'])
def update_contact(id):
    data = request.get_json()
    contact = Contact.query.get_or_404(id)
    
    contact.name = data.get('name',contact.name)
    contact.age = data.get('age',contact.age)
    contact.email = data.get('email',contact.email)
    contact.phone = data.get('phone',contact.phone)
    
    db.session.commit()
    return jsonify({"message": "Contact updated successfully"}), 200

@app.route('/delete_contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    
    contact = Contact.query.get_or_404(id)
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted successfully"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("Database tables created successfully.")
    app.run(debug=True)