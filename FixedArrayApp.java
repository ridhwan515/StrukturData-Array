import java.util.Scanner;

class Student {
    String nim;
    String nama;

    public Student(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
    }

    @Override
    public String toString() {
        return "[NIM: " + nim + ", Nama: " + nama + "]";
    }
}

class FixedArray {
    private int capacity;
    private Student[] data;
    private int count;

    public FixedArray(int capacity) {
        this.capacity = capacity;
        // Java arrays are fixed-size and initialized to null by default for objects
        this.data = new Student[capacity];
        this.count = 0;
    }

    public boolean isFull() {
        return count >= capacity;
    }

    public boolean isEmpty() {
        return count == 0;
    }

    public void insertAtPosition(Student student, int position) {
        if (isFull()) {
            System.out.println("Error: Array is full!");
            return;
        }

        // Position is 1-based index
        if (position < 1 || position > count + 1) {
            System.out.println("Error: Invalid position! Must be between 1 and " + (count + 1) + ".");
            return;
        }

        int index = position - 1; // Convert to 0-based index

        // Shift elements to the right from the last element down to the insertion index
        for (int i = count; i > index; i--) {
            data[i] = data[i - 1];
        }

        data[index] = student;
        count++;
        System.out.println("Inserted at position " + position + " successfully.");
    }

    public void insertAtBeginning(Student student) {
        insertAtPosition(student, 1);
    }

    public void insertAtEnd(Student student) {
        insertAtPosition(student, count + 1);
    }

    public void deleteFromPosition(int position) {
        if (isEmpty()) {
            System.out.println("Error: Array is empty!");
            return;
        }

        if (position < 1 || position > count) {
            System.out.println("Error: Invalid position! Must be between 1 and " + count + ".");
            return;
        }

        int index = position - 1;
        System.out.println("Deleting: " + data[index]);

        // Shift elements to the left
        for (int i = index; i < count - 1; i++) {
            data[i] = data[i + 1];
        }

        data[count - 1] = null; // Clear the last element to avoid memory leak reference
        count--;
        System.out.println("Deleted from position " + position + " successfully.");
    }

    public void deleteFromBeginning() {
        deleteFromPosition(1);
    }

    public void deleteFromEnd() {
        deleteFromPosition(count);
    }

    public void deleteFirstOccurrence(String nim) {
        if (isEmpty()) {
            System.out.println("Error: Array is empty!");
            return;
        }

        int index = -1;
        for (int i = 0; i < count; i++) {
            if (data[i].nim.equals(nim)) {
                index = i;
                break;
            }
        }

        if (index == -1) {
            System.out.println("Error: Student with NIM " + nim + " not found.");
            return;
        }

        System.out.println("Deleting: " + data[index]);

        // Shift elements to the left
        for (int i = index; i < count - 1; i++) {
            data[i] = data[i + 1];
        }

        data[count - 1] = null;
        count--;
        System.out.println("Deleted student with NIM " + nim + " successfully.");
    }

    public void showData() {
        System.out.println("\n--- Current Data ---");
        if (isEmpty()) {
            System.out.println("Array is empty.");
        } else {
            for (int i = 0; i < count; i++) {
                System.out.println((i + 1) + ". " + data[i]);
            }
        }
        System.out.println("Count: " + count + "/" + capacity);
        System.out.println("--------------------");
    }
}

public class FixedArrayApp {
    private static Scanner scanner = new Scanner(System.in);

    // Returns null if cancelled (input "0")
    private static Student getStudentInput() {
        System.out.print("Enter NIM (0 to back): ");
        String nim = scanner.nextLine();
        if (nim.trim().equals("0")) {
            return null;
        }
        
        System.out.print("Enter Nama: ");
        String nama = scanner.nextLine();
        return new Student(nim, nama);
    }

    // Returns null if cancelled (input "0"), uses Integer object to allow null
    private static Integer getIntInput(String prompt, boolean allowCancel) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine();
            
            if (allowCancel && input.trim().equals("0")) {
                return null;
            }

            try {
                return Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }

    public static void main(String[] args) {
        FixedArray arr = new FixedArray(10);

        while (true) {
            System.out.println("\n=== MENU ===");
            System.out.println("1. Insert at beginning");
            System.out.println("2. Insert at given position");
            System.out.println("3. Insert at end");
            System.out.println("4. Delete from beginning");
            System.out.println("5. Delete given position");
            System.out.println("6. Delete from end");
            System.out.println("7. Delete first occurrence (by NIM)");
            System.out.println("8. Show data");
            System.out.println("9. Exit");
            System.out.println("0. Back to Menu (Refresh)");

            // We don't need allowCancel=true here because 0 is handled effectively by logic or loop
            Integer choice = getIntInput("Select menu (1-9): ", false);
            
            // Just in case, though getIntInput in loop handles retries
            if (choice == null) continue; 

            if (choice == 9) {
                System.out.println("Exiting program...");
                break;
            } else if (choice == 0) {
                continue;
            }

            if (choice == 1) {
                Student student = getStudentInput();
                if (student != null) arr.insertAtBeginning(student);
            } else if (choice == 2) {
                Integer pos = getIntInput("Enter position (0 to back): ", true);
                if (pos != null) {
                    Student student = getStudentInput();
                    if (student != null) arr.insertAtPosition(student, pos);
                }
            } else if (choice == 3) {
                Student student = getStudentInput();
                if (student != null) arr.insertAtEnd(student);
            } else if (choice == 4) {
                arr.deleteFromBeginning();
            } else if (choice == 5) {
                Integer pos = getIntInput("Enter position (0 to back): ", true);
                if (pos != null) arr.deleteFromPosition(pos);
            } else if (choice == 6) {
                arr.deleteFromEnd();
            } else if (choice == 7) {
                System.out.print("Enter NIM to delete (0 to back): ");
                String nim = scanner.nextLine();
                if (!nim.trim().equals("0")) {
                    arr.deleteFirstOccurrence(nim);
                }
            } else if (choice == 8) {
                arr.showData();
            } else {
                System.out.println("Invalid choice, please try again.");
            }
        }
        
        scanner.close();
    }
}
