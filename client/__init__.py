try:
    from cprint import cprint
    print = cprint.warn
except: pass
print("Nothing to see here...")
sys.exit(69)
