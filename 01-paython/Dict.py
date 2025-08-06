d={}
print(type(d))
d1 = {"name":"Navneet"}
print(d1)
d1 = {'name':'Akhilesh', 'Email':"Ak@gmail.com",'number':67564534}
print(d1)
print(d1['name'])
d2 = {True:"1234"}
print(d2[1])
d3 = {"company":"pwskills", 'course':["web dev", "java","css"]}  # list ko bhi pass kr sakte h
print(d3["course"])
print(d3["course"][2])
d4 = {"number":[2,3,4,5,], "assignment":(4,5,6,7),"data":{123},"class":{"web":8, "science":5}}
print(d4)
print(d4["class"][ "science"])  # 5 inkalne ke kiye
d4['Mentor']=["hayder","jaydeep","sudhansu"]  # add a key value
print(d4)
del d4["number"]
print(d4)
print(d4.keys())
print(d4.values())
print(d4.items())
print(d4.__sizeof__())
print(d4.copy())
print(d4.pop("data"))
print(d4)
print(list(d4.keys()))

