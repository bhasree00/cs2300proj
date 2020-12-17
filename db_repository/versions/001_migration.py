from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
nurse = Table('nurse', pre_meta,
    Column('nID', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=80)),
    Column('dID', INTEGER),
)

nurse = Table('nurse', post_meta,
    Column('nID', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
    Column('assignedDoctorID', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['nurse'].columns['dID'].drop()
    post_meta.tables['nurse'].columns['assignedDoctorID'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['nurse'].columns['dID'].create()
    post_meta.tables['nurse'].columns['assignedDoctorID'].drop()
