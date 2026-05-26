from wechatbot import WeChatBot
import os
import subprocess

def run_cli(args, timeout: int = 300):
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            cwd=os.getcwd(),
            timeout=timeout,
            shell=False
        )
        output = f"{result.stdout}"
        if result.stderr:
            output += f"\nSTDERR:\n{result.stderr}"
        return output.strip() or "(no output)"
    except Exception as e:
        return f"执行失败：{str(e)}"


def clean_eva_output(out: str):
    eva_s = "[*] EVA:"
    if eva_s in out:
        out = out[out.rindex(eva_s)+len(eva_s):]
    
    session_s = "> 会话已保存到："
    if session_s in out:
        out = out[:out.rindex(session_s)]

    return out.strip().replace('\033[2m', '').replace('\033[0m', '\n\n___\n')


bot = WeChatBot()

@bot.on_message
async def handle(msg):
    await bot.send_typing(msg.user_id)
    text = msg.text.strip()
    if text.lower() in ['/clear', 'clear']:
        args = ["eva", "-c"]
    else:
        args = ["eva", "-asu", text]
    await bot.reply(msg, clean_eva_output(run_cli(args)))

bot.run()
