def display_profile(username, email, role="Member", **additional_info):
    print("--- USER PROFILE ---")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Role: {role}")
    print(f"Additional Information:")
    for key, value in additional_info.items():
        print(f"{key} : {value}")
    return {"username": username, "email": email, "role": role, **additional_info}

raw_user_data = {
    "username": "alex99",
    "email": "alex@example.com",
    "role": "Admin",
    "location": "Kerala",
    "badge": "Gold contributor",
}

display_profile(**raw_user_data)