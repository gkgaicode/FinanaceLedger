To run these assertions, ensure your local Docker Compose cluster is actively running inside your staging terminal layout (docker-compose up -d), 
then execute the following blocks inside your local backend application workspace layout:

cd backend
source venv/bin/activate

# Execute pytest execution suites against the live API gateway
pytest test_integration.py -v


If everything is configured correctly, your terminal will confirm that all handshakes, parsers, and processing boundaries have passed validation rules. 
Your system platform architecture is officially unified and certified for stable code production deployment workflows.
