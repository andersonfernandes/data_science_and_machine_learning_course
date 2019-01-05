# Hash table implementation
heroes_by_real_name = {}
heroes_by_real_name["Clark Kent"] = "Superman"
heroes_by_real_name["Bruce Wayne"] = "Batman"
heroes_by_real_name["Peter Parker"] = "Spiderman"

print(heroes_by_real_name)
print(heroes_by_real_name["Bruce Wayne"])
print(heroes_by_real_name.get("Peter Parker"))
print(heroes_by_real_name.get("Tony Stark")) # Safe for non existing keys
