import asyncio
from pathlib import Path

import asyncpg
import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    dc_file = Path(str(pytestconfig.rootdir)) / "tests" / "test_integration" / "docker-compose.yaml"
    assert dc_file.exists()
    return str(dc_file)


def ping_postgres(url):
    print(f"ping_postgres: {url}")
    try:

        async def postgres_pinger():
            try:
                conn = await asyncpg.connect(url)
                await conn.execute("SELECT 1;")
                await conn.close()
                return True
            except Exception:
                return False

        return asyncio.run(postgres_pinger())
    except Exception:
        return False


@pytest.fixture(scope="session")
def hitfactorpy_postgres_user() -> str:
    return "postgres"


@pytest.fixture(scope="session")
def hitfactorpy_postgres_password() -> str:
    return "postgres"


@pytest.fixture(scope="session")
def hitfactorpy_postgres_port(docker_services):
    return docker_services.port_for("db_postgres", 5432)


@pytest.fixture(scope="session")
def hitfactorpy_postgres_database():
    return "hitfactorpy_test"


@pytest.fixture(scope="session")
def hitfactorpy_postgres_hostname(docker_ip, hitfactorpy_postgres_port) -> str:
    return f"{docker_ip}:{hitfactorpy_postgres_port}"


@pytest.fixture(scope="session")
def hitfactory_postgres_url(
    hitfactorpy_postgres_user,
    hitfactorpy_postgres_password,
    hitfactorpy_postgres_database,
    hitfactorpy_postgres_hostname,
):
    """Postgres URL without protocol prefix"""
    return f"{hitfactorpy_postgres_user}:{hitfactorpy_postgres_password}@{hitfactorpy_postgres_hostname}/{hitfactorpy_postgres_database}"


@pytest.fixture(scope="session")
def postgres_service(docker_services):
    """Ensure that postgres is up and responsive"""
    url = f"postgres://{hitfactory_postgres_url}"
    docker_services.wait_until_responsive(timeout=30.0, pause=0.1, check=lambda: ping_postgres(url))
    return url
