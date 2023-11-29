class Editor:
    def view_document(self):
        print("Document reading: you can read this document free of charge")
    
    def edit_document(self):
        print("Editing of the document is not avaible for free version")

output=Editor()
Editor.view_document(output)
Editor.edit_document(output)
print("-----------------------")

class ProEditor(Editor):
    def edit_document(self):
        print("Congratulations! You can edit this document!")

key = str(input("Enter a key for editing this document:"))
if key == "ahFdWFB156":
    login = ProEditor()
    ProEditor.edit_document(login)
else:
    login_incorrect = Editor()
    Editor.edit_document(login_incorrect)
