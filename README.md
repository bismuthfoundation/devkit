# devkit

Bismuth development tools to simplify onboarding for direct blockchain programming.

Currently runs off the local database, API planned in the future.

Requires Bismuth essentials module, you can hack it by changing sys.path.append("d:/bismuth") to your path to folder with essentials.py

Devkit is controlled from interface.py

Functions

- backend.getbyop("_yourstring_") - seeks and returns data based on operation

- backend.getbydata("_yourstring_") - seeks and returns data based on data (openfield)

- backend.dbhandler.limiter = "_youraddress_" - optional, limits the query search with a given address (recipient or sender)
