from faker import Faker

fake = Faker() # Genera datos aleatorios

def get_login_faker(num_casos=5):


    casos = []
    # usuarios = [ "standard_user", "locked_out_user"]
    # password = "secret_sauce"

    for _ in range(num_casos):
        username = fake.user_name()
        password = fake.password(length=12) 
        login_example = fake.boolean(chance_of_getting_true=50) # % de probabilidades que sea true


        casos.append((username, password, login_example))
    
    return casos