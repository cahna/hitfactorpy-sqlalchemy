import asyncio
from pathlib import Path

import asyncpg
import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    dc_file = Path(str(pytestconfig.rootdir)) / "tests" / "test_integration" / "docker-compose.yaml"
    assert dc_file.exists()
    return str(dc_file)


@pytest.fixture(scope="session")
def hitfactorpy_postgres_user() -> str:
    return "postgres"


@pytest.fixture(scope="session")
def hitfactorpy_postgres_password() -> str:
    return ""


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
    credentials = hitfactorpy_postgres_user + (
        f":{hitfactorpy_postgres_password}" if hitfactorpy_postgres_password else ""
    )
    return f"{credentials}@{hitfactorpy_postgres_hostname}/{hitfactorpy_postgres_database}"


@pytest.fixture
def ping_postgres(hitfactory_postgres_url):
    def pinger_fn() -> bool:
        nonlocal hitfactory_postgres_url
        print(f"ping_postgres: {hitfactory_postgres_url}")
        try:

            async def postgres_pinger(purl):
                try:
                    print(f"connecting to postgres: {purl}")
                    conn = await asyncpg.connect(purl)
                    r1 = await conn.execute("SELECT 1;")
                    print(r1)
                    result = await conn.fetchrow(
                        """SELECT EXISTS (
SELECT FROM
    pg_tables
WHERE
    schemaname = 'public' AND
    tablename  = 'hitfactorpy_test'
);"""
                    )
                    import pdb

                    pdb.set_trace()
                    print(result)

                    await conn.close()
                    # assert result.EIEIO
                    return True
                except Exception:
                    return False

            return bool(asyncio.run(postgres_pinger(f"postgresql://{hitfactory_postgres_url}")))
        except Exception:
            return False

    return pinger_fn


@pytest.fixture(scope="session")
def postgres_service(docker_services, hitfactory_postgres_url, ping_postgres):
    """Ensure that postgres is up and responsive"""
    url = f"postgresql://{hitfactory_postgres_url}"
    docker_services.wait_until_responsive(timeout=30.0, pause=0.1, check=ping_postgres)
    return url
