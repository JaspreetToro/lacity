from uszipcode import SearchEngine
search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database
zipcode = search.by_zipcode("90746")
#print(zipcode)
#print(zipcode.values())
#print(zipcode.to_dict())
print(zipcode.to_json())