
## 📌 **Application Development Lifecycle & Coding Standards**

### ✅ **Application Development Lifecycle**

The application development lifecycle consists of **seven key phases**:

1. **Requirement Gathering**
   Collect user, business, and technical requirements for the application.

2. **Analysis**
   Analyze and refine the gathered requirements.

3. **Design**
   Design the complete solution, including architecture and components.

4. **Code and Test**
   Build and test components of the application.

5. **User and System Test**

   * Users perform usability testing
   * Developers perform system integration and performance testing

6. **Production**
   Release and deploy the application for all end users.

7. **Maintenance**
   Fix bugs, improve performance, and deliver updates or enhancements.

---

### ✅ **APIs vs Web Apps**

* All **web apps are APIs**, because they exchange data with other components.
* **Not all APIs are web apps**, because some APIs do **not require a network** and simply allow communication between software components.

---

### ✅ **PEP8 Guidelines for Code Readability**

PEP8 improves Python code readability with conventions such as:

* Use **4 spaces** for indentation
* Use **blank lines** to separate functions and classes
* Add **spaces around operators** and **after commas**

---

### ✅ **PEP8 Coding Conventions for Consistency**

To maintain consistent and manageable code:

* Keep larger blocks of code **inside functions**
* **Function and file names:** lowercase with underscores (example: `my_function.py`)
* **Class names:** use CamelCase (example: `MyClass`)
* **Constants:** ALL_CAPS with underscores (example: `MAX_COUNT`)

---

### ✅ **Static Code Analysis**

Use **static code analysis** to ensure your code adheres to style and standards **without executing it**.

---

### ✅ **Unit Testing**

Unit testing ensures individual components (**units**) of code work as expected.
Every unit must be tested **before integration** with the main codebase.

---

### ✅ **Creating a Python Package**

To create a Python package:

1. Create a folder with the **package name**
2. Add an empty **`__init__.py`** file
3. Create the required **modules**
4. In `__init__.py`, reference modules to expose them to the package

You can verify the package in a **Python shell** via the **bash terminal**.
