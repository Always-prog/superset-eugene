# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Add business unit

Revision ID: d10135ed4ab1
Revises: 17fcea065655
Create Date: 2025-03-30 12:37:37.384168

"""

# revision identifiers, used by Alembic.
revision = 'd10135ed4ab1'
down_revision = '17fcea065655'

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("dashboards") as batch_op:
        batch_op.add_column(sa.Column("business_unit", sa.Text(), nullable=True))


def downgrade():
    with op.batch_alter_table("dashboards") as batch_op:
        batch_op.drop_column("business_unit")