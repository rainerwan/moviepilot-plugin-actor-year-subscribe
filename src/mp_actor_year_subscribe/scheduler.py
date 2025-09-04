

---


## src/mp_actor_year_subscribe/scheduler.py（计划任务辅助）


```python
from typing import Callable


# 这里仅提供一个占位函数，实际请使用 MoviePilot 提供的调度器注册接口


def register_cron(expr: str, job: Callable[[], None]) -> None:
"""将任务注册到 MoviePilot 的调度系统。
在真实环境中，请调用 MoviePilot 暴露的 scheduler API。
这里留空由主插件在 on_load 时调用。
"""
pass
