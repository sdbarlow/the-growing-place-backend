from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

revision = '20230627_InitialMigration'
down_revision = None

def upgrade():
    op.create_table(
        'applications',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('last_name', sa.String(25), nullable=False),
        sa.Column('first_name', sa.String(25), nullable=False),
        sa.Column('middle_initial', sa.String(1), nullable=False),
        sa.Column('street_address', sa.String(50), nullable=False),
        sa.Column('apartment_unit_number', sa.Integer, nullable=True),
        sa.Column('city', sa.String(40), nullable=False),
        sa.Column('state', sa.String(20), nullable=False),
        sa.Column('zip_code', sa.Integer, nullable=False),
        sa.Column('phone_number', sa.String(12), nullable=False),
        sa.Column('email', sa.String(40), nullable=False),
        sa.Column('date_available', sa.Date, nullable=False),
        sa.Column('social_security_number', sa.String(14), nullable=False),
        sa.Column('desired_pay', sa.Float, nullable=False),
        sa.Column('position_applied_for', sa.String(30), nullable=False),
        sa.Column('legally_eligible', sa.Boolean, nullable=False),
        sa.Column('felony', sa.Boolean, nullable=False),
        sa.Column('explanation', sa.String(225), nullable=True),
        sa.Column('high_school', sa.String(40), nullable=True),
        sa.Column('address', sa.String(40), nullable=True),
        sa.Column('hs_from', sa.Date, nullable=True),
        sa.Column('hs_to', sa.Date, nullable=True),
        sa.Column('hs_graduate_bool', sa.Boolean, nullable=False, default=False),
        sa.Column('college', sa.String(40), nullable=True),
        sa.Column('co_address', sa.String(40), nullable=True),
        sa.Column('co_from', sa.Date, nullable=True),
        sa.Column('co_to', sa.Date, nullable=True),
        sa.Column('co_graduate_bool', sa.Boolean, nullable=True, default=False),
        sa.Column('degree', sa.String(50), nullable=True),
        sa.Column('other_ed', sa.String(50), nullable=True),
        sa.Column('other_address', sa.String(50), nullable=True),
        sa.Column('other_from', sa.Date, nullable=True),
        sa.Column('other_to', sa.Date, nullable=True),
        sa.Column('other_graduate_bool', sa.Boolean, nullable=True, default=False),
        sa.Column('other_degree', sa.String(50), nullable=True),
        sa.Column('cpr_firstaid', sa.String(225), nullable=True),
        sa.Column('early_childhood', sa.String(225), nullable=True),
        sa.Column('early_childhood_classes', sa.String(225), nullable=True),
        sa.Column('adjudicated', sa.String(10), nullable=True),
        sa.Column('sex_offender', sa.String(10), nullable=True),
        sa.Column('dcf', sa.String(225), nullable=False),
        sa.Column('parental_rights', sa.String(10), nullable=False),
        sa.Column('resume_path', sa.String(255), nullable=True),
        sa.Column('signature_path', sa.String(255), nullable=False),
        sa.Column('created_at', sa.Date, server_default=sa.func.current_date(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'employments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('company_name', sa.String(255), nullable=False),
        sa.Column('phone', sa.String(11)),
        sa.Column('address', sa.String, nullable=False),
        sa.Column('supervisor', sa.String(25), nullable=False),
        sa.Column('job_title', sa.String(50), nullable=False),
        sa.Column('starting_pay', sa.Float, nullable=True),
        sa.Column('ending_pay', sa.Float, nullable=True),
        sa.Column('responsibilities', sa.String(225), nullable=False),
        sa.Column('from_date', sa.Date, nullable=False),
        sa.Column('to_date', sa.Date, nullable=False),
        sa.Column('reason_for_leaving', sa.String(256), nullable=False),
        sa.Column('permission_to_contact', sa.Boolean, nullable=False),
        sa.Column('application_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['application_id'], ['applications.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'references',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('full_name', sa.String, nullable=False),
        sa.Column('relationship', sa.String, nullable=False),
        sa.Column('company', sa.String, nullable=False),
        sa.Column('phone', sa.String, nullable=False),
        sa.Column('address', sa.String, nullable=False),
        sa.Column('application_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['application_id'], ['applications.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('references')
    op.drop_table('employments')
    op.drop_table('applications')



