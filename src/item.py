class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"\nYou have picked up {self.name}")
    def on_drop(self):
        print(f"\nYou have dropped {self.name}")
    def move_item(item_name, from_list, to_list):
        item = next((x for x in from_list if x.name == item_name), None)
        if item is not None:
            from_list.remove(item)
            to_list.append(item)
            return item
        else:
            return None
