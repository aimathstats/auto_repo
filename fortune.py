from datetime import datetime, timedelta
from pathlib import Path
import csv
import random

fortunes = [
    ("大吉", "今日は集中力が高い日。短い復習を1つ片づけると流れが良くなります。"),
    ("中吉", "定義を1つ丁寧に見直すと理解が深まります。"),
    ("小吉", "証明を全部読むより、主張と仮定だけ確認すると前進できます。"),
    ("吉", "手を動かして式を1行だけ書くと調子が出ます。"),
    ("末吉", "新しいことより、昨日の内容を1つ復習するのが良い日です。"),
    ("凶", "無理に進めず、既知の定理カードを眺めるだけでも十分です。"),
]

# JST にしたいので UTC+9
now_jst = datetime.utcnow() + timedelta(hours=9)
timestamp = now_jst.strftime("%Y-%m-%d %H:%M:%S")
date_str = now_jst.strftime("%Y-%m-%d")

rank, message = random.choice(fortunes)

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

csv_path = log_dir / "fortune_log.csv"

file_exists = csv_path.exists()

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["timestamp_jst", "date_jst", "rank", "message"])
    writer.writerow([timestamp, date_str, rank, message])

latest_path = log_dir / "latest_fortune.md"
latest_path.write_text(
    f"# 最新の占い\n\n"
    f"- 時刻: {timestamp} JST\n"
    f"- 結果: **{rank}**\n"
    f"- コメント: {message}\n",
    encoding="utf-8"
)

print(f"{timestamp} JST | {rank} | {message}")
