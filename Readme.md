Python script to simulate a PGSQL (Pub/Sub) Subscriber

Steps :
Create a .env file in the main directory (same level with real_time.py file) then copy and paste the following to your .env file without the () and save .
(

SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcW5ndGxjcWxtamFkZnpqY3dvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTUxODIxNjEsImV4cCI6MjAzMDc1ODE2MX0.rchZx-t4mh9vZc8P8T-PfMusZVlpRD6IJixPz6wyczY
SUPABASE_ID=bfqngtlcqlmjadfzjcwo


)

Option 1: 
> Run this command ./setup.sh  (In Case You got this error bash: ./setup.sh: Permission denied) 
> run  chmod +x setup.sh then run the ./setup.sh

Option 2:
Create a Virtual Environment (tested on Conda )
Run the following commands :
> pip install -r requirements.txt
> python real_time.py

    the Subscriber is now listening to any changes in the notifications and users tables in the supabase Database
apply any changes to the database, and you will get a response in the python script terminal , 
you can also check realtime requests in the Supabase project dashboard ( https://supabase.com/dashboard/project/bfqngtlcqlmjadfzjcwo )

Use ctrl+C to exit close the subscriber 