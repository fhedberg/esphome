"""Support for Sonoff SPM (Smart Power Manager)."""

import esphome.codegen as cg
from esphome.components import uart
import esphome.config_validation as cv
from esphome.const import CONF_ID

CODEOWNERS = ["@fhedberg"]
DEPENDENCIES = ["uart"]
AUTO_LOAD = ["switch", "sensor"]
MULTI_CONF = False

CONF_SONOFF_SPM_ID = "sonoff_spm_id"
CONF_MODULE_COUNT = "module_count"

sonoff_spm_ns = cg.esphome_ns.namespace("sonoff_spm")
SonoffSPM = sonoff_spm_ns.class_("SonoffSPM", cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SonoffSPM),
            cv.Optional(CONF_MODULE_COUNT, default=32): cv.int_range(min=1, max=32),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)


async def to_code(config):
    """Generate code for Sonoff SPM component."""
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    cg.add(var.set_module_count(config[CONF_MODULE_COUNT]))
