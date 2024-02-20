import os

from dotenv import load_dotenv

from iota_sdk import SendParams, Wallet

load_dotenv()


FAUCET_URL = os.environ.get(
    "FAUCET_URL", "https://faucet.testnet.shimmer.network/api/enqueue"
)

wallet = Wallet(os.environ["WALLET_DB_PATH"])

account = wallet.get_account("Alice")

address = account.addresses()[0].address
# print(address)


if "STRONGHOLD_PASSWORD" not in os.environ:
    raise Exception(".env STRONGHOLD_PASSWORD is undefined, see .env.example")

wallet.set_stronghold_password(os.environ["STRONGHOLD_PASSWORD"])

balance = account.sync()

print(balance.aliases)

transaction = account.prepare_create_alias_output(None, None)

# params = [
#     SendParams(
#         address=address,
#         amount="1000000",
#     )
# ]

transaction = account.send("1000000", address, None)
print(transaction.transactionId)

print(f'Block sent: {os.environ["EXPLORER_URL"]}/block/{transaction.blockId}')

balance = account.sync()

print(balance.aliases)

# #to destroy alias output
# balance = account.sync()
# alias_id = balance.aliases[0]

# transaction = account.prepare_destroy_alias(alias_id).send()
# print(f'Block sent: {os.environ["EXPLORER_URL"]}/block/{transaction.blockId}')
