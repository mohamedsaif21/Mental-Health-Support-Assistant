import requests


def probe(msg: str) -> None:
    r = requests.post("http://127.0.0.1:5000/chat", json={"message": msg}, timeout=10)
    data = r.json()
    print("==>", repr(msg))
    print("  status:", r.status_code)
    print("  emergency:", data.get("emergency"), "is_crisis:", data.get("is_crisis"))
    print("  keys:", sorted(data.keys()))
    helplines = data.get("helplines") or []
    print("  helplines_count:", len(helplines))
    if helplines:
        print("  first_helpline:", helplines[0])


if __name__ == "__main__":
    probe("Hello there")
    probe("I want to die")

