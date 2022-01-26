# graphql

# Clone repo    
 git clone https://github.com/imosudi/graphql.git   

 cd graphql/    


# Create app/.env file
 touch app/.env     
Edit app/.env   
Add :

DB_HOST="m*******.com" 

DB_USER="graphqldb"

DB_PASS="PASS****WORD"

DB_NAME="graphqldb"

# Consider editing config.py    
 config,py

# Create Python3 virtual environment    
 python3 -m venv venv

# Start virtual environment     
 source venv/bin/activate   
 

# Flask-Migrate 
Run:    
 flask db init   
 flask db migrate   
 flask db upgrade   

# Run       
 python main.py     


Voila!