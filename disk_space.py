import shutil, sys
def report(path="/"):
    u = shutil.disk_usage(path)
    pct = round(100 * u.used / u.total, 1) if u.total else 0.0
    return {"path": path, "total_gb": round(u.total/1e9, 2), "used_gb": round(u.used/1e9, 2),
            "free_gb": round(u.free/1e9, 2), "used_pct": pct}
if __name__ == "__main__":
    r = report(sys.argv[1] if len(sys.argv) > 1 else "/")
    print(f"{r['path']}: {r['used_gb']} GB used of {r['total_gb']} GB ({r['used_pct']}%), {r['free_gb']} GB free")
