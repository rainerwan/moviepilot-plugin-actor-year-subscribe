## src/mp_actor_year_subscribe/mp_api.py（对接 MoviePilot 内部 API 的轻封装）


> 这里把 MoviePilot 对插件开放的常用接口做了最小封装。**如果你的实际 API 不同**，在此文件里改一处即可，插件其他逻辑无需更改。


```python
import os
import httpx
from typing import Dict, Any, List, Optional


class MoviePilotAPI:
def __init__(self, base_url: str, token: Optional[str] = None):
self.base_url = base_url.rstrip('/')
self.token = token or os.getenv("MOVIEPILOT_TOKEN", "")
self.client = httpx.Client(timeout=30)


def _headers(self) -> Dict[str, str]:
headers = {"Accept": "application/json"}
if self.token:
headers["Authorization"] = f"Bearer {self.token}"
return headers


# 示例：获取站点列表
def list_sites(self) -> List[Dict[str, Any]]:
url = f"{self.base_url}/api/sites"
r = self.client.get(url, headers=self._headers())
r.raise_for_status()
return r.json()


# 示例：创建订阅规则
def create_subscription(self, payload: Dict[str, Any]) -> Dict[str, Any]:
url = f"{self.base_url}/api/subscriptions"
r = self.client.post(url, json=payload, headers=self._headers())
r.raise_for_status()
return r.json()


# 示例：查询是否已有相同规则（避免重复）
def find_subscription(self, keyword: str) -> Optional[Dict[str, Any]]:
url = f"{self.base_url}/api/subscriptions?keyword={keyword}"
r = self.client.get(url, headers=self._headers())
r.raise_for_status()
items = r.json() or []
return items[0] if items else None
