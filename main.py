import time
import requests
import winsound
from datetime import datetime

link = input("Please provide the URL of the website for surveillance: ")
snapshotFile = "snapshot.txt"
timeBetweenSnapshots = int(input("Enter the time interval between snapshots (in seconds): "))


# Get a new snapshot of the site
def takeSnapshot():
    snapshot = requests.get(link).text
    open(snapshotFile, 'w', encoding='utf-8').write(snapshot)
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    print(f"[{now}] Took snapshot.")


def getCurrentSnapshot():
    return open(snapshotFile, 'r', encoding='utf-8').read()


if __name__ == '__main__':
    # Take an initial snapshot
    takeSnapshot()
    while True:
        time.sleep(timeBetweenSnapshots)
        # Take a new snapshot
        oldSnapshot = getCurrentSnapshot()
        takeSnapshot()
        newSnapshot = getCurrentSnapshot()
        # Compare the snapshots
        if newSnapshot != oldSnapshot:
            print(f"[!] The website has been updated! Check out the latest changes: {link}")
            # Notify the user using sound notifications
            while True:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                time.sleep(3)
            break
