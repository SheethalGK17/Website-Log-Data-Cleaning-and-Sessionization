import pandas as pd
import re
file_path = "apache_logs.txt"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    logs = f.readlines()

df = pd.DataFrame(logs, columns=["raw_log"])
df.head()
pattern = (
    r'(?P<ip>\d+\.\d+\.\d+\.\d+).*'
    r'\[(?P<timestamp>.*?)\].*'
    r'"(?:GET|POST) (?P<url>.*?) HTTP.*" '
    r'\d+ .* "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
)

parsed = df["raw_log"].str.extract(pattern)
parsed.head()
parsed["timestamp"] = pd.to_datetime(
    parsed["timestamp"], format="%d/%b/%Y:%H:%M:%S %z"
)
bot_keywords = [
    "bot", "crawl", "spider", "slurp", "feed", "archive", "crawler"
]

parsed = parsed[
    ~parsed["user_agent"].str.lower().str.contains(
        "|".join(bot_keywords), na=False
    )
]
parsed = parsed.sort_values(by=["ip", "timestamp"])
parsed["time_diff"] = parsed.groupby("ip")["timestamp"].diff()

parsed["new_session"] = parsed["time_diff"] > pd.Timedelta(minutes=30)

parsed["session_id"] = parsed.groupby("ip")["new_session"].cumsum()
final_df = parsed[
    ["ip", "session_id", "timestamp", "url"]
]

final_df.head()
final_df.to_csv("cleaned_sessionized_logs.csv", index=False)
