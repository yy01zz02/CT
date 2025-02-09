#drop if collections exists
dbh.drop_collection("resetpass")

#drop if collections exists
dbh.drop_collection("employees")

eh = dbh.employees
ne = [
      {
          "username" : "tedhi@jawdat.com",
          "secret" : hashlib.md5("J@wdat12345").hexdigest(),
          "first_login" : True,
          "jawdat_id" : "001",
          "roles" : ["manager", "director"],
          "fullname" : "Tedhi Achdiana",
          "position" : "Managing Director",
          "division" : "bod",
          "supervisor" : "tedhi@jawdat.com",
          "profpic" : "tedhi.jpg",
      },