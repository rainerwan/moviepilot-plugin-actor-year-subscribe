from pydantic import BaseModel, Field
from typing import List


class PluginConfig(BaseModel):
actors: List[str] = Field(default_factory=list, description="演员名单")
years: List[int] = Field(default_factory=list, description="年份（多选）")
sites: List[str] = Field(default_factory=list, description="目标站点（留空=全部）")
media_types: List[str] = Field(default_factory=lambda: ["movie", "tv"]) # movie/tv
quality: str = ""
min_seeders: int = 0
dry_run: bool = False
schedule: str = "0 8 * * *"
