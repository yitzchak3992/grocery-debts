from customer import Customer


class Tree:
    def __init__(self) -> None:
        self.root: Customer | None = None

    def add_node(self, now_node: Customer):
        if self.root is None:
            self.root = now_node
            return
        node = self.root
        while node:
            if now_node.id <= node.id:
                if node.left:
                    node = node.left
                else:
                    node.left = now_node
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = now_node
                    return

    def search_id(self, id: str) -> Customer | None:
        node = self.root
        while node:
            if node.id == id:
                break
            if id <= node.id:
                node = node.left
                continue
            if id > node.id:
                node = node.right
        return node  # will return the node whose ID matches the search, if not found it will return None .

    def set_customer(self, row: list[str]) -> True | False:
        row[-1] = float(row[-1])
        customer = self.search_id(row[2])
        if customer:
            if row[1] != customer.first_name or row[2] != customer.last_name:
                print(
                    "The ID exists under another name, the information will not be saved!"
                )
                return False
            customer.add_debt(row[-1])
            return True
        else:
            customer = Customer(*row)
            self.add_node(customer)
            return True

    def _print_customers(self, node: Customer, ret_list: list):
        if node == None:
            return
        self._print_customers(node.left, ret_list)
        ret_list.append(node.__str__())
        self._print_customers(node.right, ret_list)

    def _customers_list(self, node: Customer, ret_list: list):
        if node == None:
            return
        self._customers_list(node.left, ret_list)
        ret_list.append(node.get_list())
        self._customers_list(node.right, ret_list)

    def print_by_debt(self):
        ret_list: list[str | int] = []
        self._customers_list(self.root, ret_list)
        ret_list.sort(key=lambda c: c[-1])
        for l in ret_list:
            l[-1] = str(l[-1])
            print(" ".join(l))

    def __str__(self) -> str:
        ret_list: list[str | int] = []
        self._print_customers(self.root, ret_list)
        return "\n".join(ret_list)
