class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_dict = defaultdict(list)
        invalid_idx = set()

        for i, detail in enumerate(transactions):
            name,time_str,amount_str,city = detail.split(",")
            time = int(time_str)
            amount = int(amount_str)
            transaction_dict[name].append((time, city, i))
            if amount > 1000:
                invalid_idx.add(i)
            for other_time, other_city, other_index in transaction_dict[name]:
                if other_city!= city and abs (other_time - time) <= 60:
                    invalid_idx.add(other_index)
                    invalid_idx.add(i)
        return [transactions[i] for i in invalid_idx]
        