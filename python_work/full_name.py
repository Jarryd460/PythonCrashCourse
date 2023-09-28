first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavascript")

print("")
print("Remove spaces on right  ".rstrip())
print("  Remove spaces on left".lstrip())
print("  Remove spaces on both sides  ".strip())

print("")
nostarch_url = "https://nostarch.com"
nostarch_url = nostarch_url.removeprefix("https://")
print(nostarch_url)