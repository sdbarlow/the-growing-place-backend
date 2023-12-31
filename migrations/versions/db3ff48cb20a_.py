"""empty message

Revision ID: db3ff48cb20a
Revises: 46f8fd520168
Create Date: 2023-06-27 21:27:39.326770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db3ff48cb20a'
down_revision = '46f8fd520168'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('middle_initial', sa.String(length=1), nullable=False),
    sa.Column('street_address', sa.String(length=50), nullable=False),
    sa.Column('apartment_unit_number', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(length=40), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=False),
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(length=12), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('date_available', sa.Date(), nullable=False),
    sa.Column('social_security_number', sa.String(length=14), nullable=False),
    sa.Column('desired_pay', sa.Float(), nullable=False),
    sa.Column('position_applied_for', sa.String(length=30), nullable=False),
    sa.Column('legally_eligible', sa.Boolean(), nullable=False),
    sa.Column('felony', sa.Boolean(), nullable=False),
    sa.Column('explanation', sa.String(length=225), nullable=True),
    sa.Column('high_school', sa.String(length=40), nullable=True),
    sa.Column('address', sa.String(length=40), nullable=True),
    sa.Column('hs_from', sa.Date(), nullable=True),
    sa.Column('hs_to', sa.Date(), nullable=True),
    sa.Column('hs_graduate_bool', sa.Boolean(), nullable=False),
    sa.Column('college', sa.String(length=40), nullable=True),
    sa.Column('co_address', sa.String(length=40), nullable=True),
    sa.Column('co_from', sa.Date(), nullable=True),
    sa.Column('co_to', sa.Date(), nullable=True),
    sa.Column('co_graduate_bool', sa.Boolean(), nullable=True),
    sa.Column('degree', sa.String(length=50), nullable=True),
    sa.Column('other_ed', sa.String(length=50), nullable=True),
    sa.Column('other_address', sa.String(length=50), nullable=True),
    sa.Column('other_from', sa.Date(), nullable=True),
    sa.Column('other_to', sa.Date(), nullable=True),
    sa.Column('other_graduate_bool', sa.Boolean(), nullable=True),
    sa.Column('other_degree', sa.String(length=50), nullable=True),
    sa.Column('cpr_firstaid', sa.String(length=225), nullable=True),
    sa.Column('early_childhood', sa.String(length=225), nullable=True),
    sa.Column('early_childhood_classes', sa.String(length=225), nullable=True),
    sa.Column('adjudicated', sa.String(length=10), nullable=True),
    sa.Column('sex_offender', sa.String(length=10), nullable=True),
    sa.Column('dcf', sa.String(length=225), nullable=False),
    sa.Column('parental_rights', sa.String(length=10), nullable=False),
    sa.Column('resume_path', sa.String(length=255), nullable=True),
    sa.Column('signature_path', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.Date(), server_default=sa.text('CURRENT_DATE'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('supervisor', sa.String(length=25), nullable=False),
    sa.Column('job_title', sa.String(length=50), nullable=False),
    sa.Column('starting_pay', sa.Float(), nullable=True),
    sa.Column('ending_pay', sa.Float(), nullable=True),
    sa.Column('responsibilities', sa.String(length=225), nullable=False),
    sa.Column('from_date', sa.Date(), nullable=False),
    sa.Column('to_date', sa.Date(), nullable=False),
    sa.Column('reason_for_leaving', sa.String(length=256), nullable=False),
    sa.Column('permission_to_contact', sa.Boolean(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['applications.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('references',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('relationship', sa.String(), nullable=False),
    sa.Column('company', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['applications.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('references')
    op.drop_table('employments')
    op.drop_table('applications')
    # ### end Alembic commands ###
