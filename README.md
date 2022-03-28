# KucoinAssetManager
A helper for you to manage your assets in your kucoin account.

## Environment
`python3`
`pip3 install -r requirement.txt`

## Usage
`python3 main.py --config_path ./config.json`
the `--config_path` is default to `./config.json`

## Config
Should be as following format.
```json
{
    "transfer_list": [],
    "api": [
        {
            "name": "Any Name",
            "main": true,
            "api-key": "Your API Key",
            "api-secret": "Your API secret",
            "api-passphrase": "Your API passphrase"
        }
    ]
}
```

## Introduction
If providing config is correct, you will see something like following.
```
Enter what operation to do:
0. Reload Configuration
1. Show Main Account Info
2. Show Sub Accounts Info
3. Edit Transfer List
otherwise exit
*)
```
### `0. Reload Configuration`
This operation will load the config file from `config_path`, it will automatically perform when this program starts.
Reload the config after manually modifying the config file to apply changes.
### `1. Show Main Account Info`
This opearation will start a module that can show you the assets in your main account.
This module will prompt you to input the symbol, and the specifc accounts, `*` stands for all.
```
======= MAIN INFO =======
*) Input a symbol(* for all): USDT
*) Input a type(trade|margin|main|*): *
```
The output will be following format.
```
<type1>-<symbol>: <available balance> / <total balance>
<type2>-<symbol>: <available balance> / <total balance>
...
```
Note that providing invalid symbol will output nothing.

### `2. Show Sub Accounts Info`
This operation will start a module that can show you the assets in your subaccounts.
Only the subaccounts in `transfer_list` will be considered, the list can be updated by either using `3. Edit Transfer List` or by modifying the config file and reload.
This module will prompt you to input the symbol, and the specifc accounts, `*` stands for all.
```
======= SUB INFO =======
*) Input a symbol(* for all): USDT
*) Input an account type to inspect(main|trade|margin|*): *
```
The output will be following format
```
<subaccount0 name>-<subaccount type>-<symbol>: <available balance> / <total balance>
<subaccount1 name>-<subaccount type>-<symbol>: <available balance> / <total balance>
<subaccount2 name>-<subaccount type>-<symbol>: <available balance> / <total balance>
There are <count> subaccounts.
```
> Known Bug: povide an invalid symbol will cause crash.

### `3. Edit Transfer List`
This operation wil start a module that can modify the `transfer_list`.
This module will prompt you to choose from following operations.
```
======= EDIT TRANSFER LIST =======
Current Transfer List:
<list-item0>
<list-item1>
<list-item2>

Which Operation you want to do?
1. Add / Remove subusers
2. Batch Modify the Transfer List
0. save and exit
*)
```

#### `3-1. Add / Remove subusers`
This opeartion will help you modify the `transfer_list`.
you can add / remove subaccount into / from the `transfer_list`.
Module will first show you all the available subaccounts.
```
Subusers:
1. <subaccount0>
2. <subaccount1>
3. <subaccount2>
...
```
Then it will prompt you to modify the list as following
```
*) [add|remove] [subuser] / [exit]:
```
You can input operation like `add <subaccount0>` to add `<subaccount0>` to `transfer_list`,
or `remove <subaccount0>` to remove `<subaccount0>` from `transfer_list`
After you finishing all the operation, type `exit` to go back to the `3. Edit Transfer List` module.
- Note that you have to type `0` in `3. Edit Transfer List` to appy the modification.
#### `3-2. Batch Modify the Transfer List`
This operation is not yet implemented.
#### `3-0. save and exit`
This operation will save the list and return to the menu.
