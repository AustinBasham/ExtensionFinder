"""
Author: Austin Basham
03MAR2024
Ver 1.1 Chrome Windows only
Looking to add Opera, Opera GX and Firefox

I made this to give brief information of all the extensions installed because doing it manually is annoying
"""

import os
import json
import csv
from datetime import datetime

# global
base_path = fr"C:\Users"
username = input("Which user to parse?: ")
print("Parsing "+username+".")
csv_file_path = "extension_info_"+username+".csv"
def get_extension_info(username, base_path):
    try:
        user_path = os.path.join(base_path, username, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Extensions")
        extension_info = []

# Extension Directories
        for extension_id in os.listdir(user_path):
            extension_path = os.path.join(user_path, extension_id)

# Creation Date
            try:
                creation_date = datetime.fromtimestamp(os.path.getctime(extension_path))
            except FileNotFoundError:
                creation_date = None

# Version
            for version_dir in os.listdir(extension_path):
                version_path = os.path.join(extension_path, version_dir)

# Look for manifest.json
                manifest_path = os.path.join(version_path, "manifest.json")
                if os.path.isfile(manifest_path):
                    with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
                        manifest_data = json.load(manifest_file)
                        extension_name = manifest_data.get('name', '')
                        extension_version = manifest_data.get('version', '')

                        if extension_name:
# Replace names for default/built-in extensions
                            if extension_id == "pjkljhegncpnkpknbcohdijeoejaedia":
                                extension_name = "Google Mail"
                            elif extension_id == "apdfllckaahabafndbhieahigkjlhalf":
                                extension_name = "Google Drive"
                            elif extension_id == "aohghmighlieiainnegkcijnfilokake":
                                extension_name = "Google Docs"
                            elif extension_id == "ghbmnnjooekpmoecnnnilnnbdlolhkhi":
                                extension_name = "Google Docs Offline"
                            elif extension_id == "felcaaldnbdncclmgdcncolpebgiejap":
                                extension_name = "Google Sheets"
                            elif extension_id == "aapocclcgogkmnckokdopfmhonfmgoek":
                                extension_name = "Google Slides"
                            elif extension_id == "nmmhkkegccagdldgiimedpiccmgmieda":
                                extension_name = "Google Wallet"
                            elif extension_id == "mhjfbmdgcfjbbpaeojofohoefgiehjai":
                                extension_name = "Google PDF Viewer"
                            elif extension_id == "pkedcjkdefgpdelpbcmbmeomcjbeemfm":
                                extension_name = "Google Cast"
                            elif extension_id == "aapbdbdomjkkjkaonfhkkikfgjllcleb":
                                extension_name = "Google Translate"

                            extension_info.append({
                                "Extension Name": extension_name,
                                "Extension ID": extension_id,
                                "Version": extension_version,
                                "Creation Date": creation_date.strftime('%Y-%m-%d %H:%M:%S')
                            })
        return extension_info

    except FileNotFoundError:
        print(f"Path not found: {user_path}")
        return None
    except PermissionError:
        print(f"Permission error accessing: {user_path}")
        return None
    except Exception as e:
        print(f"Error extracting extension info: {e}")
        return None

def export_to_csv(data, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ["Extension Name", "Extension ID", "Version", "Creation Date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data has been exported to {csv_file_path}.")

    except Exception as e:
        print(f"Error exporting to CSV: {e}")

# Get extension info for the specified user and export to CSV
extension_info = get_extension_info(username, base_path)
export_to_csv(extension_info, csv_file_path)