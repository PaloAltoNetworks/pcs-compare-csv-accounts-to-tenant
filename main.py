import lib
import json
import csv


class CompareAccounts():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.rl_sess = lib.RLSession(self.config.rl_user, self.config.rl_pass, self.config.rl_cust,
                                     self.config.rl_api_base)

    def get_pcs_accounts(self):
        self.url = "https://" + self.config.rl_api_base + "/cloud/name"
        self.rl_sess.authenticate_client()
        response = self.rl_sess.client.get(self.url)
        pcs_accounts_json = response.json()


        return pcs_accounts_json

    def create_pcs_account_lists(self,pcs_accounts_json):
        pcs_cloudaccounts_list = []

        for account in pcs_accounts_json:
            pcs_cloudaccounts_list.append(account['id'])

        return pcs_cloudaccounts_list

    def read_csv_file(self):
        filename = self.config.rl_file_name ###<==Configure filename in configs.yml
        fields = []
        rows = []
        acct_id = []
        orgfile = []

        with open(filename,'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
                orgfile.append(dict(row))
                acct_id.append(row["Id"])

        return acct_id, orgfile

    def write_cs_file_update(self,pcs_account_not_exist,csvreader1):
        filename = "CloudAccounts_Updated.csv"
        fields = ['Id','InPCS']

        for i in pcs_account_not_exist:
            for account in csvreader1:
                if i == account['Id']:
                    account.update({'InPCS':'No'})
        for account in csvreader1:
            if 'InPCS' in account:
                continue
            else:
                account.update({'InPCS': 'Yes'})

        with open(filename, 'w', newline='') as fd:
            writer = csv.DictWriter(fd, fieldnames=fields)
            writer.writeheader()
            writer.writerows(csvreader1)


    def Diff(self,li1, li2):
        return (list(list(set(li1) - set(li2)) + list(set(li2) - set(li1))))

    def run(self):
        pcs_accounts_json1 = self.get_pcs_accounts()
        pcs_cloudaccounts_list1 = self.create_pcs_account_lists(pcs_accounts_json1)
        acct_id1, csvreader1 = self.read_csv_file()
        pcs_account_not_exist = self.Diff(acct_id1,pcs_cloudaccounts_list1)
        self.write_cs_file_update(pcs_account_not_exist,csvreader1)

def main():
    Compare_Accounts = CompareAccounts()
    Compare_Accounts.run()

if __name__ == "__main__":
    main()