from TextBasic import prompt_input
from Info import LoadSubAccount, LoadingConfig, ShowMainInfo, ShowSubInfo
from Transfer import UpdateTransferList
from argparse import ArgumentParser

def ShowMenu():
    print('\nEnter what operation to do:')
    print('0. Reload Configuration')
    print('1. Show Main Account Info')
    print('2. Show Sub Accounts Info')
    print('3. Edit Transfer List')
    print('otherwise exit')
    return prompt_input('')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--config_path', default='./config.json',help='where config file lies')
    args = parser.parse_args()
    return args

def main(args):
    main_account = None
    sub_accounts = {}
    transfer_list = []

    # reading config
    main_account, sub_accounts, transfer_list = LoadingConfig(args.config_path,main_account, sub_accounts, transfer_list)

    while True:
        choice = ShowMenu()
        if choice == '0':
            print('\n======= RELOAD CONDFIG =======')
            main_account, sub_accounts, transfer_list = LoadingConfig(args.config_path, main_account, sub_accounts, transfer_list)
            print('======= END OF RELOAD CONFIG =======')
        elif choice == '1':
            print('\n======= MAIN INFO =======')
            ShowMainInfo(main_account)
            print('======= END OF MAIN INFO =======')
        elif choice == '2':
            print('\n======= SUB INFO =======')
            ShowSubInfo(main_account, sub_accounts, transfer_list)
            print('======= END OF SUB INFO =======')
        elif choice == '3':
            print('\n======= EDIT TRANSFER LIST =======')
            LoadSubAccount(main_account, sub_accounts)
            UpdateTransferList(args.config_path, sub_accounts, transfer_list)
            print('======= END OF EDIT TRANSFER LIST =======')
        elif choice == '':
            continue
        else:
            exit()

if __name__ == '__main__':
    args = parse_args()
    main(args)

        

