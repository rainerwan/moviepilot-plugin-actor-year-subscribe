## README.md（使用说明）


```markdown
# Actor & Year Auto-Subscribe (MoviePilot 插件)


按照 **演员姓名** 与 **年份** 自动创建订阅规则，支持选择媒介类型（电影/剧集）、站点白名单、画质与做种过滤。可计划任务定时执行，也支持手动触发。


## 功能特性
- 批量：一次性为多位演员、多年份生成订阅
- 去重：创建前检查是否已存在相同关键字的订阅，避免重复
- 过滤：按画质、做种数等常见条件过滤
- 站点：可限定在指定 PT 站创建订阅（留空=全部）
- 调度：内置 CRON 表达式注册入口


## 安装
1. 将本仓库放入 MoviePilot 的插件目录（例如：`plugins/moviepilot-plugin-actor-year-subscribe/`）。
2. 确保环境变量：
- `MOVIEPILOT_URL`：MoviePilot 服务地址（如 `http://127.0.0.1:3000`）
- `MOVIEPILOT_TOKEN`：API Token（如需要）
3. `pip install -r requirements.txt`
4. 在 MoviePilot 后台插件页启用本插件。


## 配置
在插件设置中填写：
- **演员名单**：支持中文/英文，
