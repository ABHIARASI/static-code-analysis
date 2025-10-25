import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variable
stock_data = {}


def addItem(item="default", qty=0, logs=None):
    """Add items to inventory."""
    if logs is None:
        logs = []

    # input validation
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types: item=%s qty=%s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return logs


def removeItem(item, qty):
    """Remove items safely from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning("Attempted to remove non-existent item: %s", item)
    except Exception as e:
        logging.error("Unexpected error removing item: %s", e)


def getQty(item):
    """Return quantity for given item (0 if missing)."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning("Inventory file not found: %s", file)
    except json.JSONDecodeError:
        logging.error("Error decoding JSON data from %s", file)


def saveData(file="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def printData():
    """Print all inventory items."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def checkLowItems(threshold=5):
    """Return list of items below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution block."""
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # Invalid types - now handled by addItem
    removeItem("apple", 3)
    removeItem("orange", 1)
    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")
    saveData()
    loadData()
    printData()
    # Dangerous eval removed


if __name__ == "__main__":
    main()
