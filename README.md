<div align="center">
  <a href="https://nonebot.dev/store"><img src="https://gastigado.cnies.org/d/project_nonebot_plugin_group_welcome/nbp_logo.png?sign=8bUAF9AtoEkfP4bTe2CrYhR0WP4X6ZbGKykZgAeEWL4=:0" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://gastigado.cnies.org/d/project_nonebot_plugin_group_welcome/NoneBotPlugin.svg?sign=ksAOYnkycNpxRKXh2FsfTooiMXafUh2YpuKdAXGZF5M=:0" width="240" alt="NoneBotPluginText"></p>

<h1>NoneBot Plugin Welcome</h1>
</div>

🎉 **一款为 NoneBot2 设计的、强大且易于配置的入群欢迎插件，特别适配 Lagrange.OneBot。**

当有新成员加入群聊时，本插件可以自动发送包含 `@新成员`、自定义文本和图片的欢迎消息。

## 效果图
<img src="https://gastigado.cnies.org/d/project_nonebot_plugin_group_welcome/PixPin_2025_08_31_19_45_52.png?sign=kjsczdNeTe5BdbOm1tU-rX5Ls5XefHSDgqOjLsvKnvE=:0" alt="效果图预览" style="zoom:50%;" />

## 功能特性

- **@新成员**: 自动提及刚刚入群的新成员。
- **图文组合**: 支持发送图片和文本的组合消息。
- **适配 Lagrange.OneBot**: 支持通过 `file://` 协议发送本地图片，无需网络上传。
- **简单易用**: 只需修改配置文件，无需改动代码。
- **可靠性**: 内置详细的日志和异常处理。

## 使用方法

将 `welcome.py` 放置在 NoneBot 项目的 `src/plugins` 目录下。修改第23行的图片显示和第34行的欢迎语即可。

## 注意事项

- 本插件依赖于 `GroupIncreaseNoticeEvent` (群成员增加事件)，请确保你的 OneBot 实现可以正确上报该事件。
- 图片路径必须是 **绝对路径**，并且Lagrange.OneBot容器或进程需要有该路径的 **读权限**。如果使用 Docker 部署，请确保路径映射正确。

## 💡 鸣谢

本插件站在了巨人的肩膀上，开发过程中吸收和借鉴了许多优秀项目的思想，感谢以下项目及其开发者：

- [nonebot_plugin_admin](https://github.com/yzyyz1387/nonebot_plugin_admin)
- [zhenxun_bot](https://github.com/zhenxun-org/zhenxun_bot)

如果本插件无法满足您的全部需求，也推荐您了解和尝试上述优秀项目。

## 开源许可

本项目使用 [MIT License](LICENSE) 开源。
