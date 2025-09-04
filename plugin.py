## plugin.py（插件主入口）
key = KEY_TEMPLATE.format(actor=actor, year=year, mtype=mtype)


# 避免重复：按关键字/名称查已有订阅
keyword = rules_mod.build_rule_keyword(actor, year)
exists = None
try:
exists = self.api.find_subscription(keyword)
except Exception as e:
self.log_warn(f"查询现有订阅失败：{e}")


if exists:
skipped += 1
self.log_info(f"已存在订阅，跳过：{exists.get('name') or keyword}")
continue


payload = build_rule_payload(self.cfg, actor, year, mtype)
self.log_info(f"准备创建订阅：{payload}")


if self.cfg.dry_run:
continue


try:
_ = self.api.create_subscription(payload)
created += 1
except Exception as e:
self.log_error(f"创建订阅失败：{e}")


self.log_info(f"执行完成：新建 {created}，跳过(已存在) {skipped}")


# 可选：在配置页动态渲染表单（如框架支持）
def get_form(self) -> Dict[str, Any]:
return {
"groups": [
{
"title": "基础设置",
"fields": [
{"name": "actors", "type": "tags", "label": "演员名单", "placeholder": "如：Tom Hanks / 梁朝伟"},
{"name": "years", "type": "tags", "label": "年份（多选）", "placeholder": "例如：1994, 2019"},
{"name": "media_types", "type": "checkbox", "options": ["movie", "tv"], "label": "媒介类型"}
],
},
{
"title": "过滤与站点",
"fields": [
{"name": "sites", "type": "tags", "label": "目标站点（留空=全部）"},
{"name": "quality", "type": "input", "label": "画质首选（如：2160p/1080p/Remux）"},
{"name": "min_seeders", "type": "number", "label": "最少做种数"}
],
},
{
"title": "高级",
"fields": [
{"name": "dry_run", "type": "switch", "label": "试运行"},
{"name": "schedule", "type": "cron", "label": "计划任务CRON"}
],
}
]
}


# 假定框架以 module-level 变量导出插件实例
plugin = ActorYearSubscribePlugin()
