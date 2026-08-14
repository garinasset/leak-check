from typing import Optional, Iterable

from lib.common import iter_nonempty


# ========== 基础脱敏函数 ==========

def mask_phone(v: str) -> str:
    if not v or len(v) < 7:
        return "***"
    return v[:2] + "*******" + v[-2:]


def mask_email(v: str) -> str:
    if not v or "@" not in v:
        return "***"
    name, domain = v.split("@", 1)
    if len(name) <= 2:
        name_mask = name[0] + "***"
    else:
        name_mask = name[:2] + "***"
    return f"{name_mask}@{domain}"


def mask_id(v: str) -> str:
    if not v or len(v) < 10:
        return "***"
    return v[:2] + "********" + v[-2:]


def mask_number(v: str) -> str:
    v = str(v)
    if len(v) <= 3:
        return "*" * len(v)
    return "*" * (len(v) - 3) + v[-3:]


def mask_name(v: str) -> str:
    if not v:
        return "***"
    if len(v) == 1:
        return "*"
    return "*" + v[-1]


# car = 普通文本（车辆配置）
def mask_car(v: str) -> str:
    if not v:
        return "***"
    v = str(v).strip()
    if len(v) <= 2:
        return v[0] + "*"
    return v[:2] + "*" * (len(v) - 2)


def mask_address(v: str) -> str:
    if not v:
        return "***"
    return v[:2] + "****" if len(v) > 2 else v + "****"


# ========== 分发器 ==========

def mask_value(field: str, v: Optional[str]) -> str:
    if not v:
        return ""

    v = str(v).strip()
    if not v:
        return ""

    if field == "phone":
        return mask_phone(v)
    if field == "email":
        return mask_email(v)
    if field == "id":
        return mask_id(v)
    if field in ("qq", "weibo"):
        return mask_number(v)
    if field in ("name", "nickname", "receiver", "contact"):
        return mask_name(v)
    if field == "car":
        return mask_car(v)
    if field in ("address", "company"):
        return mask_address(v)

    return v


# ========== list 工具 ==========

def mask_list(field: str, values: Iterable) -> list[str]:
    return list({
        mask_value(field, v)
        for v in iter_nonempty(values)
    })