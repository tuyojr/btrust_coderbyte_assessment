class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        # TODO: add code to parse weight and parents fields __define-ocg__
        self.weight = int(weight)

        # if the parents field is null, it is assigned an empty list
        self.parents = [] if parents == "" else parents.split(';')

    def parse_mempool_csv():
        """Parse the CSV file and return a list of MempoolTransactions."""
        with open('mempool.csv') as f:
            return [MempoolTransaction(*line.strip().split(',')) for line in f.readlines()]

# a function to select only transactions that maximizes the fees to the miner
def max_fees(txns):
  max_fees_txids = []
  # sorts the fees from the highest to the lowest
  txns.sort(key=lambda x: x.fee, reverse=True)

  total_weight = 0

  # lets go over each data in the csv file
  for txn in txns:
    # check if the total txn weight exceeds 4,000,000
    if total_weight + txn.weight <= 4000000:
      # lets check if all the parent txn ids are already in the max_fees_list
      # this ensures all parents of the current txn are selected
      if all(parent_txid in max_fees_txids for parent_txid in txn.parents):
        max_fees_txids.append(txn.txid)
        total_weight += txn.weight

  return max_fees_txids


transactions = MempoolTransaction.parse_mempool_csv()
varOcg = max_fees(transactions)

for tx in varOcg:
  print(f"{tx}")
