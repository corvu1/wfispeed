from speedtest import Speedtest

wf = Speedtest()
print("Getting Download Speed...")
download= wf.download()
print(f"Download: {download / 1024 / 1024:.2f} mg")
print(f"Download: {download / 1024:.2f} kp")


print("Getting Upload Speed...")
upload = wf.upload()
print(f"upload : {upload / 1024 / 1024:.3f} mg ")
print(f"upload : {upload / 1024:.3f} kp ")
