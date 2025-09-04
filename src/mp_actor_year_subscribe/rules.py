

---


## src/mp_actor_year_subscribe/rules.py（规则构建与去重）


```python
from typing import Dict, Any, List


from .config import PluginConfig


KEY_TEMPLATE = "actor:{actor}|year:{year}|type:{mtype}"




def build_rule_keyword(actor: str, year: int) -> str:
# 关键字示例（兼容多数站点的普通关键词检索）：
# 可扩展为：actor:Name year:2023、"Name" 2023、Name (2023) 等
return f"\"{actor}\" {year}"




def build_rule_payload(cfg: PluginConfig, actor: str, year: int, mtype: str) -> Dict[str, Any]:
# MoviePilot 订阅示例通用字段（按你的后端约定替换）
payload: Dict[str, Any] = {
"name": f"{actor} {year} {mtype}",
"keyword": build_rule_keyword(actor, year),
"media_type": mtype, # movie / tv
"sites": cfg.sites or None, # None=全部站点
"quality": cfg.quality or None, # None=不过滤画质
"filters": {
"min_seeders": cfg.min_seeders,
# 可继续扩展：字幕、编码、分辨率、团队、排除词等
},
"tags": ["auto", "actor_year"],
"enabled": True
}
return payload




def desired_rule_keys(cfg: PluginConfig) -> List[str]:
keys: List[str] = []
for actor in cfg.actors:
for year in cfg.years:
for mtype in cfg.media_types:
keys.append(KEY_TEMPLATE.format(actor=actor, year=year, mtype=mtype))
return keys
