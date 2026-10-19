Run these terminal commands to initialize the workspace directory layout, compile configuration blocks, and start up your local web development dashboard:

# Navigate to the frontend UI workspace directory
cd web

# Clear and install Node modules dependencies
npm install

# Boot up the Vite hot-reloading development server
npm run dev

The console engine will run locally at http://localhost:3000. You can input mock Indian bank transactional messages,
watch the system transform the unstructured data strings live, and monitor the automated double-entry ledger routing variables.


---
---
To enable safe communication between your new React Web Dashboard (running at http://localhost:3000) and your FastAPI Backend Gateway (running at http://localhost:8000), we must explicitly configure Cross-Origin Resource Sharing (CORS). Without this, modern web browsers will block all incoming financial API telemetry requests due to security protocols.

---
---
