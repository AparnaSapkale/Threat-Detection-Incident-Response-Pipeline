from fastapi import APIRouter

from services.config_service import (
    get_config,
    update_config
)

from services.rules_service import (
    get_rules,
    add_rule,
    delete_rule
)

from services.admin_service import (
    get_blocked_ips,
    unblock_ip
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

@router.get("/config")
def read_config():

    return get_config()


@router.put("/config")
def edit_config(data: dict):

    return update_config(data)

# ---------------------------------------------------
# RULES
# ---------------------------------------------------

@router.get("/rules")
def read_rules():

    return get_rules()


@router.post("/rules")
def create_rule(rule: dict):

    return add_rule(rule)


@router.delete("/rules/{rule_id}")
def remove_rule(rule_id: str):

    return delete_rule(rule_id)

# ---------------------------------------------------
# BLOCKED IPS
# ---------------------------------------------------

@router.get("/blocked-ips")
def read_blocked_ips():

    return get_blocked_ips()


@router.delete("/unblock/{ip}")
def remove_block(ip: str):

    return unblock_ip(ip)