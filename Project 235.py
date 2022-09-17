import requests

no_of_websites = 0
checked_websites =0
print("Started...\n\n")

for i in range(1,5000):
    URL = f"http://ec2-3-6-91-214.ap-south-1.compute.amazonaws.com/profile?id={i}"
    r = requests.get(url=URL)

    checked_websites += 1
    if checked_websites%100==0:
        print(f"No of Websites Checked: {checked_websites}")

    if r.status_code == 200:
        print(URL)
        no_of_websites += 1

print(f"No Of Websites: {no_of_websites}")
input("\n\nExit...")
