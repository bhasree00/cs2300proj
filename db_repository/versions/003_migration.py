from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
conducts = Table('conducts', post_meta,
    Column('conductsID', Integer, primary_key=True, nullable=False),
    Column('sID', Integer),
    Column('dID', Integer),
)

treats = Table('treats', post_meta,
    Column('treatsID', Integer, primary_key=True, nullable=False),
    Column('pID', Integer),
    Column('dID', Integer),
)

undergoes = Table('undergoes', post_meta,
    Column('undergoesID', Integer, primary_key=True, nullable=False),
    Column('sID', Integer),
    Column('pID', Integer),
)

works_for = Table('works_for', post_meta,
    Column('worksForID', Integer, primary_key=True, nullable=False),
    Column('dID', Integer),
    Column('dNum', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['conducts'].create()
    post_meta.tables['treats'].create()
    post_meta.tables['undergoes'].create()
    post_meta.tables['works_for'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['conducts'].drop()
    post_meta.tables['treats'].drop()
    post_meta.tables['undergoes'].drop()
    post_meta.tables['works_for'].drop()
