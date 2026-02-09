from typing import Optional

class Student:
    """Represents a student with NIM and Name."""
    def __init__(self, nim: str, nama: str):
        self.nim = nim
        self.nama = nama

    def __str__(self) -> str:
        return f"[NIM: {self.nim}, Nama: {self.nama}]"

class FixedArray:
    """
    A fixed-size array implementation demonstrating manual memory management 
    and element shifting, similar to C-style arrays.
    """
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        # Fixed-size array initialized with None
        self.data: list[Optional[Student]] = [None] * capacity  
        self.count = 0

    def is_full(self) -> bool:
        return self.count >= self.capacity

    def is_empty(self) -> bool:
        return self.count == 0

    def insert_at_position(self, student: Student, position: int) -> None:
        """
        Inserts a student at a specific 1-based position.
        Shifts existing elements to the right.
        """
        if self.is_full():
            print("Error: Array is full!")
            return
        
        # Position is 1-based index (1 to count + 1)
        if position < 1 or position > self.count + 1:
            print(f"Error: Invalid position! Must be between 1 and {self.count + 1}.")
            return

        index = position - 1 # Convert to 0-based index

        # Shift elements to the right from the last element down to the insertion index
        # We start from self.count (empty spot) down to index + 1
        for i in range(self.count, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = student
        self.count += 1
        print(f"Inserted at position {position} successfully.")

    def insert_at_beginning(self, student: Student) -> None:
        """Wrapper to insert at position 1."""
        self.insert_at_position(student, 1)

    def insert_at_end(self, student: Student) -> None:
        """Wrapper to insert after the last element."""
        self.insert_at_position(student, self.count + 1)

    def delete_from_position(self, position: int) -> None:
        """
        Deletes a student from a specific 1-based position.
        Shifts subsequent elements to the left.
        """
        if self.is_empty():
            print("Error: Array is empty!")
            return
        
        if position < 1 or position > self.count:
            print(f"Error: Invalid position! Must be between 1 and {self.count}.")
            return

        index = position - 1
        deleted_student = self.data[index]
        print(f"Deleting: {deleted_student}")

        # Shift elements to the left
        for i in range(index, self.count - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.count - 1] = None # Clear the last occupied slot
        self.count -= 1
        print(f"Deleted from position {position} successfully.")

    def delete_from_beginning(self) -> None:
        """Wrapper to delete from position 1."""
        self.delete_from_position(1)

    def delete_from_end(self) -> None:
        """Wrapper to delete the last element."""
        self.delete_from_position(self.count)

    def delete_first_occurrence(self, nim: str) -> None:
        """Deletes the first student matching the given NIM."""
        if self.is_empty():
            print("Error: Array is empty!")
            return

        index = -1
        # Iterate only up to count
        for i in range(self.count):
            if self.data[i] and self.data[i].nim == nim:
                index = i
                break
        
        if index == -1:
            print(f"Error: Student with NIM {nim} not found.")
            return

        print(f"Deleting: {self.data[index]}")
        
        # Shift elements to the left
        for i in range(index, self.count - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.count - 1] = None
        self.count -= 1
        print(f"Deleted student with NIM {nim} successfully.")

    def show_data(self) -> None:
        """Displays all students in the array."""
        print("\n--- Current Data ---")
        if self.is_empty():
            print("Array is empty.")
        else:
            for i in range(self.count):
                print(f"{i + 1}. {self.data[i]}")
        print(f"Count: {self.count}/{self.capacity}")
        print("--------------------")

def get_student_input() -> Optional[Student]:
    """Helper to get student details from user. Returns None if cancelled."""
    nim = input("Enter NIM (0 to back): ")
    if nim.strip() == '0':
        return None
    nama = input("Enter Nama: ")
    return Student(nim, nama)

def get_int_input(prompt: str, allow_cancel: bool = False) -> Optional[int]:
    """Helper to safely get integer input. Returns None if cancelled."""
    while True:
        user_input = input(prompt)
        if allow_cancel and user_input.strip() == '0':
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    arr = FixedArray(10)

    while True:
        print("\n=== MENU ===")
        print("1. Insert at beginning")
        print("2. Insert at given position")
        print("3. Insert at end")
        print("4. Delete from beginning")
        print("5. Delete given position")
        print("6. Delete from end")
        print("7. Delete first occurrence (by NIM)")
        print("8. Show data")
        print("9. Exit")
        print("0. Back to Menu (Refresh)") # Added for consistency, though just refreshes here cause it's the root

        # No allow_cancel here because 0 is handled effectively by the loop or logic (though 1-9 is expected)
        # Actually let's allow 0 to just refresh/continue
        choice = get_int_input("Select menu (1-9): ")
        
        # If user typed something non-int that wasn't handled, get_int_input loops. 
        # If they type 0 (if we allowed it), it would return None.
        # But here we didn't pass allow_cancel=True. 
        # Let's simple check the integer returned.
        
        if choice == 9:
            print("Exiting program...")
            break
        
        # Checking for None (if we ever enabled cancel on main menu, but we didn't)
        if choice is None: 
            continue

        if choice == 1:
            student = get_student_input()
            if student:
                arr.insert_at_beginning(student)
        elif choice == 2:
            pos = get_int_input("Enter position (0 to back): ", allow_cancel=True)
            if pos is not None:
                student = get_student_input()
                if student:
                    arr.insert_at_position(student, pos)
        elif choice == 3:
            student = get_student_input()
            if student:
                arr.insert_at_end(student)
        elif choice == 4:
            arr.delete_from_beginning()
        elif choice == 5:
            pos = get_int_input("Enter position (0 to back): ", allow_cancel=True)
            if pos is not None:
                arr.delete_from_position(pos)
        elif choice == 6:
            arr.delete_from_end()
        elif choice == 7:
            nim = input("Enter NIM to delete (0 to back): ")
            if nim.strip() != '0':
                arr.delete_first_occurrence(nim)
        elif choice == 8:
            arr.show_data()
        elif choice == 0:
             continue # Just refresh
        else:
            if choice is not None: # Avoid printing this if choice was None (though currently impossible)
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
