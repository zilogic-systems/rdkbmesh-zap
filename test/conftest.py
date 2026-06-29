# Copyright 2026 Zilogic Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import zaero
import pytest
import time
from pathlib import Path

@pytest.fixture(scope='session', autouse=True)
def initialize():
    zaero_obj = zaero.zaero()
    current_file = Path(__file__)
    current_directory = current_file.parent / "config"
    zaero_obj.initialize_database(current_directory)
    platform = zaero_obj.read_from_database("controller", "platform")
    zaero_obj.configure_platform(platform)
    zaero_obj.connect_with_device("controller")
    zaero_obj.connect_with_device("extender1")
    zaero_obj.connect_with_device("extender2")
    zaero_obj.connect_with_device("ap_wlan_client_1")
    pcap_log_dir = zaero_obj.read_from_database("controller", 'pcap_remote_dir')
    zaero_obj.set_sniffer_log_location("controller", pcap_log_dir)
    zaero_obj.ui_start_playwright("controller")
    time.sleep(1)
    zaero_obj.ui_open_browser("controller")
    time.sleep(1)
    yield zaero_obj
    zaero_obj.ui_close_browser("controller")
    zaero_obj.ui_stop_playwright("controller")
    del(zaero_obj)

@pytest.fixture(scope='function', autouse=True)
def test_setup(initialize):
    initialize.ui_open_context("controller")
    time.sleep(1)
    initialize.ui_open_page("controller")
    time.sleep(1)
    yield initialize
    initialize.ui_close_page("controller")
    initialize.ui_close_context("controller")
    initialize.stop_frame_capture("controller")
