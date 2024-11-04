import asyncio
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "hyundai_bluelink"
LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Initialize Bluelinky client here
    hass.data[DOMAIN] = BluelinkyClient(entry.data)
    return True
