from pathlib import Path
from datetime import datetime, timezone
import subprocess
import re

REPO_EPG_DIR = Path("epg")

providers = []

for file in sorted(REPO_EPG_DIR.glob("*.xml.gz")):
    provider = file.stem.replace(".xml", "")

    try:
        ts = subprocess.check_output(
            [
                "git",
                "log",
                "-1",
                "--format=%ct",
                "--",
                str(file),
            ],
            text=True,
        ).strip()

        commit_time = datetime.fromtimestamp(int(ts), tz=timezone.utc)
        now = datetime.now(timezone.utc)

        age = now - commit_time
        hours = age.total_seconds() / 3600

        if hours < 1:
            updated = f"{int(age.total_seconds() // 60)}m ago"
        elif hours < 24:
            updated = f"{int(hours)}h ago"
        else:
            updated = f"{age.days}d ago"

        status = "🟢" if hours < 24 else "🔴"

    except Exception:
        updated = "Unknown"
        status = "🔴"

    providers.append(
        (
            provider,
            updated,
            status,
            f"https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/{provider}.xml",
            f"https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/{provider}.xml.gz",
        )
    )

table = [
    "| Provider | Last Updated | Status | XML | XML.GZ |",
    "|----------|--------------|:------:|-----|--------|",
]

for provider, updated, status, xml, gz in providers:
    display = {
        "airtel": "Airtel",
        "dishtv": "Dish TV",
        "jiotv": "JioTV",
        "runntv": "RunNTV",
        "slingtv": "Sling TV",
        "sundirectgo": "SunDirect GO",
        "tataplay": "Tata Play",
        "yupptv": "YuppTV",
        "zee5": "ZEE5",
    }.get(provider, provider.title())

    table.append(
        f"| {display} | {updated} | {status} | [XML]({xml}) | [GZ]({gz}) |"
    )

table_text = "\n".join(table)

readme = Path("README.md")
content = readme.read_text(encoding="utf-8")

content = re.sub(
    r"<!-- EPG_STATUS_START -->.*?<!-- EPG_STATUS_END -->",
    f"<!-- EPG_STATUS_START -->\n{table_text}\n<!-- EPG_STATUS_END -->",
    content,
    flags=re.S,
)

readme.write_text(content, encoding="utf-8")

print("README status table updated.")
