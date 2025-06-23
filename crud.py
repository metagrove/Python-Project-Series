contacts = {
    "john@example.com": {"name": "John Doe", "phone": "1234567890"},
    "jane@example.com": {"name": "Jane Smith", "phone": "9876543210"}
}


def check_contact():
    
    if not contacts:
        print("no contacts")
        return
    for email,info in contacts.items():
        print(f"Email : {email}\n Name : {info['name']} \n phone : {info['phone']}")
        
def update_contact():
    email = input("Enter the email of the contact to update: ")
    if email not in contacts:
        print("Contact not found.")
        return
    name = input("Enter the new name: ")
    phone = input("Enter the new phone number: ")
    if name:
        contacts[email]['name'] = name
    if phone:
        contacts[email]['phone'] = phone
    print("Contact updated successfully.")
    return contacts

def delete_contact():
    email = input("enter mail to delete: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

#check_contact()
update_contact()
delete_contact()