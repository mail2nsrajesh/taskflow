# -*- coding: utf-8 -*-

# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright (C) 2013 Yahoo! Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import os
import sys

logging.basicConfig(level=logging.ERROR)

self_dir = os.path.abspath(os.path.dirname(__file__))
top_dir = os.path.abspath(
    os.path.join(self_dir, os.pardir, os.pardir, os.pardir))

sys.path.insert(0, top_dir)
sys.path.insert(0, self_dir)

import taskflow.engines
from taskflow.utils import persistence_utils as p_utils

import my_flows  # noqa
import my_utils  # noqa


backend = my_utils.get_backend()
logbook = p_utils.temporary_log_book(backend)

flow = my_flows.flow_factory()

flowdetail = p_utils.create_flow_detail(flow, logbook, backend)
engine = taskflow.engines.load(flow, flow_detail=flowdetail,
                               backend=backend)

print('Running flow %s %s' % (flowdetail.name, flowdetail.uuid))
engine.run()