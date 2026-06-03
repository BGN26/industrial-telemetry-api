# Industrial Telemetry Analytics API 🚀🏭

An asynchronous high-concurrency Backend API built to ingest, store, and analyze real-time IoT sensor telemetry data from industrial chemical reactors. 

This project bridges the gap between **Process Engineering (Domain Knowledge)** and **Robust Backend Architecture**, applying professional software standards to industrial data management.

## 🛠️ System Architecture & Stack

- **Framework:** FastAPI (Python 3.12) - Fully Asynchronous (async/await) to handle high-concurrency sensor bursts.
- **Database:** PostgreSQL 15 - Relational store optimized for indexed historical reads.
- **ORM / Driver:** SQLAlchemy 2.0 (Async Engine) + `asyncpg`.
- **Containerization:** Docker & Docker Compose for isolated microservices orchestration.
- **Quality Assurance:** Automated Testing via Pytest & Code Formatting via Ruff.
- **CI/CD:** GitHub Actions automation pipeline.

---

## 🚀 Quick Start (Production-ready via Docker)

You don't need to install Python or PostgreSQL locally. The entire ecosystem is orchestrating into an isolated network.

### Prerequisites
- Docker & Docker Compose installed.

### Execution
1. Clone this repository.
2. Run the following command in the root directory:
    ``` 
   docker compose up --build
3. Once the logs show Application startup complete, open your browser at:

    * Interactive API Documentation (Swagger UI): http://localhost:8000/docs

    * System Health Check Endpoint: http://localhost:8000/health

# 📈 Business Intelligence Endpoints
1. Telemetry Ingestion (POST /api/v1/telemetry)
Simulates an IoT gateway pushing live readings from critical plant hardware.

Payload:

    JSON
    {
    "reactor_id": "R-101",
    "temperature": 245.5,
    "pressure": 4.2
    }
2. Reactor Analytical Breakdown (GET /api/v1/analytics/{reactor_id})
Aggregates historical time-series data using optimized SQL functions. Returns real-time metrics essential for Process Control Engineers (e.g., thermal stability and stress variables).

   * Graceful Error Handling: Returns an explicit HTTP 404 Not Found if a reactor profile contains zero historical records, avoiding unexpected system failures in tracking dashboards


# 🧪 Quality Control & CI/CD
* Automated Tests (Pytest).
    Integrated asynchronous client fixtures test the full life-cycle of the API against a live database instance.
    ````
    pytest -v

* Continuous Integration (GitHub Actions).
Every push or pull_request to the main branch triggers an automated runner that:

  1. Provisions an isolated Linux environment.

  2. Spawns an ephemeral PostgreSQL service container.

  3. Installs dependencies and verifies code integrity via pytest.