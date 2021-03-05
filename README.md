#Prisma Cloud CSV account checker

Version: *1.0*
Author: *Marc Hobson*

### Summary
This script will ingest a ```.csv``` file with a header named ```Id``` and the following entries in that column being 
cloud account ID's; ex. AWS: 012345678901, GCP: project-123, and compare the ```.csv``` to the accounts already onboarded 
into a Prisma Cloud tenant. The script will then create a new ```.csv``` with an additional ```InPCS``` header and 
mark ```yes``` or ```no``` in that column if it has already been onboarded.

#### CSV Table example:
Input:  
|Id|  
|--------|  
|01234|  

Output:   
|Id|InPCS|   
|--------|--------|   
|01234| yes    |   
|56789| no     |   

### Requirements and Dependencies

1. Python 3.7 or newer

2. OpenSSL 1.0.2 or newer

(if using on Mac OS, additional items may be nessessary.)

3. Pip

```sudo easy_install pip```

4. Requests (Python library)

```sudo pip install requests```

5. YAML (Python library)

```sudo pip install pyyaml```


### Configuration

1. Create CSV file with header ```Id``` and paste the cloud account ID's below that header in the same column.

2. Place the CSV file to be checked in the ```/main``` directory of this repository after pulling down from GitHub.

3. Navigate to ```config/configs.yml```

4. Fill out your Prisma Cloud access key/secret, stack info, and CSV filename to be scanned.  
   *To determine stack, look at your browser when access console (appX.prismacloud.io, where X is the stack number.  
   Change this to apiX.prismacloud.io and populate it in the configs.yml.  
    Or go here for more information:* https://api.docs.prismacloud.io/

### Run

```
python main.py
```