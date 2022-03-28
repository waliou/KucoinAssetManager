from MyClient import MyClient
from TextBasic import bcolors, prompt_input
import json

def LoadSubAccount(main_account, sub_accounts):
    res = main_account['client'].get_subusers()
    for sub in res:
        if sub['subName'] not in sub_accounts.keys() and sub['subName'].startswith('bert'):
            sub_accounts[sub['subName']] = {}
            sub_accounts[sub['subName']]['id'] = sub['userId']

def LoadingConfig(config_path,main_account, sub_accounts, transfer_list):
    if main_account == None:
        with open(config_path) as f:
            accounts_config = json.load(f)
            transfer_list = accounts_config["transfer_list"]
            transfer_list.sort()
            for config in accounts_config["api"]:
                if 'main' in config.keys() and config['main']:
                    if main_account != None:
                        print("[Error] there should be only one main account")
                        exit(-1)
                    print(f'Adding Main account {config["name"]}...')
                    main_account = {
                        'client': MyClient(config["api-key"], config["api-secret"], config["api-passphrase"])
                    }
            f.close()
    if main_account == None:
        print(f"There is no main account!")
        exit(-1)
    LoadSubAccount(main_account, sub_accounts)
    with open(config_path) as f:
        accounts_config = json.load(f)
        for config in accounts_config["api"]:
            if 'main' not in config.keys() and not config['main']:
                if config['name'] in sub_accounts.keys():
                    print(f'Adding sub account {config["name"]}...')
                    sub_accounts[config["name"]] = {}
                    sub_accounts[config["name"]]["client"] = MyClient(config["api-key"], config["api-secret"], config["api-passphrase"])
                else:
                    print(f'{bcolors.RED}{config["name"]} is not an subuser{bcolors.ENDC} Skip.')
    return main_account, sub_accounts, transfer_list



def print_specific_balance(symbol, accounts):
    for account in accounts:
        if account['currency'] == symbol:
            print(f"{bcolors.GREEN}{account['available']}{bcolors.ENDC} / {bcolors.GREEN}{account['balance']}{bcolors.ENDC}")


def ShowMainInfo(main_account):
    symbol = prompt_input('Input a symbol(* for all): ')
    account_type = prompt_input('Input a type(trade|margin|main|*): ')
    res = main_account['client'].get_accounts()
    for account in res:
        if (symbol == '*' or account['currency'] == symbol) and (account_type == '*' or account['type'] == account_type):
            print(f"{bcolors.PURPLE}{account['type']}-{account['currency']}{bcolors.ENDC}: {bcolors.GREEN}{account['available']}{bcolors.ENDC} / {bcolors.GREEN}{account['balance']}{bcolors.ENDC}")

def ShowSubInfo(main_account, sub_accounts):
    # get subaccount info
    symbol = prompt_input('Input a symbol: ')
    account_type = prompt_input('Input an account type to inspect(main|trade|margin|*): ')
    for name, item in sub_accounts.items():
        res = main_account['client'].get_subuser_balance(item["id"])
        # Main Accounts
        if account_type == 'main' or account_type == '*':
            print(f"{bcolors.LCYAN}{name}-main-{symbol}{bcolors.ENDC}: ", end = '')
            print_specific_balance(symbol, res['mainAccounts'])
        # Trade Accounts
        if account_type == 'trade' or account_type == '*':
            print(f"{bcolors.LCYAN}{name}-trade-{symbol}{bcolors.ENDC}: ", end = '')
            print_specific_balance(symbol, res['tradeAccounts'])
        # Future Accounts
        if account_type == 'margin' or account_type == '*':
            print(f"{bcolors.LCYAN}{name}-margin-{symbol}{bcolors.ENDC}: ", end = '')
            print_specific_balance(symbol, res['marginAccounts'])
        if account_type not in ['margin', 'trade', 'main', '*']:
            print(f'{bcolors.RED}Invalid Account Type!{bcolors.ENDC}')
            return
    print(f"There are {bcolors.YELLOW}{len(sub_accounts)}{bcolors.ENDC} subaccounts.")

