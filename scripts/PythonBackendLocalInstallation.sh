# Navigate to the backend service layout
cd backend

# Create an isolated python virtual environment
python3 -m venv venv

# Activate the virtual subsystem loop
# (Use `venv\Scripts\activate` if operating on Windows environments)
source venv/bin/activate

# Upgrade pip installer core packages
pip install --upgrade pip

# Install the exact software compilation dependencies mapped inside your code blocks
pip install -r requirements.txt
