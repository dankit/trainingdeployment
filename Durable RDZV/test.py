from torch.distributed import TCPStore

store = TCPStore("127.0.0.1", 29400, is_master=False)
store.set("test_key", "42")
print("Connected! Value:", store.get("test_key"))