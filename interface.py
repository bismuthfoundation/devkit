import backend

#backend.dbhandler.limiter = "de98671db1ce0e5c9ba89ab7ccdca6c427460295b8dd3642e9b2bb96"

result = backend.getbydata("NKANJECD00000000000000000000000000000000000000000000AKAAHDKN")
print (result)

result = backend.getbyop("autogame")
print (result)

