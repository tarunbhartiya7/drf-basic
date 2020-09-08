# interact with sqlite from django terminal
python manage.py shell
from firstApp.models import Employee
t = Employee(name="Johnny", salary=100000)
t.save()

This will insert a record in the db

# In django there are two modules - web and rest