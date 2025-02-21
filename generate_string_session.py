try:
    from pyrogram import Client
except Exception as e:
    print(e)
    print("\nInstall pyrogram: pip3 install pyrogram")
    exit(1)

print("Required pyrogram V2 or greater.")
API_KEY = int(input("27707164 "))
API_HASH = input("3d1ab21b51395b1d8297932e7a264e96 ")
with Client(name="USS", api_id=API_KEY, api_hash=API_HASH, in_memory=True) as app:
    print(app.export_session_string())
