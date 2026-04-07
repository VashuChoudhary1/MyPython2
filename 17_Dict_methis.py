info ={
    "name":"Vashu",
    "cgpa":9.2,
    "subject": ["math","physics"],
    3.14:"PI"
}

#d.keys() - return dict keys
print(info.keys()) 

#d.values() - return all values
dict_vals = list(info.values())
print(dict_vals)

#d.items() - returns key value pairs
print(info.items())

#d.get(val) - returns val according to key
print(info.get("name"))

#d.update(new_item)
info.update({"surname":"Choudhary"})
print(info)