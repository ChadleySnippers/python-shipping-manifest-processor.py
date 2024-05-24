import pandas as pd
import os
import random

# Load dataset from CSV file
def load_dataset(filename):
    try:
        if os.path.exists(filename):
            return pd.read_csv(filename)
        else:
            return pd.DataFrame(columns=['Order ID', 'Customer Name', 'Surname', 'Email', 'Shipping Country', 'Shipping Time', 'Item', 'Item Colour', 'Item Size'])
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return pd.DataFrame()

# Save dataset to CSV file
def save_dataset(df, filename):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"Error saving dataset: {e}")

# Function to generate a unique 4-digit order ID
def generate_order_id(df):
    existing_order_ids = df['Order ID'].tolist()
    while True:
        order_id = random.randint(1000, 9999)  # Generate a random 4-digit number
        if order_id not in existing_order_ids:
            return order_id

# Add a new entry to the dataset
def add_entry(df):
    try:
        if df.empty:
            df = pd.DataFrame(columns=['Order ID', 'Customer Name', 'Surname', 'Email', 'Shipping Country', 'Shipping Time', 'Item', 'Item Colour', 'Item Size'])

        customer_name = input("Enter Customer Name: ").strip()
        surname = input("Enter Surname: ").strip()
        email = input("Enter Email: ").strip()
        shipping_country = input("Enter Shipping Country: ").strip()
        shipping_time = input("Enter Shipping Time (YYYY-MM-DD): ").strip()
        item = input("Enter Item: ").strip()
        item_colour = input("Enter Item Colour: ").strip()
        item_size = input("Enter Item Size: ").strip()

        if not (customer_name and surname and email and shipping_country and shipping_time and item and item_colour and item_size):
            print("Incomplete entry. Please provide all details.")
            return df

        # Generate a unique 4-digit order ID
        order_id = generate_order_id(df)

        new_entry = {
            'Order ID': order_id,
            'Customer Name': customer_name,
            'Surname': surname,
            'Email': email,
            'Shipping Country': shipping_country,
            'Shipping Time': shipping_time,
            'Item': item,
            'Item Colour': item_colour,
            'Item Size': item_size
        }

        # Append the new entry to the list of dictionaries
        entries = df.to_dict('records')
        entries.append(new_entry)

        # Convert the list of dictionaries back to a DataFrame
        df = pd.DataFrame(entries)

        print("Entry added successfully.")
    except Exception as e:
        print(f"Error adding entry: {e}")
    return df

# Delete an entry from the dataset
def delete_entry(df):
    try:
        order_id_input = input("Enter Order ID to delete: ").strip()
        if not order_id_input:
            print("No Order ID provided. Deletion canceled.")
            return df

        order_id = int(order_id_input)

        if order_id not in df['Order ID'].values:
            print(f"Order ID {order_id} does not exist. Deletion canceled.")
            return df

        df = df[df['Order ID'] != order_id]
        print(f"Entry with Order ID {order_id} deleted successfully.")
    except ValueError:
        print("Invalid Order ID format. Please enter a valid integer.")
    except Exception as e:
        print(f"Error deleting entry: {e}")
    return df

# Edit an existing entry in the dataset
def edit_entry(df):
    try:
        order_id_input = input("Enter Order ID to edit: ").strip()
        if not order_id_input:
            print("No Order ID provided. Editing canceled.")
            return df

        order_id = int(order_id_input)

        if order_id not in df['Order ID'].values:
            print(f"Order ID {order_id} does not exist. Editing canceled.")
            return df

        print("Leave blank if you do not want to change the value.")
        customer_name = input("Enter new Customer Name: ").strip()
        surname = input("Enter new Surname: ").strip()
        email = input("Enter new Email: ").strip()
        shipping_country = input("Enter new Shipping Country: ").strip()
        shipping_time = input("Enter new Shipping Time (YYYY-MM-DD): ").strip()
        item = input("Enter new Item: ").strip()
        item_colour = input("Enter new Item Colour: ").strip()
        item_size = input("Enter new Item Size: ").strip()

        if customer_name:
            df.loc[df['Order ID'] == order_id, 'Customer Name'] = customer_name
        if surname:
            df.loc[df['Order ID'] == order_id, 'Surname'] = surname
        if email:
            df.loc[df['Order ID'] == order_id, 'Email'] = email
        if shipping_country:
            df.loc[df['Order ID'] == order_id, 'Shipping Country'] = shipping_country
        if shipping_time:
            df.loc[df['Order ID'] == order_id, 'Shipping Time'] = shipping_time
        if item:
            df.loc[df['Order ID'] == order_id, 'Item'] = item
        if item_colour:
            df.loc[df['Order ID'] == order_id, 'Item Colour'] = item_colour
        if item_size:
            df.loc[df['Order ID'] == order_id, 'Item Size'] = item_size

        print(f"Entry with Order ID {order_id} updated successfully.")
    except ValueError:
        print("Invalid Order ID format. Please enter a valid integer.")
    except Exception as e:
        print(f"Error editing entry: {e}")
    return df

# Search the dataset
def search_entries(df):
    try:
        search_term = input("Enter search term: ").strip()
        result = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        if not result.empty:
            print("Search results:")
            print(result)
        else:
            print("No matching entries found.")
    except Exception as e:
        print(f"Error searching entries: {e}")

# Display the dataset
def display_dataset(df):
    try:
        print("Current dataset:")
        print(df)
    except Exception as e:
        print(f"Error displaying dataset: {e}")


# Main menu
def main_menu():
    filename = 'dataset.csv'
    df = load_dataset(filename)
    
    while True:
        print("\nShipping Manifest Menu:")
        print("1. Display dataset")
        print("2. Add entry")
        print("3. Delete entry")
        print("4. Edit entry")
        print("5. Search entries")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_dataset(df)
            elif choice == 2:
                df = add_entry(df)
                save_dataset(df, filename)
            elif choice == 3:
                df = delete_entry(df)
                save_dataset(df, filename)
            elif choice == 4:
                df = edit_entry(df)
                save_dataset(df, filename)
            elif choice == 5:
                search_entries(df)
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main_menu()
