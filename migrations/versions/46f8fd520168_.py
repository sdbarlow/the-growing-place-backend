"""empty message

Revision ID: 46f8fd520168
Revises: 20230627_InitialMigration
Create Date: 2023-06-27 20:59:07.010731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46f8fd520168'
down_revision = '20230627_InitialMigration'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employments')
    op.drop_table('references')
    op.drop_table('applications')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('applications_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('middle_initial', sa.VARCHAR(length=1), autoincrement=False, nullable=False),
    sa.Column('street_address', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('apartment_unit_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('zip_code', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.VARCHAR(length=12), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('date_available', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('social_security_number', sa.VARCHAR(length=14), autoincrement=False, nullable=False),
    sa.Column('desired_pay', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('position_applied_for', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('legally_eligible', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('felony', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('explanation', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('high_school', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('hs_from', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('hs_to', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('hs_graduate_bool', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('college', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('co_address', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('co_from', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('co_to', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('co_graduate_bool', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('degree', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('other_ed', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('other_address', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('other_from', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('other_to', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('other_graduate_bool', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('other_degree', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('cpr_firstaid', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('early_childhood', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('early_childhood_classes', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.Column('adjudicated', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('sex_offender', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('dcf', sa.VARCHAR(length=225), autoincrement=False, nullable=False),
    sa.Column('parental_rights', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('resume_path', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('signature_path', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.DATE(), server_default=sa.text('CURRENT_DATE'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='applications_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('references',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('relationship', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('company', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('application_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['applications.id'], name='references_application_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='references_pkey')
    )
    op.create_table('employments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('company_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=11), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('supervisor', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('job_title', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('starting_pay', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('ending_pay', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('responsibilities', sa.VARCHAR(length=225), autoincrement=False, nullable=False),
    sa.Column('from_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('to_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('reason_for_leaving', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('permission_to_contact', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('application_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['applications.id'], name='employments_application_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='employments_pkey')
    )
    # ### end Alembic commands ###
