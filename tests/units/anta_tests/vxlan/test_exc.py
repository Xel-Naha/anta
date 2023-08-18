# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Tests for anta.tests.vxlan.py
"""
from __future__ import annotations

import asyncio
import logging
from typing import Any
from unittest.mock import MagicMock

import pytest

from anta.tests.vxlan import VerifyVxlan1Interface, VerifyVxlanConfigSanity
from tests.lib.utils import generate_test_ids_list

from .data import INPUT_VXLAN_CONFIG_SANITY, INPUT_VXLAN_STATUS


@pytest.mark.parametrize("test_data", INPUT_VXLAN_STATUS, ids=generate_test_ids_list(INPUT_VXLAN_STATUS))
def test_VerifyVxlan1Interface(mocked_device: MagicMock, test_data: Any) -> None:
    """Check VerifyVxlan1Interface"""

    logging.info(f"Mocked device is: {mocked_device.host}")
    logging.info(f"Mocked HW is: {mocked_device.hw_model}")

    test = VerifyVxlan1Interface(mocked_device, eos_data=test_data["eos_data"])
    asyncio.run(test.test())
    logging.info(f"test result is: {test.result}")

    assert str(test.result.name) == mocked_device.name
    assert test.result.result == test_data["expected_result"]
    assert test.result.messages == test_data["expected_messages"]


@pytest.mark.parametrize("test_data", INPUT_VXLAN_CONFIG_SANITY, ids=generate_test_ids_list(INPUT_VXLAN_CONFIG_SANITY))
def test_VerifyVxlanConfigSanity(mocked_device: MagicMock, test_data: Any) -> None:
    """Check VerifyVxlanConfigSanity"""

    logging.info(f"Mocked device is: {mocked_device.host}")
    logging.info(f"Mocked HW is: {mocked_device.hw_model}")

    test = VerifyVxlanConfigSanity(mocked_device, eos_data=test_data["eos_data"])
    asyncio.run(test.test())
    logging.info(f"test result is: {test.result}")

    assert str(test.result.name) == mocked_device.name
    assert test.result.result == test_data["expected_result"]
    assert test.result.messages == test_data["expected_messages"]
