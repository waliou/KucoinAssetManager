from TextBasic import bcolors, prompt_input
import json
       
def ShowTargetList(transfer_list):
    print(f"{bcolors.YELLOW}Current Target List{bcolors.ENDC}: ", end = '')
    if len(transfer_list) == 0:
        print('[]')
    for i, name in enumerate(transfer_list):
        print(f'\n{i+1}. {bcolors.LCYAN}{name}{bcolors.ENDC}', end='')
    print('')

def AddTargetList(name, sub_accounts,transfer_list):
    if name not in sub_accounts.keys():
        print(f"{bcolors.RED}{name} is not an valid subuser.{bcolors.ENDC}")
        return
    if name not in transfer_list:
        print(f"{bcolors.LCYAN}{name}{bcolors.GREEN} is added to the transfer list{bcolors.ENDC}")
        transfer_list.append(name)
    else:
        print(f"{bcolors.RED}{name} is already in the transfer list{bcolors.ENDC}")

def RemoveTargetList(name, sub_accounts, transfer_list):
    if name not in sub_accounts.keys():
        print(f"{bcolors.RED}{name} is not an valid subuser.{bcolors.ENDC}")
        return
    if name in transfer_list:
        print(f"{bcolors.LCYAN}{name}{bcolors.GREEN} is removed from the transfer list{bcolors.ENDC}")
        transfer_list.remove(name)
    else:
        print(f"{bcolors.RED}{name} is not in the transfer list{bcolors.ENDC}")

def UpdateTargetList(config_path, sub_accounts, transfer_list):
    end = False
    while not end:
        ShowTargetList(transfer_list)
        print(f"\nWhich Operation you want to do?")
        print(f"1. Add / Remove subusers")
        print(f"2. Batch Modify the Transfer List")
        print(f'0. save and exit')
        choice = prompt_input("")
        if choice == '1':
            print(f'Subusers:')
            for i, name in enumerate(sub_accounts):
                print(f'{i+1}. {bcolors.LCYAN}{name}{bcolors.ENDC}')
            finish = False
            while not finish:
                raw_ops = []
                operation = None
                name = None
                while len(raw_ops) != 2:
                    raw_ops = prompt_input("[add|remove] [subuser] / [exit]: ").split(' ')
                    if raw_ops[0] == 'exit':
                        finish = True
                        break
                if (len(raw_ops) == 2): operation, name = raw_ops
                if operation == 'add':
                    AddTargetList(name, sub_accounts, transfer_list)
                elif operation == 'remove':
                    RemoveTargetList(name, sub_accounts, transfer_list)
                transfer_list.sort()
        elif choice == '2':
            print(f"{bcolors.RED}Not allow to use now.{bcolors.ENDC}")
        elif choice == '0':
            end = True


    with open(config_path, 'r') as f:
        accounts_config = json.load(f)
        f.close()
        accounts_config['transfer_list'] = list(transfer_list)
        accounts_config['transfer_list'].sort()
        f = open(config_path, 'w')
        json.dump(accounts_config, f)
        f.close()
