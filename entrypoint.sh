#
#echo "Waiting for PostgreSQL..."
#
#while ! pg_isready -h db -p 5432 > /dev/null 2>&1; do
#    sleep 0.1
#done
#
#echo "PostgreSQL started!"
#
#python manage.py migrate
#python manage.py runserver 0.0.0.0:8000