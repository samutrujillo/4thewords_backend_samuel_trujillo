from app.core.database import init_db

def run_migrations():
    print("Running migrations...")
    init_db()
    print("Migrations completed.")

if __name__ == "__main__":
    run_migrations()