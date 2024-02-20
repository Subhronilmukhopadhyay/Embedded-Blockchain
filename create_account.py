import os
from dotenv import load_dotenv
from iota_sdk import ClientOptions, CoinType, StrongholdSecretManager, Wallet

load_dotenv()

node_url = os.environ.get('NODE_URL', 'https://api.testnet.shimmer.network')
client_options = ClientOptions(nodes=[node_url])

coin_type = CoinType.SHIMMER

for env_var in ['STRONGHOLD_PASSWORD', 'MNEMONIC']:
    if env_var not in os.environ:
        raise Exception(f".env {env_var} is undefined, see .env.example")


secret_manager = StrongholdSecretManager(
    os.environ['STRONGHOLD_SNAPSHOT_PATH'], os.environ['STRONGHOLD_PASSWORD'])

wallet = Wallet(
    os.environ['WALLET_DB_PATH'],
    client_options,
    coin_type,
    secret_manager)

name = input("name of the patient")

account = wallet.create_account(name)
print("Account created:", account.get_metadata())
