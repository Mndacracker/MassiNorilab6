import requests
import hashlib
import os
import subprocess

def part1():
    
    # Send GET message to download the file
    url_file = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.msi.sha256'
    resp_msg = requests.get(url_file)
    # If download is successful 
    if resp_msg.status_code == requests.codes.ok:
    # Getting the message from the response text 
        file_content = resp_msg.text
        print (url_file)

    def part2():

        url_file = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.msi'
        resp_msg = requests.get(url_file)
    if resp_msg.status_code == requests.codes.ok:
        file_content = resp_msg.text
        print (url_file)

        def part3():

        # Calculating the has value
            image_hash = hashlib.sha256(file_content).hexdigest()
        # This is to print the hash
            print(image_hash)
        
        def part4():
        # Save the binary file to disk
            with open(r'C:\Users\massi\Documents\GitHub\MassiNorilab6', 'wb') as file:
                file.write(file_content)
                print()

        def part5():
       # Silently run the VLC installer
            run_installer = r'C:\Users\massi\Documents\GitHub\MassiNorilab6\output.exe'
            subprocess.run([run_installer, '/L=1033', '/S'])

        def part6():
        # Deleting the VLC disk and to run from the file
             run_installer = r'C:\Users\massi\Documents\GitHub\MassiNorilab6\output.exe'
             os.remove(run_installer)
             print("File is changed")



    def main():  

            part1()
            part2()
            part3()
            part4()
            part5()
            part6()

    main()