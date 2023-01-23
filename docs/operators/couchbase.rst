 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.



.. _howto/operator:CouchbaseOperator:

CouchbaseOperator
=================

Use the :class:`~airflow.providers.couchbase.operators.CouchbaseOperator` to execute
N1QL commands in a `Couchbase <https://couchbase.com/>`__ database.


Using the Operator
^^^^^^^^^^^^^^^^^^

Use the ``couchbase_conn_id`` argument to connect to your couchbase instance where
the connection metadata is structured as follows:

.. list-table:: Couchbase Airflow Connection Metadata
   :widths: 25 25
   :header-rows: 1

   * - Parameter
     - Input
   * - Host: string
     - couchbase hostname
   * - Scheme: string
     - Database schema string
   * - username: string
     - Couchbase user
   * - Password: string
     - Couchbase user password
   * - Port: int
     - couchbase port
