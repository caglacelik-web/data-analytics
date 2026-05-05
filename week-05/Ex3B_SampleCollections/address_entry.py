# Dictionary containing contact info
contact_info = {
    "address": "123 Main Street",
    "city": "Chicago",
    "state": "IL",
    "zip": "60601"
}

# Print formatted mailing address
print(f"{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

# Remove the name key (it doesn't exist yet but we'll add it properly later)

# Create full_name dictionary
full_name = {
    "first name": "Cagla",
    "last name": "Celik"
}

# Add honorific using .update()
full_name.update({"honorific": "Ms."})

# Add full_name to contact_info using .update()
contact_info.update({"full_name": full_name})

# Print formatted address with full name
print(f"{full_name['honorific']} {full_name['first name']} {full_name['last name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")