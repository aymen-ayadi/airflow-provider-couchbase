#
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
from __future__ import annotations


from airflow.models import Connection
from airflow.providers.couchbase.hooks.couchbase import CouchbaseHook
from airflow.utils import db


class TestCouchbaseHook:

    def test_couchbase_with_ssl(self):
        db.merge_conn(
            Connection(
                conn_id="couchbase_with_ssl",
                conn_type="couchbase",
                host="couchbase",
                extra={
                    "ssl_ca_certs": "/path/to/custom/ca-cert.pem",
                    "ssl_keyfile": "/path/to/key-file.pem",
                },
            )
        )
        hook = CouchbaseHook(conn_id="couchbase_with_ssl")
        assert hook.uri["uri"].startswith("couchbases://")
