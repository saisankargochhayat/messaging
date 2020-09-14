#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Sai Sankar Gochhayat
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""This is Thoth Messaging module for SIUnanalyzedPackageMessage."""

import logging

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class SIUnanalyzedPackageMessage(MessageBase):
    """Class used by Producer events on Kafka topic on packages not analyzed by SI."""

    topic_name = "thoth.investigator.si-unanalyzed-package"

    class MessageContents(BaseMessageContents, serializer="json"):  # type: ignore
        """Class used to represent contents of a SI unanalyzed package message Kafka topic."""

        package_name: str
        package_version: str
        index_url: str

    def __init__(
        self,
        num_partitions: int = 1,
        replication_factor: int = 1,
        client_id: str = "thoth-messaging",
        ssl_auth: int = 1,
        bootstrap_server: str = "localhost:9092",
        topic_retention_time_second: int = 60 * 60 * 24 * 45,
        protocol: str = "SSL",
    ):
        """Initialize si-unanalyzed-package topic."""
        super(SIUnanalyzedPackageMessage, self).__init__(
            topic_name=self.topic_name,
            value_type=self.MessageContents,
            num_partitions=num_partitions,
            replication_factor=replication_factor,
            client_id=client_id,
            ssl_auth=ssl_auth,
            bootstrap_server=bootstrap_server,
            topic_retention_time_second=topic_retention_time_second,
            protocol=protocol,
        )
