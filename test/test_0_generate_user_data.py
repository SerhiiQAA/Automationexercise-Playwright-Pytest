# # test_generate_user_data.py

# from faker import Faker
# import json
# from data.test_data import USER_DATA 

# fake = Faker()

# def test_generate_user_data():
#     # Генеруємо дані користувача з Faker
#     name = fake.first_name()
#     email = fake.email()
#     password = fake.password(length=10, special_chars=True)
#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     company = fake.company()
#     address1 = fake.street_address()
#     address2 = fake.secondary_address()
#     country = "United States"  
#     state = fake.state()
#     city = fake.city()
#     zipcode = fake.zipcode()
#     mobile_number = fake.phone_number()

#     user_data = {
#         "name": name,
#         "email": email,
#         "password": password,
#         "first_name": first_name,
#         "last_name": last_name,
#         "company": company,
#         "address1": address1,
#         "address2": address2,
#         "country": country,
#         "state": state,
#         "city": city,
#         "zipcode": zipcode,
#         "mobile": mobile_number
#     }
    
#     with open('data/test_data.py', 'w') as f:
#         f.write(f"USER_DATA = {json.dumps(user_data, indent=4)}")
