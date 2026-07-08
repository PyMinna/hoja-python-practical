from tkinter import *

# Prices of items
rice_price = 60
sugar_price = 45
milk_price = 30
bread_price = 40

def generate_bill():
    bill.delete("1.0", END)

    rice_qty = int(rice_entry.get() or 0)
    sugar_qty = int(sugar_entry.get() or 0)
    milk_qty = int(milk_entry.get() or 0)
    bread_qty = int(bread_entry.get() or 0)

    rice_total = rice_qty * rice_price
    sugar_total = sugar_qty * sugar_price
    milk_total = milk_qty * milk_price
    bread_total = bread_qty * bread_price

    total = rice_total + sugar_total + milk_total + bread_total

    bill.insert(END, "******** GROCERY BILL ********\n")
    bill.insert(END, "Item\tQty\tPrice\n")
    bill.insert(END, "-" * 30 + "\n")

    if rice_qty > 0:
        bill.insert(END, f"Rice\t{rice_qty}\t₹{rice_total}\n")
    if sugar_qty > 0:
        bill.insert(END, f"Sugar\t{sugar_qty}\t₹{sugar_total}\n")
    if milk_qty > 0:
        bill.insert(END, f"Milk\t{milk_qty}\t₹{milk_total}\n")
    if bread_qty > 0:
        bill.insert(END, f"Bread\t{bread_qty}\t₹{bread_total}\n")

    bill.insert(END, "-" * 30 + "\n")
    bill.insert(END, f"Total Bill = ₹{total}")

# Main Window
root = Tk()
root.title("Grocery Bill Generator")
root.geometry("500x500")

Label(root, text="Grocery Bill Generator", font=("Arial", 16, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack()

Label(frame, text="Rice Qty").grid(row=0, column=0, padx=5, pady=5)
rice_entry = Entry(frame)
rice_entry.grid(row=0, column=1)

Label(frame, text="Sugar Qty").grid(row=1, column=0, padx=5, pady=5)
sugar_entry = Entry(frame)
sugar_entry.grid(row=1, column=1)

Label(frame, text="Milk Qty").grid(row=2, column=0, padx=5, pady=5)
milk_entry = Entry(frame)
milk_entry.grid(row=2, column=1)

Label(frame, text="Bread Qty").grid(row=3, column=0, padx=5, pady=5)
bread_entry = Entry(frame)
bread_entry.grid(row=3, column=1)

Button(root, text="Generate Bill", command=generate_bill).pack(pady=10)

bill = Text(root, width=45, height=15)
bill.pack()

Button(root, text="Exit", command=root.destroy).pack(pady=10)

root.mainloop()