"""
 This file is part of the GetWVKeys project (https://github.com/GetWVKeys/getwvkeys)
 Copyright (C) 2022-2024 Notaghost, Puyodead1 and GetWVKeys contributors 
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published
 by the Free Software Foundation, version 3 of the License.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import time

from sqlalchemy import ForeignKey

from getwvkeys.models.Shared import db


class Key(db.Model):
    __tablename__ = "keys_"
    kid = db.Column(
        db.String(32),
        primary_key=True,
        nullable=False,
    )
    added_at = db.Column(db.Integer, nullable=False, default=int(time.time()))
    added_by = db.Column(db.String(255), ForeignKey("users.id"), nullable=True)
    license_url = db.Column(db.Text, nullable=False)
    key_ = db.Column(db.String(255), nullable=False)
