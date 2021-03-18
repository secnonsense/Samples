from faker import Faker
Faker.seed(0)

for _ in range(2):
    print(Faker().bothify(text='## ??', letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    print(Faker().credit_card_number())
    print(Faker().address())
    print(Faker().license_plate())
    print(Faker().bban())
    print(Faker().credit_card_full())
    print(Faker().dga())
    print(Faker().company_email())
    print(Faker().phone_number())
    print(Faker().simple_profile())
    print(Faker().ssn())
    print(Faker().user_agent())
    print("\n")
#for _ in range(2):
    #print(Faker().pydict())   # fake python dictionary
    #print(Faker().csv(data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False))
