import os
from dotenv import load_dotenv
from iota_sdk import Wallet

load_dotenv()

wallet = Wallet(os.environ['WALLET_DB_PATH'])

for account in wallet.get_accounts():
    print(account.get_metadata())