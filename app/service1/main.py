from storage import NoteStorage, GroupStorage
from note_service import NoteService
from group_service import GroupService

note_storage = NoteStorage()
group_storage = GroupStorage()

notes = NoteService(note_storage)
groups = GroupService(group_storage, note_storage)

n = notes.create_note("Shopping", "milk, eggs")
g = groups.create_group("Personal")
groups.add_note(g.id, n.id)

notes.view_note(n.id)
print(groups.get_group_notes(g.id))   # [Note(id=1, title='Shopping', views=1)]
