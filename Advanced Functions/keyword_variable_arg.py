def show_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


show_details(name="Minna", age=18, place="Mlp")
