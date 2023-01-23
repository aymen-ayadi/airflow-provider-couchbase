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



.. _howto/connection:couchbase:

Couchbase Connection
====================
The Couchbase connection type provides connection to a Couchbase database using the `Couchbase Python client
<https://docs.couchbase.com/python-sdk/current/hello-world/overview.html/>`_.

Configuring the Connection
--------------------------
Host (required)
    The host to connect to.

Port (optional)
    Specify the the port to connect to the database.

Scheme (optional)
    Specify the schema name to be used in the database.

username (required)
    Specify the user name to connect.

Password (required)
    Specify the password to connect.

Extra (optional)
    Specify the extra parameters (as json dictionary) that can be used in Neo4j
    connection.

    The following extras are supported:

        - default: None - couchbase://
        - cert_path - couchbases://
        - ssl - couchbases://
        - ssl_cert_reqs - couchbases://
        - ssl_ca_certs - couchbases://
        - ssl_keyfile - couchbases://
        - ssl_cert_file - couchbases://
        - ssl_check_hostname - couchbases://

      Example "extras" field:

      .. code-block:: json

         {
            "ssl_cert_reqs": "ssl_certificate_file_path",
         }
