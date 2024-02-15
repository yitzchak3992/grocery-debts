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

    def search_id(self, id: str):
        node = self.root
        while node:
            if node.id == id:
                break
            if id <= node.id:
                node = node.left
                continue
            if id > node.id:
                node = node.right
        return node  # will return the node whose ID matches the search, if not found it will return NonE .

    def _print_customers(self, node, ret_list: list):
        if node == None:
            return
        ret_list.append(node.__str__())
        self._print_customers(node.left, ret_list)
        self._print_customers(node.right, ret_list)

    def __str__(self) -> str:
        ret_list: list[str | int] = []
        self._print_customers(self.root, ret_list)
        return " ".join(ret_list)
