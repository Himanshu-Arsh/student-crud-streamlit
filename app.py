import streamlit as st
import os

FILE_NAME = "students.txt"

# ---------------- FILE HANDLING ----------------
def read_students():
    students = []
    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                id, name, age, course = line.strip().split(",")
                students.append({
                    "id": id,
                    "name": name,
                    "age": age,
                    "course": course
                })
    return students


def write_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['id']},{s['name']},{s['age']},{s['course']}\n")


# ---------------- CRUD OPERATIONS ----------------
def create_student(id, name, age, course):
    students = read_students()
    for s in students:
        if s["id"] == id:
            return False

    students.append({
        "id": id,
        "name": name,
        "age": age,
        "course": course
    })
    write_students(students)
    return True


def update_student(id, name, age, course):
    students = read_students()
    for s in students:
        if s["id"] == id:
            s["name"] = name
            s["age"] = age
            s["course"] = course
            write_students(students)
            return True
    return False


def delete_student(id):
    students = read_students()
    students = [s for s in students if s["id"] != id]
    write_students(students)


# ---------------- STREAMLIT UI ----------------
st.title("📚 Student Record Manager (Text File Based)")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Create", "Read", "Update", "Delete"]
)

if menu == "Create":
    st.subheader("➕ Add Student")
    id = st.text_input("ID")
    name = st.text_input("Name")
    age = st.text_input("Age")
    course = st.text_input("Course")

    if st.button("Add"):
        if create_student(id, name, age, course):
            st.success("Student added successfully")
        else:
            st.error("Student ID already exists")

elif menu == "Read":
    st.subheader("📄 View Students")
    students = read_students()
    if students:
        st.table(students)
    else:
        st.info("No records found")

elif menu == "Update":
    st.subheader("✏️ Update Student")
    id = st.text_input("Enter Student ID")
    name = st.text_input("New Name")
    age = st.text_input("New Age")
    course = st.text_input("New Course")

    if st.button("Update"):
        if update_student(id, name, age, course):
            st.success("Student updated successfully")
        else:
            st.error("Student not found")

elif menu == "Delete":
    st.subheader("🗑️ Delete Student")
    id = st.text_input("Enter Student ID")

    if st.button("Delete"):
        delete_student(id)
        st.success("Student deleted successfully")
