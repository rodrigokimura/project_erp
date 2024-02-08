from pathlib import Path

from invoke.context import Context
from invoke.tasks import task

from project_erp.settings import INTERNAL_APPS


def manage(subcommand: str):
    return f"python manage.py {subcommand}"


def _make_migrations(c: Context):
    c.run(manage("makemigrations"))


def _migrate(c: Context):
    c.run(manage("migrate"))


def _remove_migrations():
    for app in INTERNAL_APPS:
        migrations_dir = Path(app) / "migrations"
        for migration_file in migrations_dir.glob("0*.py"):
            if migration_file.is_file():
                migration_file.unlink()


def _create_superuser(c: Context):
    c.run(manage("createsuperuser --noinput"))


def _remove_db():
    db_file = Path("db.sqlite3")
    if db_file.exists() and db_file.is_file():
        db_file.unlink()


def _dump_db(c: Context):
    c.run(
        manage(
            "dumpdata -a -e=auth -e=contenttypes -e=admin -e=sessions --indent=2 > dump/all.json"
        )
    )


def _load_db(c: Context):
    c.run(manage("loaddata dump/all.json"))


@task
def dev(c: Context):
    c.run(manage("runserver 0.0.0.0:8888"))


@task
def migrations(c: Context):
    _make_migrations(c)


@task
def migrate(c: Context):
    _migrate(c)


@task
def reset(c: Context):
    _remove_migrations()
    _remove_db()
    _make_migrations(c)
    _migrate(c)
    _create_superuser(c)


@task
def dump(c: Context):
    _dump_db(c)


@task
def load(c: Context):
    _load_db(c)


@task
def lint(c: Context):
    c.run("python -m black .")
    c.run("python -m isort .")


@task
def static(c: Context):
    c.run(manage("collectstatic --no-input --clear"))
