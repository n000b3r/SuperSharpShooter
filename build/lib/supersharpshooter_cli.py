# Wrapper so we don't have to modify SuperSharpShooter.py
def main():
    try:
        import SuperSharpShooter as sss
        if hasattr(sss, "main"):
            return sss.main()
    except Exception:
        pass
    import runpy
    runpy.run_module("SuperSharpShooter", run_name="__main__")

