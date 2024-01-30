from services.file_services import (get_last_id,
                                    get_last_name,
                                    get_contact)
from models.contacts import Contact

if get_last_id() != -1:
    id = get_last_id()
else:
    id = 1

print(id)

contact = get_contact(5)
print(contact)