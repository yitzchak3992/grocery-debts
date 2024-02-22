class Customer:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        id: str,
        phone: str,
        date: str,
        debt: float,
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = id
        self.__phone = phone
        self.__date = date
        self.__debt = debt
        self.__right: Customer | None = None
        self.__left: Customer | None = None

    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name

    @property
    def id(self):
        return self.__id

    @property
    def debt(self):
        return self.__debt

    def add_debt(self, add: float):
        self.__debt = self.__debt + add

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, now_right_node):
        self.__right = now_right_node

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, now_left_node):
        self.__left = now_left_node

    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name} {self.__id} {self.__phone} {self.__date} {self.__debt}"

    # @property
    def get_list(self) -> list[str | int]:
        return [
            self.__first_name,
            self.__last_name,
            self.__id,
            self.__phone,
            self.__date,
            self.__debt,
        ]

    # @staticmethod
    # def
