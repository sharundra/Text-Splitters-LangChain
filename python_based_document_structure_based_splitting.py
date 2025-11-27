from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return self.name"

    def is_passing(self):
        return self.grade >= 6.0


# Example usage
student1 = Student("Aarav", 20, 8.2)
print(student1.get_details())

if student1.is_passing():
    print("The student is passing.")
else:
    print("The student is not passing.")

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,                             # we can choose different languages here like Javascript, PHP, markdown etc.
    chunk_size = 200,
    chunk_overlap = 0
)

doc_chunks = splitter.split_text(text)

print(len(doc_chunks))
print(doc_chunks)
print(type(doc_chunks[0]))
print(f'first chunk : {doc_chunks[0]}')
print(f'Second chunk : {doc_chunks[1]}')
print(f'Third chunk : {doc_chunks[2]}')