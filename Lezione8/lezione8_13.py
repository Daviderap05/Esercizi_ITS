def build_profile(first_name, last_name, **info):
    
    profile = f"{first_name} {last_name}"
    
    for key, value in info.items():
        
        profile += f", {key} {value}"
        
    return profile

profile = build_profile("Davide", "Raponi", age = 19, hair = "brown", weight = 70)

print(profile)