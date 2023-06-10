import cosmospy
import pandas as pd

# Генерация нового кошелька
wallets = []

for i in range(400):
    wallet = cosmospy.generate_wallet()
    wallets.append(wallet)

data = pd.DataFrame({
    'Addresses': map((lambda x: x["address"]), wallets),
    'Seed Phrases': map((lambda x: x["seed"]), wallets)
})

# Сохранение DataFrame в Excel файл
data.to_excel('wallets.xlsx', index=False)
