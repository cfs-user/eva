# EVA

如果一个智能体的执行层小到只是一个脚本，那它具有病毒传播一样的潜力。

EVA是个麻雀虽小、五脏俱全的Agent智能体，相当于低配版Claude Code，能帮你写脚本、写测试案例、执行shell、分析数据等。我自己就是EVA的重度用户，日常使用频率非常高。

各种好玩案例见当前仓库的 [showcase](./showcase) 🦖🦖🦖

## 特性

- 本地化：可以接入本地部署的OpenAI接口模型，如vLLM，或者是外网模型
- 极致轻量化：单文件，仅一个`eva.py`，有python就能运行
- 目录级Session：下次同样目录启动会延续之前对话
- 安全审查：默认只执行读命令，其他命令需要安全确认
- 移植性：很容易将EVA接入你现有的自动化流程，例如：`eva -au '计算100w以内所有素数和并写到/tmp/result.txt'`。当前就借助`-asu`选项将EVA接入了微信Bot


## 快速开始

0. 直接创建一个eva.py并复制本仓库的eva.py文本内容粘贴进去（docker环境、运维环境等也很容易粘贴代码，无需复杂安装，Just **Paste and Go**）。当然，你也可以git clone本仓库

1. 在终端执行`export EVA_API_KEY=你的deepseek API key`（Windows系统则是`set`命令）

EVA支持OpenAI接口形式的LLM，可以是Ollma、vLLM拉起的本地模型，也可以是DeepSeek、OpenAI等官网API。切换方法是设置`EVA_BASE_URL`, `EVA_MODEL_NAME`, `EVA_API_KEY`这三个环境变量。

Linux设置方法：

```bash
export EVA_BASE_URL=http://xxxxxxxxx/v1
export EVA_MODEL_NAME=xxxxx
export EVA_API_KEY=sk-xxxxx
```

Windows 命令行设置方法：

```cmd
set EVA_BASE_URL=http://xxxxxxxxx/v1
set EVA_MODEL_NAME=xxxxx
set EVA_API_KEY=sk-xxxxx
```

Windows PowerShell设置方法：

```powershell
$env:EVA_BASE_URL=http://xxxxxxxxx/v1
$env:EVA_MODEL_NAME=xxxxx
$env:EVA_API_KEY=sk-xxxxx
```

2. 运行`python3 eva.py`。首次运行会生成`eva`脚本，你需要执行下`source ~/.bashrc`让脚本生效。后续直接输入命令`eva`即可

```python
eva支持的选项：
  -h, --help            show this help message and exit
  -a, --allow-all       允许所有命令无需用户确认即可执行
  -l, --list-session    列出所有session
  -c, --clear-session   清除当前目录session
  -u USER_ASK, --user-ask USER_ASK
                        独立地针对一条用户提问执行EVA
  -s, --with-session    搭配-u使用，载入并保存session
```

## EVA退出说明（按Ctrl + C）

1、EVA运行过程可以随时打断，无论是打断LLM推理、打断工具执行、还是退出EVA，都是按 Ctrl + C

2、打断是个很有用的行为，比如某个命令超时时间太久你不想再等待，或者你想起有个背景忘记向EVA澄清需要补充说明，或者你发现前面对话有错别字想做修正说明  —— **注意，无论何时你都可以 Ctrl + C 打断EVA，无论何时 🎯🎯**

## 关于 Skill

EVA通过`.eva/hints.md`获取记忆线索，无论是外部技能，还是EVA自己提炼的技能/知识，都会将对应线索放在`hints.md`中。

为了支持外部技能，你只需要在eva启动时让它“分析下xxx/xxx/skills目录中的可用技能，提炼线索到hints.md中” 或者 “分析下skillhub上的xxx技能，提炼线索到hints.md中”，然后重启eva即可  —— **EVA的事情EVA自己做 🤖🤖**

## Star记录

<a href="https://www.star-history.com/?repos=usepr%2Feva&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=usepr/eva&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=usepr/eva&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=usepr/eva&type=date&legend=top-left" />
 </picture>
</a>

## 贡献者 ✨

<a href="https://github.com/usepr/eva/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=usepr/eva" />
</a>
